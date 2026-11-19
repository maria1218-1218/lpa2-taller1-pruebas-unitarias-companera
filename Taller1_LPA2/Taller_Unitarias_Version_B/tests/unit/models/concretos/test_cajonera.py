# Explicacion linea 1: Importa las herramientas o clases usadas en este modulo.
import pytest
# Explicacion linea 2: Importa las herramientas o clases usadas en este modulo.
from src.models.concretos.cajonera import Cajonera

# Explicacion linea 4: Define datos reutilizables e independientes para las pruebas.
@pytest.fixture
# Explicacion linea 5: Define un escenario de prueba con un resultado esperado.
def producto():
    # Explicacion linea 6: Devuelve al llamador el resultado construido por este metodo.
    return Cajonera("Ejemplo", "Madera", "Azul", 100)

# Explicacion linea 8: Agrupa verificaciones de un mismo comportamiento.
class VerificacionCajonera:
    # Explicacion linea 9: Define un escenario de prueba con un resultado esperado.
    def test_escenario_construccion(self, producto):
        # Explicacion linea 10: Comprueba el resultado real; pytest marca un fallo si no se cumple.
        assert producto.nombre == "Ejemplo"
        # Explicacion linea 11: Comprueba el resultado real; pytest marca un fallo si no se cumple.
        assert producto.material == "Madera"
        # Explicacion linea 12: Comprueba el resultado real; pytest marca un fallo si no se cumple.
        assert producto.precio_base == 100

    # Explicacion linea 14: Define un escenario de prueba con un resultado esperado.
    def test_escenario_precio(self, producto):
        # Explicacion linea 15: Comprueba el resultado real; pytest marca un fallo si no se cumple.
        assert isinstance(producto.calcular_precio(), (int, float))
        # Explicacion linea 16: Comprueba el resultado real; pytest marca un fallo si no se cumple.
        assert producto.calcular_precio() >= 100

    # Explicacion linea 18: Define un escenario de prueba con un resultado esperado.
    def test_escenario_descripcion(self, producto):
        # Explicacion linea 19: Comprueba el resultado real; pytest marca un fallo si no se cumple.
        assert "Ejemplo" in producto.obtener_descripcion()

    # Explicacion linea 21: Repite la misma verificacion con distintos valores de entrada.
    @pytest.mark.parametrize("precio", [1, 100, 1000])
    # Explicacion linea 22: Define un escenario de prueba con un resultado esperado.
    def test_escenario_varios_precios(self, precio):
        # Explicacion linea 23: Asigna un valor, configura un argumento o actualiza un dato del escenario.
        producto = Cajonera("Ejemplo", "Madera", "Azul", precio)
        # Explicacion linea 24: Comprueba el resultado real; pytest marca un fallo si no se cumple.
        assert producto.calcular_precio() >= precio
