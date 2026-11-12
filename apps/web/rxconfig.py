import sys
from pathlib import Path

# La web se arranca desde apps/web; el núcleo compartido vive en el complemento.
_RAIZ = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(_RAIZ / "apps" / "ortesis-plugin"))

import reflex as rx

config = rx.Config(
    app_name="GenerateModelsApp",
    # El paquete GenerateModelsApp es el complemento, en apps/ortesis-plugin.
    # La página es el paquete web de esta carpeta.
    app_module_import="web.GenerateModelsApp",
    plugins=[
        rx.plugins.SitemapPlugin(),
        rx.plugins.TailwindV4Plugin(),
        rx.plugins.RadixThemesPlugin(
            theme=rx.theme(accent_color="indigo", gray_color="slate", radius="medium"),
        ),
    ],
)