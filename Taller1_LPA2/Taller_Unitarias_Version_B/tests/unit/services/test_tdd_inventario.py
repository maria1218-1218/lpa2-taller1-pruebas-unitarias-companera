# Explicacion linea 1: Documenta el objetivo y el uso de este bloque.
"""TDD: pruebas escritas antes de implementar los métodos pendientes."""
# Explicacion linea 2: Importa las herramientas o clases usadas en este modulo.
import pytest
# Explicacion linea 3: Importa las herramientas o clases usadas en este modulo.
from unittest.mock import Mock
# Explicacion linea 4: Importa las herramientas o clases usadas en este modulo.
from src.models.concretos.silla import Silla
# Explicacion linea 5: Importa las herramientas o clases usadas en este modulo.
from src.models.concretos.mesa import Mesa


# Explicacion linea 8: Define un escenario de prueba con un resultado esperado.
def test_escenario_filtrar_muebles_por_tipo(tienda, silla, mesa):
    # Explicacion linea 9: Ejecuta una operacion del objeto dentro del flujo.
    tienda.agregar_mueble(silla)
    # Explicacion linea 10: Ejecuta una operacion del objeto dentro del flujo.
    tienda.agregar_mueble(mesa)
    # Explicacion linea 11: Comprueba el resultado real; pytest marca un fallo si no se cumple.
    assert tienda.obtener_muebles_por_tipo(Silla) == [silla]
    # Explicacion linea 12: Comprueba el resultado real; pytest marca un fallo si no se cumple.
    assert tienda.obtener_muebles_por_tipo(Mesa) == [mesa]


# Explicacion linea 15: Define un escenario de prueba con un resultado esperado.
def test_escenario_inventario_vacio(tienda):
    # Explicacion linea 16: Comprueba el resultado real; pytest marca un fallo si no se cumple.
    assert tienda.calcular_valor_inventario() == 0


# Explicacion linea 19: Define un escenario de prueba con un resultado esperado.
def test_escenario_valor_inventario_incluye_comedores(tienda, silla, comedor):
    # Explicacion linea 20: Ejecuta una operacion del objeto dentro del flujo.
    tienda.agregar_mueble(silla)
    # Explicacion linea 21: Ejecuta una operacion del objeto dentro del flujo.
    tienda.agregar_comedor(comedor)
    # Explicacion linea 22: Asigna un valor, configura un argumento o actualiza un dato del escenario.
    esperado = silla.calcular_precio() + comedor.calcular_precio_total()
    # Explicacion linea 23: Comprueba el resultado real; pytest marca un fallo si no se cumple.
    assert tienda.calcular_valor_inventario() == pytest.approx(esperado)


# Explicacion linea 26: Define un escenario de prueba con un resultado esperado.
def test_escenario_valor_inventario_omite_error_de_precio(tienda):
    # Explicacion linea 27: Asigna un valor, configura un argumento o actualiza un dato del escenario.
    mueble = Mock()
    # Explicacion linea 28: Asigna un valor, configura un argumento o actualiza un dato del escenario.
    mueble.calcular_precio.side_effect = RuntimeError('Error de cálculo')
    # Explicacion linea 29: Ejecuta una operacion del objeto dentro del flujo.
    tienda._inventario.append(mueble)
    # Explicacion linea 30: Comprueba el resultado real; pytest marca un fallo si no se cumple.
    assert tienda.calcular_valor_inventario() == 0
