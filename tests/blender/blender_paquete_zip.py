"""Comprueba el paquete distribuido en aislamiento, sin assets ni Reflex."""
import sys
import logging
import os
import runpy
import tempfile
from pathlib import Path
from zipfile import ZipFile

import bpy

ROOT = Path(__file__).resolve().parents[2]
test_root = (ROOT/'dist').resolve()
test_root.mkdir(exist_ok=True)
paquete = Path(os.environ.get('ORTESISLAB_ZIP', ROOT/'GenerateModelsApp.zip')).resolve()
with tempfile.TemporaryDirectory(dir=test_root, prefix="zip_verificado_") as tmp:
    tmp_path = Path(tmp)
    assert tmp_path.resolve().is_relative_to(test_root)
    with ZipFile(paquete) as archive:
        assert archive.testzip() is None
        assert not any(name.endswith('.npz') for name in archive.namelist())
        assert not any(name.endswith(('.pyc', '.pyo')) or '__pycache__' in name
                       for name in archive.namelist())
        archive.extractall(tmp)
    sys.path.insert(0, tmp)
    import GenerateModelsApp
    assert Path(GenerateModelsApp.__file__).is_relative_to(tmp_path)
    assert GenerateModelsApp.bl_info['version'] == runpy.run_path(
        str(ROOT/'GenerateModelsApp'/'__init__.py')
    )['bl_info']['version']
    bpy.ops.wm.read_factory_settings(use_empty=True)
    GenerateModelsApp.register()
    settings = bpy.context.scene.ortesislab
    assert settings.source is None and not settings.repair
    bpy.ops.mesh.primitive_plane_add(size=30)
    base = bpy.context.object
    settings.pattern = 'SQUARE'
    assert bpy.ops.ortesislab.use_surface() == {'FINISHED'}
    assert bpy.ops.ortesislab.generate() == {'FINISHED'}
    assert len(base.data.vertices) == 4
    assert len(bpy.data.objects['OL_Ortesis'].data.vertices) > 8
    assert bpy.ops.ortesislab.validate() == {'FINISHED'}
    from GenerateModelsApp.Exportacion import ExportadorStl
    ExportadorStl.Exportar(bpy.data.objects['OL_Ortesis'], str(tmp_path/'pared.stl'))
    assert (tmp_path/'pared.stl').stat().st_size > 84
    GenerateModelsApp.unregister()
    sys.path.remove(tmp)
    logging.shutdown()  # Libera el archivo de log antes de limpiar la carpeta en Windows.
print('PASS_ZIP: paquete aislado, panel, plano de cuatro vértices, patrón y exportación.', flush=True)
