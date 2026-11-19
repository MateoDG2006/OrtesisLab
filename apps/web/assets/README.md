# Assets de la aplicación

Reflex publica esta carpeta en la raíz del sitio.

| Ruta | Qué es |
|---|---|
| [visor.html](visor.html) | Cáscara del visor Three.js (CSS + `main.js`). Cada comparación lo carga en un iframe con la `object_url` del STL. |
| [visor/](visor/) | Módulos reutilizables del visor: `tema.js`, `stl.js`, `camara.js`, `controles.js`, `main.js`, `visor.css`. |
| [auth/](auth/) | Plantilla `auth.html` y `auth.css` de login/registro. El API las incrusta con `PlantillaAuth` (no depende de servir estáticos del frontend). |
| [ortesislab.css](ortesislab.css) | Tokens y clases `ol-*` de la app Reflex. |
| [favicon.ico](favicon.ico) | Icono del sitio. |
| [superficie_interior_mm.npz](superficie_interior_mm.npz) | Superficie de ejemplo incluida. |
| [vendor/](vendor/) | Three.js local. |

`visor.html`, `favicon.ico` y `superficie_interior_mm.npz` permanecen en la raíz de `assets/` porque el sitio los espera en `/visor.html`, `/favicon.ico` y el núcleo busca esa ruta del NPZ.

Los fixtures de pruebas están en [tests/assets](../tests/assets/Test.stl). `assets/external/` es salida generada e ignorada por Git.
