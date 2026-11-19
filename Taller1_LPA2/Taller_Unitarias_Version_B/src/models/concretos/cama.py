# Explicacion linea 1: Documenta el objetivo y el uso de este bloque.
"""
Clase concreta Cama.
Representa una cama genérica.
"""

# Explicacion linea 6: Importa las herramientas o clases usadas en este modulo.
from ..mueble import Mueble


# Explicacion linea 9: Declara una clase que organiza atributos y operaciones del dominio.
class Cama(Mueble):
    # Explicacion linea 10: Documenta el objetivo y el uso de este bloque.
    """
    Clase concreta que representa una cama.
    """

    # Explicacion linea 14: Declara la funcion y sus parametros de entrada.
    def __init__(
        # Explicacion linea 15: Continua la expresion del bloque anterior o ejecuta esta instruccion.
        self,
        # Explicacion linea 16: Continua la expresion del bloque anterior o ejecuta esta instruccion.
        nombre: str,
        # Explicacion linea 17: Continua la expresion del bloque anterior o ejecuta esta instruccion.
        material: str,
        # Explicacion linea 18: Continua la expresion del bloque anterior o ejecuta esta instruccion.
        color: str,
        # Explicacion linea 19: Continua la expresion del bloque anterior o ejecuta esta instruccion.
        precio_base: float,
        # Explicacion linea 20: Asigna un valor, configura un argumento o actualiza un dato del escenario.
        tamaño: str = "individual",
        # Explicacion linea 21: Asigna un valor, configura un argumento o actualiza un dato del escenario.
        incluye_colchon: bool = False,
        # Explicacion linea 22: Asigna un valor, configura un argumento o actualiza un dato del escenario.
        tiene_cabecera: bool = False,
    # Explicacion linea 23: Cierra la expresion o estructura iniciada anteriormente.
    ):
        # Explicacion linea 24: Continua la expresion del bloque anterior o ejecuta esta instruccion.
        super().__init__(nombre, material, color, precio_base)
        # Explicacion linea 25: Asigna un valor, configura un argumento o actualiza un dato del escenario.
        self._tamaño = tamaño
        # Explicacion linea 26: Asigna un valor, configura un argumento o actualiza un dato del escenario.
        self._incluye_colchon = incluye_colchon
        # Explicacion linea 27: Asigna un valor, configura un argumento o actualiza un dato del escenario.
        self._tiene_cabecera = tiene_cabecera

    # Explicacion linea 29: Aplica un decorador a la funcion que aparece a continuacion.
    @property
    # Explicacion linea 30: Declara la funcion y sus parametros de entrada.
    def tamaño(self) -> str:
        # Explicacion linea 31: Documenta el objetivo y el uso de este bloque.
        """Getter para tamaño."""
        # Explicacion linea 32: Devuelve al llamador el resultado construido por este metodo.
        return self._tamaño

    # Explicacion linea 34: Aplica un decorador a la funcion que aparece a continuacion.
    @tamaño.setter
    # Explicacion linea 35: Declara la funcion y sus parametros de entrada.
    def tamaño(self, value: str) -> None:
        # Explicacion linea 36: Documenta el objetivo y el uso de este bloque.
        """Setter para tamaño con validación."""
        # Explicacion linea 37: Asigna un valor, configura un argumento o actualiza un dato del escenario.
        tamaños_validos = ["individual", "matrimonial", "queen", "king"]
        # Explicacion linea 38: Evalua una condicion para elegir el camino de ejecucion.
        if value not in tamaños_validos:
            # Explicacion linea 39: Informa de una condicion de error mediante una excepcion.
            raise ValueError(f"Tamaño debe ser uno de: {tamaños_validos}")
        # Explicacion linea 40: Asigna un valor, configura un argumento o actualiza un dato del escenario.
        self._tamaño = value

    # Explicacion linea 42: Aplica un decorador a la funcion que aparece a continuacion.
    @property
    # Explicacion linea 43: Declara la funcion y sus parametros de entrada.
    def incluye_colchon(self) -> bool:
        # Explicacion linea 44: Documenta el objetivo y el uso de este bloque.
        """Getter para colchón."""
        # Explicacion linea 45: Devuelve al llamador el resultado construido por este metodo.
        return self._incluye_colchon

    # Explicacion linea 47: Aplica un decorador a la funcion que aparece a continuacion.
    @property
    # Explicacion linea 48: Declara la funcion y sus parametros de entrada.
    def tiene_cabecera(self) -> bool:
        # Explicacion linea 49: Documenta el objetivo y el uso de este bloque.
        """Getter para cabecera."""
        # Explicacion linea 50: Devuelve al llamador el resultado construido por este metodo.
        return self._tiene_cabecera

    # Explicacion linea 52: Declara la funcion y sus parametros de entrada.
    def calcular_precio(self) -> float:
        # Explicacion linea 53: Documenta el objetivo y el uso de este bloque.
        """Calcula el precio final de la cama."""
        # Explicacion linea 54: Asigna un valor, configura un argumento o actualiza un dato del escenario.
        precio = self.precio_base

        # Ajuste por tamaño
        # Explicacion linea 57: Evalua una condicion para elegir el camino de ejecucion.
        if self.tamaño == "matrimonial":
            # Explicacion linea 58: Asigna un valor, configura un argumento o actualiza un dato del escenario.
            precio += 200
        # Explicacion linea 59: Evalua una condicion para elegir el camino de ejecucion.
        elif self.tamaño == "queen":
            # Explicacion linea 60: Asigna un valor, configura un argumento o actualiza un dato del escenario.
            precio += 400
        # Explicacion linea 61: Evalua una condicion para elegir el camino de ejecucion.
        elif self.tamaño == "king":
            # Explicacion linea 62: Asigna un valor, configura un argumento o actualiza un dato del escenario.
            precio += 600

        # Extras
        # Explicacion linea 65: Evalua una condicion para elegir el camino de ejecucion.
        if self.incluye_colchon:
            # Explicacion linea 66: Asigna un valor, configura un argumento o actualiza un dato del escenario.
            precio += 300
        # Explicacion linea 67: Evalua una condicion para elegir el camino de ejecucion.
        if self.tiene_cabecera:
            # Explicacion linea 68: Asigna un valor, configura un argumento o actualiza un dato del escenario.
            precio += 100

        # Explicacion linea 70: Devuelve al llamador el resultado construido por este metodo.
        return round(precio, 2)

    # Explicacion linea 72: Declara la funcion y sus parametros de entrada.
    def obtener_descripcion(self) -> str:
        # Explicacion linea 73: Documenta el objetivo y el uso de este bloque.
        """
        Retorna una descripción detallada de la cama.
        """
        # Explicacion linea 76: Asigna un valor, configura un argumento o actualiza un dato del escenario.
        desc = f"Cama: {self.nombre}\n"
        # Explicacion linea 77: Asigna un valor, configura un argumento o actualiza un dato del escenario.
        desc += f"  Material: {self.material}\n"
        # Explicacion linea 78: Asigna un valor, configura un argumento o actualiza un dato del escenario.
        desc += f"  Color: {self.color}\n"
        # Explicacion linea 79: Asigna un valor, configura un argumento o actualiza un dato del escenario.
        desc += f"  Tamaño: {self.tamaño}\n"
        # Explicacion linea 80: Asigna un valor, configura un argumento o actualiza un dato del escenario.
        desc += f"  Incluye colchón: {'Sí' if self.incluye_colchon else 'No'}\n"
        # Explicacion linea 81: Asigna un valor, configura un argumento o actualiza un dato del escenario.
        desc += f"  Cabecera: {'Sí' if self.tiene_cabecera else 'No'}\n"
        # Explicacion linea 82: Asigna un valor, configura un argumento o actualiza un dato del escenario.
        desc += f"  Precio final: ${self.calcular_precio()}"
        # Explicacion linea 83: Devuelve al llamador el resultado construido por este metodo.
        return desc
