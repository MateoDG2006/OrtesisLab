"""Crea o actualiza el objeto OL_Ortesis en la escena de Blender."""

from __future__ import annotations

import json

from .ApiBlender import bmesh, bpy
from .constants.Nombres import (
    ALCANCE,
    MALLA_GEOMETRIA,
    MOD_RECONSTRUCCION,
    MOD_SUAVIZADO,
    PROP_ALCANCE,
    PROP_CARAS,
    PROP_CONFIG,
    PROP_FRAGMENTOS,
    PROP_RESOLUCION,
    PROP_ROL,
    PROP_VALIDACION,
    PROP_VERTICES,
    RESULT,
    ROL_RESULTADO,
    VALIDACION_PENDIENTE,
)
from .constants.Paterns import Patron
from .Excepciones import (
    GeometriaFragmentada,
    MallaNoConstruida,
    ReconstruccionFallida,
    ResolucionDemasiadoFina,
)
from .Modeling import Model3DForPrinting
from .RefinadorMalla import RefinadorMalla
from .Superficie import SuperficieInterior
from .util.Utilidades import Configuracion, Registro

_TRABAJO = "OL_Ortesis__trabajo"


class GeneradorObjeto:
    """Escribe el cascarón en la escena y, si se pide, lo reconstruye con voxel."""

    @staticmethod
    def _EspesorMinimo(cfg: dict) -> float:
        # El voxel no puede ser más fino que un tercio de este espesor.
        if not Patron.Celosia(cfg["pattern"]):
            return cfg["solid_mm"]
        if cfg["liner"]:
            return cfg["skin_mm"]
        return min(cfg["rib_height_mm"], cfg["rib_width_mm"])

    @staticmethod
    def _Componentes(bm):
        # Agrupa vértices unidos por aristas. El grupo mayor es la pieza que se conserva.
        vistos = set()
        grupos = []
        for vertice in bm.verts:
            if vertice in vistos:
                continue
            vistos.add(vertice)
            pendientes = [vertice]
            grupo = []
            while pendientes:
                actual = pendientes.pop()
                grupo.append(actual)
                for arista in actual.link_edges:
                    vecino = arista.other_vert(actual)
                    if vecino not in vistos:
                        vistos.add(vecino)
                        pendientes.append(vecino)
            grupos.append(grupo)
        grupos.sort(key=len, reverse=True)
        return grupos

    @staticmethod
    def _AplicarModificador(objeto, modificador):
        try:
            bpy.ops.object.modifier_apply(modifier=modificador.name)
        except RuntimeError as exc:
            raise ReconstruccionFallida(str(exc)) from exc

    @staticmethod
    def _DescartarTrabajo(trabajo) -> None:
        if trabajo is None:
            return
        malla = trabajo.data
        bpy.data.objects.remove(trabajo, do_unlink=True)
        if malla is not None and malla.users == 0:
            bpy.data.meshes.remove(malla)

    @staticmethod
    def _PromoverResultado(trabajo, previo, source, cfg, paso, interiores, caras_interiores, *, eliminados=0, voxel=None):
        # Sustituye OL_Ortesis solo al terminar con éxito; el previo conserva identidad en escena.
        logger = Registro.Obtener("objeto")
        if previo is None:
            trabajo.name = RESULT
            resultado = trabajo
            logger.info("Objeto %s creado.", RESULT)
        else:
            anterior = previo.data
            previo.data = trabajo.data
            previo.matrix_world = trabajo.matrix_world.copy()
            for clave in list(trabajo.keys()):
                previo[clave] = trabajo[clave]
            for modificador in list(previo.modifiers):
                previo.modifiers.remove(modificador)
            GeneradorObjeto._DescartarTrabajo(trabajo)
            if anterior is not None and anterior.users == 0:
                bpy.data.meshes.remove(anterior)
            resultado = previo
            logger.info("Objeto %s actualizado.", RESULT)
        resultado[PROP_CONFIG] = json.dumps(cfg, ensure_ascii=False)
        resultado[PROP_ROL] = ROL_RESULTADO
        resultado[PROP_VERTICES] = interiores
        resultado[PROP_CARAS] = caras_interiores
        resultado[PROP_VALIDACION] = VALIDACION_PENDIENTE
        resultado[PROP_ALCANCE] = ALCANCE
        resultado["ol_source_object"] = source.name
        resultado["ol_surface_step_mm"] = paso
        if eliminados:
            resultado[PROP_FRAGMENTOS] = eliminados
        if voxel is not None:
            resultado[PROP_RESOLUCION] = voxel
        source.hide_set(True)
        source.hide_render = True
        resultado.hide_set(False)
        resultado.hide_render = False
        bpy.ops.object.select_all(action="DESELECT")
        resultado.select_set(True)
        bpy.context.view_layer.objects.active = resultado
        return resultado

    @staticmethod
    def Crear(source, **options):
        # Genera o sustituye OL_Ortesis a partir de la superficie interior.
        logger = Registro.Obtener("objeto")
        opciones = Model3DForPrinting.ValidarOpciones(options)
        paso = RefinadorMalla.PasoPatron(opciones)
        puntos, caras, normales, borde = SuperficieInterior.Leer(source, paso_mm=paso)
        modelo = Model3DForPrinting()
        vertices, faces, cfg, interiores, caras_interiores = modelo.Construir(
            puntos, caras, normales, borde, **opciones
        )
        minimo = GeneradorObjeto._EspesorMinimo(cfg)
        voxel = min(cfg["resolution_mm"], minimo / 3.0)
        if cfg["repair"] and voxel < Configuracion.ValorLimite("min_voxel_repair_mm"):
            raise ResolucionDemasiadoFina(Configuracion.ValorLimite("min_voxel_repair_mm") * 3)

        previo = bpy.data.objects.get(RESULT)
        trabajo = None
        try:
            malla = bpy.data.meshes.new(MALLA_GEOMETRIA)
            try:
                malla.from_pydata(vertices, [], faces)
                malla.update()
            except (ValueError, RuntimeError) as exc:
                bpy.data.meshes.remove(malla)
                raise MallaNoConstruida(str(exc)) from exc

            for poligono in malla.polygons:
                poligono.use_smooth = True
            trabajo = bpy.data.objects.new(_TRABAJO, malla)
            bpy.context.scene.collection.objects.link(trabajo)
            trabajo.matrix_world = source.matrix_world.copy()
            objeto = trabajo

            # Si un intento anterior dejó el modificador sin aplicar, se retira antes de crear otro.
            for nombre in (MOD_RECONSTRUCCION, MOD_SUAVIZADO):
                pendiente = objeto.modifiers.get(nombre)
                if pendiente is not None:
                    objeto.modifiers.remove(pendiente)
                    logger.warning("Se retiró un modificador que había quedado sin aplicar: %s", nombre)

            if not cfg["repair"]:
                logger.info("Pared engrosada; las aberturas de la superficie se conservan sin voxel.")
                return GeneradorObjeto._PromoverResultado(
                    trabajo, previo, source, cfg, paso, interiores, caras_interiores
                )

            remesh = objeto.modifiers.new(MOD_RECONSTRUCCION, "REMESH")
            remesh.mode = "VOXEL"
            remesh.voxel_size = voxel
            remesh.adaptivity = 0.0
            remesh.use_smooth_shade = True
            logger.info("Reconstrucción voxel a %.3f mm.", voxel)
            bpy.ops.object.select_all(action="DESELECT")
            objeto.select_set(True)
            bpy.context.view_layer.objects.active = objeto
            try:
                GeneradorObjeto._AplicarModificador(objeto, remesh)
            except ReconstruccionFallida:
                if objeto.modifiers.get(MOD_RECONSTRUCCION) is not None:
                    objeto.modifiers.remove(remesh)
                raise

            eliminados = 0
            bm = bmesh.new()
            try:
                bm.from_mesh(objeto.data)
                grupos = GeneradorObjeto._Componentes(bm)
                eliminados = sum(len(grupo) for grupo in grupos[1:])
                umbral = max(
                    Configuracion.ValorLimite("fragment_vertex_floor"),
                    len(bm.verts) * Configuracion.ValorLimite("fragment_vertex_ratio"),
                )
                if eliminados > umbral:
                    raise GeometriaFragmentada(eliminados, umbral)
                if eliminados:
                    bmesh.ops.delete(
                        bm,
                        geom=[vertice for grupo in grupos[1:] for vertice in grupo],
                        context="VERTS",
                    )
                    logger.info("Fragmentos residuales eliminados: %s vértices.", eliminados)
                bm.to_mesh(objeto.data)
            finally:
                bm.free()

            suavizado = objeto.modifiers.new(MOD_SUAVIZADO, "SMOOTH")
            suavizado.factor = Configuracion.ValorLimite("smooth_factor")
            suavizado.iterations = int(Configuracion.ValorLimite("smooth_iterations"))
            try:
                GeneradorObjeto._AplicarModificador(objeto, suavizado)
            except ReconstruccionFallida:
                if objeto.modifiers.get(MOD_SUAVIZADO) is not None:
                    objeto.modifiers.remove(suavizado)
                raise
            logger.info("Reconstrucción y suavizado aplicados sobre %s.", _TRABAJO)
            return GeneradorObjeto._PromoverResultado(
                trabajo,
                previo,
                source,
                cfg,
                paso,
                0,
                0,
                eliminados=eliminados,
                voxel=voxel,
            )
        except Exception:
            GeneradorObjeto._DescartarTrabajo(trabajo)
            raise
