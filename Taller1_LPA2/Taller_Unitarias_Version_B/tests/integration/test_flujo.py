# Explicacion linea 1: Importa las herramientas o clases usadas en este modulo.
import pytest

# Explicacion linea 3: Clasifica la prueba para poder ejecutarla por grupo.
@pytest.mark.integration
# Explicacion linea 4: Define un escenario de prueba con un resultado esperado.
def test_escenario_flujo_completo(tienda,mesa,silla,comedor):
    # Explicacion linea 5: Ejecuta una operacion del objeto dentro del flujo.
    tienda.agregar_mueble(silla)
    # Explicacion linea 6: Ejecuta una operacion del objeto dentro del flujo.
    tienda.agregar_mueble(mesa)
    # Explicacion linea 7: Ejecuta una operacion del objeto dentro del flujo.
    tienda.agregar_comedor(comedor)
    # Explicacion linea 8: Comprueba el resultado real; pytest marca un fallo si no se cumple.
    assert len(tienda.buscar_muebles_por_nombre("Silla"))==1
    # Explicacion linea 9: Asigna un valor, configura un argumento o actualiza un dato del escenario.
    venta=tienda.realizar_venta(silla,"Comprador")
    # Explicacion linea 10: Comprueba el resultado real; pytest marca un fallo si no se cumple.
    assert venta["precio_final"]>0
    # Explicacion linea 11: Comprueba el resultado real; pytest marca un fallo si no se cumple.
    assert len(tienda.buscar_muebles_por_nombre("Silla"))==0
    # Explicacion linea 12: Comprueba el resultado real; pytest marca un fallo si no se cumple.
    assert len(tienda.buscar_muebles_por_nombre("Mesa"))==1
