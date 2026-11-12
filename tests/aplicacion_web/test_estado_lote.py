"""La página /lote recibe todas las variantes con su estado, no solo las terminadas."""

import unittest
import uuid
from datetime import datetime, timezone
from types import SimpleNamespace

from web.EstadoApp import EstadoApp
from web.persistence.Contratos import ItemLote, LoteDTO, ProgresoLote


def Item(estado: str, error: str | None = None) -> ItemLote:
    return ItemLote(
        uuid.uuid4(), uuid.uuid4(), 0, estado, uuid.uuid4(), 1,
        {"pattern": "SOLID", "solid_mm": 2.4}, 1, error, None,
    )


def Progreso(estado_lote: str, *items: ItemLote) -> ProgresoLote:
    lote = LoteDTO(
        uuid.uuid4(), uuid.uuid4(), uuid.uuid4(), "sweep", estado_lote, len(items),
        None, datetime.now(timezone.utc), None,
    )
    return ProgresoLote(lote, list(items))


def Pagina():
    pagina = SimpleNamespace(archivo="", resultados=[], total=0, hechos=0, mensaje="")
    pagina._Mostrar = lambda ficha: EstadoApp._Mostrar(pagina, ficha)
    return pagina


class PublicarLote(unittest.TestCase):
    def test_lote_abierto_muestra_variantes_en_cola_y_en_curso(self):
        pagina = Pagina()
        EstadoApp._Publicar(pagina, Progreso("running", Item("running"), Item("queued"), Item("failed", "roto")))
        self.assertEqual([ficha["estado"] for ficha in pagina.resultados], ["running", "queued", "failed"])
        self.assertEqual([ficha["error"] for ficha in pagina.resultados], ["", "", "roto"])
        self.assertEqual((pagina.hechos, pagina.total), (1, 3))
        self.assertEqual(pagina.mensaje, "1 de 3")

    def test_lote_cerrado_cuenta_fallos(self):
        pagina = Pagina()
        EstadoApp._Publicar(pagina, Progreso("failed", Item("failed", "roto")))
        self.assertEqual(pagina.mensaje, "Listo. 1 de 1 no se pudieron construir.")


if __name__ == "__main__":
    unittest.main()
