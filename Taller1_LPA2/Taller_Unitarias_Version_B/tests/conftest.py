# Explicacion linea 1: Importa las herramientas o clases usadas en este modulo.
import pytest
# Explicacion linea 2: Importa las herramientas o clases usadas en este modulo.
from src.models.concretos.silla import Silla
# Explicacion linea 3: Importa las herramientas o clases usadas en este modulo.
from src.models.concretos.mesa import Mesa
# Explicacion linea 4: Importa las herramientas o clases usadas en este modulo.
from src.models.composicion.comedor import Comedor
# Explicacion linea 5: Importa las herramientas o clases usadas en este modulo.
from src.services.tienda import TiendaMuebles

# Explicacion linea 7: Define datos reutilizables e independientes para las pruebas.
@pytest.fixture
# Explicacion linea 8: Define un escenario de prueba con un resultado esperado.
def silla():
    # Explicacion linea 9: Devuelve al llamador el resultado construido por este metodo.
    return Silla("Silla clásica", "Roble", "Marrón", 100)

# Explicacion linea 11: Define datos reutilizables e independientes para las pruebas.
@pytest.fixture
# Explicacion linea 12: Define un escenario de prueba con un resultado esperado.
def mesa():
    # Explicacion linea 13: Devuelve al llamador el resultado construido por este metodo.
    return Mesa("Mesa clásica", "Roble", "Marrón", 300)

# Explicacion linea 15: Define datos reutilizables e independientes para las pruebas.
@pytest.fixture
# Explicacion linea 16: Define un escenario de prueba con un resultado esperado.
def comedor(mesa, silla):
    # Explicacion linea 17: Devuelve al llamador el resultado construido por este metodo.
    return Comedor("Familiar", mesa, [silla])

# Explicacion linea 19: Define datos reutilizables e independientes para las pruebas.
@pytest.fixture
# Explicacion linea 20: Define un escenario de prueba con un resultado esperado.
def tienda():
    # Explicacion linea 21: Devuelve al llamador el resultado construido por este metodo.
    return TiendaMuebles("Tienda de pruebas")
