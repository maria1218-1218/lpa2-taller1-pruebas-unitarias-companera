# Explicacion linea 1: Importa las herramientas o clases usadas en este modulo.
import pytest
# Explicacion linea 2: Importa las herramientas o clases usadas en este modulo.
from unittest.mock import patch
# Explicacion linea 3: Importa las herramientas o clases usadas en este modulo.
from src import main
# Explicacion linea 4: Importa las herramientas o clases usadas en este modulo.
from src.ui.menu import MenuTienda

# Explicacion linea 6: Clasifica la prueba para poder ejecutarla por grupo.
@pytest.mark.integration
# Explicacion linea 7: Define un escenario de prueba con un resultado esperado.
def test_escenario_preparacion_catalogo_y_menu(tienda, monkeypatch):
    # Explicacion linea 8: Continua la expresion del bloque anterior o ejecuta esta instruccion.
    monkeypatch.setattr("builtins.input", lambda *args: "")
    # Explicacion linea 9: Continua la expresion del bloque anterior o ejecuta esta instruccion.
    monkeypatch.setattr("src.ui.menu.Confirm.ask", lambda *args, **kwargs: False)
    # Evitar esperas por confirmaciones interactivas

    # Explicacion linea 12: Continua la expresion del bloque anterior o ejecuta esta instruccion.
    main.crear_catalogo_inicial(tienda)
    # Explicacion linea 13: Continua la expresion del bloque anterior o ejecuta esta instruccion.
    main.crear_comedores_ejemplo(tienda)
    # Explicacion linea 14: Continua la expresion del bloque anterior o ejecuta esta instruccion.
    main.aplicar_descuentos_ejemplo(tienda)
    # Explicacion linea 15: Continua la expresion del bloque anterior o ejecuta esta instruccion.
    main.mostrar_estadisticas_iniciales(tienda)
    # Explicacion linea 16: Comprueba el resultado real; pytest marca un fallo si no se cumple.
    assert tienda.buscar_muebles_por_nombre('Silla')
    # Explicacion linea 17: Asigna un valor, configura un argumento o actualiza un dato del escenario.
    menu = MenuTienda(tienda)
    # Explicacion linea 18: Ejecuta una operacion del objeto dentro del flujo.
    menu.mostrar_banner()
    # Explicacion linea 19: Ejecuta una operacion del objeto dentro del flujo.
    menu.mostrar_catalogo_completo()
    # Explicacion linea 20: Ejecuta una operacion del objeto dentro del flujo.
    menu.mostrar_comedores()
    # Explicacion linea 21: Ejecuta una operacion del objeto dentro del flujo.
    menu.mostrar_estadisticas()
    # Explicacion linea 22: Ejecuta una operacion del objeto dentro del flujo.
    menu.generar_reporte_interactivo()

# Explicacion linea 24: Clasifica la prueba para poder ejecutarla por grupo.
@pytest.mark.integration
# Explicacion linea 25: Define un escenario de prueba con un resultado esperado.
def test_escenario_main_con_menu_simulado(monkeypatch):
    # Explicacion linea 26: Continua la expresion del bloque anterior o ejecuta esta instruccion.
    monkeypatch.setattr('builtins.input',lambda *args:'')
    # Explicacion linea 27: Sustituye temporalmente una dependencia externa durante la prueba.
    with patch('src.main.MenuTienda.ejecutar') as run:
        # Explicacion linea 28: Continua la expresion del bloque anterior o ejecuta esta instruccion.
        main.main()
    # Explicacion linea 29: Continua la expresion del bloque anterior o ejecuta esta instruccion.
    run.assert_called_once()

# Explicacion linea 31: Clasifica la prueba para poder ejecutarla por grupo.
@pytest.mark.integration
# Explicacion linea 32: Define un escenario de prueba con un resultado esperado.
def test_escenario_menu_vacio(tienda):
    # Explicacion linea 33: Asigna un valor, configura un argumento o actualiza un dato del escenario.
    menu = MenuTienda(tienda)
    # Explicacion linea 34: Ejecuta una operacion del objeto dentro del flujo.
    menu.mostrar_catalogo_completo()
    # Explicacion linea 35: Ejecuta una operacion del objeto dentro del flujo.
    menu.mostrar_comedores()
    # Explicacion linea 36: Ejecuta una operacion del objeto dentro del flujo.
    menu._mostrar_lista_muebles([])
    # Explicacion linea 37: Sustituye temporalmente una dependencia externa durante la prueba.
    with patch('src.ui.menu.IntPrompt.ask', return_value=0):
        # Explicacion linea 38: Comprueba el resultado real; pytest marca un fallo si no se cumple.
        assert menu.mostrar_menu_principal()==0
    # Explicacion linea 39: Sustituye temporalmente una dependencia externa durante la prueba.
    with patch('src.ui.menu.IntPrompt.ask', return_value=0):
        # Explicacion linea 40: Ejecuta una operacion del objeto dentro del flujo.
        menu.ejecutar()

