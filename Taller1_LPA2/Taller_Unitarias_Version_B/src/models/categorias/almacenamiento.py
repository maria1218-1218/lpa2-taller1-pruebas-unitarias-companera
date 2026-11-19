# Explicacion linea 1: Documenta el objetivo y el uso de este bloque.
"""
Clase abstracta para muebles de almacenamiento.
"""

# Explicacion linea 5: Importa las herramientas o clases usadas en este modulo.
from abc import ABC, abstractmethod
# Explicacion linea 6: Importa las herramientas o clases usadas en este modulo.
from models.mueble import Mueble


# Explicacion linea 9: Declara una clase que organiza atributos y operaciones del dominio.
class Almacenamiento(Mueble, ABC):
    # Explicacion linea 10: Documenta el objetivo y el uso de este bloque.
    """
    Clase abstracta para muebles de almacenamiento (como armarios, cajoneras, etc).
    Hereda de Mueble y define la interfaz base para este tipo de muebles.

    Conceptos OOP aplicados:
    - Herencia: Extiende la clase Mueble
    - Abstracción: Define características comunes de almacenamiento
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
        num_compartimentos: int,
        # Explicacion linea 26: Continua la expresion del bloque anterior o ejecuta esta instruccion.
        capacidad_litros: float,
    # Explicacion linea 27: Cierra la expresion o estructura iniciada anteriormente.
    ):
        # Explicacion linea 28: Documenta el objetivo y el uso de este bloque.
        """
        Constructor para muebles de almacenamiento.

        Args:
            num_compartimentos: Número de compartimentos/divisiones
            capacidad_litros: Capacidad en litros de almacenamiento
        """
        # Explicacion linea 35: Continua la expresion del bloque anterior o ejecuta esta instruccion.
        super().__init__(nombre, material, color, precio_base)
        # Explicacion linea 36: Asigna un valor, configura un argumento o actualiza un dato del escenario.
        self._num_compartimentos = num_compartimentos
        # Explicacion linea 37: Asigna un valor, configura un argumento o actualiza un dato del escenario.
        self._capacidad_litros = capacidad_litros

    # Explicacion linea 39: Aplica un decorador a la funcion que aparece a continuacion.
    @property
    # Explicacion linea 40: Declara la funcion y sus parametros de entrada.
    def num_compartimentos(self) -> int:
        # Explicacion linea 41: Documenta el objetivo y el uso de este bloque.
        """Getter para número de compartimentos."""
        # Explicacion linea 42: Devuelve al llamador el resultado construido por este metodo.
        return self._num_compartimentos

    # Explicacion linea 44: Aplica un decorador a la funcion que aparece a continuacion.
    @num_compartimentos.setter
    # Explicacion linea 45: Declara la funcion y sus parametros de entrada.
    def num_compartimentos(self, value: int) -> None:
        # Explicacion linea 46: Documenta el objetivo y el uso de este bloque.
        """Setter para compartimentos con validación."""
        # Explicacion linea 47: Evalua una condicion para elegir el camino de ejecucion.
        if value <= 0:
            # Explicacion linea 48: Informa de una condicion de error mediante una excepcion.
            raise ValueError("El número de compartimentos debe ser mayor a 0")
        # Explicacion linea 49: Asigna un valor, configura un argumento o actualiza un dato del escenario.
        self._num_compartimentos = value

    # Explicacion linea 51: Aplica un decorador a la funcion que aparece a continuacion.
    @property
    # Explicacion linea 52: Declara la funcion y sus parametros de entrada.
    def capacidad_litros(self) -> float:
        # Explicacion linea 53: Documenta el objetivo y el uso de este bloque.
        """Getter para capacidad en litros."""
        # Explicacion linea 54: Devuelve al llamador el resultado construido por este metodo.
        return self._capacidad_litros

    # Explicacion linea 56: Aplica un decorador a la funcion que aparece a continuacion.
    @capacidad_litros.setter
    # Explicacion linea 57: Declara la funcion y sus parametros de entrada.
    def capacidad_litros(self, value: float) -> None:
        # Explicacion linea 58: Documenta el objetivo y el uso de este bloque.
        """Setter para capacidad con validación."""
        # Explicacion linea 59: Evalua una condicion para elegir el camino de ejecucion.
        if value <= 0:
            # Explicacion linea 60: Informa de una condicion de error mediante una excepcion.
            raise ValueError("La capacidad debe ser mayor a 0")
        # Explicacion linea 61: Asigna un valor, configura un argumento o actualiza un dato del escenario.
        self._capacidad_litros = value

    # Explicacion linea 63: Declara la funcion y sus parametros de entrada.
    def calcular_factor_almacenamiento(self) -> float:
        # Explicacion linea 64: Documenta el objetivo y el uso de este bloque.
        """
        Calcula un factor basado en la capacidad de almacenamiento.

        Returns:
            float: Factor multiplicador para el precio
        """
        # Explicacion linea 70: Asigna un valor, configura un argumento o actualiza un dato del escenario.
        factor = 1.0
        # Más compartimentos = más funcionalidad
        # Explicacion linea 72: Asigna un valor, configura un argumento o actualiza un dato del escenario.
        factor += (self.num_compartimentos - 1) * 0.05
        # Mayor capacidad = mayor precio
        # Explicacion linea 74: Asigna un valor, configura un argumento o actualiza un dato del escenario.
        factor += (self.capacidad_litros / 100) * 0.02
        # Explicacion linea 75: Devuelve al llamador el resultado construido por este metodo.
        return factor

    # Explicacion linea 77: Declara la funcion y sus parametros de entrada.
    def obtener_info_almacenamiento(self) -> str:
        # Explicacion linea 78: Documenta el objetivo y el uso de este bloque.
        """
        Obtiene información específica del almacenamiento.

        Returns:
            str: Información detallada del almacenamiento
        """
        # Explicacion linea 84: Devuelve al llamador el resultado construido por este metodo.
        return f"Compartimentos: {self.num_compartimentos}, Capacidad: {self.capacidad_litros}L"

    # Explicacion linea 86: Aplica un decorador a la funcion que aparece a continuacion.
    @abstractmethod
    # Explicacion linea 87: Declara la funcion y sus parametros de entrada.
    def calcular_precio(self) -> float:
        # Explicacion linea 88: Documenta el objetivo y el uso de este bloque.
        """Método abstracto para calcular precio."""
        # Explicacion linea 89: No realiza ninguna accion en este bloque.
        pass

    # Explicacion linea 91: Aplica un decorador a la funcion que aparece a continuacion.
    @abstractmethod
    # Explicacion linea 92: Declara la funcion y sus parametros de entrada.
    def obtener_descripcion(self) -> str:
        # Explicacion linea 93: Documenta el objetivo y el uso de este bloque.
        """Método abstracto para obtener descripción."""
        # Explicacion linea 94: No realiza ninguna accion en este bloque.
        pass
