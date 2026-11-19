# Explicacion linea 1: Documenta el objetivo y el uso de este bloque.
"""
Clase abstracta para muebles para superficies de trabajo o del hogar.
"""

# Explicacion linea 5: Importa las herramientas o clases usadas en este modulo.
from abc import ABC, abstractmethod
# Explicacion linea 6: Importa las herramientas o clases usadas en este modulo.
from models.mueble import Mueble


# Explicacion linea 9: Declara una clase que organiza atributos y operaciones del dominio.
class Superficie(Mueble, ABC):
    # Explicacion linea 10: Documenta el objetivo y el uso de este bloque.
    """
    Clase abstracta para muebles tipo superficie (mesas, escritorios, etc).
    Hereda de Mueble y define la interfaz base para este tipo de muebles.

    Conceptos OOP aplicados:
    - Herencia: Extiende la clase Mueble
    - Abstracción: Define características comunes de superficies
    """

    # Explicacion linea 19: Declara la funcion y sus parametros de entrada.
    def __init__(
        # Explicacion linea 20: Continua la expresion del bloque anterior o ejecuta esta instruccion.
        self,
        # Explicacion linea 21: Continua la expresion del bloque anterior o ejecuta esta instruccion.
        nombre: str,
        # Explicacion linea 22: Continua la expresion del bloque anterior o ejecuta esta instruccion.
        material: str,
        # Explicacion linea 23: Continua la expresion del bloque anterior o ejecuta esta instruccion.
        color: str,
        # Explicacion linea 24: Continua la expresion del bloque anterior o ejecuta esta instruccion.
        precio_base: float,
        # Explicacion linea 25: Continua la expresion del bloque anterior o ejecuta esta instruccion.
        largo: float,
        # Explicacion linea 26: Continua la expresion del bloque anterior o ejecuta esta instruccion.
        ancho: float,
        # Explicacion linea 27: Continua la expresion del bloque anterior o ejecuta esta instruccion.
        altura: float,
    # Explicacion linea 28: Cierra la expresion o estructura iniciada anteriormente.
    ):
        # Explicacion linea 29: Documenta el objetivo y el uso de este bloque.
        """
        Constructor para muebles de superficie.

        Args:
            largo: Largo de la superficie en cm
            ancho: Ancho de la superficie en cm
            altura: Altura de la superficie en cm
        """
        # Explicacion linea 37: Continua la expresion del bloque anterior o ejecuta esta instruccion.
        super().__init__(nombre, material, color, precio_base)
        # Explicacion linea 38: Asigna un valor, configura un argumento o actualiza un dato del escenario.
        self._largo = largo
        # Explicacion linea 39: Asigna un valor, configura un argumento o actualiza un dato del escenario.
        self._ancho = ancho
        # Explicacion linea 40: Asigna un valor, configura un argumento o actualiza un dato del escenario.
        self._altura = altura

    # Explicacion linea 42: Aplica un decorador a la funcion que aparece a continuacion.
    @property
    # Explicacion linea 43: Declara la funcion y sus parametros de entrada.
    def largo(self) -> float:
        # Explicacion linea 44: Documenta el objetivo y el uso de este bloque.
        """Getter para largo."""
        # Explicacion linea 45: Devuelve al llamador el resultado construido por este metodo.
        return self._largo

    # Explicacion linea 47: Aplica un decorador a la funcion que aparece a continuacion.
    @largo.setter
    # Explicacion linea 48: Declara la funcion y sus parametros de entrada.
    def largo(self, value: float) -> None:
        # Explicacion linea 49: Documenta el objetivo y el uso de este bloque.
        """Setter para largo con validación."""
        # Explicacion linea 50: Evalua una condicion para elegir el camino de ejecucion.
        if value <= 0:
            # Explicacion linea 51: Informa de una condicion de error mediante una excepcion.
            raise ValueError("El largo debe ser mayor a 0")
        # Explicacion linea 52: Asigna un valor, configura un argumento o actualiza un dato del escenario.
        self._largo = value

    # Explicacion linea 54: Aplica un decorador a la funcion que aparece a continuacion.
    @property
    # Explicacion linea 55: Declara la funcion y sus parametros de entrada.
    def ancho(self) -> float:
        # Explicacion linea 56: Documenta el objetivo y el uso de este bloque.
        """Getter para ancho."""
        # Explicacion linea 57: Devuelve al llamador el resultado construido por este metodo.
        return self._ancho

    # Explicacion linea 59: Aplica un decorador a la funcion que aparece a continuacion.
    @ancho.setter
    # Explicacion linea 60: Declara la funcion y sus parametros de entrada.
    def ancho(self, value: float) -> None:
        # Explicacion linea 61: Documenta el objetivo y el uso de este bloque.
        """Setter para ancho con validación."""
        # Explicacion linea 62: Evalua una condicion para elegir el camino de ejecucion.
        if value <= 0:
            # Explicacion linea 63: Informa de una condicion de error mediante una excepcion.
            raise ValueError("El ancho debe ser mayor a 0")
        # Explicacion linea 64: Asigna un valor, configura un argumento o actualiza un dato del escenario.
        self._ancho = value

    # Explicacion linea 66: Aplica un decorador a la funcion que aparece a continuacion.
    @property
    # Explicacion linea 67: Declara la funcion y sus parametros de entrada.
    def altura(self) -> float:
        # Explicacion linea 68: Documenta el objetivo y el uso de este bloque.
        """Getter para altura."""
        # Explicacion linea 69: Devuelve al llamador el resultado construido por este metodo.
        return self._altura

    # Explicacion linea 71: Aplica un decorador a la funcion que aparece a continuacion.
    @altura.setter
    # Explicacion linea 72: Declara la funcion y sus parametros de entrada.
    def altura(self, value: float) -> None:
        # Explicacion linea 73: Documenta el objetivo y el uso de este bloque.
        """Setter para altura con validación."""
        # Explicacion linea 74: Evalua una condicion para elegir el camino de ejecucion.
        if value <= 0:
            # Explicacion linea 75: Informa de una condicion de error mediante una excepcion.
            raise ValueError("La altura debe ser mayor a 0")
        # Explicacion linea 76: Asigna un valor, configura un argumento o actualiza un dato del escenario.
        self._altura = value

    # Explicacion linea 78: Declara la funcion y sus parametros de entrada.
    def calcular_area(self) -> float:
        # Explicacion linea 79: Documenta el objetivo y el uso de este bloque.
        """
        Calcula el área de la superficie.

        Returns:
            float: Área en cm²
        """
        # Explicacion linea 85: Devuelve al llamador el resultado construido por este metodo.
        return self.largo * self.ancho

    # Explicacion linea 87: Declara la funcion y sus parametros de entrada.
    def calcular_factor_tamaño(self) -> float:
        # Explicacion linea 88: Documenta el objetivo y el uso de este bloque.
        """
        Calcula un factor basado en el tamaño de la superficie.

        Returns:
            float: Factor multiplicador para el precio
        """
        # Explicacion linea 94: Asigna un valor, configura un argumento o actualiza un dato del escenario.
        area = self.calcular_area()
        # Factor basado en área (cada 10000 cm² = +5%)
        # Explicacion linea 96: Asigna un valor, configura un argumento o actualiza un dato del escenario.
        factor = 1.0 + (area / 10000) * 0.05
        # Explicacion linea 97: Devuelve al llamador el resultado construido por este metodo.
        return factor

    # Explicacion linea 99: Declara la funcion y sus parametros de entrada.
    def obtener_info_superficie(self) -> str:
        # Explicacion linea 100: Documenta el objetivo y el uso de este bloque.
        """
        Obtiene información específica de la superficie.

        Returns:
            str: Información detallada de dimensiones
        """
        # Explicacion linea 106: Asigna un valor, configura un argumento o actualiza un dato del escenario.
        area = self.calcular_area()
        # Explicacion linea 107: Devuelve al llamador el resultado construido por este metodo.
        return (
            # Explicacion linea 108: Continua la expresion del bloque anterior o ejecuta esta instruccion.
            f"Dimensiones: {self.largo}x{self.ancho}x{self.altura}cm (Área: {area}cm²)"
        # Explicacion linea 109: Cierra la expresion o estructura iniciada anteriormente.
        )

    # Explicacion linea 111: Aplica un decorador a la funcion que aparece a continuacion.
    @abstractmethod
    # Explicacion linea 112: Declara la funcion y sus parametros de entrada.
    def calcular_precio(self) -> float:
        # Explicacion linea 113: Documenta el objetivo y el uso de este bloque.
        """Método abstracto para calcular precio."""
        # Explicacion linea 114: No realiza ninguna accion en este bloque.
        pass

    # Explicacion linea 116: Aplica un decorador a la funcion que aparece a continuacion.
    @abstractmethod
    # Explicacion linea 117: Declara la funcion y sus parametros de entrada.
    def obtener_descripcion(self) -> str:
        # Explicacion linea 118: Documenta el objetivo y el uso de este bloque.
        """Método abstracto para obtener descripción."""
        # Explicacion linea 119: No realiza ninguna accion en este bloque.
        pass
