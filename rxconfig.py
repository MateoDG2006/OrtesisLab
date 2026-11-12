import reflex as rx

config = rx.Config(
    app_name="GenerateModelsApp",
    cors_allowed_origins=["http://localhost:3000", "http://127.0.0.1:3000", "http://localhost:8000", "http://127.0.0.1:8000"],
    # El paquete GenerateModelsApp es el complemento de Blender.
    # La página vive fuera, en web/.
    app_module_import="web.GenerateModelsApp",
    plugins=[
        rx.plugins.SitemapPlugin(),
        rx.plugins.TailwindV4Plugin(),
        rx.plugins.RadixThemesPlugin(
            theme=rx.theme(accent_color="indigo", gray_color="slate", radius="medium"),
        ),
    ],
)