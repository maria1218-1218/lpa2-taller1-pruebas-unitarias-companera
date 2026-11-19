# Explicacion linea 1: Importa las herramientas o clases usadas en este modulo.
import pytest
# Explicacion linea 2: Importa las herramientas o clases usadas en este modulo.
from src.models.composicion.comedor import Comedor
# Explicacion linea 3: Importa las herramientas o clases usadas en este modulo.
from src.models.concretos.silla import Silla

# Explicacion linea 5: Define un escenario de prueba con un resultado esperado.
def test_escenario_composicion(comedor, mesa, silla):
    # Explicacion linea 6: Comprueba el resultado real; pytest marca un fallo si no se cumple.
    assert comedor.mesa is mesa
    # Explicacion linea 7: Comprueba el resultado real; pytest marca un fallo si no se cumple.
    assert len(comedor) == 2
    # Explicacion linea 8: Comprueba el resultado real; pytest marca un fallo si no se cumple.
    assert comedor.calcular_precio_total() == pytest.approx(mesa.calcular_precio()+silla.calcular_precio())
    # Explicacion linea 9: Comprueba el resultado real; pytest marca un fallo si no se cumple.
    assert "FAMILIAR" in comedor.obtener_descripcion_completa()
    # Explicacion linea 10: Comprueba el resultado real; pytest marca un fallo si no se cumple.
    assert isinstance(comedor.obtener_resumen(), dict)
    # Explicacion linea 11: Comprueba el resultado real; pytest marca un fallo si no se cumple.
    assert "Familiar" in str(comedor)

# Explicacion linea 13: Define un escenario de prueba con un resultado esperado.
def test_escenario_agregar_y_quitar(comedor):
    # Explicacion linea 14: Asigna un valor, configura un argumento o actualiza un dato del escenario.
    otra = Silla("Extra", "Roble", "Marrón", 100)
    # Explicacion linea 15: Comprueba el resultado real; pytest marca un fallo si no se cumple.
    assert "agregada" in comedor.agregar_silla(otra)
    # Explicacion linea 16: Comprueba el resultado real; pytest marca un fallo si no se cumple.
    assert len(comedor) == 3
    # Explicacion linea 17: Comprueba el resultado real; pytest marca un fallo si no se cumple.
    assert "removida" in comedor.quitar_silla()
    # Explicacion linea 18: Comprueba el resultado real; pytest marca un fallo si no se cumple.
    assert "inválido" in comedor.quitar_silla(999)

# Explicacion linea 20: Define un escenario de prueba con un resultado esperado.
def test_escenario_comedor_vacio(mesa):
    # Explicacion linea 21: Asigna un valor, configura un argumento o actualiza un dato del escenario.
    c = Comedor("Vacío", mesa)
    # Explicacion linea 22: Comprueba el resultado real; pytest marca un fallo si no se cumple.
    assert "No hay" in c.quitar_silla()
    # Explicacion linea 23: Comprueba el resultado real; pytest marca un fallo si no se cumple.
    assert c.calcular_precio_total() == mesa.calcular_precio()

# Explicacion linea 25: Define un escenario de prueba con un resultado esperado.
def test_escenario_descuento_por_cuatro_sillas(mesa, silla):
    # Explicacion linea 26: Asigna un valor, configura un argumento o actualiza un dato del escenario.
    c = Comedor("Cuatro", mesa, [silla]*4)
    # Explicacion linea 27: Asigna un valor, configura un argumento o actualiza un dato del escenario.
    esperado = round((mesa.calcular_precio()+4*silla.calcular_precio())*.95,2)
    # Explicacion linea 28: Comprueba el resultado real; pytest marca un fallo si no se cumple.
    assert c.calcular_precio_total() == esperado