# Explicacion linea 42: Clasifica la prueba para poder ejecutarla por grupo.
@pytest.mark.integration
# Explicacion linea 43: Define un escenario de prueba con un resultado esperado.
def test_escenario_busquedas_interactivas(tienda, silla, monkeypatch):
    # Explicacion linea 44: Ejecuta una operacion del objeto dentro del flujo.
    tienda.agregar_mueble(silla)
    # Explicacion linea 45: Asigna un valor, configura un argumento o actualiza un dato del escenario.
    menu = MenuTienda(tienda)
    # Explicacion linea 46: Continua la expresion del bloque anterior o ejecuta esta instruccion.
    monkeypatch.setattr('src.ui.menu.time.sleep', lambda _: None)
    # Explicacion linea 47: Sustituye temporalmente una dependencia externa durante la prueba.
    with patch('src.ui.menu.Prompt.ask', side_effect=['Silla', 'Inexistente', '', 'Roble', 'Desconocido', '']):
        # Explicacion linea 48: Ejecuta una operacion del objeto dentro del flujo.
        menu.buscar_muebles_interactivo()
        # Explicacion linea 49: Ejecuta una operacion del objeto dentro del flujo.
        menu.buscar_muebles_interactivo()
        # Explicacion linea 50: Ejecuta una operacion del objeto dentro del flujo.
        menu.buscar_muebles_interactivo()
        # Explicacion linea 51: Ejecuta una operacion del objeto dentro del flujo.
        menu.filtrar_por_material_interactivo()
        # Explicacion linea 52: Ejecuta una operacion del objeto dentro del flujo.
        menu.filtrar_por_material_interactivo()
        # Explicacion linea 53: Ejecuta una operacion del objeto dentro del flujo.
        menu.filtrar_por_material_interactivo()
    # Explicacion linea 54: Sustituye temporalmente una dependencia externa durante la prueba.
    with patch('src.ui.menu.IntPrompt.ask', side_effect=[0, 0, 200, 300, 500, 200, 0]):
        # Explicacion linea 55: Ejecuta una operacion del objeto dentro del flujo.
        menu.filtrar_por_precio_interactivo()
        # Explicacion linea 56: Ejecuta una operacion del objeto dentro del flujo.
        menu.filtrar_por_precio_interactivo()
        # Explicacion linea 57: Ejecuta una operacion del objeto dentro del flujo.
        menu.filtrar_por_precio_interactivo()

# Explicacion linea 59: Clasifica la prueba para poder ejecutarla por grupo.
@pytest.mark.integration
# Explicacion linea 60: Define un escenario de prueba con un resultado esperado.
def test_escenario_ventas_interactivas(tienda, silla, monkeypatch):
    # Explicacion linea 61: Asigna un valor, configura un argumento o actualiza un dato del escenario.
    menu = MenuTienda(tienda)
    # Explicacion linea 62: Ejecuta una operacion del objeto dentro del flujo.
    menu.realizar_venta_interactiva()
    # Explicacion linea 63: Ejecuta una operacion del objeto dentro del flujo.
    tienda.agregar_mueble(silla)
    # Explicacion linea 64: Sustituye temporalmente una dependencia externa durante la prueba.
    with patch('src.ui.menu.IntPrompt.ask', return_value=1), patch('src.ui.menu.Confirm.ask', side_effect=[False, True]), patch('src.ui.menu.Prompt.ask', return_value='Cliente'):
        # Explicacion linea 65: Ejecuta una operacion del objeto dentro del flujo.
        menu.realizar_venta_interactiva()
        # Explicacion linea 66: Comprueba el resultado real; pytest marca un fallo si no se cumple.
        assert tienda.buscar_muebles_por_nombre('Silla')
        # Explicacion linea 67: Ejecuta una operacion del objeto dentro del flujo.
        menu.realizar_venta_interactiva()
    # Explicacion linea 68: Comprueba el resultado real; pytest marca un fallo si no se cumple.
    assert not tienda.buscar_muebles_por_nombre('Silla')

# Explicacion linea 70: Clasifica la prueba para poder ejecutarla por grupo.
@pytest.mark.integration
# Explicacion linea 71: Define un escenario de prueba con un resultado esperado.
def test_escenario_descuento_interactivo(tienda):
    # Explicacion linea 72: Asigna un valor, configura un argumento o actualiza un dato del escenario.
    menu=MenuTienda(tienda)
    # Explicacion linea 73: Sustituye temporalmente una dependencia externa durante la prueba.
    with patch('src.ui.menu.IntPrompt.ask', side_effect=[1, 10]):
        # Explicacion linea 74: Ejecuta una operacion del objeto dentro del flujo.
        menu.aplicar_descuentos_interactivo()
    # Explicacion linea 75: Comprueba el resultado real; pytest marca un fallo si no se cumple.
    assert 'Silla' in tienda._descuentos_activos
