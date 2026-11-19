# Explicacion linea 1: Documenta el objetivo y el uso de este bloque.
"""
Clase Comedor que implementa composición.
Un comedor está compuesto por una mesa y varias sillas.
"""

# Importar List para anotaciones de tipo
# Explicacion linea 7: Importa las herramientas o clases usadas en este modulo.
from typing import List
# from ..concretos.mesa import Mesa
# from ..concretos.silla import Silla


# Explicacion linea 12: Declara una clase que organiza atributos y operaciones del dominio.
class Comedor:
    # Explicacion linea 13: Documenta el objetivo y el uso de este bloque.
    """
    Clase que implementa composición conteniendo una mesa y sillas.

    Un comedor es un conjunto de muebles que trabajan juntos.
    La relación es de composición porque el comedor "tiene" una mesa
    y "tiene" sillas, pero estas pueden existir independientemente.

    Conceptos OOP aplicados:
    - Composición: El comedor contiene otros objetos (mesa y sillas)
    - Agregación: Los objetos contenidos pueden existir independientemente
    - Encapsulación: Controla el acceso a los componentes internos
    - Abstracción: Simplifica la gestión de múltiples muebles
    """

    # Explicacion linea 27: Declara la funcion y sus parametros de entrada.
    def __init__(self, nombre: str, mesa: "Mesa", sillas: List["Silla"] = None):
        # Explicacion linea 28: Documenta el objetivo y el uso de este bloque.
        """
        Constructor del comedor.
        Args:
            nombre: Nombre del set de comedor
            mesa: Objeto Mesa que forma parte del comedor
            sillas: Lista de objetos Silla (opcional, se puede crear vacía)
        """
        # Explicacion linea 35: Asigna un valor, configura un argumento o actualiza un dato del escenario.
        self._nombre = nombre
        # Explicacion linea 36: Asigna un valor, configura un argumento o actualiza un dato del escenario.
        self._mesa = mesa
        # Explicacion linea 37: Asigna un valor, configura un argumento o actualiza un dato del escenario.
        self._sillas = sillas if sillas is not None else []

    # Explicacion linea 39: Aplica un decorador a la funcion que aparece a continuacion.
    @property
    # Explicacion linea 40: Declara la funcion y sus parametros de entrada.
    def nombre(self) -> str:
        # Explicacion linea 41: Devuelve al llamador el resultado construido por este metodo.
        return self._nombre

    # Explicacion linea 43: Aplica un decorador a la funcion que aparece a continuacion.
    @property
    # Explicacion linea 44: Declara la funcion y sus parametros de entrada.
    def mesa(self) -> "Mesa":
        # Explicacion linea 45: Devuelve al llamador el resultado construido por este metodo.
        return self._mesa

    # Explicacion linea 47: Aplica un decorador a la funcion que aparece a continuacion.
    @property
    # Explicacion linea 48: Declara la funcion y sus parametros de entrada.
    def sillas(self) -> List["Silla"]:
        # Explicacion linea 49: Devuelve al llamador el resultado construido por este metodo.
        return self._sillas.copy()

    # Explicacion linea 51: Declara la funcion y sus parametros de entrada.
    def agregar_silla(self, silla: "Silla") -> str:
        # Explicacion linea 52: Documenta el objetivo y el uso de este bloque.
        """
        Agrega una silla al comedor.

        Args:
            silla: Objeto Silla a agregar

        Returns:
            str: Mensaje de confirmación
        """
        # Validar que sea realmente una Silla (importación dinámica para evitar problemas de import)
        # Explicacion linea 62: Asigna un valor, configura un argumento o actualiza un dato del escenario.
        Silla = type(self._sillas[0]) if self._sillas else None
        # Explicacion linea 63: Evalua una condicion para elegir el camino de ejecucion.
        if Silla and not isinstance(silla, Silla):
            # Explicacion linea 64: Devuelve al llamador el resultado construido por este metodo.
            return "Error: Solo se pueden agregar objetos de tipo Silla"
        # Explicacion linea 65: Asigna un valor, configura un argumento o actualiza un dato del escenario.
        capacidad_maxima = self._calcular_capacidad_maxima()
        # Explicacion linea 66: Evalua una condicion para elegir el camino de ejecucion.
        if len(self._sillas) >= capacidad_maxima:
            # Explicacion linea 67: Devuelve al llamador el resultado construido por este metodo.
            return (
                # Explicacion linea 68: Continua la expresion del bloque anterior o ejecuta esta instruccion.
                f"No se pueden agregar más sillas. Capacidad máxima: {capacidad_maxima}"
            # Explicacion linea 69: Cierra la expresion o estructura iniciada anteriormente.
            )
        # Explicacion linea 70: Ejecuta una operacion del objeto dentro del flujo.
        self._sillas.append(silla)
        # Explicacion linea 71: Devuelve al llamador el resultado construido por este metodo.
        return f"Silla {getattr(silla, 'nombre', str(silla))} agregada exitosamente al comedor"

    # Explicacion linea 73: Declara la funcion y sus parametros de entrada.
    def quitar_silla(self, indice: int = -1) -> str:
        # Explicacion linea 74: Documenta el objetivo y el uso de este bloque.
        """
        Quita una silla del comedor.

        Args:
            indice: Índice de la silla a quitar (-1 para la última)

        Returns:
            str: Mensaje de confirmación
        """
        # Explicacion linea 83: Evalua una condicion para elegir el camino de ejecucion.
        if not self._sillas:
            # Explicacion linea 84: Devuelve al llamador el resultado construido por este metodo.
            return "No hay sillas para quitar"
        # Explicacion linea 85: Inicia una operacion que puede generar una excepcion.
        try:
            # Explicacion linea 86: Asigna un valor, configura un argumento o actualiza un dato del escenario.
            silla_removida = self._sillas.pop(indice)
            # Explicacion linea 87: Devuelve al llamador el resultado construido por este metodo.
            return f"Silla {getattr(silla_removida, 'nombre', str(silla_removida))} removida del comedor"
        # Explicacion linea 88: Controla la excepcion indicada sin detener el flujo principal.
        except IndexError:
            # Explicacion linea 89: Devuelve al llamador el resultado construido por este metodo.
            return "Índice de silla inválido"

    # Explicacion linea 91: Declara la funcion y sus parametros de entrada.
    def calcular_precio_total(self) -> float:
        # Explicacion linea 92: Documenta el objetivo y el uso de este bloque.
        """
        Calcula el precio total del comedor sumando todos sus componentes.

        Returns:
            float: Precio total del set de comedor
        """
        # Explicacion linea 98: Asigna un valor, configura un argumento o actualiza un dato del escenario.
        precio_total = self._mesa.calcular_precio()
        # Explicacion linea 99: Recorre los elementos de una coleccion para procesarlos.
        for silla in self._sillas:
            # Explicacion linea 100: Asigna un valor, configura un argumento o actualiza un dato del escenario.
            precio_total += silla.calcular_precio()
        # Explicacion linea 101: Evalua una condicion para elegir el camino de ejecucion.
        if len(self._sillas) >= 4:
            # Explicacion linea 102: Asigna un valor, configura un argumento o actualiza un dato del escenario.
            precio_total *= 0.95  # 5% de descuento
        # Explicacion linea 103: Devuelve al llamador el resultado construido por este metodo.
        return round(precio_total, 2)

    # Explicacion linea 105: Declara la funcion y sus parametros de entrada.
    def obtener_descripcion_completa(self) -> str:
        # Explicacion linea 106: Documenta el objetivo y el uso de este bloque.
        """
        Obtiene una descripción completa del comedor y todos sus componentes.

        Returns:
            str: Descripción detallada del comedor
        """
        # Explicacion linea 112: Asigna un valor, configura un argumento o actualiza un dato del escenario.
        descripcion = f"=== COMEDOR {self.nombre.upper()} ===\n\n"
        # Explicacion linea 113: Asigna un valor, configura un argumento o actualiza un dato del escenario.
        descripcion += "MESA:\n"
        # Explicacion linea 114: Asigna un valor, configura un argumento o actualiza un dato del escenario.
        descripcion += self._mesa.obtener_descripcion() + "\n\n"
        # Explicacion linea 115: Evalua una condicion para elegir el camino de ejecucion.
        if self._sillas:
            # Explicacion linea 116: Asigna un valor, configura un argumento o actualiza un dato del escenario.
            descripcion += f"SILLAS ({len(self._sillas)} unidades):\n"
            # Explicacion linea 117: Recorre los elementos de una coleccion para procesarlos.
            for i, silla in enumerate(self._sillas, 1):
                # Explicacion linea 118: Asigna un valor, configura un argumento o actualiza un dato del escenario.
                descripcion += f"{i}. {silla.obtener_descripcion()}\n"
        # Explicacion linea 119: Ejecuta la alternativa cuando las condiciones anteriores no aplican.
        else:
            # Explicacion linea 120: Asigna un valor, configura un argumento o actualiza un dato del escenario.
            descripcion += "SILLAS: Ninguna incluida\n"
        # Explicacion linea 121: Asigna un valor, configura un argumento o actualiza un dato del escenario.
        descripcion += f"\n--- PRECIO TOTAL: ${self.calcular_precio_total():.2f} ---"
        # Explicacion linea 122: Evalua una condicion para elegir el camino de ejecucion.
        if len(self._sillas) >= 4:
            # Explicacion linea 123: Asigna un valor, configura un argumento o actualiza un dato del escenario.
            descripcion += "\n(Incluye 5% de descuento por set completo)"
        # Explicacion linea 124: Devuelve al llamador el resultado construido por este metodo.
        return descripcion

    # Explicacion linea 126: Declara la funcion y sus parametros de entrada.
    def obtener_resumen(self) -> dict:
        # Explicacion linea 127: Documenta el objetivo y el uso de este bloque.
        """
        Obtiene un resumen estadístico del comedor.

        Returns:
            dict: Diccionario con información resumida
        """
        # Explicacion linea 133: Asigna un valor, configura un argumento o actualiza un dato del escenario.
        resumen = {
            # Explicacion linea 134: Continua la expresion del bloque anterior o ejecuta esta instruccion.
            "nombre": self.nombre,
            # Explicacion linea 135: Continua la expresion del bloque anterior o ejecuta esta instruccion.
            "total_muebles": 1 + len(self._sillas),  # mesa + sillas
            # Explicacion linea 136: Continua la expresion del bloque anterior o ejecuta esta instruccion.
            "precio_mesa": self._mesa.calcular_precio(),
            # Explicacion linea 137: Continua la expresion del bloque anterior o ejecuta esta instruccion.
            "precio_sillas": sum(silla.calcular_precio() for silla in self._sillas),
            # Explicacion linea 138: Continua la expresion del bloque anterior o ejecuta esta instruccion.
            "precio_total": self.calcular_precio_total(),
            # Explicacion linea 139: Continua la expresion del bloque anterior o ejecuta esta instruccion.
            "capacidad_personas": len(self._sillas),
            # Explicacion linea 140: Continua la expresion del bloque anterior o ejecuta esta instruccion.
            "materiales_utilizados": self._obtener_materiales_unicos(),
        # Explicacion linea 141: Cierra la expresion o estructura iniciada anteriormente.
        }
        # Explicacion linea 142: Devuelve al llamador el resultado construido por este metodo.
        return resumen

    # Explicacion linea 144: Declara la funcion y sus parametros de entrada.
    def _obtener_materiales_unicos(self) -> list:
        # Explicacion linea 145: Documenta el objetivo y el uso de este bloque.
        """
        Obtiene una lista de materiales únicos usados en el comedor.
        Método privado auxiliar.

        Returns:
            list: Lista de materiales únicos
        """
        # Explicacion linea 152: Asigna un valor, configura un argumento o actualiza un dato del escenario.
        materiales = set()
        # Explicacion linea 153: Evalua una condicion para elegir el camino de ejecucion.
        if hasattr(self._mesa, "material"):
            # Explicacion linea 154: Continua la expresion del bloque anterior o ejecuta esta instruccion.
            materiales.add(self._mesa.material)
        # Explicacion linea 155: Recorre los elementos de una coleccion para procesarlos.
        for silla in self._sillas:
            # Explicacion linea 156: Evalua una condicion para elegir el camino de ejecucion.
            if hasattr(silla, "material"):
                # Explicacion linea 157: Continua la expresion del bloque anterior o ejecuta esta instruccion.
                materiales.add(silla.material)
            # Explicacion linea 158: Evalua una condicion para elegir el camino de ejecucion.
            if hasattr(silla, "material_tapizado") and getattr(
                # Explicacion linea 159: Continua la expresion del bloque anterior o ejecuta esta instruccion.
                silla, "material_tapizado", None
            # Explicacion linea 160: Cierra la expresion o estructura iniciada anteriormente.
            ):
                # Explicacion linea 161: Continua la expresion del bloque anterior o ejecuta esta instruccion.
                materiales.add(silla.material_tapizado)
        # Explicacion linea 162: Devuelve al llamador el resultado construido por este metodo.
        return list(materiales)

    # Explicacion linea 164: Declara la funcion y sus parametros de entrada.
    def _calcular_capacidad_maxima(self) -> int:
        # Explicacion linea 165: Documenta el objetivo y el uso de este bloque.
        """
        Calcula la capacidad máxima de sillas basada en el tamaño de la mesa.
        Método privado auxiliar.
        """
        # Si la mesa tiene un atributo 'capacidad_personas', úsalo
        # Explicacion linea 170: Evalua una condicion para elegir el camino de ejecucion.
        if hasattr(self._mesa, "capacidad_personas"):
            # Explicacion linea 171: Devuelve al llamador el resultado construido por este metodo.
            return getattr(self._mesa, "capacidad_personas")
        # Valor por defecto
        # Explicacion linea 173: Devuelve al llamador el resultado construido por este metodo.
        return 6

    # Explicacion linea 175: Declara la funcion y sus parametros de entrada.
    def __str__(self) -> str:
        # Explicacion linea 176: Documenta el objetivo y el uso de este bloque.
        """Representación en cadena del comedor."""
        # Explicacion linea 177: Asigna un valor, configura un argumento o actualiza un dato del escenario.
        nombre = getattr(self, "_nombre", "Comedor")
        # Explicacion linea 178: Asigna un valor, configura un argumento o actualiza un dato del escenario.
        sillas = getattr(self, "_sillas", [])
        # Explicacion linea 179: Devuelve al llamador el resultado construido por este metodo.
        return f"Comedor {nombre}: Mesa + {len(sillas)} sillas"

    # Explicacion linea 181: Declara la funcion y sus parametros de entrada.
    def __len__(self) -> int:
        # Explicacion linea 182: Documenta el objetivo y el uso de este bloque.
        """Retorna el número total de muebles en el comedor."""
        # Explicacion linea 183: Devuelve al llamador el resultado construido por este metodo.
        return 1 + len(self._sillas)  # mesa + sillas
