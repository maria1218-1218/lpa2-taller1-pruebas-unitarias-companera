# Explicacion linea 1: Importa las herramientas o clases usadas en este modulo.
from rich.prompt import Confirm
# Explicacion linea 2: Importa las herramientas o clases usadas en este modulo.
from rich.table import Table
# Explicacion linea 3: Importa las herramientas o clases usadas en este modulo.
from rich.prompt import Prompt
# Explicacion linea 4: Importa las herramientas o clases usadas en este modulo.
from rich.prompt import IntPrompt

# Explicacion linea 6: Documenta el objetivo y el uso de este bloque.
"""
Interfaz de usuario usando Rich para crear un menú interactivo y atractivo.
"""

# Explicacion linea 10: Importa las herramientas o clases usadas en este modulo.
from rich.console import Console
# Explicacion linea 11: Importa las herramientas o clases usadas en este modulo.
from rich.text import Text
# Explicacion linea 12: Importa las herramientas o clases usadas en este modulo.
from rich.panel import Panel
# Explicacion linea 13: Importa las herramientas o clases usadas en este modulo.
from typing import List, Optional
# Explicacion linea 14: Importa las herramientas o clases usadas en este modulo.
import time

# Corrección de imports para ejecución directa
# Explicacion linea 17: Importa las herramientas o clases usadas en este modulo.
from services.tienda import TiendaMuebles
# Explicacion linea 18: Importa las herramientas o clases usadas en este modulo.
from models.mueble import Mueble
# TODO: Importar los servicios y modelos


