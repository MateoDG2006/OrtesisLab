"""Rollback de generación y publicación atómica de archivos."""

import json
import unittest
from pathlib import Path
import tempfile

from GenerateModelsApp.InstantaneaExportacion import PublicacionArchivos


class PublicacionPar(unittest.TestCase):
    def test_confirmar_reemplaza_destino(self):
        with tempfile.TemporaryDirectory() as carpeta:
            destino = Path(carpeta) / "modelo.stl"
            destino.write_bytes(b"\0" * 84)
            sidecar = Path(str(destino) + ".json")
            sidecar.write_text("{}", encoding="utf-8")
            stl_temp, json_temp = PublicacionArchivos.RutasTemporales(destino)
            stl_temp.write_bytes(b"cabecera" + b"\0" * 76 + b"\x01\0\0\0" + b"x" * 50)
            json_temp.write_text(json.dumps({"ok": True}), encoding="utf-8")
            PublicacionArchivos.Confirmar(stl_temp, json_temp, destino)
            self.assertFalse(stl_temp.exists())
            self.assertGreater(destino.stat().st_size, 10)
            self.assertTrue(sidecar.is_file())

    def test_descartar_json_fallido_no_deja_part(self):
        with tempfile.TemporaryDirectory() as carpeta:
            destino = Path(carpeta) / "modelo.stl"
            stl_temp, json_temp = PublicacionArchivos.RutasTemporales(destino)
            stl_temp.write_bytes(b"nuevo")
            PublicacionArchivos.Descartar(stl_temp, json_temp)
            self.assertFalse(stl_temp.exists())


try:
    import bpy
except ImportError:
    bpy = None


@unittest.skipIf(bpy is None, "bpy no disponible")
class RollbackGeneracion(unittest.TestCase):
    def test_fallo_deja_resultado_previo(self):
        bpy.ops.wm.read_factory_settings(use_empty=True)
        bpy.ops.mesh.primitive_uv_sphere_add(segments=16, ring_count=8)
        fuente = bpy.context.object
        from GenerateModelsApp.constants.Nombres import PROP_ROL, ROL_SUPERFICIE, RESULT, SOURCE

        fuente.name = SOURCE
        fuente[PROP_ROL] = ROL_SUPERFICIE
        bpy.ops.mesh.primitive_cube_add(size=1)
        previo = bpy.context.object
        previo.name = RESULT
        previo["ol_config"] = "{}"
        from GenerateModelsApp.Excepciones import ResolucionDemasiadoFina
        from GenerateModelsApp.Objeto import GeneradorObjeto

        with self.assertRaises(ResolucionDemasiadoFina):
            GeneradorObjeto.Crear(
                fuente,
                repair=True,
                resolution_mm=0.001,
                pattern="SQUARE",
            )
        self.assertIsNotNone(bpy.data.objects.get(RESULT))
        self.assertIsNone(bpy.data.objects.get("OL_Ortesis__trabajo"))


if __name__ == "__main__":
    unittest.main()
