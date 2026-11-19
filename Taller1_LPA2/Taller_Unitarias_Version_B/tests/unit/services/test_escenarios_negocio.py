# Explicacion linea 1: Documenta el objetivo y el uso de este bloque.
"""Escenarios de negocio: limites, descuentos y registros acumulados."""
# Explicacion linea 2: Importa las herramientas o clases usadas en este modulo.
import pytest
# Explicacion linea 3: Importa las herramientas o clases usadas en este modulo.
from unittest.mock import Mock
# Explicacion linea 4: Importa las herramientas o clases usadas en este modulo.
from src.services.tienda import TiendaMuebles
# Explicacion linea 5: Importa las herramientas o clases usadas en este modulo.
from src.models.concretos.silla import Silla
# Explicacion linea 6: Importa las herramientas o clases usadas en este modulo.
from src.models.concretos.mesa import Mesa

# Explicacion linea 8: Repite la misma verificacion con distintos valores de entrada.
@pytest.mark.parametrize("texto", ["", "   ", None])
# Explicacion linea 9: Define un escenario de prueba con un resultado esperado.
def test_busqueda_sin_criterio_retorna_lista_vacia(texto):
    # Explicacion linea 10: Asigna un valor, configura un argumento o actualiza un dato del escenario.
    tienda = TiendaMuebles("Deposito Norte")
    # Explicacion linea 11: Ejecuta una operacion del objeto dentro del flujo.
    tienda.agregar_mueble(Silla("Silla Sur", "Roble", "Negro", 80))
    # Explicacion linea 12: Comprueba el resultado real; pytest marca un fallo si no se cumple.
    assert tienda.buscar_muebles_por_nombre(texto) == []

# Explicacion linea 14: Repite la misma verificacion con distintos valores de entrada.
@pytest.mark.parametrize("porcentaje", [-20, 0, 101])
# Explicacion linea 15: Define un escenario de prueba con un resultado esperado.
def test_descuento_fuera_de_limite_es_rechazado(porcentaje):
    # Explicacion linea 16: Asigna un valor, configura un argumento o actualiza un dato del escenario.
    tienda = TiendaMuebles("Deposito Norte")
    # Explicacion linea 17: Comprueba el resultado real; pytest marca un fallo si no se cumple.
    assert tienda.aplicar_descuento("sillas", porcentaje).startswith("Error")
    # Explicacion linea 18: Comprueba el resultado real; pytest marca un fallo si no se cumple.
    assert tienda.obtener_estadisticas()["descuentos_activos"] == {}

# Explicacion linea 20: Repite la misma verificacion con distintos valores de entrada.
@pytest.mark.parametrize("porcentaje", [1, 25, 100])
# Explicacion linea 21: Define un escenario de prueba con un resultado esperado.
def test_descuento_valido_se_registra_con_precision(porcentaje):
    # Explicacion linea 22: Asigna un valor, configura un argumento o actualiza un dato del escenario.
    tienda = TiendaMuebles("Deposito Norte")
    # Explicacion linea 23: Ejecuta una operacion del objeto dentro del flujo.
    tienda.aplicar_descuento("mesas", porcentaje)
    # Explicacion linea 24: Comprueba el resultado real; pytest marca un fallo si no se cumple.
    assert tienda.obtener_estadisticas()["descuentos_activos"]["Mesa"] == pytest.approx(porcentaje / 100)

# Explicacion linea 26: Define un escenario de prueba con un resultado esperado.
def test_dos_ventas_actualizan_las_estadisticas():
    # Explicacion linea 27: Asigna un valor, configura un argumento o actualiza un dato del escenario.
    tienda = TiendaMuebles("Deposito Norte")
    # Explicacion linea 28: Asigna un valor, configura un argumento o actualiza un dato del escenario.
    productos = [Silla("Silla A", "Roble", "Negro", 90), Mesa("Mesa B", "Metal", "Gris", 240)]
    # Explicacion linea 29: Recorre los elementos de una coleccion para procesarlos.
    for producto in productos:
        # Explicacion linea 30: Comprueba el resultado real; pytest marca un fallo si no se cumple.
        assert "agregado" in tienda.agregar_mueble(producto)
    # Explicacion linea 31: Recorre los elementos de una coleccion para procesarlos.
    for producto in productos:
        # Explicacion linea 32: Comprueba el resultado real; pytest marca un fallo si no se cumple.
        assert tienda.realizar_venta(producto, "Cliente B")["precio_final"] > 0
    # Explicacion linea 33: Asigna un valor, configura un argumento o actualiza un dato del escenario.
    estado = tienda.obtener_estadisticas()
    # Explicacion linea 34: Comprueba el resultado real; pytest marca un fallo si no se cumple.
    assert estado["total_muebles"] == 0
    # Explicacion linea 35: Comprueba el resultado real; pytest marca un fallo si no se cumple.
    assert estado["total_muebles_vendidos"] == 2
    # Explicacion linea 36: Comprueba el resultado real; pytest marca un fallo si no se cumple.
    assert estado["valor_total_ventas"] > 0

