# Explicacion linea 1: Importa las herramientas o clases usadas en este modulo.
import pytest
# Explicacion linea 2: Importa las herramientas o clases usadas en este modulo.
from src.models.concretos.sofacama import SofaCama
# Explicacion linea 3: Importa las herramientas o clases usadas en este modulo.
from src.models.concretos.sofa import Sofa
# Explicacion linea 4: Importa las herramientas o clases usadas en este modulo.
from src.models.concretos.cama import Cama

# Explicacion linea 6: Define un escenario de prueba con un resultado esperado.
def test_escenario_herencia_multiple():
    # Explicacion linea 7: Asigna un valor, configura un argumento o actualiza un dato del escenario.
    s = SofaCama("Dos usos", "Tela", "Gris", 500)
    # Explicacion linea 8: Comprueba el resultado real; pytest marca un fallo si no se cumple.
    assert isinstance(s, Sofa) and isinstance(s, Cama)
    # Explicacion linea 9: Comprueba el resultado real; pytest marca un fallo si no se cumple.
    assert s.calcular_precio() > 500
    # Explicacion linea 10: Comprueba el resultado real; pytest marca un fallo si no se cumple.
    assert s.modo_actual == "sofa"
    # Explicacion linea 11: Comprueba el resultado real; pytest marca un fallo si no se cumple.
    assert isinstance(s.convertir_a_cama(), str)
    # Explicacion linea 12: Comprueba el resultado real; pytest marca un fallo si no se cumple.
    assert s.modo_actual == "cama"
    # Explicacion linea 13: Comprueba el resultado real; pytest marca un fallo si no se cumple.
    assert isinstance(s.convertir_a_sofa(), str)
    # Explicacion linea 14: Comprueba el resultado real; pytest marca un fallo si no se cumple.
    assert s.modo_actual == "sofa"
    # Explicacion linea 15: Comprueba el resultado real; pytest marca un fallo si no se cumple.
    assert isinstance(s.obtener_capacidad_total(), dict)
    # Explicacion linea 16: Comprueba el resultado real; pytest marca un fallo si no se cumple.
    assert "Dos usos" in str(s)

# Explicacion linea 18: Repite la misma verificacion con distintos valores de entrada.
@pytest.mark.parametrize("tamano,mecanismo", [("queen", "hidraulico"), ("king", "electrico"), ("individual", "plegable")])
# Explicacion linea 19: Define un escenario de prueba con un resultado esperado.
def test_escenario_variantes(tamano, mecanismo):
    # Explicacion linea 20: Asigna un valor, configura un argumento o actualiza un dato del escenario.
    s = SofaCama("S", "T", "C", 500, tamaño_cama=tamano, mecanismo_conversion=mecanismo)
    # Explicacion linea 21: Comprueba el resultado real; pytest marca un fallo si no se cumple.
    assert s.calcular_precio() > 500
