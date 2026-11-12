"""Inspección de cabeceras NPY dentro de un NPZ, sin materializar arrays grandes."""

from __future__ import annotations

import ast
import io
import struct
import zipfile

import numpy as np

from .Excepciones import ArchivoSuperficieIlegible
from .util.Utilidades import Configuracion


_MAGIA = b"\x93NUMPY"
_CLAVES = ("vertices", "faces", "normals")


class InspeccionNpz:
    """Rechaza un NPZ cuya cabecera declare más bytes de los que el ZIP contiene."""

    @staticmethod
    def CabeceraNpy(datos: bytes) -> dict:
        """Entrada: bytes de un miembro ``.npy``. Proceso: lee solo la cabecera.
        Salida: descr, shape y bytes esperados del payload. Errores: ilegible.
        """
        if len(datos) < 10 or not datos.startswith(_MAGIA):
            raise ValueError("El miembro no es un NPY válido.")
        mayor, menor = datos[6], datos[7]
        if mayor == 1:
            (largo,) = struct.unpack_from("<H", datos, 8)
            inicio = 10
        elif mayor == 2 or (mayor == 3 and menor == 0):
            (largo,) = struct.unpack_from("<I", datos, 8)
            inicio = 12
        else:
            raise ValueError(f"Versión NPY no soportada: {mayor}.{menor}.")
        fin = inicio + largo
        if fin > len(datos):
            raise ValueError("La cabecera NPY declara más bytes de los disponibles.")
        meta = ast.literal_eval(datos[inicio:fin].decode("latin1"))
        if not isinstance(meta, dict):
            raise ValueError("La cabecera NPY no es un diccionario.")
        forma = tuple(int(valor) for valor in meta["shape"])
        if any(valor < 0 for valor in forma):
            raise ValueError("La forma NPY contiene dimensiones negativas.")
        dtype = np.dtype(meta["descr"])
        producto = 1
        for valor in forma:
            producto *= valor
        if producto and producto > (1 << 40):
            raise ValueError("La forma NPY declara demasiados elementos.")
        esperado = int(producto) * int(dtype.itemsize)
        if fin + esperado > len(datos):
            raise ValueError(
                f"La cabecera declara {esperado} bytes y el miembro solo tiene "
                f"{max(0, len(datos) - fin)}."
            )
        return {"descr": meta["descr"], "shape": forma, "bytes": esperado, "dtype": dtype}

    @staticmethod
    def VerificarContenido(contenido: bytes, nombre: str, maximo_descomprimido: int) -> None:
        """Entrada: bytes NPZ y tope descomprimido. Proceso: suma tamaños ZIP e
        inspecciona cabeceras de vertices/faces/normals. Salida: ninguna.
        Errores: ArchivoSuperficieIlegible antes de reservar arrays grandes.
        """
        try:
            with zipfile.ZipFile(io.BytesIO(contenido)) as archivo:
                total = sum(entrada.file_size for entrada in archivo.infolist())
                if total > maximo_descomprimido:
                    raise ArchivoSuperficieIlegible(
                        nombre, "El NPZ descomprimido supera el límite permitido."
                    )
                nombres = {PathStem(entrada.filename): entrada.filename for entrada in archivo.infolist()}
                faltan = [clave for clave in _CLAVES if clave not in nombres]
                if faltan:
                    raise ArchivoSuperficieIlegible(
                        nombre, f"Faltan arreglos en el NPZ: {', '.join(faltan)}."
                    )
                for clave in _CLAVES:
                    InspeccionNpz.CabeceraNpy(archivo.read(nombres[clave]))
        except ArchivoSuperficieIlegible:
            raise
        except (OSError, ValueError, KeyError, zipfile.BadZipFile) as exc:
            raise ArchivoSuperficieIlegible(nombre, str(exc)) from exc

    @staticmethod
    def VerificarPresupuesto(vertices: np.ndarray, caras: np.ndarray, nombre: str = "superficie") -> None:
        """Entrada: vértices y caras ya materializados. Proceso: compara conteos
        con límites. Salida: ninguna. Errores: ArchivoSuperficieIlegible.
        """
        max_v = int(Configuracion.ValorLimite("max_surface_vertices"))
        max_c = int(Configuracion.ValorLimite("max_surface_faces"))
        if len(vertices) > max_v:
            raise ArchivoSuperficieIlegible(
                nombre, f"La superficie supera el máximo de {max_v} vértices."
            )
        if len(caras) > max_c:
            raise ArchivoSuperficieIlegible(
                nombre, f"La superficie supera el máximo de {max_c} caras."
            )


def PathStem(nombre: str) -> str:
    base = nombre.rsplit("/", 1)[-1]
    if base.endswith(".npy"):
        return base[:-4]
    return base
