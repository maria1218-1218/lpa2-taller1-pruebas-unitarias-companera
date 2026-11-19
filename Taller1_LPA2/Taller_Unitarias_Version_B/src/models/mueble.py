# Explicacion linea 1: Documenta el objetivo y el uso de este bloque.
"""
Clase base abstracta Mueble
Este es el punto de partida de nuestra jerarquía de clases.
"""

# Explicacion linea 6: Importa las herramientas o clases usadas en este modulo.
from abc import ABC, abstractmethod


# Explicacion linea 9: Declara una clase que organiza atributos y operaciones del dominio.
class Mueble(ABC):
    # Explicacion linea 10: Documenta el objetivo y el uso de este bloque.
    """
    Clase abstracta base para todos los muebles.

    Esta clase define la estructura común que deben tener todos los muebles
    de nuestra tienda, pero no puede ser instanciada directamente.

    Conceptos OOP aplicados:
    - Abstracción: Define una interfaz común sin implementación específica
    - Encapsulación: Usa atributos privados con getters/setters
    """

    # Explicacion linea 21: Declara la funcion y sus parametros de entrada.
    def __init__(self, nombre: str, material: str, color: str, precio_base: float):
        # Explicacion linea 22: Documenta el objetivo y el uso de este bloque.
        """
        Constructor de la clase Mueble.

        Args:
            nombre: Nombre del mueble
            material: Material principal (madera, metal, plástico, etc.)
            color: Color del mueble
            precio_base: Precio base antes de aplicar modificadores
        """
        # Explicacion linea 31: Asigna un valor, configura un argumento o actualiza un dato del escenario.
        self._nombre = nombre
        # Explicacion linea 32: Asigna un valor, configura un argumento o actualiza un dato del escenario.
        self._material = material
        # Explicacion linea 33: Asigna un valor, configura un argumento o actualiza un dato del escenario.
        self._color = color
        # Explicacion linea 34: Asigna un valor, configura un argumento o actualiza un dato del escenario.
        self._precio_base = precio_base

    # Explicacion linea 36: Aplica un decorador a la funcion que aparece a continuacion.
    @property
    # Explicacion linea 37: Declara la funcion y sus parametros de entrada.
    def nombre(self) -> str:
        # Explicacion linea 38: Documenta el objetivo y el uso de este bloque.
        """Getter para el nombre del mueble."""
        # Explicacion linea 39: Devuelve al llamador el resultado construido por este metodo.
        return self._nombre

    # Explicacion linea 41: Aplica un decorador a la funcion que aparece a continuacion.
    @nombre.setter
    # Explicacion linea 42: Declara la funcion y sus parametros de entrada.
    def nombre(self, value: str) -> None:
        # Explicacion linea 43: Documenta el objetivo y el uso de este bloque.
        """Setter para el nombre con validación."""
        # Explicacion linea 44: Evalua una condicion para elegir el camino de ejecucion.
        if not value or not value.strip():
            # Explicacion linea 45: Informa de una condicion de error mediante una excepcion.
            raise ValueError("El nombre no puede estar vacío")
        # Explicacion linea 46: Asigna un valor, configura un argumento o actualiza un dato del escenario.
        self._nombre = value.strip()

    # Explicacion linea 48: Aplica un decorador a la funcion que aparece a continuacion.
    @property
    # Explicacion linea 49: Declara la funcion y sus parametros de entrada.
    def material(self) -> str:
        # Explicacion linea 50: Documenta el objetivo y el uso de este bloque.
        """Getter para el material del mueble."""
        # Explicacion linea 51: Devuelve al llamador el resultado construido por este metodo.
        return self._material

    # Explicacion linea 53: Aplica un decorador a la funcion que aparece a continuacion.
    @material.setter
    # Explicacion linea 54: Declara la funcion y sus parametros de entrada.
    def material(self, value: str) -> None:
        # Explicacion linea 55: Documenta el objetivo y el uso de este bloque.
        """Setter para el material con validación."""
        # Explicacion linea 56: Evalua una condicion para elegir el camino de ejecucion.
        if not value or not value.strip():
            # Explicacion linea 57: Informa de una condicion de error mediante una excepcion.
            raise ValueError("El material no puede estar vacío")
        # Explicacion linea 58: Asigna un valor, configura un argumento o actualiza un dato del escenario.
        self._material = value.strip()

    # Explicacion linea 60: Aplica un decorador a la funcion que aparece a continuacion.
    @property
    # Explicacion linea 61: Declara la funcion y sus parametros de entrada.
    def color(self) -> str:
        # Explicacion linea 62: Documenta el objetivo y el uso de este bloque.
        """Getter para el color del mueble."""
        # Explicacion linea 63: Devuelve al llamador el resultado construido por este metodo.
        return self._color

    # Explicacion linea 65: Aplica un decorador a la funcion que aparece a continuacion.
    @color.setter
    # Explicacion linea 66: Declara la funcion y sus parametros de entrada.
    def color(self, value: str) -> None:
        # Explicacion linea 67: Documenta el objetivo y el uso de este bloque.
        """Setter para el color con validación."""
        # Explicacion linea 68: Evalua una condicion para elegir el camino de ejecucion.
        if not value or not value.strip():
            # Explicacion linea 69: Informa de una condicion de error mediante una excepcion.
            raise ValueError("El color no puede estar vacío")
        # Explicacion linea 70: Asigna un valor, configura un argumento o actualiza un dato del escenario.
        self._color = value.strip()

    # Explicacion linea 72: Aplica un decorador a la funcion que aparece a continuacion.
    @property
    # Explicacion linea 73: Declara la funcion y sus parametros de entrada.
    def precio_base(self) -> float:
        # Explicacion linea 74: Documenta el objetivo y el uso de este bloque.
        """Getter para el precio base del mueble."""
        # Explicacion linea 75: Devuelve al llamador el resultado construido por este metodo.
        return self._precio_base

    # Explicacion linea 77: Aplica un decorador a la funcion que aparece a continuacion.
    @precio_base.setter
    # Explicacion linea 78: Declara la funcion y sus parametros de entrada.
    def precio_base(self, value: float) -> None:
        # Explicacion linea 79: Documenta el objetivo y el uso de este bloque.
        """Setter para el precio base con validación."""
        # Explicacion linea 80: Evalua una condicion para elegir el camino de ejecucion.
        if value < 0:
            # Explicacion linea 81: Informa de una condicion de error mediante una excepcion.
            raise ValueError("El precio base no puede ser negativo")
        # Explicacion linea 82: Asigna un valor, configura un argumento o actualiza un dato del escenario.
        self._precio_base = value

    # Explicacion linea 84: Aplica un decorador a la funcion que aparece a continuacion.
    @abstractmethod
    # Explicacion linea 85: Declara la funcion y sus parametros de entrada.
    def calcular_precio(self) -> float:
        # Explicacion linea 86: Documenta el objetivo y el uso de este bloque.
        """
        Calcula el precio final del mueble.
        Este método debe ser implementado por cada clase concreta.

        Returns:
            float: Precio final calculado
        """
        # Explicacion linea 93: No realiza ninguna accion en este bloque.
        pass

    # Explicacion linea 95: Aplica un decorador a la funcion que aparece a continuacion.
    @abstractmethod
    # Explicacion linea 96: Declara la funcion y sus parametros de entrada.
    def obtener_descripcion(self) -> str:
        # Explicacion linea 97: Documenta el objetivo y el uso de este bloque.
        """
        Obtiene una descripción detallada del mueble.
        Este método debe ser implementado por cada clase concreta.

        Returns:
            str: Descripción completa del mueble
        """
        # Explicacion linea 104: No realiza ninguna accion en este bloque.
        pass

    # Explicacion linea 106: Declara la funcion y sus parametros de entrada.
    def __str__(self) -> str:
        # Explicacion linea 107: Documenta el objetivo y el uso de este bloque.
        """
        Representación en cadena del mueble.
        Este método concreto puede ser usado por todas las clases hijas.
        """
        # Explicacion linea 111: Devuelve al llamador el resultado construido por este metodo.
        return f"{self.nombre} de {self.material} en color {self.color}"

    # Explicacion linea 113: Declara la funcion y sus parametros de entrada.
    def __repr__(self) -> str:
        # Explicacion linea 114: Documenta el objetivo y el uso de este bloque.
        """
        Representación técnica del mueble para debugging.
        """
        # Explicacion linea 117: Devuelve al llamador el resultado construido por este metodo.
        return f"Mueble(nombre='{self.nombre}', material='{self.material}', color='{self.color}', precio_base={self.precio_base})"
