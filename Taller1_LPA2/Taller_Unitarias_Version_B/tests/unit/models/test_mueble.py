# Explicacion linea 1: Importa las herramientas o clases usadas en este modulo.
import pytest
# Explicacion linea 2: Importa las herramientas o clases usadas en este modulo.
from src.models.mueble import Mueble

# Explicacion linea 4: Agrupa verificaciones de un mismo comportamiento.
class VerificacionMueble:
    # Explicacion linea 5: Define un escenario de prueba con un resultado esperado.
    def test_escenario_abstracta(self):
        # Explicacion linea 6: Verifica que la operacion produzca la excepcion esperada.
        with pytest.raises(TypeError):
            # Explicacion linea 7: Continua la expresion del bloque anterior o ejecuta esta instruccion.
            Mueble("Mesa", "Roble", "Negro", 100)

    # Explicacion linea 9: Define un escenario de prueba con un resultado esperado.
    def test_escenario_metodos_abstractos(self):
        # Explicacion linea 10: Comprueba el resultado real; pytest marca un fallo si no se cumple.
        assert Mueble.calcular_precio.__isabstractmethod__
        # Explicacion linea 11: Comprueba el resultado real; pytest marca un fallo si no se cumple.
        assert Mueble.obtener_descripcion.__isabstractmethod__

    # Explicacion linea 13: Repite la misma verificacion con distintos valores de entrada.
    @pytest.mark.parametrize("atributo,valor", [("nombre", ""), ("material", "  "), ("color", ""), ("precio_base", -1)])
    # Explicacion linea 14: Define un escenario de prueba con un resultado esperado.
    def test_escenario_validaciones(self, silla, atributo, valor):
        # Explicacion linea 15: Verifica que la operacion produzca la excepcion esperada.
        with pytest.raises(ValueError):
            # Explicacion linea 16: Continua la expresion del bloque anterior o ejecuta esta instruccion.
            setattr(silla, atributo, valor)

    # Explicacion linea 18: Define un escenario de prueba con un resultado esperado.
    def test_escenario_getters_setters(self, silla):
        # Explicacion linea 19: Asigna un valor, configura un argumento o actualiza un dato del escenario.
        silla.nombre = "  Nueva silla  "
        # Explicacion linea 20: Asigna un valor, configura un argumento o actualiza un dato del escenario.
        silla.material = "Metal"
        # Explicacion linea 21: Asigna un valor, configura un argumento o actualiza un dato del escenario.
        silla.color = "Negro"
        # Explicacion linea 22: Asigna un valor, configura un argumento o actualiza un dato del escenario.
        silla.precio_base = 150
        # Explicacion linea 23: Comprueba el resultado real; pytest marca un fallo si no se cumple.
        assert (silla.nombre, silla.material, silla.color, silla.precio_base) == ("Nueva silla", "Metal", "Negro", 150)
        # Explicacion linea 24: Comprueba el resultado real; pytest marca un fallo si no se cumple.
        assert "Nueva silla" in str(silla)
        # Explicacion linea 25: Comprueba el resultado real; pytest marca un fallo si no se cumple.
        assert "Mueble" in repr(silla)
