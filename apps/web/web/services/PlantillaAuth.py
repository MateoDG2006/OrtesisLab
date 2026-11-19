"""Plantilla HTML/CSS de login y registro (sin HTML embebido en la ruta)."""

from __future__ import annotations

from functools import lru_cache
from html import escape
from pathlib import Path

from starlette.responses import HTMLResponse

_DIR = Path(__file__).resolve().parents[2] / "assets" / "auth"


@lru_cache(maxsize=1)
def _Css() -> str:
    return (_DIR / "auth.css").read_text(encoding="utf-8")


@lru_cache(maxsize=1)
def _Html() -> str:
    return (_DIR / "auth.html").read_text(encoding="utf-8")


class PlantillaAuth:
    """Rellena ``assets/auth/auth.html`` e incrusta ``auth.css`` (el API no sirve assets Reflex)."""

    @staticmethod
    def Pagina(
        titulo: str,
        accion: str,
        error: str,
        enlace_html: str,
        *,
        registro: bool = False,
    ) -> HTMLResponse:
        aviso = f'<p class="ol-error" role="alert">{escape(error)}</p>' if error else ""
        cuerpo = (
            _Html()
            .replace("{{estilos}}", _Css())
            .replace("{{titulo}}", escape(titulo))
            .replace("{{accion}}", escape(accion))
            .replace("{{aviso}}", aviso)
            .replace("{{autocomplete_password}}", "new-password" if registro else "current-password")
            .replace("{{enlace}}", enlace_html)
        )
        return HTMLResponse(cuerpo)
