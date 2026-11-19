# Explicacion linea 1: Documenta el objetivo y el uso de este bloque.
"""
Servicio de la tienda que maneja la lógica de negocio.
Esta clase implementa el patrón de servicio para separar la lógica de negocio de la UI.
"""

# Explicacion linea 6: Importa las herramientas o clases usadas en este modulo.
from typing import List, Dict, Optional, Union

# Corrección de imports para ejecución directa
# Explicacion linea 9: Importa las herramientas o clases usadas en este modulo.
from models.mueble import Mueble
# Explicacion linea 10: Importa las herramientas o clases usadas en este modulo.
from models.composicion.comedor import Comedor
# TODO: Importar las clases necesarias


# Explicacion linea 14: Declara una clase que organiza atributos y operaciones del dominio.
class TiendaMuebles:
    # Explicacion linea 15: Declara la funcion y sus parametros de entrada.
    def obtener_estadisticas(self) -> dict:
        # Explicacion linea 16: Documenta el objetivo y el uso de este bloque.
        """
        Retorna estadísticas básicas y acumulativas de la tienda para la UI.
        Returns:
            dict: Diccionario con estadísticas
        """
        # Explicacion linea 21: Inicia una operacion que puede generar una excepcion.
        try:
            # Explicacion linea 22: Asigna un valor, configura un argumento o actualiza un dato del escenario.
            total_muebles = len(self._inventario)
            # Explicacion linea 23: Asigna un valor, configura un argumento o actualiza un dato del escenario.
            total_comedores = len(self._comedores)
            # Explicacion linea 24: Asigna un valor, configura un argumento o actualiza un dato del escenario.
            valor_inventario = 0
            # Explicacion linea 25: Recorre los elementos de una coleccion para procesarlos.
            for mueble in self._inventario:
                # Explicacion linea 26: Inicia una operacion que puede generar una excepcion.
                try:
                    # Explicacion linea 27: Asigna un valor, configura un argumento o actualiza un dato del escenario.
                    valor_inventario += mueble.calcular_precio()
                # Explicacion linea 28: Controla la excepcion indicada sin detener el flujo principal.
                except Exception:
                    # Explicacion linea 29: No realiza ninguna accion en este bloque.
                    pass
            # Explicacion linea 30: Asigna un valor, configura un argumento o actualiza un dato del escenario.
            tipos_muebles = {}
            # Explicacion linea 31: Recorre los elementos de una coleccion para procesarlos.
            for mueble in self._inventario:
                # Explicacion linea 32: Asigna un valor, configura un argumento o actualiza un dato del escenario.
                tipo = type(mueble).__name__
                # Explicacion linea 33: Asigna un valor, configura un argumento o actualiza un dato del escenario.
                tipos_muebles[tipo] = tipos_muebles.get(tipo, 0) + 1
            # Explicacion linea 34: Asigna un valor, configura un argumento o actualiza un dato del escenario.
            ventas_realizadas = (
                # Explicacion linea 35: Continua la expresion del bloque anterior o ejecuta esta instruccion.
                len(self._ventas_realizadas)
                # Explicacion linea 36: Evalua una condicion para elegir el camino de ejecucion.
                if hasattr(self, "_ventas_realizadas")
                # Explicacion linea 37: Continua la expresion del bloque anterior o ejecuta esta instruccion.
                else 0
            # Explicacion linea 38: Cierra la expresion o estructura iniciada anteriormente.
            )
            # Acumulativos
            # Explicacion linea 40: Asigna un valor, configura un argumento o actualiza un dato del escenario.
            total_muebles_vendidos = getattr(self, "_total_muebles_vendidos", 0)
            # Explicacion linea 41: Asigna un valor, configura un argumento o actualiza un dato del escenario.
            valor_total_ventas = getattr(self, "_valor_total_ventas", 0.0)
            # Explicacion linea 42: Devuelve al llamador el resultado construido por este metodo.
            return {
                # Explicacion linea 43: Continua la expresion del bloque anterior o ejecuta esta instruccion.
                "total_muebles": total_muebles,
                # Explicacion linea 44: Continua la expresion del bloque anterior o ejecuta esta instruccion.
                "total_comedores": total_comedores,
                # Explicacion linea 45: Continua la expresion del bloque anterior o ejecuta esta instruccion.
                "valor_inventario": valor_inventario,
                # Explicacion linea 46: Continua la expresion del bloque anterior o ejecuta esta instruccion.
                "tipos_muebles": tipos_muebles,
                # Explicacion linea 47: Continua la expresion del bloque anterior o ejecuta esta instruccion.
                "descuentos_activos": self._descuentos_activos.copy(),
                # Explicacion linea 48: Continua la expresion del bloque anterior o ejecuta esta instruccion.
                "ventas_realizadas": ventas_realizadas,
                # Explicacion linea 49: Continua la expresion del bloque anterior o ejecuta esta instruccion.
                "total_muebles_vendidos": total_muebles_vendidos,
                # Explicacion linea 50: Continua la expresion del bloque anterior o ejecuta esta instruccion.
                "valor_total_ventas": valor_total_ventas,
            # Explicacion linea 51: Cierra la expresion o estructura iniciada anteriormente.
            }
        # Explicacion linea 52: Controla la excepcion indicada sin detener el flujo principal.
        except Exception:
            # Explicacion linea 53: Devuelve al llamador el resultado construido por este metodo.
            return {
                # Explicacion linea 54: Continua la expresion del bloque anterior o ejecuta esta instruccion.
                "total_muebles": 0,
                # Explicacion linea 55: Continua la expresion del bloque anterior o ejecuta esta instruccion.
                "total_comedores": 0,
                # Explicacion linea 56: Continua la expresion del bloque anterior o ejecuta esta instruccion.
                "valor_inventario": 0.0,
                # Explicacion linea 57: Continua la expresion del bloque anterior o ejecuta esta instruccion.
                "tipos_muebles": {},
                # Explicacion linea 58: Continua la expresion del bloque anterior o ejecuta esta instruccion.
                "descuentos_activos": {},
                # Explicacion linea 59: Continua la expresion del bloque anterior o ejecuta esta instruccion.
                "ventas_realizadas": 0,
                # Explicacion linea 60: Continua la expresion del bloque anterior o ejecuta esta instruccion.
                "total_muebles_vendidos": 0,
                # Explicacion linea 61: Continua la expresion del bloque anterior o ejecuta esta instruccion.
                "valor_total_ventas": 0.0,
            # Explicacion linea 62: Cierra la expresion o estructura iniciada anteriormente.
            }

    # Explicacion linea 64: Declara la funcion y sus parametros de entrada.
    def estadisticas(self) -> dict:
        # Explicacion linea 65: Documenta el objetivo y el uso de este bloque.
        """
        Retorna estadísticas básicas y acumulativas de la tienda para la UI.
        Returns:
            dict: Diccionario con estadísticas
        """
        # Explicacion linea 70: Inicia una operacion que puede generar una excepcion.
        try:
            # Explicacion linea 71: Asigna un valor, configura un argumento o actualiza un dato del escenario.
            total_muebles = len(self._inventario)
            # Explicacion linea 72: Asigna un valor, configura un argumento o actualiza un dato del escenario.
            total_comedores = len(self._comedores)
            # Explicacion linea 73: Asigna un valor, configura un argumento o actualiza un dato del escenario.
            valor_inventario = 0
            # Explicacion linea 74: Recorre los elementos de una coleccion para procesarlos.
            for mueble in self._inventario:
                # Explicacion linea 75: Inicia una operacion que puede generar una excepcion.
                try:
                    # Explicacion linea 76: Asigna un valor, configura un argumento o actualiza un dato del escenario.
                    valor_inventario += mueble.calcular_precio()
                # Explicacion linea 77: Controla la excepcion indicada sin detener el flujo principal.
                except Exception:
                    # Explicacion linea 78: No realiza ninguna accion en este bloque.
                    pass
            # Explicacion linea 79: Asigna un valor, configura un argumento o actualiza un dato del escenario.
            tipos_muebles = {}
            # Explicacion linea 80: Recorre los elementos de una coleccion para procesarlos.
            for mueble in self._inventario:
                # Explicacion linea 81: Asigna un valor, configura un argumento o actualiza un dato del escenario.
                tipo = type(mueble).__name__
                # Explicacion linea 82: Asigna un valor, configura un argumento o actualiza un dato del escenario.
                tipos_muebles[tipo] = tipos_muebles.get(tipo, 0) + 1
            # Explicacion linea 83: Asigna un valor, configura un argumento o actualiza un dato del escenario.
            ventas_realizadas = (
                # Explicacion linea 84: Continua la expresion del bloque anterior o ejecuta esta instruccion.
                len(self._ventas_realizadas)
                # Explicacion linea 85: Evalua una condicion para elegir el camino de ejecucion.
                if hasattr(self, "_ventas_realizadas")
                # Explicacion linea 86: Continua la expresion del bloque anterior o ejecuta esta instruccion.
                else 0
            # Explicacion linea 87: Cierra la expresion o estructura iniciada anteriormente.
            )
            # Explicacion linea 88: Asigna un valor, configura un argumento o actualiza un dato del escenario.
            total_muebles_vendidos = getattr(self, "_total_muebles_vendidos", 0)
            # Explicacion linea 89: Asigna un valor, configura un argumento o actualiza un dato del escenario.
            valor_total_ventas = getattr(self, "_valor_total_ventas", 0.0)
            # Explicacion linea 90: Devuelve al llamador el resultado construido por este metodo.
            return {
                # Explicacion linea 91: Continua la expresion del bloque anterior o ejecuta esta instruccion.
                "total_muebles": total_muebles,
                # Explicacion linea 92: Continua la expresion del bloque anterior o ejecuta esta instruccion.
                "total_comedores": total_comedores,
                # Explicacion linea 93: Continua la expresion del bloque anterior o ejecuta esta instruccion.
                "valor_inventario": valor_inventario,
                # Explicacion linea 94: Continua la expresion del bloque anterior o ejecuta esta instruccion.
                "tipos_muebles": tipos_muebles,
                # Explicacion linea 95: Continua la expresion del bloque anterior o ejecuta esta instruccion.
                "descuentos_activos": self._descuentos_activos.copy(),
                # Explicacion linea 96: Continua la expresion del bloque anterior o ejecuta esta instruccion.
                "ventas_realizadas": ventas_realizadas,
                # Explicacion linea 97: Continua la expresion del bloque anterior o ejecuta esta instruccion.
                "total_muebles_vendidos": total_muebles_vendidos,
                # Explicacion linea 98: Continua la expresion del bloque anterior o ejecuta esta instruccion.
                "valor_total_ventas": valor_total_ventas,
            # Explicacion linea 99: Cierra la expresion o estructura iniciada anteriormente.
            }
        # Explicacion linea 100: Controla la excepcion indicada sin detener el flujo principal.
        except Exception:
            # Explicacion linea 101: Devuelve al llamador el resultado construido por este metodo.
            return {
                # Explicacion linea 102: Continua la expresion del bloque anterior o ejecuta esta instruccion.
                "total_muebles": 0,
                # Explicacion linea 103: Continua la expresion del bloque anterior o ejecuta esta instruccion.
                "total_comedores": 0,
                # Explicacion linea 104: Continua la expresion del bloque anterior o ejecuta esta instruccion.
                "valor_inventario": 0.0,
                # Explicacion linea 105: Continua la expresion del bloque anterior o ejecuta esta instruccion.
                "tipos_muebles": {},
                # Explicacion linea 106: Continua la expresion del bloque anterior o ejecuta esta instruccion.
                "descuentos_activos": {},
                # Explicacion linea 107: Continua la expresion del bloque anterior o ejecuta esta instruccion.
                "ventas_realizadas": 0,
                # Explicacion linea 108: Continua la expresion del bloque anterior o ejecuta esta instruccion.
                "total_muebles_vendidos": 0,
                # Explicacion linea 109: Continua la expresion del bloque anterior o ejecuta esta instruccion.
                "valor_total_ventas": 0.0,
            # Explicacion linea 110: Cierra la expresion o estructura iniciada anteriormente.
            }

    # Explicacion linea 112: Documenta el objetivo y el uso de este bloque.
    """
    Clase que maneja toda la lógica de negocio de la tienda de muebles.
    
    Esta clase implementa:
    - Gestión de inventario
    - Búsquedas y filtros
    - Cálculos de precios y descuentos
    - Operaciones de venta
    
    Conceptos OOP aplicados:
    - Encapsulación: Agrupa toda la lógica relacionada con la tienda
    - Abstracción: Oculta la complejidad del manejo de inventario
    - Composición: Contiene colecciones de muebles
    """

    # Explicacion linea 127: Declara la funcion y sus parametros de entrada.
    def __init__(self, nombre_tienda: str = "Mueblería OOP"):
        # Explicacion linea 128: Documenta el objetivo y el uso de este bloque.
        """
        Constructor de la tienda.

        Args:
            nombre_tienda: Nombre de la tienda
        """
        # Explicacion linea 134: Asigna un valor, configura un argumento o actualiza un dato del escenario.
        self._nombre = nombre_tienda
        # Explicacion linea 135: Asigna un valor, configura un argumento o actualiza un dato del escenario.
        self._inventario: List[Mueble] = []
        # Explicacion linea 136: Asigna un valor, configura un argumento o actualiza un dato del escenario.
        self._comedores: List[Comedor] = []
        # Explicacion linea 137: Asigna un valor, configura un argumento o actualiza un dato del escenario.
        self._ventas_realizadas: List[Dict] = []
        # Explicacion linea 138: Asigna un valor, configura un argumento o actualiza un dato del escenario.
        self._descuentos_activos: Dict[str, float] = {}
        # Campos acumulativos
        # Explicacion linea 140: Asigna un valor, configura un argumento o actualiza un dato del escenario.
        self._total_muebles_vendidos: int = 0
        # Explicacion linea 141: Asigna un valor, configura un argumento o actualiza un dato del escenario.
        self._valor_total_ventas: float = 0.0
        # Explicacion linea 142: No realiza ninguna accion en este bloque.
        pass

    # Explicacion linea 144: Aplica un decorador a la funcion que aparece a continuacion.
    @property
    # Explicacion linea 145: Declara la funcion y sus parametros de entrada.
    def nombre(self) -> str:
        # Explicacion linea 146: Documenta el objetivo y el uso de este bloque.
        """Getter para el nombre de la tienda."""
        # Explicacion linea 147: Devuelve al llamador el resultado construido por este metodo.
        return self._nombre

    # @property
    # def total_muebles(self) -> int:
    #     """Retorna el total de muebles en inventario."""
    #     return len(self._inventario)

    # Explicacion linea 154: Declara la funcion y sus parametros de entrada.
    def agregar_mueble(self, mueble: "Mueble") -> str:
        # Explicacion linea 155: Documenta el objetivo y el uso de este bloque.
        """
        Agrega un mueble al inventario de la tienda.
        Args:
            mueble: Objeto mueble a agregar
        Returns:
            str: Mensaje de confirmación
        """
        # Explicacion linea 162: Evalua una condicion para elegir el camino de ejecucion.
        if mueble is None:
            # Explicacion linea 163: Devuelve al llamador el resultado construido por este metodo.
            return "Error: El mueble no puede ser None"
        # Explicacion linea 164: Inicia una operacion que puede generar una excepcion.
        try:
            # Explicacion linea 165: Asigna un valor, configura un argumento o actualiza un dato del escenario.
            precio = mueble.calcular_precio()
            # Explicacion linea 166: Evalua una condicion para elegir el camino de ejecucion.
            if precio <= 0:
                # Explicacion linea 167: Devuelve al llamador el resultado construido por este metodo.
                return "Error: El mueble debe tener un precio válido mayor a 0"
        # Explicacion linea 168: Controla la excepcion indicada sin detener el flujo principal.
        except Exception as e:
            # Explicacion linea 169: Devuelve al llamador el resultado construido por este metodo.
            return f"Error al calcular precio del mueble: {str(e)}"
        # Explicacion linea 170: Ejecuta una operacion del objeto dentro del flujo.
        self._inventario.append(mueble)
        # Explicacion linea 171: Devuelve al llamador el resultado construido por este metodo.
        return f"Mueble {getattr(mueble, 'nombre', str(mueble))} agregado exitosamente al inventario"

    # Explicacion linea 173: Declara la funcion y sus parametros de entrada.
    def agregar_comedor(self, comedor: "Comedor") -> str:
        # Explicacion linea 174: Documenta el objetivo y el uso de este bloque.
        """
        Agrega un comedor completo a la tienda.
        Args:
            comedor: Objeto Comedor a agregar
        Returns:
            str: Mensaje de confirmación
        """
        # Explicacion linea 181: Evalua una condicion para elegir el camino de ejecucion.
        if comedor is None:
            # Explicacion linea 182: Devuelve al llamador el resultado construido por este metodo.
            return "Error: El comedor no puede ser None"
        # Explicacion linea 183: Ejecuta una operacion del objeto dentro del flujo.
        self._comedores.append(comedor)
        # Explicacion linea 184: Devuelve al llamador el resultado construido por este metodo.
        return (
            # Explicacion linea 185: Continua la expresion del bloque anterior o ejecuta esta instruccion.
            f"Comedor {getattr(comedor, 'nombre', str(comedor))} agregado exitosamente"
        # Explicacion linea 186: Cierra la expresion o estructura iniciada anteriormente.
        )

    # Explicacion linea 188: Declara la funcion y sus parametros de entrada.
    def buscar_muebles_por_nombre(self, nombre: str) -> List["Mueble"]:
        # Explicacion linea 189: Documenta el objetivo y el uso de este bloque.
        """
        Busca muebles por nombre (búsqueda parcial, case-insensitive).
        Args:
            nombre: Nombre o parte del nombre a buscar
        Returns:
            List[Mueble]: Lista de muebles que coinciden con la búsqueda
        """
        # Explicacion linea 196: Evalua una condicion para elegir el camino de ejecucion.
        if not nombre or not nombre.strip():
            # Explicacion linea 197: Devuelve al llamador el resultado construido por este metodo.
            return []
        # Explicacion linea 198: Asigna un valor, configura un argumento o actualiza un dato del escenario.
        nombre_lower = nombre.lower().strip()
        # Explicacion linea 199: Asigna un valor, configura un argumento o actualiza un dato del escenario.
        resultados = []
        # Explicacion linea 200: Recorre los elementos de una coleccion para procesarlos.
        for mueble in self._inventario:
            # Explicacion linea 201: Evalua una condicion para elegir el camino de ejecucion.
            if nombre_lower in mueble.nombre.lower():
                # Explicacion linea 202: Continua la expresion del bloque anterior o ejecuta esta instruccion.
                resultados.append(mueble)
        # Explicacion linea 203: Devuelve al llamador el resultado construido por este metodo.
        return resultados

    # Explicacion linea 205: Declara la funcion y sus parametros de entrada.
    def filtrar_por_precio(
        # Explicacion linea 206: Asigna un valor, configura un argumento o actualiza un dato del escenario.
        self, precio_min: float = 0, precio_max: float = float("inf")
    # Explicacion linea 207: Cierra la expresion o estructura iniciada anteriormente.
    ) -> List["Mueble"]:
        # Explicacion linea 208: Documenta el objetivo y el uso de este bloque.
        """
        Filtra muebles por rango de precios.

        Args:
            precio_min: Precio mínimo (inclusivo)
            precio_max: Precio máximo (inclusivo)
        Returns:
            List[Mueble]: Lista de muebles en el rango de precios
        """
        # Explicacion linea 217: Evalua una condicion para elegir el camino de ejecucion.
        if precio_min < 0:
            # Explicacion linea 218: Asigna un valor, configura un argumento o actualiza un dato del escenario.
            precio_min = 0
        # Explicacion linea 219: Asigna un valor, configura un argumento o actualiza un dato del escenario.
        resultados = []
        # Explicacion linea 220: Recorre los elementos de una coleccion para procesarlos.
        for mueble in self._inventario:
            # Explicacion linea 221: Inicia una operacion que puede generar una excepcion.
            try:
                # Explicacion linea 222: Asigna un valor, configura un argumento o actualiza un dato del escenario.
                precio = mueble.calcular_precio()
                # Explicacion linea 223: Evalua una condicion para elegir el camino de ejecucion.
                if precio_min <= precio <= precio_max:
                    # Explicacion linea 224: Continua la expresion del bloque anterior o ejecuta esta instruccion.
                    resultados.append(mueble)
            # Explicacion linea 225: Controla la excepcion indicada sin detener el flujo principal.
            except Exception:
                # Explicacion linea 226: Avanza a la siguiente iteracion del ciclo.
                continue  # Saltar muebles con errores de precio
        # Explicacion linea 227: Devuelve al llamador el resultado construido por este metodo.
        return resultados

    # Explicacion linea 229: Declara la funcion y sus parametros de entrada.
    def filtrar_por_material(self, material: str) -> List["Mueble"]:
        # Explicacion linea 230: Documenta el objetivo y el uso de este bloque.
        """
        Filtra muebles por material.

        Args:
            material: Material a buscar
        Returns:
            List[Mueble]: Lista de muebles del material especificado
        """
        # Explicacion linea 238: Evalua una condicion para elegir el camino de ejecucion.
        if not material or not material.strip():
            # Explicacion linea 239: Devuelve al llamador el resultado construido por este metodo.
            return []
        # Explicacion linea 240: Asigna un valor, configura un argumento o actualiza un dato del escenario.
        material_lower = material.lower().strip()
        # Explicacion linea 241: Asigna un valor, configura un argumento o actualiza un dato del escenario.
        resultados = []
        # Explicacion linea 242: Recorre los elementos de una coleccion para procesarlos.
        for mueble in self._inventario:
            # Explicacion linea 243: Inicia una operacion que puede generar una excepcion.
            try:
                # Explicacion linea 244: Evalua una condicion para elegir el camino de ejecucion.
                if (
                    # Explicacion linea 245: Continua la expresion del bloque anterior o ejecuta esta instruccion.
                    hasattr(mueble, "material")
                    # Explicacion linea 246: Continua la expresion del bloque anterior o ejecuta esta instruccion.
                    and mueble.material
                    # Explicacion linea 247: Asigna un valor, configura un argumento o actualiza un dato del escenario.
                    and mueble.material.lower().strip() == material_lower
                # Explicacion linea 248: Cierra la expresion o estructura iniciada anteriormente.
                ):
                    # Explicacion linea 249: Continua la expresion del bloque anterior o ejecuta esta instruccion.
                    resultados.append(mueble)
            # Explicacion linea 250: Controla la excepcion indicada sin detener el flujo principal.
            except Exception:
                # Explicacion linea 251: Avanza a la siguiente iteracion del ciclo.
                continue
        # Explicacion linea 252: Devuelve al llamador el resultado construido por este metodo.
        return resultados

    # Explicacion linea 254: Declara la funcion y sus parametros de entrada.
    def obtener_muebles_por_tipo(self, tipo_clase: type) -> List["Mueble"]:
        # Explicacion linea 255: Documenta el objetivo y el uso de este bloque.
        """Retorna los muebles del inventario que pertenecen al tipo solicitado."""
        # Explicacion linea 256: Devuelve al llamador el resultado construido por este metodo.
        return [mueble for mueble in self._inventario if isinstance(mueble, tipo_clase)]

    # Explicacion linea 258: Declara la funcion y sus parametros de entrada.
    def calcular_valor_inventario(self) -> float:
        # Explicacion linea 259: Documenta el objetivo y el uso de este bloque.
        """Suma los precios de muebles y comedores, ignorando precios defectuosos."""
        # Explicacion linea 260: Asigna un valor, configura un argumento o actualiza un dato del escenario.
        valor_total = 0.0
        # Explicacion linea 261: Recorre los elementos de una coleccion para procesarlos.
        for producto in [*self._inventario, *self._comedores]:
            # Explicacion linea 262: Inicia una operacion que puede generar una excepcion.
            try:
                # Explicacion linea 263: Evalua una condicion para elegir el camino de ejecucion.
                if hasattr(producto, "calcular_precio_total"):
                    # Explicacion linea 264: Asigna un valor, configura un argumento o actualiza un dato del escenario.
                    valor_total += producto.calcular_precio_total()
                # Explicacion linea 265: Ejecuta la alternativa cuando las condiciones anteriores no aplican.
                else:
                    # Explicacion linea 266: Asigna un valor, configura un argumento o actualiza un dato del escenario.
                    valor_total += producto.calcular_precio()
            # Explicacion linea 267: Controla la excepcion indicada sin detener el flujo principal.
            except Exception:
                # Explicacion linea 268: Avanza a la siguiente iteracion del ciclo.
                continue
        # Explicacion linea 269: Devuelve al llamador el resultado construido por este metodo.
        return round(valor_total, 2)

    # Explicacion linea 271: Declara la funcion y sus parametros de entrada.
    def aplicar_descuento(self, categoria: str, porcentaje: float) -> str:
        # Explicacion linea 272: Documenta el objetivo y el uso de este bloque.
        """
        Aplica un descuento a una categoría de muebles.

        Args:
            categoria: Nombre de la categoría (ej: "sillas", "mesas")
            porcentaje: Porcentaje de descuento (0-100)
        Returns:
            str: Mensaje de confirmación
        """
        # Explicacion linea 281: Evalua una condicion para elegir el camino de ejecucion.
        if not 0 < porcentaje <= 100:
            # Explicacion linea 282: Devuelve al llamador el resultado construido por este metodo.
            return "Error: El porcentaje debe estar entre 1 y 100"
        # Explicacion linea 283: Asigna un valor, configura un argumento o actualiza un dato del escenario.
        categoria_lower = categoria.lower().strip()
        # Normalizar nombres de clase (Silla, Mesa, etc.)
        # El sistema usa el nombre de la clase, por ejemplo 'Silla', 'Mesa', etc.
        # Si el usuario ingresa 'sillas', 'mesas', etc., quitamos la 's' final si existe
        # Explicacion linea 287: Evalua una condicion para elegir el camino de ejecucion.
        if categoria_lower.endswith("s"):
            # Explicacion linea 288: Asigna un valor, configura un argumento o actualiza un dato del escenario.
            categoria_lower = categoria_lower[:-1]
        # Capitalizar para coincidir con el nombre de clase
        # Explicacion linea 290: Asigna un valor, configura un argumento o actualiza un dato del escenario.
        categoria_clase = categoria_lower.capitalize()
        # Explicacion linea 291: Asigna un valor, configura un argumento o actualiza un dato del escenario.
        self._descuentos_activos[categoria_clase] = porcentaje / 100
        # Explicacion linea 292: Devuelve al llamador el resultado construido por este metodo.
        return (
            # Explicacion linea 293: Continua la expresion del bloque anterior o ejecuta esta instruccion.
            f"Descuento del {porcentaje}% aplicado a la categoría '{categoria_clase}'"
        # Explicacion linea 294: Cierra la expresion o estructura iniciada anteriormente.
        )

    # Explicacion linea 296: Declara la funcion y sus parametros de entrada.
    def realizar_venta(
        # Explicacion linea 297: Asigna un valor, configura un argumento o actualiza un dato del escenario.
        self, mueble: "Mueble", cliente: str = "Cliente Anónimo"
    # Explicacion linea 298: Cierra la expresion o estructura iniciada anteriormente.
    ) -> Dict:
        # Explicacion linea 299: Documenta el objetivo y el uso de este bloque.
        """
        Procesa la venta de un mueble.
        Args:
            mueble: Mueble a vender
            cliente: Nombre del cliente
        Returns:
            Dict: Información de la venta realizada o error
        """
        # Explicacion linea 307: Evalua una condicion para elegir el camino de ejecucion.
        if mueble not in self._inventario:
            # Explicacion linea 308: Devuelve al llamador el resultado construido por este metodo.
            return {"error": "El mueble no está disponible en inventario"}
        # Explicacion linea 309: Inicia una operacion que puede generar una excepcion.
        try:
            # Explicacion linea 310: Asigna un valor, configura un argumento o actualiza un dato del escenario.
            precio_original = mueble.calcular_precio()
            # Explicacion linea 311: Asigna un valor, configura un argumento o actualiza un dato del escenario.
            descuento_aplicado = 0
            # Use the class name as key, matching how discounts are registered
            # Explicacion linea 313: Asigna un valor, configura un argumento o actualiza un dato del escenario.
            tipo_mueble = type(mueble).__name__
            # Explicacion linea 314: Evalua una condicion para elegir el camino de ejecucion.
            if self._descuentos_activos and tipo_mueble in self._descuentos_activos:
                # Explicacion linea 315: Asigna un valor, configura un argumento o actualiza un dato del escenario.
                descuento_aplicado = self._descuentos_activos[tipo_mueble]
            # Explicacion linea 316: Asigna un valor, configura un argumento o actualiza un dato del escenario.
            precio_final = precio_original * (1 - descuento_aplicado)
            # Explicacion linea 317: Importa las herramientas o clases usadas en este modulo.
            from datetime import datetime

            # Ensure mueble.nombre is always a string
            # Explicacion linea 320: Asigna un valor, configura un argumento o actualiza un dato del escenario.
            nombre_mueble = getattr(mueble, "nombre", None)
            # Explicacion linea 321: Evalua una condicion para elegir el camino de ejecucion.
            if not nombre_mueble:
                # Explicacion linea 322: Asigna un valor, configura un argumento o actualiza un dato del escenario.
                nombre_mueble = tipo_mueble
            # Explicacion linea 323: Asigna un valor, configura un argumento o actualiza un dato del escenario.
            venta = {
                # Explicacion linea 324: Continua la expresion del bloque anterior o ejecuta esta instruccion.
                "mueble": nombre_mueble,
                # Explicacion linea 325: Continua la expresion del bloque anterior o ejecuta esta instruccion.
                "cliente": cliente,
                # Explicacion linea 326: Continua la expresion del bloque anterior o ejecuta esta instruccion.
                "precio_original": precio_original,
                # Explicacion linea 327: Continua la expresion del bloque anterior o ejecuta esta instruccion.
                "descuento": descuento_aplicado * 100,
                # Explicacion linea 328: Continua la expresion del bloque anterior o ejecuta esta instruccion.
                "precio_final": round(precio_final, 2),
                # Explicacion linea 329: Continua la expresion del bloque anterior o ejecuta esta instruccion.
                "fecha": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            # Explicacion linea 330: Cierra la expresion o estructura iniciada anteriormente.
            }
            # Explicacion linea 331: Ejecuta una operacion del objeto dentro del flujo.
            self._ventas_realizadas.append(venta)
            # Explicacion linea 332: Ejecuta una operacion del objeto dentro del flujo.
            self._inventario.remove(mueble)
            # Acumulativos
            # Explicacion linea 334: Asigna un valor, configura un argumento o actualiza un dato del escenario.
            self._total_muebles_vendidos += 1
            # Explicacion linea 335: Asigna un valor, configura un argumento o actualiza un dato del escenario.
            self._valor_total_ventas += venta["precio_final"]
            # Explicacion linea 336: Devuelve al llamador el resultado construido por este metodo.
            return venta
        # Explicacion linea 337: Controla la excepcion indicada sin detener el flujo principal.
        except Exception as e:
            # Explicacion linea 338: Devuelve al llamador el resultado construido por este metodo.
            return {"error": f"Error al procesar la venta: {str(e)}"}

    # Explicacion linea 340: Declara la funcion y sus parametros de entrada.
    def _contar_tipos_muebles(self) -> Dict[str, int]:
        # Explicacion linea 341: Documenta el objetivo y el uso de este bloque.
        """
        Cuenta cuántos muebles hay de cada tipo.
        Método privado auxiliar.

        Returns:
            Dict[str, int]: Diccionario con el conteo por tipo
        """
        # TODO: Implementar conteo por tipos
        # conteo = {}
        # for mueble in self._inventario:
        #     tipo = type(mueble).__name__
        #     conteo[tipo] = conteo.get(tipo, 0) + 1
        # return conteo
        # Explicacion linea 354: No realiza ninguna accion en este bloque.
        pass

    # Explicacion linea 356: Declara la funcion y sus parametros de entrada.
    def generar_reporte_inventario(self) -> str:
        # Explicacion linea 357: Documenta el objetivo y el uso de este bloque.
        """
        Genera un reporte completo del inventario.
        Returns:
            str: Reporte detallado del inventario
        """
        # Explicacion linea 362: Asigna un valor, configura un argumento o actualiza un dato del escenario.
        estadisticas = self.obtener_estadisticas() or {}
        # Explicacion linea 363: Asigna un valor, configura un argumento o actualiza un dato del escenario.
        nombre_tienda = getattr(self, "_nombre", "Tienda")
        # Explicacion linea 364: Evalua una condicion para elegir el camino de ejecucion.
        if not isinstance(estadisticas, dict):
            # Explicacion linea 365: Asigna un valor, configura un argumento o actualiza un dato del escenario.
            estadisticas = {}
        # Explicacion linea 366: Asigna un valor, configura un argumento o actualiza un dato del escenario.
        reporte = f"=== REPORTE DE INVENTARIO - {nombre_tienda} ===\n\n"
        # Explicacion linea 367: Asigna un valor, configura un argumento o actualiza un dato del escenario.
        reporte += f"Total de muebles: {estadisticas.get('total_muebles', 0)}\n"
        # Explicacion linea 368: Asigna un valor, configura un argumento o actualiza un dato del escenario.
        reporte += f"Total de comedores: {estadisticas.get('total_comedores', 0)}\n"
        # Explicacion linea 369: Asigna un valor, configura un argumento o actualiza un dato del escenario.
        reporte += f"Valor total del inventario: ${estadisticas.get('valor_inventario', 0):.2f}\n\n"
        # Explicacion linea 370: Asigna un valor, configura un argumento o actualiza un dato del escenario.
        reporte += "DISTRIBUCIÓN POR TIPOS:\n"
        # Explicacion linea 371: Asigna un valor, configura un argumento o actualiza un dato del escenario.
        tipos = estadisticas.get("tipos_muebles", {}) or {}
        # Explicacion linea 372: Recorre los elementos de una coleccion para procesarlos.
        for tipo, cantidad in tipos.items():
            # Explicacion linea 373: Asigna un valor, configura un argumento o actualiza un dato del escenario.
            reporte += f"- {tipo}: {cantidad} unidades\n"
        # Explicacion linea 374: Asigna un valor, configura un argumento o actualiza un dato del escenario.
        descuentos = estadisticas.get("descuentos_activos", {}) or {}
        # Explicacion linea 375: Evalua una condicion para elegir el camino de ejecucion.
        if descuentos:
            # Explicacion linea 376: Asigna un valor, configura un argumento o actualiza un dato del escenario.
            reporte += "\nDESCUENTOS ACTIVOS:\n"
            # Explicacion linea 377: Recorre los elementos de una coleccion para procesarlos.
            for categoria, descuento in descuentos.items():
                # Explicacion linea 378: Asigna un valor, configura un argumento o actualiza un dato del escenario.
                reporte += f"- {categoria}: {descuento * 100:.1f}%\n"
        # Explicacion linea 379: Devuelve al llamador el resultado construido por este metodo.
        return reporte