# Explicacion linea 22: Declara una clase que organiza atributos y operaciones del dominio.
class MenuTienda:
    # Explicacion linea 23: Documenta el objetivo y el uso de este bloque.
    """
    Clase que maneja la interfaz de usuario de la tienda usando Rich.

    Proporciona un menú interactivo con opciones para:
    - Ver catálogo de muebles
    - Buscar y filtrar productos
    - Realizar ventas
    - Ver estadísticas
    - Gestionar inventario

    Conceptos aplicados:
    - Separación de responsabilidades: La UI está separada de la lógica de negocio
    - Encapsulación: Agrupa toda la lógica de interfaz de usuario
    - Composición: Usa una instancia de TiendaMuebles para las operaciones
    """

    # Explicacion linea 39: Declara la funcion y sus parametros de entrada.
    def __init__(self, tienda: "TiendaMuebles"):
        # Explicacion linea 40: Documenta el objetivo y el uso de este bloque.
        """
        Constructor del menú.

        Args:
            tienda: Instancia de TiendaMuebles para las operaciones
        """
        # Inicializar atributos
        # Explicacion linea 47: Asigna un valor, configura un argumento o actualiza un dato del escenario.
        self.tienda = tienda
        # Explicacion linea 48: Asigna un valor, configura un argumento o actualiza un dato del escenario.
        self.console = Console()
        # Explicacion linea 49: Asigna un valor, configura un argumento o actualiza un dato del escenario.
        self.running = True

    # Explicacion linea 51: Declara la funcion y sus parametros de entrada.
    def mostrar_catalogo_completo(self):
        # Explicacion linea 52: Documenta el objetivo y el uso de este bloque.
        """Muestra todos los muebles disponibles en una tabla."""

        # Implementar visualización del catálogo
        # Explicacion linea 55: Asigna un valor, configura un argumento o actualiza un dato del escenario.
        muebles = self.tienda._inventario  # Acceso directo para el ejemplo

        # Explicacion linea 57: Evalua una condicion para elegir el camino de ejecucion.
        if not muebles:
            # Explicacion linea 58: Ejecuta una operacion del objeto dentro del flujo.
            self.console.print("[yellow]No hay muebles en el inventario.[/yellow]")
            # Explicacion linea 59: Continua la expresion del bloque anterior o ejecuta esta instruccion.
            return

        # Explicacion linea 61: Asigna un valor, configura un argumento o actualiza un dato del escenario.
        table = Table(title="📋 Catálogo de Muebles")
        # Explicacion linea 62: Asigna un valor, configura un argumento o actualiza un dato del escenario.
        table.add_column("ID", style="cyan", no_wrap=True)
        # Explicacion linea 63: Asigna un valor, configura un argumento o actualiza un dato del escenario.
        table.add_column("Nombre", style="magenta")
        # Explicacion linea 64: Asigna un valor, configura un argumento o actualiza un dato del escenario.
        table.add_column("Tipo", style="green")
        # Explicacion linea 65: Asigna un valor, configura un argumento o actualiza un dato del escenario.
        table.add_column("Material", style="yellow")
        # Explicacion linea 66: Asigna un valor, configura un argumento o actualiza un dato del escenario.
        table.add_column("Color", style="blue")
        # Explicacion linea 67: Asigna un valor, configura un argumento o actualiza un dato del escenario.
        table.add_column("Precio", style="red", justify="right")

        # Explicacion linea 69: Recorre los elementos de una coleccion para procesarlos.
        for i, mueble in enumerate(muebles, 1):
            # Explicacion linea 70: Inicia una operacion que puede generar una excepcion.
            try:
                # Explicacion linea 71: Asigna un valor, configura un argumento o actualiza un dato del escenario.
                precio = f"${mueble.calcular_precio():.2f}"
                # Explicacion linea 72: Asigna un valor, configura un argumento o actualiza un dato del escenario.
                tipo = type(mueble).__name__
                # Explicacion linea 73: Continua la expresion del bloque anterior o ejecuta esta instruccion.
                table.add_row(
                    # Explicacion linea 74: Continua la expresion del bloque anterior o ejecuta esta instruccion.
                    str(i), mueble.nombre, tipo, mueble.material, mueble.color, precio
                # Explicacion linea 75: Cierra la expresion o estructura iniciada anteriormente.
                )
            # Explicacion linea 76: Controla la excepcion indicada sin detener el flujo principal.
            except Exception as e:
                # Explicacion linea 77: Continua la expresion del bloque anterior o ejecuta esta instruccion.
                table.add_row(str(i), mueble.nombre, "Error", "-", "-", "Error")

        # Explicacion linea 79: Ejecuta una operacion del objeto dentro del flujo.
        self.console.print(table)

    # Explicacion linea 81: Declara la funcion y sus parametros de entrada.
    def buscar_muebles_interactivo(self):
        # Explicacion linea 82: Documenta el objetivo y el uso de este bloque.
        """Interfaz interactiva para buscar muebles."""

        # Explicacion linea 84: Asigna un valor, configura un argumento o actualiza un dato del escenario.
        termino_busqueda = Prompt.ask(
            # Explicacion linea 85: Continua la expresion del bloque anterior o ejecuta esta instruccion.
            "[green]Ingresa el nombre o parte del nombre a buscar[/green]"
        # Explicacion linea 86: Cierra la expresion o estructura iniciada anteriormente.
        )

        # Explicacion linea 88: Evalua una condicion para elegir el camino de ejecucion.
        if not termino_busqueda.strip():
            # Explicacion linea 89: Ejecuta una operacion del objeto dentro del flujo.
            self.console.print("[red]Término de búsqueda vacío.[/red]")
            # Explicacion linea 90: Continua la expresion del bloque anterior o ejecuta esta instruccion.
            return

        # Explicacion linea 92: Abre un contexto que libera sus recursos al terminar.
        with self.console.status("[bold green]Buscando muebles..."):
            # Explicacion linea 93: Continua la expresion del bloque anterior o ejecuta esta instruccion.
            time.sleep(0.5)  # Simular tiempo de búsqueda
            # Explicacion linea 94: Asigna un valor, configura un argumento o actualiza un dato del escenario.
            resultados = self.tienda.buscar_muebles_por_nombre(termino_busqueda)

        # Explicacion linea 96: Evalua una condicion para elegir el camino de ejecucion.
        if not resultados:
            # Explicacion linea 97: Ejecuta una operacion del objeto dentro del flujo.
            self.console.print(
                # Explicacion linea 98: Continua la expresion del bloque anterior o ejecuta esta instruccion.
                f"[yellow]No se encontraron muebles que contengan '{termino_busqueda}'.[/yellow]"
            # Explicacion linea 99: Cierra la expresion o estructura iniciada anteriormente.
            )
            # Explicacion linea 100: Continua la expresion del bloque anterior o ejecuta esta instruccion.
            return

        # Explicacion linea 102: Ejecuta una operacion del objeto dentro del flujo.
        self.console.print(
            # Explicacion linea 103: Continua la expresion del bloque anterior o ejecuta esta instruccion.
            f"\n[green]Se encontraron {len(resultados)} resultado(s):[/green]"
        # Explicacion linea 104: Cierra la expresion o estructura iniciada anteriormente.
        )
        # Explicacion linea 105: Ejecuta una operacion del objeto dentro del flujo.
        self._mostrar_lista_muebles(resultados)

    # Explicacion linea 107: Declara la funcion y sus parametros de entrada.
    def filtrar_por_precio_interactivo(self):
        # Explicacion linea 108: Documenta el objetivo y el uso de este bloque.
        """Interfaz interactiva para filtrar por precio."""

        # Explicacion linea 110: Ejecuta una operacion del objeto dentro del flujo.
        self.console.print("[cyan]Filtrar muebles por rango de precio[/cyan]")

        # Explicacion linea 112: Asigna un valor, configura un argumento o actualiza un dato del escenario.
        precio_min = IntPrompt.ask("Precio mínimo", default=0, show_default=True)

        # Explicacion linea 114: Asigna un valor, configura un argumento o actualiza un dato del escenario.
        precio_max = IntPrompt.ask(
            # Explicacion linea 115: Asigna un valor, configura un argumento o actualiza un dato del escenario.
            "Precio máximo (0 = sin límite)", default=0, show_default=True
        # Explicacion linea 116: Cierra la expresion o estructura iniciada anteriormente.
        )

        # Explicacion linea 118: Evalua una condicion para elegir el camino de ejecucion.
        if precio_max == 0:
            # Explicacion linea 119: Asigna un valor, configura un argumento o actualiza un dato del escenario.
            precio_max = float("inf")

        # Explicacion linea 121: Evalua una condicion para elegir el camino de ejecucion.
        if precio_min > precio_max:
            # Explicacion linea 122: Ejecuta una operacion del objeto dentro del flujo.
            self.console.print(
                # Explicacion linea 123: Continua la expresion del bloque anterior o ejecuta esta instruccion.
                "[red]Error: El precio mínimo no puede ser mayor al máximo.[/red]"
            # Explicacion linea 124: Cierra la expresion o estructura iniciada anteriormente.
            )
            # Explicacion linea 125: Continua la expresion del bloque anterior o ejecuta esta instruccion.
            return

        # Explicacion linea 127: Abre un contexto que libera sus recursos al terminar.
        with self.console.status("[bold green]Filtrando muebles..."):
            # Explicacion linea 128: Continua la expresion del bloque anterior o ejecuta esta instruccion.
            time.sleep(0.3)
            # Explicacion linea 129: Asigna un valor, configura un argumento o actualiza un dato del escenario.
            resultados = self.tienda.filtrar_por_precio(precio_min, precio_max)

        # Explicacion linea 131: Evalua una condicion para elegir el camino de ejecucion.
        if not resultados:
            # Explicacion linea 132: Ejecuta una operacion del objeto dentro del flujo.
            self.console.print(
                # Explicacion linea 133: Continua la expresion del bloque anterior o ejecuta esta instruccion.
                f"[yellow]No hay muebles en el rango ${precio_min} - ${precio_max}.[/yellow]"
            # Explicacion linea 134: Cierra la expresion o estructura iniciada anteriormente.
            )
            # Explicacion linea 135: Continua la expresion del bloque anterior o ejecuta esta instruccion.
            return

        # Explicacion linea 137: Ejecuta una operacion del objeto dentro del flujo.
        self.console.print(
            # Explicacion linea 138: Continua la expresion del bloque anterior o ejecuta esta instruccion.
            f"\n[green]Se encontraron {len(resultados)} mueble(s) en el rango:[/green]"
        # Explicacion linea 139: Cierra la expresion o estructura iniciada anteriormente.
        )
        # Explicacion linea 140: Ejecuta una operacion del objeto dentro del flujo.
        self._mostrar_lista_muebles(resultados)

    # Explicacion linea 142: Declara la funcion y sus parametros de entrada.
    def filtrar_por_material_interactivo(self):
        # Explicacion linea 143: Documenta el objetivo y el uso de este bloque.
        """Interfaz interactiva para filtrar por material."""

        # Explicacion linea 145: Asigna un valor, configura un argumento o actualiza un dato del escenario.
        material = Prompt.ask(
            # Explicacion linea 146: Continua la expresion del bloque anterior o ejecuta esta instruccion.
            "[green]Ingresa el material a buscar (ej: madera, metal, plástico)[/green]"
        # Explicacion linea 147: Cierra la expresion o estructura iniciada anteriormente.
        )

        # Explicacion linea 149: Evalua una condicion para elegir el camino de ejecucion.
        if not material.strip():
            # Explicacion linea 150: Ejecuta una operacion del objeto dentro del flujo.
            self.console.print("[red]Material no puede estar vacío.[/red]")
            # Explicacion linea 151: Continua la expresion del bloque anterior o ejecuta esta instruccion.
            return

        # Explicacion linea 153: Abre un contexto que libera sus recursos al terminar.
        with self.console.status(f"[bold green]Buscando muebles de {material}..."):
            # Explicacion linea 154: Continua la expresion del bloque anterior o ejecuta esta instruccion.
            time.sleep(0.3)
            # Explicacion linea 155: Asigna un valor, configura un argumento o actualiza un dato del escenario.
            resultados = self.tienda.filtrar_por_material(material)

        # Explicacion linea 157: Evalua una condicion para elegir el camino de ejecucion.
        if not resultados:
            # Explicacion linea 158: Ejecuta una operacion del objeto dentro del flujo.
            self.console.print(
                # Explicacion linea 159: Continua la expresion del bloque anterior o ejecuta esta instruccion.
                f"[yellow]No hay muebles de material '{material}'.[/yellow]"
            # Explicacion linea 160: Cierra la expresion o estructura iniciada anteriormente.
            )
            # Explicacion linea 161: Continua la expresion del bloque anterior o ejecuta esta instruccion.
            return

        # Explicacion linea 163: Ejecuta una operacion del objeto dentro del flujo.
        self.console.print(f"\n[green]Muebles de {material} encontrados:[/green]")
        # Explicacion linea 164: Ejecuta una operacion del objeto dentro del flujo.
        self._mostrar_lista_muebles(resultados)

    # Explicacion linea 166: Declara la funcion y sus parametros de entrada.
    def mostrar_comedores(self):
        # Explicacion linea 167: Documenta el objetivo y el uso de este bloque.
        """Muestra todos los comedores disponibles."""

        # Explicacion linea 169: Asigna un valor, configura un argumento o actualiza un dato del escenario.
        comedores = self.tienda._comedores

        # Explicacion linea 171: Evalua una condicion para elegir el camino de ejecucion.
        if not comedores:
            # Explicacion linea 172: Ejecuta una operacion del objeto dentro del flujo.
            self.console.print("[yellow]No hay comedores disponibles.[/yellow]")
            # Explicacion linea 173: Continua la expresion del bloque anterior o ejecuta esta instruccion.
            return

        # Explicacion linea 175: Recorre los elementos de una coleccion para procesarlos.
        for i, comedor in enumerate(comedores, 1):
            # Explicacion linea 176: Asigna un valor, configura un argumento o actualiza un dato del escenario.
            panel_content = comedor.obtener_descripcion_completa()
            # Explicacion linea 177: Asigna un valor, configura un argumento o actualiza un dato del escenario.
            panel = Panel(panel_content, title=f"Comedor #{i}", border_style="green")
            # Explicacion linea 178: Ejecuta una operacion del objeto dentro del flujo.
            self.console.print(panel)

    # Explicacion linea 180: Declara la funcion y sus parametros de entrada.
    def realizar_venta_interactiva(self):
        # Explicacion linea 181: Documenta el objetivo y el uso de este bloque.
        """Interfaz interactiva para realizar ventas."""

        # Explicacion linea 183: Asigna un valor, configura un argumento o actualiza un dato del escenario.
        muebles = self.tienda._inventario

        # Explicacion linea 185: Evalua una condicion para elegir el camino de ejecucion.
        if not muebles:
            # Explicacion linea 186: Ejecuta una operacion del objeto dentro del flujo.
            self.console.print("[red]No hay muebles disponibles para venta.[/red]")
            # Explicacion linea 187: Continua la expresion del bloque anterior o ejecuta esta instruccion.
            return

        # Explicacion linea 189: Ejecuta una operacion del objeto dentro del flujo.
        self.console.print("[cyan]Selecciona un mueble para vender:[/cyan]")
        # Explicacion linea 190: Asigna un valor, configura un argumento o actualiza un dato del escenario.
        self._mostrar_lista_muebles(muebles, numerada=True)

        # Explicacion linea 192: Inicia una operacion que puede generar una excepcion.
        try:
            # Explicacion linea 193: Asigna un valor, configura un argumento o actualiza un dato del escenario.
            indice = IntPrompt.ask(
                # Explicacion linea 194: Continua la expresion del bloque anterior o ejecuta esta instruccion.
                "Número del mueble",
                # Explicacion linea 195: Asigna un valor, configura un argumento o actualiza un dato del escenario.
                choices=[str(i) for i in range(1, len(muebles) + 1)],
            # Explicacion linea 196: Cierra la expresion o estructura iniciada anteriormente.
            )

            # Explicacion linea 198: Asigna un valor, configura un argumento o actualiza un dato del escenario.
            mueble_seleccionado = muebles[indice - 1]

            # Mostrar detalles del mueble
            # Explicacion linea 201: Ejecuta una operacion del objeto dentro del flujo.
            self.console.print(f"\n[green]Mueble seleccionado:[/green]")
            # Explicacion linea 202: Ejecuta una operacion del objeto dentro del flujo.
            self.console.print(mueble_seleccionado.obtener_descripcion())

            # Explicacion linea 204: Asigna un valor, configura un argumento o actualiza un dato del escenario.
            confirmar = Confirm.ask("\n¿Confirmar la venta?")
            # Explicacion linea 205: Evalua una condicion para elegir el camino de ejecucion.
            if not confirmar:
                # Explicacion linea 206: Ejecuta una operacion del objeto dentro del flujo.
                self.console.print("[yellow]Venta cancelada.[/yellow]")
                # Explicacion linea 207: Continua la expresion del bloque anterior o ejecuta esta instruccion.
                return

            # Explicacion linea 209: Asigna un valor, configura un argumento o actualiza un dato del escenario.
            cliente = Prompt.ask("Nombre del cliente", default="Cliente Anónimo")

            # Explicacion linea 211: Asigna un valor, configura un argumento o actualiza un dato del escenario.
            resultado = self.tienda.realizar_venta(mueble_seleccionado, cliente)

            # Explicacion linea 213: Evalua una condicion para elegir el camino de ejecucion.
            if "error" in resultado:
                # Explicacion linea 214: Ejecuta una operacion del objeto dentro del flujo.
                self.console.print(f"[red]Error: {resultado['error']}[/red]")
            # Explicacion linea 215: Ejecuta la alternativa cuando las condiciones anteriores no aplican.
            else:
                # Explicacion linea 216: Ejecuta una operacion del objeto dentro del flujo.
                self._mostrar_comprobante_venta(resultado)

        # Explicacion linea 218: Controla la excepcion indicada sin detener el flujo principal.
        except (ValueError, IndexError):
            # Explicacion linea 219: Ejecuta una operacion del objeto dentro del flujo.
            self.console.print("[red]Selección inválida.[/red]")

    # Explicacion linea 221: Declara la funcion y sus parametros de entrada.
    def mostrar_estadisticas(self):
        # Explicacion linea 222: Documenta el objetivo y el uso de este bloque.
        """Muestra las estadísticas de la tienda."""

        # Explicacion linea 224: Abre un contexto que libera sus recursos al terminar.
        with self.console.status("[bold green]Calculando estadísticas..."):
            # Explicacion linea 225: Continua la expresion del bloque anterior o ejecuta esta instruccion.
            time.sleep(0.5)
            # Explicacion linea 226: Asigna un valor, configura un argumento o actualiza un dato del escenario.
            stats = self.tienda.obtener_estadisticas()
            # Explicacion linea 227: Evalua una condicion para elegir el camino de ejecucion.
            if not isinstance(stats, dict):
                # Explicacion linea 228: Asigna un valor, configura un argumento o actualiza un dato del escenario.
                stats = {}
        # Explicacion linea 229: Asigna un valor, configura un argumento o actualiza un dato del escenario.
        table = Table(title="📊 Estadísticas de la Tienda")
        # Explicacion linea 230: Asigna un valor, configura un argumento o actualiza un dato del escenario.
        table.add_column("Métrica", style="cyan", no_wrap=True)
        # Explicacion linea 231: Asigna un valor, configura un argumento o actualiza un dato del escenario.
        table.add_column("Valor", style="magenta", justify="right")
        # Explicacion linea 232: Continua la expresion del bloque anterior o ejecuta esta instruccion.
        table.add_row("Total de muebles", str(stats.get("total_muebles", 0)))
        # Explicacion linea 233: Continua la expresion del bloque anterior o ejecuta esta instruccion.
        table.add_row("Total de comedores", str(stats.get("total_comedores", 0)))
        # Explicacion linea 234: Continua la expresion del bloque anterior o ejecuta esta instruccion.
        table.add_row(
            # Explicacion linea 235: Continua la expresion del bloque anterior o ejecuta esta instruccion.
            "Valor del inventario", f"${stats.get('valor_inventario', 0):.2f}"
        # Explicacion linea 236: Cierra la expresion o estructura iniciada anteriormente.
        )
        # Explicacion linea 237: Continua la expresion del bloque anterior o ejecuta esta instruccion.
        table.add_row("Ventas realizadas", str(stats.get("ventas_realizadas", 0)))
        # Explicacion linea 238: Continua la expresion del bloque anterior o ejecuta esta instruccion.
        table.add_row("Descuentos activos", str(stats.get("descuentos_activos", {})))
        # Estadísticas acumulativas
        # Explicacion linea 240: Continua la expresion del bloque anterior o ejecuta esta instruccion.
        table.add_row(
            # Explicacion linea 241: Continua la expresion del bloque anterior o ejecuta esta instruccion.
            "Total muebles vendidos (acumulado)",
            # Explicacion linea 242: Continua la expresion del bloque anterior o ejecuta esta instruccion.
            str(stats.get("total_muebles_vendidos", 0)),
        # Explicacion linea 243: Cierra la expresion o estructura iniciada anteriormente.
        )
        # Explicacion linea 244: Continua la expresion del bloque anterior o ejecuta esta instruccion.
        table.add_row(
            # Explicacion linea 245: Continua la expresion del bloque anterior o ejecuta esta instruccion.
            "Valor total de ventas (acumulado)",
            # Explicacion linea 246: Continua la expresion del bloque anterior o ejecuta esta instruccion.
            f"${stats.get('valor_total_ventas', 0):.2f}",
        # Explicacion linea 247: Cierra la expresion o estructura iniciada anteriormente.
        )
        # Explicacion linea 248: Ejecuta una operacion del objeto dentro del flujo.
        self.console.print(table)
        # Explicacion linea 249: Asigna un valor, configura un argumento o actualiza un dato del escenario.
        tipos = stats.get("tipos_muebles", {})
        # Explicacion linea 250: Evalua una condicion para elegir el camino de ejecucion.
        if tipos:
            # Explicacion linea 251: Ejecuta una operacion del objeto dentro del flujo.
            self.console.print("\n[cyan]Distribución por tipos:[/cyan]")
            # Explicacion linea 252: Recorre los elementos de una coleccion para procesarlos.
            for tipo, cantidad in tipos.items():
                # Explicacion linea 253: Ejecuta una operacion del objeto dentro del flujo.
                self.console.print(f"  • {tipo}: {cantidad} unidades")

    # Explicacion linea 255: Declara la funcion y sus parametros de entrada.
    def generar_reporte_interactivo(self):
        # Explicacion linea 256: Documenta el objetivo y el uso de este bloque.
        """Genera y muestra el reporte de inventario."""

        # Explicacion linea 258: Abre un contexto que libera sus recursos al terminar.
        with self.console.status("[bold green]Generando reporte..."):
            # Explicacion linea 259: Continua la expresion del bloque anterior o ejecuta esta instruccion.
            time.sleep(1)  # Simular tiempo de generación
            # Explicacion linea 260: Asigna un valor, configura un argumento o actualiza un dato del escenario.
            reporte = self.tienda.generar_reporte_inventario()

        # Explicacion linea 262: Asigna un valor, configura un argumento o actualiza un dato del escenario.
        panel = Panel(
            # Explicacion linea 263: Continua la expresion del bloque anterior o ejecuta esta instruccion.
            reporte,
            # Explicacion linea 264: Asigna un valor, configura un argumento o actualiza un dato del escenario.
            title="📋 Reporte de Inventario",
            # Explicacion linea 265: Asigna un valor, configura un argumento o actualiza un dato del escenario.
            border_style="blue",
            # Explicacion linea 266: Asigna un valor, configura un argumento o actualiza un dato del escenario.
            padding=(1, 2),
        # Explicacion linea 267: Cierra la expresion o estructura iniciada anteriormente.
        )

        # Explicacion linea 269: Ejecuta una operacion del objeto dentro del flujo.
        self.console.print(panel)

        # Preguntar si desea guardar el reporte
        # Explicacion linea 272: Asigna un valor, configura un argumento o actualiza un dato del escenario.
        guardar = Confirm.ask("¿Deseas guardar el reporte en un archivo?")
        # Explicacion linea 273: Evalua una condicion para elegir el camino de ejecucion.
        if guardar:
            # Explicacion linea 274: Asigna un valor, configura un argumento o actualiza un dato del escenario.
            filename = Prompt.ask(
                # Explicacion linea 275: Asigna un valor, configura un argumento o actualiza un dato del escenario.
                "Nombre del archivo", default="reporte_inventario.txt"
            # Explicacion linea 276: Cierra la expresion o estructura iniciada anteriormente.
            )
            # Explicacion linea 277: Inicia una operacion que puede generar una excepcion.
            try:
                # Explicacion linea 278: Abre un contexto que libera sus recursos al terminar.
                with open(filename, "w", encoding="utf-8") as f:
                    # Explicacion linea 279: Continua la expresion del bloque anterior o ejecuta esta instruccion.
                    f.write(reporte)
                # Explicacion linea 280: Ejecuta una operacion del objeto dentro del flujo.
                self.console.print(f"[green]Reporte guardado en {filename}[/green]")
            # Explicacion linea 281: Controla la excepcion indicada sin detener el flujo principal.
            except Exception as e:
                # Explicacion linea 282: Ejecuta una operacion del objeto dentro del flujo.
                self.console.print(f"[red]Error al guardar: {str(e)}[/red]")

    # Explicacion linea 284: Declara la funcion y sus parametros de entrada.
    def aplicar_descuentos_interactivo(self):
        # Explicacion linea 285: Documenta el objetivo y el uso de este bloque.
        """Interfaz para aplicar descuentos por categoría."""

        # Explicacion linea 287: Asigna un valor, configura un argumento o actualiza un dato del escenario.
        categorias_disponibles = [
            # Explicacion linea 288: Continua la expresion del bloque anterior o ejecuta esta instruccion.
            "silla",
            # Explicacion linea 289: Continua la expresion del bloque anterior o ejecuta esta instruccion.
            "mesa",
            # Explicacion linea 290: Continua la expresion del bloque anterior o ejecuta esta instruccion.
            "sofa",
            # Explicacion linea 291: Continua la expresion del bloque anterior o ejecuta esta instruccion.
            "cama",
            # Explicacion linea 292: Continua la expresion del bloque anterior o ejecuta esta instruccion.
            "armario",
            # Explicacion linea 293: Continua la expresion del bloque anterior o ejecuta esta instruccion.
            "escritorio",
        # Explicacion linea 294: Cierra la expresion o estructura iniciada anteriormente.
        ]

        # Explicacion linea 296: Ejecuta una operacion del objeto dentro del flujo.
        self.console.print("[cyan]Categorías disponibles:[/cyan]")
        # Explicacion linea 297: Recorre los elementos de una coleccion para procesarlos.
        for i, categoria in enumerate(categorias_disponibles, 1):
            # Explicacion linea 298: Ejecuta una operacion del objeto dentro del flujo.
            self.console.print(f"  {i}. {categoria.title()}")

        # Explicacion linea 300: Inicia una operacion que puede generar una excepcion.
        try:
            # Explicacion linea 301: Asigna un valor, configura un argumento o actualiza un dato del escenario.
            indice = IntPrompt.ask(
                # Explicacion linea 302: Continua la expresion del bloque anterior o ejecuta esta instruccion.
                "Selecciona una categoría",
                # Explicacion linea 303: Asigna un valor, configura un argumento o actualiza un dato del escenario.
                choices=[str(i) for i in range(1, len(categorias_disponibles) + 1)],
            # Explicacion linea 304: Cierra la expresion o estructura iniciada anteriormente.
            )

            # Explicacion linea 306: Asigna un valor, configura un argumento o actualiza un dato del escenario.
            categoria = categorias_disponibles[indice - 1]

            # Explicacion linea 308: Asigna un valor, configura un argumento o actualiza un dato del escenario.
            porcentaje = IntPrompt.ask(
                # Explicacion linea 309: Continua la expresion del bloque anterior o ejecuta esta instruccion.
                f"Porcentaje de descuento para {categoria}s (1-50)",
                # Explicacion linea 310: Asigna un valor, configura un argumento o actualiza un dato del escenario.
                choices=[str(i) for i in range(1, 51)],
            # Explicacion linea 311: Cierra la expresion o estructura iniciada anteriormente.
            )

            # Explicacion linea 313: Asigna un valor, configura un argumento o actualiza un dato del escenario.
            resultado = self.tienda.aplicar_descuento(categoria, porcentaje)
            # Explicacion linea 314: Ejecuta una operacion del objeto dentro del flujo.
            self.console.print(f"[green]{resultado}[/green]")

        # Explicacion linea 316: Controla la excepcion indicada sin detener el flujo principal.
        except (ValueError, IndexError):
            # Explicacion linea 317: Ejecuta una operacion del objeto dentro del flujo.
            self.console.print("[red]Selección inválida.[/red]")

    # Explicacion linea 319: Declara la funcion y sus parametros de entrada.
    def _mostrar_lista_muebles(self, muebles: List["Mueble"], numerada: bool = False):
        # Explicacion linea 320: Documenta el objetivo y el uso de este bloque.
        """
        Muestra una lista de muebles en formato tabla.
        Método auxiliar privado.

        Args:
            muebles: Lista de muebles a mostrar
            numerada: Si incluir números para selección
        """

        # Explicacion linea 329: Asigna un valor, configura un argumento o actualiza un dato del escenario.
        table = Table()

        # Explicacion linea 331: Evalua una condicion para elegir el camino de ejecucion.
        if numerada:
            # Explicacion linea 332: Asigna un valor, configura un argumento o actualiza un dato del escenario.
            table.add_column("#", style="cyan", no_wrap=True)

        # Explicacion linea 334: Asigna un valor, configura un argumento o actualiza un dato del escenario.
        table.add_column("Nombre", style="magenta")
        # Explicacion linea 335: Asigna un valor, configura un argumento o actualiza un dato del escenario.
        table.add_column("Tipo", style="green")
        # Explicacion linea 336: Asigna un valor, configura un argumento o actualiza un dato del escenario.
        table.add_column("Material", style="yellow")
        # Explicacion linea 337: Asigna un valor, configura un argumento o actualiza un dato del escenario.
        table.add_column("Precio", style="red", justify="right")

        # Explicacion linea 339: Recorre los elementos de una coleccion para procesarlos.
        for i, mueble in enumerate(muebles, 1):
            # Explicacion linea 340: Inicia una operacion que puede generar una excepcion.
            try:
                # Explicacion linea 341: Asigna un valor, configura un argumento o actualiza un dato del escenario.
                precio = f"${mueble.calcular_precio():.2f}"
                # Explicacion linea 342: Asigna un valor, configura un argumento o actualiza un dato del escenario.
                tipo = type(mueble).__name__

                # Explicacion linea 344: Asigna un valor, configura un argumento o actualiza un dato del escenario.
                row_data = [mueble.nombre, tipo, mueble.material, precio]
                # Explicacion linea 345: Evalua una condicion para elegir el camino de ejecucion.
                if numerada:
                    # Explicacion linea 346: Continua la expresion del bloque anterior o ejecuta esta instruccion.
                    row_data.insert(0, str(i))

                # Explicacion linea 348: Continua la expresion del bloque anterior o ejecuta esta instruccion.
                table.add_row(*row_data)
            # Explicacion linea 349: Controla la excepcion indicada sin detener el flujo principal.
            except Exception:
                # Explicacion linea 350: Asigna un valor, configura un argumento o actualiza un dato del escenario.
                row_data = [mueble.nombre, "Error", mueble.material, "Error"]
                # Explicacion linea 351: Evalua una condicion para elegir el camino de ejecucion.
                if numerada:
                    # Explicacion linea 352: Continua la expresion del bloque anterior o ejecuta esta instruccion.
                    row_data.insert(0, str(i))
                # Explicacion linea 353: Continua la expresion del bloque anterior o ejecuta esta instruccion.
                table.add_row(*row_data)

        # Explicacion linea 355: Ejecuta una operacion del objeto dentro del flujo.
        self.console.print(table)

    # Explicacion linea 357: Declara la funcion y sus parametros de entrada.
    def _mostrar_comprobante_venta(self, venta: dict):
        # Explicacion linea 358: Documenta el objetivo y el uso de este bloque.
        """
        Muestra el comprobante de venta.
        Método auxiliar privado.

        Args:
            venta: Diccionario con información de la venta
        """

        # Explicacion linea 366: Asigna un valor, configura un argumento o actualiza un dato del escenario.
        comprobante = f"""
        # Explicacion linea 367: Continua la expresion del bloque anterior o ejecuta esta instruccion.
        🧾 COMPROBANTE DE VENTA 🧾
        
        # Explicacion linea 369: Continua la expresion del bloque anterior o ejecuta esta instruccion.
        Cliente: {venta["cliente"]}
        # Explicacion linea 370: Continua la expresion del bloque anterior o ejecuta esta instruccion.
        Producto: {venta["mueble"]}
        # Explicacion linea 371: Continua la expresion del bloque anterior o ejecuta esta instruccion.
        Precio original: ${venta["precio_original"]:.2f}
        # Explicacion linea 372: Continua la expresion del bloque anterior o ejecuta esta instruccion.
        Descuento aplicado: {venta["descuento"]:.1f}%
        # Explicacion linea 373: Continua la expresion del bloque anterior o ejecuta esta instruccion.
        PRECIO FINAL: ${venta["precio_final"]:.2f}
        
        # Explicacion linea 375: Continua la expresion del bloque anterior o ejecuta esta instruccion.
        ¡Gracias por su compra!
        # Explicacion linea 376: Documenta el objetivo y el uso de este bloque.
        """

        # Explicacion linea 378: Asigna un valor, configura un argumento o actualiza un dato del escenario.
        panel = Panel(
            # Explicacion linea 379: Continua la expresion del bloque anterior o ejecuta esta instruccion.
            comprobante.strip(),
            # Explicacion linea 380: Asigna un valor, configura un argumento o actualiza un dato del escenario.
            title="Venta Exitosa",
            # Explicacion linea 381: Asigna un valor, configura un argumento o actualiza un dato del escenario.
            border_style="green",
            # Explicacion linea 382: Asigna un valor, configura un argumento o actualiza un dato del escenario.
            padding=(1, 2),
        # Explicacion linea 383: Cierra la expresion o estructura iniciada anteriormente.
        )

        # Explicacion linea 385: Ejecuta una operacion del objeto dentro del flujo.
        self.console.print(panel)

    # Explicacion linea 387: Declara la funcion y sus parametros de entrada.
    def ejecutar(self):
        # Explicacion linea 388: Documenta el objetivo y el uso de este bloque.
        """Ejecuta el bucle principal del menú."""

        # Explicacion linea 390: Ejecuta una operacion del objeto dentro del flujo.
        self.console.clear()
        # Explicacion linea 391: Ejecuta una operacion del objeto dentro del flujo.
        self.mostrar_banner()

        # Explicacion linea 393: Repite la operacion mientras la condicion sea verdadera.
        while self.running:
            # Explicacion linea 394: Inicia una operacion que puede generar una excepcion.
            try:
                # Explicacion linea 395: Asigna un valor, configura un argumento o actualiza un dato del escenario.
                opcion = self.mostrar_menu_principal()

                # Explicacion linea 397: Evalua una condicion para elegir el camino de ejecucion.
                if opcion == 0:
                    # Explicacion linea 398: Ejecuta una operacion del objeto dentro del flujo.
                    self.console.print("[red]¡Hasta luego! 👋[/red]")
                    # Explicacion linea 399: Asigna un valor, configura un argumento o actualiza un dato del escenario.
                    self.running = False
                # Explicacion linea 400: Evalua una condicion para elegir el camino de ejecucion.
                elif opcion == 1:
                    # Explicacion linea 401: Ejecuta una operacion del objeto dentro del flujo.
                    self.mostrar_catalogo_completo()
                # Explicacion linea 402: Evalua una condicion para elegir el camino de ejecucion.
                elif opcion == 2:
                    # Explicacion linea 403: Ejecuta una operacion del objeto dentro del flujo.
                    self.buscar_muebles_interactivo()
                # Explicacion linea 404: Evalua una condicion para elegir el camino de ejecucion.
                elif opcion == 3:
                    # Explicacion linea 405: Ejecuta una operacion del objeto dentro del flujo.
                    self.filtrar_por_precio_interactivo()
                # Explicacion linea 406: Evalua una condicion para elegir el camino de ejecucion.
                elif opcion == 4:
                    # Explicacion linea 407: Ejecuta una operacion del objeto dentro del flujo.
                    self.filtrar_por_material_interactivo()
                # Explicacion linea 408: Evalua una condicion para elegir el camino de ejecucion.
                elif opcion == 5:
                    # Explicacion linea 409: Ejecuta una operacion del objeto dentro del flujo.
                    self.mostrar_comedores()
                # Explicacion linea 410: Evalua una condicion para elegir el camino de ejecucion.
                elif opcion == 6:
                    # Explicacion linea 411: Ejecuta una operacion del objeto dentro del flujo.
                    self.realizar_venta_interactiva()
                # Explicacion linea 412: Evalua una condicion para elegir el camino de ejecucion.
                elif opcion == 7:
                    # Explicacion linea 413: Ejecuta una operacion del objeto dentro del flujo.
                    self.mostrar_estadisticas()
                # Explicacion linea 414: Evalua una condicion para elegir el camino de ejecucion.
                elif opcion == 8:
                    # Explicacion linea 415: Ejecuta una operacion del objeto dentro del flujo.
                    self.generar_reporte_interactivo()
                # Explicacion linea 416: Evalua una condicion para elegir el camino de ejecucion.
                elif opcion == 9:
                    # Explicacion linea 417: Ejecuta una operacion del objeto dentro del flujo.
                    self.aplicar_descuentos_interactivo()

                # Explicacion linea 419: Evalua una condicion para elegir el camino de ejecucion.
                if self.running:
                    # Explicacion linea 420: Continua la expresion del bloque anterior o ejecuta esta instruccion.
                    input("\nPresiona Enter para continuar...")
                    # Explicacion linea 421: Ejecuta una operacion del objeto dentro del flujo.
                    self.console.clear()

            # Explicacion linea 423: Controla la excepcion indicada sin detener el flujo principal.
            except KeyboardInterrupt:
                # Explicacion linea 424: Ejecuta una operacion del objeto dentro del flujo.
                self.console.print("\n[red]Operación cancelada por el usuario.[/red]")
                # Explicacion linea 425: Asigna un valor, configura un argumento o actualiza un dato del escenario.
                self.running = False
            # Explicacion linea 426: Controla la excepcion indicada sin detener el flujo principal.
            except Exception as e:
                # Explicacion linea 427: Ejecuta una operacion del objeto dentro del flujo.
                self.console.print(f"[red]Error inesperado: {str(e)}[/red]")
                # Explicacion linea 428: Continua la expresion del bloque anterior o ejecuta esta instruccion.
                input("Presiona Enter para continuar...")

    # Explicacion linea 430: Declara la funcion y sus parametros de entrada.
    def mostrar_banner(self):
        # Explicacion linea 431: Documenta el objetivo y el uso de este bloque.
        """Muestra el banner de bienvenida de la tienda."""

        # Explicacion linea 433: Asigna un valor, configura un argumento o actualiza un dato del escenario.
        banner_text = Text(f"🏠 {self.tienda.nombre} 🏠", style="bold magenta")
        # Explicacion linea 434: Continua la expresion del bloque anterior o ejecuta esta instruccion.
        banner_text.stylize("bold blue", 0, 2)  # Emoji inicial
        # Explicacion linea 435: Continua la expresion del bloque anterior o ejecuta esta instruccion.
        banner_text.stylize("bold blue", -2, -0)  # Emoji final

        # Explicacion linea 437: Asigna un valor, configura un argumento o actualiza un dato del escenario.
        panel = Panel(
            # Explicacion linea 438: Continua la expresion del bloque anterior o ejecuta esta instruccion.
            banner_text,
            # Explicacion linea 439: Asigna un valor, configura un argumento o actualiza un dato del escenario.
            title="Bienvenido",
            # Explicacion linea 440: Asigna un valor, configura un argumento o actualiza un dato del escenario.
            subtitle="Tu tienda de muebles favorita",
            # Explicacion linea 441: Asigna un valor, configura un argumento o actualiza un dato del escenario.
            border_style="blue",
        # Explicacion linea 442: Cierra la expresion o estructura iniciada anteriormente.
        )

        # Explicacion linea 444: Ejecuta una operacion del objeto dentro del flujo.
        self.console.print(panel)
        # Explicacion linea 445: Ejecuta una operacion del objeto dentro del flujo.
        self.console.print()

    # Explicacion linea 447: Declara la funcion y sus parametros de entrada.
    def mostrar_menu_principal(self) -> int:
        # Explicacion linea 448: Documenta el objetivo y el uso de este bloque.
        """
        Muestra el menú principal y obtiene la selección del usuario.

        Returns:
            int: Opción seleccionada por el usuario
        """

        # Explicacion linea 455: Asigna un valor, configura un argumento o actualiza un dato del escenario.
        menu_text = Text()
        # Explicacion linea 456: Asigna un valor, configura un argumento o actualiza un dato del escenario.
        menu_text.append("🔹 MENÚ PRINCIPAL 🔹\n\n", style="bold cyan")

        # Explicacion linea 458: Asigna un valor, configura un argumento o actualiza un dato del escenario.
        opciones = [
            # Explicacion linea 459: Continua la expresion del bloque anterior o ejecuta esta instruccion.
            "1. Ver catálogo completo",
            # Explicacion linea 460: Continua la expresion del bloque anterior o ejecuta esta instruccion.
            "2. Buscar muebles",
            # Explicacion linea 461: Continua la expresion del bloque anterior o ejecuta esta instruccion.
            "3. Filtrar por precio",
            # Explicacion linea 462: Continua la expresion del bloque anterior o ejecuta esta instruccion.
            "4. Filtrar por material",
            # Explicacion linea 463: Continua la expresion del bloque anterior o ejecuta esta instruccion.
            "5. Ver comedores disponibles",
            # Explicacion linea 464: Continua la expresion del bloque anterior o ejecuta esta instruccion.
            "6. Realizar venta",
            # Explicacion linea 465: Continua la expresion del bloque anterior o ejecuta esta instruccion.
            "7. Ver estadísticas",
            # Explicacion linea 466: Continua la expresion del bloque anterior o ejecuta esta instruccion.
            "8. Generar reporte de inventario",
            # Explicacion linea 467: Continua la expresion del bloque anterior o ejecuta esta instruccion.
            "9. Aplicar descuentos",
            # Explicacion linea 468: Continua la expresion del bloque anterior o ejecuta esta instruccion.
            "0. Salir",
        # Explicacion linea 469: Cierra la expresion o estructura iniciada anteriormente.
        ]

        # Explicacion linea 471: Recorre los elementos de una coleccion para procesarlos.
        for opcion in opciones:
            # Explicacion linea 472: Asigna un valor, configura un argumento o actualiza un dato del escenario.
            menu_text.append(f"{opcion}\n", style="green")

        # Explicacion linea 474: Asigna un valor, configura un argumento o actualiza un dato del escenario.
        panel = Panel(
            # Explicacion linea 475: Continua la expresion del bloque anterior o ejecuta esta instruccion.
            menu_text,
            # Explicacion linea 476: Asigna un valor, configura un argumento o actualiza un dato del escenario.
            title="Opciones Disponibles",
            # Explicacion linea 477: Asigna un valor, configura un argumento o actualiza un dato del escenario.
            border_style="yellow",
            # Explicacion linea 478: Asigna un valor, configura un argumento o actualiza un dato del escenario.
            padding=(1, 2),
        # Explicacion linea 479: Cierra la expresion o estructura iniciada anteriormente.
        )

        # Explicacion linea 481: Ejecuta una operacion del objeto dentro del flujo.
        self.console.print(panel)

        # Explicacion linea 483: Inicia una operacion que puede generar una excepcion.
        try:
            # Explicacion linea 484: Asigna un valor, configura un argumento o actualiza un dato del escenario.
            opcion = IntPrompt.ask(
                # Explicacion linea 485: Asigna un valor, configura un argumento o actualiza un dato del escenario.
                "Selecciona una opción", choices=[str(i) for i in range(0, 10)]
            # Explicacion linea 486: Cierra la expresion o estructura iniciada anteriormente.
            )
            # Explicacion linea 487: Devuelve al llamador el resultado construido por este metodo.
            return opcion
        # Explicacion linea 488: Controla la excepcion indicada sin detener el flujo principal.
        except ValueError:
            # Explicacion linea 489: Ejecuta una operacion del objeto dentro del flujo.
            self.console.print("[red]Opción inválida. Intenta de nuevo.[/red]")
            # Explicacion linea 490: Devuelve al llamador el resultado construido por este metodo.
            return self.mostrar_menu_principal()
