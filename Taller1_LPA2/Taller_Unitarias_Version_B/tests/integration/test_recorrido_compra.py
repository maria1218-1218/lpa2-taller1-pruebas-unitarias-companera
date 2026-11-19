# Explicacion linea 1: Documenta el objetivo y el uso de este bloque.
"""Verifica la colaboracion entre catalogo, tienda y venta."""
# Explicacion linea 2: Importa las herramientas o clases usadas en este modulo.
import pytest
# Explicacion linea 3: Importa las herramientas o clases usadas en este modulo.
from src.models.concretos.mesa import Mesa
# Explicacion linea 4: Importa las herramientas o clases usadas en este modulo.
from src.models.concretos.silla import Silla
# Explicacion linea 5: Importa las herramientas o clases usadas en este modulo.
from src.services.tienda import TiendaMuebles

# Explicacion linea 7: Clasifica la prueba para poder ejecutarla por grupo.
@pytest.mark.integration
# Explicacion linea 8: Define un escenario de prueba con un resultado esperado.
def test_recorrido_de_cliente_desde_busqueda_hasta_venta():
    # Explicacion linea 9: Asigna un valor, configura un argumento o actualiza un dato del escenario.
    tienda = TiendaMuebles("Muebles Aurora")
    # Explicacion linea 10: Asigna un valor, configura un argumento o actualiza un dato del escenario.
    mesa = Mesa("Mesa Verde", "Roble", "Verde", 250)
    # Explicacion linea 11: Asigna un valor, configura un argumento o actualiza un dato del escenario.
    silla = Silla("Silla Verde", "Roble", "Verde", 75)
    # Explicacion linea 12: Ejecuta una operacion del objeto dentro del flujo.
    tienda.agregar_mueble(mesa)
    # Explicacion linea 13: Ejecuta una operacion del objeto dentro del flujo.
    tienda.agregar_mueble(silla)
    # Explicacion linea 14: Asigna un valor, configura un argumento o actualiza un dato del escenario.
    encontrados = tienda.filtrar_por_material("roble")
    # Explicacion linea 15: Comprueba el resultado real; pytest marca un fallo si no se cumple.
    assert len(encontrados) == 2
    # Explicacion linea 16: Asigna un valor, configura un argumento o actualiza un dato del escenario.
    articulo = tienda.buscar_muebles_por_nombre("Mesa")[0]
    # Explicacion linea 17: Asigna un valor, configura un argumento o actualiza un dato del escenario.
    recibo = tienda.realizar_venta(articulo, "Compradora")
    # Explicacion linea 18: Comprueba el resultado real; pytest marca un fallo si no se cumple.
    assert recibo["mueble"] == "Mesa Verde"
    # Explicacion linea 19: Comprueba el resultado real; pytest marca un fallo si no se cumple.
    assert recibo["cliente"] == "Compradora"
    # Explicacion linea 20: Comprueba el resultado real; pytest marca un fallo si no se cumple.
    assert tienda.buscar_muebles_por_nombre("Mesa") == []
    # Explicacion linea 21: Comprueba el resultado real; pytest marca un fallo si no se cumple.
    assert tienda.buscar_muebles_por_nombre("Silla") == [silla]
