"""Genera el ZIP instalable de Blender, sin Reflex, logs ni la base v5."""
from pathlib import Path
from zipfile import ZipFile, ZIP_DEFLATED
import shutil

ROOT = Path(__file__).resolve().parents[1]
PAQUETE = ROOT / 'apps' / 'ortesis-plugin' / 'OrtesisLabPlugin'
ZIP = ROOT / 'apps' / 'ortesis-plugin' / 'GenerateModelsApp.zip'


def empaquetar(destino=None):
    paquete = PAQUETE
    destino = Path(destino) if destino is not None else ZIP
    temporal = destino.with_name(destino.stem + '.nuevo.zip')
    archivos = sorted(p for p in paquete.rglob('*') if p.is_file()
                      and p.suffix in {'.py', '.json'}
                      and not any(part in {'__pycache__', 'logs'} for part in p.relative_to(paquete).parts))
    with ZipFile(temporal, 'w', ZIP_DEFLATED) as zipfile:
        for archivo in archivos:
            zipfile.write(archivo, 'OrtesisLabPlugin/' + archivo.relative_to(paquete).as_posix())
        for archivo in sorted((ROOT / 'core' / 'config').glob('*.json')):
            zipfile.write(archivo, 'OrtesisLabPlugin/config/' + archivo.name)
        zipfile.write(ROOT / 'docs' / 'BlenderPlugin' / 'LEEME.md', 'OrtesisLabPlugin/LEEME.md')
    with ZipFile(temporal) as zipfile:
        assert zipfile.testzip() is None
        assert 'OrtesisLabPlugin/__init__.py' in zipfile.namelist()
    anterior = ROOT / 'dist' / 'GenerateModelsApp-anterior.zip'
    if destino == ZIP and destino.exists() and not anterior.exists():
        anterior.parent.mkdir(exist_ok=True)
        shutil.copy2(destino, anterior)
    temporal.replace(destino)
    print(f'ZIP de Blender actualizado: {destino}')


if __name__ == '__main__':
    empaquetar()
