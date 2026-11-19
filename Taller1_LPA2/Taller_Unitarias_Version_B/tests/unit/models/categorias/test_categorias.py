# Explicacion linea 1: Importa las herramientas o clases usadas en este modulo.
import pytest
# Explicacion linea 2: Importa las herramientas o clases usadas en este modulo.
from src.models.categorias.almacenamiento import Almacenamiento
# Explicacion linea 3: Importa las herramientas o clases usadas en este modulo.
from src.models.categorias.asientos import Asiento
# Explicacion linea 4: Importa las herramientas o clases usadas en este modulo.
from src.models.categorias.superficies import Superficie
# Explicacion linea 5: Importa las herramientas o clases usadas en este modulo.
from src.models.concretos.mesa import Mesa
# Explicacion linea 6: Importa las herramientas o clases usadas en este modulo.
from src.models.concretos.silla import Silla

# Explicacion linea 8: Repite la misma verificacion con distintos valores de entrada.
@pytest.mark.parametrize("cls", [Almacenamiento,Asiento,Superficie])
# Explicacion linea 9: Define un escenario de prueba con un resultado esperado.
def test_escenario_categorias_abstractas(cls):
    # Explicacion linea 10: Comprueba el resultado real; pytest marca un fallo si no se cumple.
    assert bool(cls.__abstractmethods__)

# Explicacion linea 12: Repite la misma verificacion con distintos valores de entrada.
@pytest.mark.parametrize("atributo,valor", [("largo",0),("ancho",-1),("altura",0)])
# Explicacion linea 13: Define un escenario de prueba con un resultado esperado.
def test_escenario_superficie_invalida(mesa, atributo, valor):
    # Explicacion linea 14: Verifica que la operacion produzca la excepcion esperada.
    with pytest.raises(ValueError):
        # Explicacion linea 15: Continua la expresion del bloque anterior o ejecuta esta instruccion.
        setattr(mesa,atributo,valor)

# Explicacion linea 17: Define un escenario de prueba con un resultado esperado.
def test_escenario_superficie_calculos(mesa):
    # Explicacion linea 18: Comprueba el resultado real; pytest marca un fallo si no se cumple.
    assert mesa.calcular_area()>0
    # Explicacion linea 19: Comprueba el resultado real; pytest marca un fallo si no se cumple.
    assert mesa.calcular_factor_tamaño()>0
    # Explicacion linea 20: Comprueba el resultado real; pytest marca un fallo si no se cumple.
    assert "Mesa" in mesa.obtener_info_superficie() or isinstance(mesa.obtener_info_superficie(),str)
    # Explicacion linea 21: Asigna un valor, configura un argumento o actualiza un dato del escenario.
    mesa.largo=200
    # Explicacion linea 22: Asigna un valor, configura un argumento o actualiza un dato del escenario.
    mesa.ancho=100
    # Explicacion linea 23: Asigna un valor, configura un argumento o actualiza un dato del escenario.
    mesa.altura=80
    # Explicacion linea 24: Comprueba el resultado real; pytest marca un fallo si no se cumple.
    assert mesa.largo==200

# Explicacion linea 26: Define un escenario de prueba con un resultado esperado.
def test_escenario_mesa_capacidad_y_forma(mesa):
    # Explicacion linea 27: Asigna un valor, configura un argumento o actualiza un dato del escenario.
    mesa.forma="redonda"
    # Explicacion linea 28: Asigna un valor, configura un argumento o actualiza un dato del escenario.
    mesa.capacidad_personas=6
    # Explicacion linea 29: Comprueba el resultado real; pytest marca un fallo si no se cumple.
    assert mesa.forma=="redonda"
    # Explicacion linea 30: Comprueba el resultado real; pytest marca un fallo si no se cumple.
    assert mesa.capacidad_personas==6
    # Explicacion linea 31: Verifica que la operacion produzca la excepcion esperada.
    with pytest.raises(ValueError):
        # Explicacion linea 32: Asigna un valor, configura un argumento o actualiza un dato del escenario.
        mesa.capacidad_personas=0
