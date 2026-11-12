"""Contrato de instantánea evaluada para exportación Blender."""

import unittest

try:
    import bpy
except ImportError:  # pragma: no cover
    bpy = None

from GenerateModelsApp.InstantaneaExportacion import MallaEvaluada, PublicacionArchivos
from pathlib import Path


@unittest.skipIf(bpy is None, "bpy no disponible")
class InstantaneaExportacion(unittest.TestCase):
    def test_instantanea_incluye_modificador_sin_aplicar(self):
        bpy.ops.wm.read_factory_settings(use_empty=True)
        bpy.ops.mesh.primitive_cube_add(size=2)
        objeto = bpy.context.object
        mod = objeto.modifiers.new("espesor", "SOLIDIFY")
        mod.thickness = 0.4
        crudo = len(objeto.data.polygons)
        evaluado, _ = MallaEvaluada.Extraer(objeto)
        self.assertGreater(len(evaluado), crudo)

    def test_publicacion_temporal_usa_sufijos_part(self):
        destino = Path("salida/pared.stl")
        stl_temp, json_temp = PublicacionArchivos.RutasTemporales(destino)
        self.assertTrue(str(stl_temp).endswith(".stl.part"))
        self.assertTrue(str(json_temp).endswith(".json.part"))


if __name__ == "__main__":
    unittest.main()
