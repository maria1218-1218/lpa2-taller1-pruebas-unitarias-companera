# Explicacion linea 1: Importa las herramientas o clases usadas en este modulo.
from src.models.concretos.comedor import Comedor

# Explicacion linea 3: Define un escenario de prueba con un resultado esperado.
def test_escenario_comedor_concreto(mesa,silla):
    # Explicacion linea 4: Asigna un valor, configura un argumento o actualiza un dato del escenario.
    c=Comedor(mesa,[silla])
    # Explicacion linea 5: Comprueba el resultado real; pytest marca un fallo si no se cumple.
    assert c.cantidad_sillas()==1
    # Explicacion linea 6: Comprueba el resultado real; pytest marca un fallo si no se cumple.
    assert c.calcular_precio_total()==mesa.calcular_precio()+silla.calcular_precio()
    # Explicacion linea 7: Comprueba el resultado real; pytest marca un fallo si no se cumple.
    assert isinstance(c.descripcion(),str)
    # Explicacion linea 8: Continua la expresion del bloque anterior o ejecuta esta instruccion.
    c.agregar_silla(silla)
    # Explicacion linea 9: Comprueba el resultado real; pytest marca un fallo si no se cumple.
    assert c.cantidad_sillas()==2
    # Explicacion linea 10: Continua la expresion del bloque anterior o ejecuta esta instruccion.
    c.quitar_silla(silla)
    # Explicacion linea 11: Comprueba el resultado real; pytest marca un fallo si no se cumple.
    assert c.cantidad_sillas()==1
