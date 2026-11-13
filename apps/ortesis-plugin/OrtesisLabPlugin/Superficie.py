"""Carga y lectura de la superficie interior dentro de Blender.

Este módulo sí depende de Blender. El análisis geométrico está en AnalizadorMalla.
"""

from __future__ import annotations

import hashlib
from collections import OrderedDict
from pathlib import Path

import numpy as np

from .ApiBlender import bpy
from .Excepciones import (
    ArchivoSuperficieIlegible,
    ArchivoSuperficieNoEncontrado,
    EscalaSinAplicar,
    ModificadoresSinAplicar,
    SuperficieNoEsMalla,
    SuperficieInvalida,
    SuperficieSinCaras,
)
from .Malla import AnalizadorMalla
from .RefinadorMalla import RefinadorMalla
from .constants.Nombres import (
    ARCHIVO_SUPERFICIE,
    ATTR_NORMAL,
    PROP_ROL,
    ROL_SUPERFICIE,
    SOURCE,
    RESULT,
    ROL_RESULTADO,
)
from .util.Utilidades import Configuracion, Registro


class SuperficieInterior:
    """Prepara una copia de la superficie elegida, sin cerrar sus aberturas."""
    _refinadas: OrderedDict[tuple, tuple] = OrderedDict()

    @staticmethod
    def VaciarCache() -> None:
        SuperficieInterior._refinadas.clear()

    @staticmethod
    def _Candidatos(path=None) -> list[Path]:
        # Orden de búsqueda: ruta pedida, assets del repo, junto al módulo y junto al blend.
        rutas = []
        if path:
            rutas.append(Path(path))
        if "__file__" in globals():
            rutas.append(Path(__file__).resolve().parent.parent / "assets" / ARCHIVO_SUPERFICIE)
            rutas.append(Path(__file__).resolve().parent / ARCHIVO_SUPERFICIE)
        if bpy.data.filepath:
            rutas.append(Path(bpy.data.filepath).parent / ARCHIVO_SUPERFICIE)
        return rutas

    @staticmethod
    def Cargar(path=None):
        # Trae la superficie en milímetros, sin volver a escalar, y la oculta.
        logger = Registro.Obtener("superficie")
        obj = bpy.data.objects.get(SOURCE)
        if obj is not None:
            logger.info("Superficie ya presente en la escena: %s", obj.name)
            return obj

        candidatos = SuperficieInterior._Candidatos(path)
        elegido = next((ruta for ruta in candidatos if ruta.is_file()), None)
        if elegido is None:
            raise ArchivoSuperficieNoEncontrado(
                detalle="; ".join(str(ruta) for ruta in candidatos) or "sin rutas candidatas"
            )
        logger.info("Cargando superficie desde %s", elegido)
        try:
            with np.load(elegido, allow_pickle=False) as datos:
                vertices = datos["vertices"]
                faces = datos["faces"]
                normals = datos["normals"]
        except (OSError, ValueError, KeyError) as exc:
            raise ArchivoSuperficieIlegible(str(elegido), str(exc)) from exc

        malla = bpy.data.meshes.new(SOURCE)
        malla.from_pydata(vertices, [], faces)
        malla.update()
        atributo = malla.attributes.new(ATTR_NORMAL, "FLOAT_VECTOR", "POINT")
        atributo.data.foreach_set("vector", normals.astype(np.float32).ravel())
        obj = bpy.data.objects.new(SOURCE, malla)
        bpy.context.scene.collection.objects.link(obj)
        unidades = bpy.context.scene.unit_settings
        unidades.system = "METRIC"
        unidades.scale_length = 0.001
        unidades.length_unit = "MILLIMETERS"
        obj[PROP_ROL] = ROL_SUPERFICIE
        obj.hide_render = True
        obj.hide_set(True)
        logger.info(
            "Superficie cargada (%s vértices) y unidades de la escena fijadas en milímetros.",
            len(vertices),
        )
        return obj

    @staticmethod
    def Leer(source, *, paso_mm=None):
        # Lee la malla de Blender y devuelve vértices, caras, normales y distancia al borde.
        logger = Registro.Obtener("superficie")
        if source is None or getattr(source, "type", None) != "MESH":
            raise SuperficieNoEsMalla()
        if source.name == RESULT or source.get(PROP_ROL) == ROL_RESULTADO:
            raise SuperficieInvalida("Seleccione la superficie base, no la ortesis ya generada.")
        if source.mode != 'OBJECT':
            raise SuperficieInvalida("Salga de Edit Mode antes de generar para usar las caras actuales.")
        if source.modifiers:
            raise ModificadoresSinAplicar(getattr(source, "name", SOURCE))
        escala = tuple(source.scale)
        tolerancia = Configuracion.ValorLimite("scale_tolerance")
        if any(abs(valor - 1) > tolerancia for valor in escala):
            raise EscalaSinAplicar(escala)

        malla = source.data
        malla.calc_loop_triangles()
        coordenadas = np.empty(len(malla.vertices) * 3)
        malla.vertices.foreach_get("co", coordenadas)
        puntos = coordenadas.reshape(-1, 3)
        caras = np.array([triangulo.vertices[:] for triangulo in malla.loop_triangles], dtype=np.int32)
        if len(caras) == 0:
            raise SuperficieSinCaras()
        # El STL web reconstruye normales ponderadas por área. Usar la misma
        # regla evita desplazamientos distintos en superficies curvas.
        normales = AnalizadorMalla.NormalesDeCaras(puntos, caras)
        if paso_mm is None:
            return AnalizadorMalla.Preparar(puntos, caras, normales, suavizarNormales=False)
        if not np.isfinite(paso_mm) or paso_mm <= 0:
            raise SuperficieInvalida("El paso de la superficie debe ser positivo y finito.")

        huella = hashlib.blake2b(digest_size=16)
        huella.update(puntos.tobytes())
        huella.update(caras.tobytes())
        clave_malla = huella.digest()
        limites = tuple(sorted(Configuracion.Limites().items()))
        clave = (clave_malla, limites, float(paso_mm))
        cache = SuperficieInterior._refinadas
        if clave in cache:
            cache.move_to_end(clave)
            return tuple(np.array(arreglo, copy=True) for arreglo in cache[clave])
        resultado = RefinadorMalla.Refinar(puntos, caras, normales, paso_mm)
        cache[clave] = tuple(np.array(arreglo, copy=True) for arreglo in resultado)
        while len(cache) > int(Configuracion.ValorLimite("max_refined_cache_entries")):
            cache.popitem(last=False)
        logger.info(
            "Superficie subdividida en una copia: %s vértices, paso %.3f mm.",
            len(resultado[0]),
            paso_mm,
        )
        return resultado