# Explicacion linea 38: Define un escenario de prueba con un resultado esperado.
def test_venta_no_disponible_no_modifica_estadisticas():
    # Explicacion linea 39: Asigna un valor, configura un argumento o actualiza un dato del escenario.
    tienda = TiendaMuebles("Deposito Norte")
    # Explicacion linea 40: Asigna un valor, configura un argumento o actualiza un dato del escenario.
    articulo = Silla("Fuera de catalogo", "Metal", "Gris", 90)
    # Explicacion linea 41: Comprueba el resultado real; pytest marca un fallo si no se cumple.
    assert "error" in tienda.realizar_venta(articulo)
    # Explicacion linea 42: Comprueba el resultado real; pytest marca un fallo si no se cumple.
    assert tienda.obtener_estadisticas()["ventas_realizadas"] == 0

# Explicacion linea 44: Define un escenario de prueba con un resultado esperado.
def test_busqueda_parcial_ignora_mayusculas():
    # Explicacion linea 45: Asigna un valor, configura un argumento o actualiza un dato del escenario.
    tienda = TiendaMuebles("Deposito Norte")
    # Explicacion linea 46: Asigna un valor, configura un argumento o actualiza un dato del escenario.
    articulo = Mesa("Mesa Central", "Roble", "Blanco", 300)
    # Explicacion linea 47: Ejecuta una operacion del objeto dentro del flujo.
    tienda.agregar_mueble(articulo)
    # Explicacion linea 48: Comprueba el resultado real; pytest marca un fallo si no se cumple.
    assert tienda.buscar_muebles_por_nombre(" cEnTr ") == [articulo]

# Explicacion linea 50: Define un escenario de prueba con un resultado esperado.
def test_precio_defectuoso_no_bloquea_busqueda_por_rango():
    # Explicacion linea 51: Asigna un valor, configura un argumento o actualiza un dato del escenario.
    tienda = TiendaMuebles("Deposito Norte")
    # Explicacion linea 52: Asigna un valor, configura un argumento o actualiza un dato del escenario.
    correcto = Silla("Silla Real", "Metal", "Rojo", 90)
    # Explicacion linea 53: Asigna un valor, configura un argumento o actualiza un dato del escenario.
    defectuoso = Mock()
    # Explicacion linea 54: Asigna un valor, configura un argumento o actualiza un dato del escenario.
    defectuoso.calcular_precio.side_effect = ValueError("precio no disponible")
    # Explicacion linea 55: Ejecuta una operacion del objeto dentro del flujo.
    tienda.agregar_mueble(correcto)
    # Explicacion linea 56: Ejecuta una operacion del objeto dentro del flujo.
    tienda._inventario.append(defectuoso)
    # Explicacion linea 57: Comprueba el resultado real; pytest marca un fallo si no se cumple.
    assert tienda.filtrar_por_precio(0, 1000) == [correcto]

# Explicacion linea 59: Define un escenario de prueba con un resultado esperado.
def test_reporte_incluye_nombre_y_total_inventario():
    # Explicacion linea 60: Asigna un valor, configura un argumento o actualiza un dato del escenario.
    tienda = TiendaMuebles("Deposito Norte")
    # Explicacion linea 61: Ejecuta una operacion del objeto dentro del flujo.
    tienda.agregar_mueble(Silla("Silla", "Madera", "Negro", 75))
    # Explicacion linea 62: Asigna un valor, configura un argumento o actualiza un dato del escenario.
    reporte = tienda.generar_reporte_inventario()
    # Explicacion linea 63: Comprueba el resultado real; pytest marca un fallo si no se cumple.
    assert "Deposito Norte" in reporte
    # Explicacion linea 64: Comprueba el resultado real; pytest marca un fallo si no se cumple.
    assert "Total de muebles: 1" in reporte
