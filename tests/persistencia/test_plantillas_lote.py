"""CRUD de lote_plantillas por usuario."""

from __future__ import annotations

import unittest
import uuid

from web.services.ServicioPlantillasLote import ServicioPlantillasLote

from tests.persistencia.apoyo_persistencia import Conectar, CrearUsuario, EntornoServicios, requiere_base


@requiere_base
class PlantillasLote(unittest.TestCase):
    def test_guardar_listar_cargar_borrar(self):
        with EntornoServicios():
            with Conectar() as conexion:
                usuario = CrearUsuario(conexion, "Plantillas")
            payload = {
                "parametros": {"cell_mm": "12", "pattern": "HEX"},
                "patrones": ["HEX"],
                "barridos": [{"clave": "cell_mm", "desde": "10", "hasta": "20", "paso": "5"}],
                "ambos_revestimientos": False,
                "superficie": "",
            }
            guardada = ServicioPlantillasLote.Guardar(usuario, "Barrido celda", payload)
            self.assertEqual(guardada.nombre, "Barrido celda")
            self.assertEqual(guardada.payload["patrones"], ["HEX"])
            lista = ServicioPlantillasLote.Listar(usuario)
            self.assertTrue(any(fila.id == guardada.id for fila in lista))
            otra = ServicioPlantillasLote.Obtener(usuario, guardada.id)
            self.assertEqual(otra.nombre, "Barrido celda")
            ServicioPlantillasLote.Borrar(usuario, guardada.id)
            self.assertFalse(any(fila.id == guardada.id for fila in ServicioPlantillasLote.Listar(usuario)))

    def test_nombre_duplicado(self):
        with EntornoServicios():
            with Conectar() as conexion:
                usuario = CrearUsuario(conexion, "DupPlantilla")
            ServicioPlantillasLote.Guardar(usuario, "Misma", {"patrones": ["HEX"]})
            with self.assertRaises(ValueError):
                ServicioPlantillasLote.Guardar(usuario, "Misma", {"patrones": ["SQUARE"]})

    def test_no_ve_plantillas_de_otro(self):
        with EntornoServicios():
            with Conectar() as conexion:
                uno = CrearUsuario(conexion, "Dueño")
                otro = CrearUsuario(conexion, "Ajeno")
            plantilla = ServicioPlantillasLote.Guardar(uno, "Privada", {"patrones": ["VORONOI"]})
            with self.assertRaises(Exception):
                ServicioPlantillasLote.Obtener(otro, plantilla.id)
