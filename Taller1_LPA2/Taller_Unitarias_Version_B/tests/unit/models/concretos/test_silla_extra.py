# Explicacion linea 1: Importa las herramientas o clases usadas en este modulo.
import pytest
# Explicacion linea 2: Importa las herramientas o clases usadas en este modulo.
from src.models.concretos.silla import Silla

# Explicacion linea 4: Repite la misma verificacion con distintos valores de entrada.
@pytest.mark.parametrize("respaldo,tapizado,esperado", [(False,None,1.0),(True,None,1.1),(True,"cuero",1.3),(True,"tela",1.2)])
# Explicacion linea 5: Define un escenario de prueba con un resultado esperado.
def test_escenario_factor_comodidad(respaldo,tapizado,esperado):
    # Explicacion linea 6: Asigna un valor, configura un argumento o actualiza un dato del escenario.
    silla = Silla("S", "M", "N", 100, respaldo, tapizado)
    # Explicacion linea 7: Comprueba el resultado real; pytest marca un fallo si no se cumple.
    assert silla.calcular_factor_comodidad() == pytest.approx(esperado)

# Explicacion linea 9: Define un escenario de prueba con un resultado esperado.
def test_escenario_altura_y_ruedas():
    # Explicacion linea 10: Asigna un valor, configura un argumento o actualiza un dato del escenario.
    s = Silla("S", "M", "N", 100, altura_regulable=True, tiene_ruedas=True)
    # Explicacion linea 11: Comprueba el resultado real; pytest marca un fallo si no se cumple.
    assert s.calcular_precio() == pytest.approx(160)
    # Explicacion linea 12: Comprueba el resultado real; pytest marca un fallo si no se cumple.
    assert "ajustada" in s.regular_altura(60)
    # Explicacion linea 13: Comprueba el resultado real; pytest marca un fallo si no se cumple.
    assert "entre" in s.regular_altura(101)
    # Explicacion linea 14: Asigna un valor, configura un argumento o actualiza un dato del escenario.
    s.altura_regulable = False
    # Explicacion linea 15: Comprueba el resultado real; pytest marca un fallo si no se cumple.
    assert "no tiene" in s.regular_altura(60)
    # Explicacion linea 16: Asigna un valor, configura un argumento o actualiza un dato del escenario.
    s.tiene_ruedas = False
    # Explicacion linea 17: Comprueba el resultado real; pytest marca un fallo si no se cumple.
    assert s.tiene_ruedas is False
    # Explicacion linea 18: Comprueba el resultado real; pytest marca un fallo si no se cumple.
    assert isinstance(s.es_silla_oficina(), bool)

# Explicacion linea 20: Define un escenario de prueba con un resultado esperado.
def test_escenario_capacidad_invalida(silla):
    # Explicacion linea 21: Verifica que la operacion produzca la excepcion esperada.
    with pytest.raises(ValueError):
        # Explicacion linea 22: Asigna un valor, configura un argumento o actualiza un dato del escenario.
        silla.capacidad_personas = 0
    # Explicacion linea 23: Asigna un valor, configura un argumento o actualiza un dato del escenario.
    silla.tiene_respaldo = False
    # Explicacion linea 24: Asigna un valor, configura un argumento o actualiza un dato del escenario.
    silla.material_tapizado = "tela"
    # Explicacion linea 25: Comprueba el resultado real; pytest marca un fallo si no se cumple.
    assert "tela" in silla.obtener_info_asiento().lower()
