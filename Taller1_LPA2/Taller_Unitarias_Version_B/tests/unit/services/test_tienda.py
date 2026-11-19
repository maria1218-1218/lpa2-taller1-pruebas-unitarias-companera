# Explicacion linea 1: Importa las herramientas o clases usadas en este modulo.
import pytest
# Explicacion linea 2: Importa las herramientas o clases usadas en este modulo.
from unittest.mock import Mock
# Explicacion linea 3: Importa las herramientas o clases usadas en este modulo.
from src.models.concretos.silla import Silla
# Explicacion linea 4: Importa las herramientas o clases usadas en este modulo.
from src.services.tienda import TiendaMuebles

# Explicacion linea 6: Define un escenario de prueba con un resultado esperado.
def test_escenario_agregar_y_buscar(tienda,silla):
    # Explicacion linea 7: Comprueba el resultado real; pytest marca un fallo si no se cumple.
    assert "agregado" in tienda.agregar_mueble(silla)
    # Explicacion linea 8: Comprueba el resultado real; pytest marca un fallo si no se cumple.
    assert tienda.buscar_muebles_por_nombre("CLÁSICA")==[silla]
    # Explicacion linea 9: Comprueba el resultado real; pytest marca un fallo si no se cumple.
    assert tienda.filtrar_por_material(" ROBLE ")==[silla]
    # Explicacion linea 10: Comprueba el resultado real; pytest marca un fallo si no se cumple.
    assert tienda.filtrar_por_precio(0,200)==[silla]
    # Explicacion linea 11: Comprueba el resultado real; pytest marca un fallo si no se cumple.
    assert tienda.filtrar_por_precio(300,400)==[]
    # Explicacion linea 12: Comprueba el resultado real; pytest marca un fallo si no se cumple.
    assert tienda.filtrar_por_material("")==[]
    # Explicacion linea 13: Comprueba el resultado real; pytest marca un fallo si no se cumple.
    assert tienda.nombre=="Tienda de pruebas"

# Explicacion linea 15: Define un escenario de prueba con un resultado esperado.
def test_escenario_errores_con_mock(tienda):
    # Explicacion linea 16: Comprueba el resultado real; pytest marca un fallo si no se cumple.
    assert "Error" in tienda.agregar_mueble(None)
    # Explicacion linea 17: Asigna un valor, configura un argumento o actualiza un dato del escenario.
    malo=Mock()
    # Explicacion linea 18: Asigna un valor, configura un argumento o actualiza un dato del escenario.
    malo.calcular_precio.return_value=0
    # Explicacion linea 19: Comprueba el resultado real; pytest marca un fallo si no se cumple.
    assert "Error" in tienda.agregar_mueble(malo)
    # Explicacion linea 20: Asigna un valor, configura un argumento o actualiza un dato del escenario.
    malo.calcular_precio.side_effect=RuntimeError("fallo externo")
    # Explicacion linea 21: Comprueba el resultado real; pytest marca un fallo si no se cumple.
    assert "fallo externo" in tienda.agregar_mueble(malo)
    # Explicacion linea 22: Comprueba el resultado real; pytest marca un fallo si no se cumple.
    assert "Error" in tienda.agregar_comedor(None)

# Explicacion linea 24: Define un escenario de prueba con un resultado esperado.
def test_escenario_venta_y_descuento(tienda,silla):
    # Explicacion linea 25: Comprueba el resultado real; pytest marca un fallo si no se cumple.
    assert "error" in tienda.realizar_venta(silla)
    # Explicacion linea 26: Ejecuta una operacion del objeto dentro del flujo.
    tienda.agregar_mueble(silla)
    # Explicacion linea 27: Comprueba el resultado real; pytest marca un fallo si no se cumple.
    assert "Error" in tienda.aplicar_descuento("sillas",0)
    # Explicacion linea 28: Comprueba el resultado real; pytest marca un fallo si no se cumple.
    assert "aplicado" in tienda.aplicar_descuento("sillas",10)
    # Explicacion linea 29: Asigna un valor, configura un argumento o actualiza un dato del escenario.
    venta=tienda.realizar_venta(silla,"Ana")
    # Explicacion linea 30: Comprueba el resultado real; pytest marca un fallo si no se cumple.
    assert venta["cliente"]=="Ana"
    # Explicacion linea 31: Comprueba el resultado real; pytest marca un fallo si no se cumple.
    assert venta["precio_final"]==pytest.approx(silla.calcular_precio()*.9)
    # Explicacion linea 32: Comprueba el resultado real; pytest marca un fallo si no se cumple.
    assert tienda.buscar_muebles_por_nombre("Silla")==[]

# Explicacion linea 34: Define un escenario de prueba con un resultado esperado.
def test_escenario_integracion_comedor(tienda,comedor):
    # Explicacion linea 35: Comprueba el resultado real; pytest marca un fallo si no se cumple.
    assert "agregado" in tienda.agregar_comedor(comedor)
    # Explicacion linea 36: Comprueba el resultado real; pytest marca un fallo si no se cumple.
    assert isinstance(tienda.generar_reporte_inventario(),str)
    # Explicacion linea 37: Comprueba el resultado real; pytest marca un fallo si no se cumple.
    assert isinstance(tienda.obtener_estadisticas(),dict)
