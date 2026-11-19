# Explicacion linea 1: Documenta el objetivo y el uso de este bloque.
"""
Clase concreta Mesa.
Representa una mesa genérica.
"""

# Explicacion linea 6: Importa las herramientas o clases usadas en este modulo.
from ..categorias.superficies import Superficie


# Explicacion linea 9: Declara una clase que organiza atributos y operaciones del dominio.
class Mesa(Superficie):
    # Explicacion linea 10: Documenta el objetivo y el uso de este bloque.
    """
    Clase concreta que representa una mesa.
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
        forma: str = "rectangular",
        # Explicacion linea 21: Asigna un valor, configura un argumento o actualiza un dato del escenario.
        largo: float = 120.0,
        # Explicacion linea 22: Asigna un valor, configura un argumento o actualiza un dato del escenario.
        ancho: float = 80.0,
        # Explicacion linea 23: Asigna un valor, configura un argumento o actualiza un dato del escenario.
        altura: float = 75.0,
        # Explicacion linea 24: Asigna un valor, configura un argumento o actualiza un dato del escenario.
        capacidad_personas: int = 4,
    # Explicacion linea 25: Cierra la expresion o estructura iniciada anteriormente.
    ):
        # Explicacion linea 26: Continua la expresion del bloque anterior o ejecuta esta instruccion.
        super().__init__(nombre, material, color, precio_base, largo, ancho, altura)
        # Explicacion linea 27: Asigna un valor, configura un argumento o actualiza un dato del escenario.
        self._forma = forma
        # Explicacion linea 28: Asigna un valor, configura un argumento o actualiza un dato del escenario.
        self._capacidad_personas = capacidad_personas

    # Explicacion linea 30: Aplica un decorador a la funcion que aparece a continuacion.
    @property
    # Explicacion linea 31: Declara la funcion y sus parametros de entrada.
    def forma(self) -> str:
        # Explicacion linea 32: Documenta el objetivo y el uso de este bloque.
        """Getter para forma."""
        # Explicacion linea 33: Devuelve al llamador el resultado construido por este metodo.
        return self._forma

    # Explicacion linea 35: Aplica un decorador a la funcion que aparece a continuacion.
    @forma.setter
    # Explicacion linea 36: Declara la funcion y sus parametros de entrada.
    def forma(self, value: str) -> None:
        # Explicacion linea 37: Documenta el objetivo y el uso de este bloque.
        """Setter para forma con validación."""
        # Explicacion linea 38: Asigna un valor, configura un argumento o actualiza un dato del escenario.
        formas_validas = ["rectangular", "redonda", "cuadrada", "ovalada"]
        # Explicacion linea 39: Evalua una condicion para elegir el camino de ejecucion.
        if value not in formas_validas:
            # Explicacion linea 40: Informa de una condicion de error mediante una excepcion.
            raise ValueError(f"Forma debe ser una de: {formas_validas}")
        # Explicacion linea 41: Asigna un valor, configura un argumento o actualiza un dato del escenario.
        self._forma = value

    # Explicacion linea 43: Aplica un decorador a la funcion que aparece a continuacion.
    @property
    # Explicacion linea 44: Declara la funcion y sus parametros de entrada.
    def capacidad_personas(self) -> int:
        # Explicacion linea 45: Documenta el objetivo y el uso de este bloque.
        """Getter para capacidad de personas."""
        # Explicacion linea 46: Devuelve al llamador el resultado construido por este metodo.
        return self._capacidad_personas

    # Explicacion linea 48: Aplica un decorador a la funcion que aparece a continuacion.
    @capacidad_personas.setter
    # Explicacion linea 49: Declara la funcion y sus parametros de entrada.
    def capacidad_personas(self, value: int) -> None:
        # Explicacion linea 50: Documenta el objetivo y el uso de este bloque.
        """Setter para capacidad con validación."""
        # Explicacion linea 51: Evalua una condicion para elegir el camino de ejecucion.
        if value <= 0:
            # Explicacion linea 52: Informa de una condicion de error mediante una excepcion.
            raise ValueError("La capacidad debe ser mayor a 0")
        # Explicacion linea 53: Asigna un valor, configura un argumento o actualiza un dato del escenario.
        self._capacidad_personas = value

    # Explicacion linea 55: Declara la funcion y sus parametros de entrada.
    def calcular_precio(self) -> float:
        # Explicacion linea 56: Documenta el objetivo y el uso de este bloque.
        """Calcula el precio final de la mesa."""
        # Explicacion linea 57: Asigna un valor, configura un argumento o actualiza un dato del escenario.
        precio = self.precio_base

        # Aplicar factor de tamaño
        # Explicacion linea 60: Asigna un valor, configura un argumento o actualiza un dato del escenario.
        factor_tamaño = self.calcular_factor_tamaño()
        # Explicacion linea 61: Asigna un valor, configura un argumento o actualiza un dato del escenario.
        precio *= factor_tamaño

        # Ajuste por forma
        # Explicacion linea 64: Evalua una condicion para elegir el camino de ejecucion.
        if self.forma != "rectangular":
            # Explicacion linea 65: Asigna un valor, configura un argumento o actualiza un dato del escenario.
            precio += 50

        # Ajuste por capacidad de personas
        # Explicacion linea 68: Evalua una condicion para elegir el camino de ejecucion.
        if self.capacidad_personas > 6:
            # Explicacion linea 69: Asigna un valor, configura un argumento o actualiza un dato del escenario.
            precio += 100
        # Explicacion linea 70: Evalua una condicion para elegir el camino de ejecucion.
        elif self.capacidad_personas > 4:
            # Explicacion linea 71: Asigna un valor, configura un argumento o actualiza un dato del escenario.
            precio += 50

        # Explicacion linea 73: Devuelve al llamador el resultado construido por este metodo.
        return round(precio, 2)

    # Explicacion linea 75: Declara la funcion y sus parametros de entrada.
    def obtener_descripcion(self) -> str:
        # Explicacion linea 76: Documenta el objetivo y el uso de este bloque.
        """
        Retorna una descripción detallada de la mesa.
        """
        # Explicacion linea 79: Asigna un valor, configura un argumento o actualiza un dato del escenario.
        desc = f"Mesa: {self.nombre}\n"
        # Explicacion linea 80: Asigna un valor, configura un argumento o actualiza un dato del escenario.
        desc += f"  Material: {self.material}\n"
        # Explicacion linea 81: Asigna un valor, configura un argumento o actualiza un dato del escenario.
        desc += f"  Color: {self.color}\n"
        # Explicacion linea 82: Asigna un valor, configura un argumento o actualiza un dato del escenario.
        desc += f"  Forma: {self.forma}\n"
        # Explicacion linea 83: Asigna un valor, configura un argumento o actualiza un dato del escenario.
        desc += f"  {self.obtener_info_superficie()}\n"
        # Explicacion linea 84: Asigna un valor, configura un argumento o actualiza un dato del escenario.
        desc += f"  Capacidad: {self.capacidad_personas} personas\n"
        # Explicacion linea 85: Asigna un valor, configura un argumento o actualiza un dato del escenario.
        desc += f"  Precio final: ${self.calcular_precio()}"
        # Explicacion linea 86: Devuelve al llamador el resultado construido por este metodo.
        return desc
