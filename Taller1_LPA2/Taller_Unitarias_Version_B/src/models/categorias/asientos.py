# Explicacion linea 1: Documenta el objetivo y el uso de este bloque.
"""
Clase abstracta para muebles de asiento.
Esta clase agrupa las características comunes de sillas, sillones y sofás.
"""

# Explicacion linea 6: Importa las herramientas o clases usadas en este modulo.
from abc import ABC, abstractmethod
# Explicacion linea 7: Importa las herramientas o clases usadas en este modulo.
from models.mueble import Mueble


# Explicacion linea 10: Declara una clase que organiza atributos y operaciones del dominio.
class Asiento(Mueble, ABC):
    # Explicacion linea 11: Documenta el objetivo y el uso de este bloque.
    """
    Clase abstracta para todos los muebles donde las personas se sientan.

    Hereda de Mueble y añade características específicas de los asientos
    como capacidad de personas, tipo de respaldo, etc.

    Conceptos OOP aplicados:
    - Herencia: Extiende la clase Mueble
    - Abstracción: Agrupa características comunes de asientos
    - Polimorfismo: Permite diferentes implementaciones del cálculo de comodidad
    """

    # Explicacion linea 23: Declara la funcion y sus parametros de entrada.
    def __init__(
        # Explicacion linea 24: Continua la expresion del bloque anterior o ejecuta esta instruccion.
        self,
        # Explicacion linea 25: Continua la expresion del bloque anterior o ejecuta esta instruccion.
        nombre: str,
        # Explicacion linea 26: Continua la expresion del bloque anterior o ejecuta esta instruccion.
        material: str,
        # Explicacion linea 27: Continua la expresion del bloque anterior o ejecuta esta instruccion.
        color: str,
        # Explicacion linea 28: Continua la expresion del bloque anterior o ejecuta esta instruccion.
        precio_base: float,
        # Explicacion linea 29: Continua la expresion del bloque anterior o ejecuta esta instruccion.
        capacidad_personas: int,
        # Explicacion linea 30: Continua la expresion del bloque anterior o ejecuta esta instruccion.
        tiene_respaldo: bool,
        # Explicacion linea 31: Asigna un valor, configura un argumento o actualiza un dato del escenario.
        material_tapizado: str = None,
    # Explicacion linea 32: Cierra la expresion o estructura iniciada anteriormente.
    ):
        # Explicacion linea 33: Documenta el objetivo y el uso de este bloque.
        """
        Constructor para muebles de asiento.

        Args:
            capacidad_personas: Número de personas que pueden sentarse
            tiene_respaldo: Si el asiento tiene respaldo o no
            material_tapizado: Material del tapizado (opcional)
            Otros argumentos heredados de Mueble
        """
        # Explicacion linea 42: Continua la expresion del bloque anterior o ejecuta esta instruccion.
        super().__init__(nombre, material, color, precio_base)

        # Explicacion linea 44: Asigna un valor, configura un argumento o actualiza un dato del escenario.
        self._capacidad_personas = capacidad_personas
        # Explicacion linea 45: Asigna un valor, configura un argumento o actualiza un dato del escenario.
        self._tiene_respaldo = tiene_respaldo
        # Explicacion linea 46: Asigna un valor, configura un argumento o actualiza un dato del escenario.
        self._material_tapizado = material_tapizado

    # Explicacion linea 48: Aplica un decorador a la funcion que aparece a continuacion.
    @property
    # Explicacion linea 49: Declara la funcion y sus parametros de entrada.
    def capacidad_personas(self) -> int:
        # Explicacion linea 50: Documenta el objetivo y el uso de este bloque.
        """Getter para la capacidad de personas."""
        # Explicacion linea 51: Devuelve al llamador el resultado construido por este metodo.
        return self._capacidad_personas

    # Explicacion linea 53: Aplica un decorador a la funcion que aparece a continuacion.
    @capacidad_personas.setter
    # Explicacion linea 54: Declara la funcion y sus parametros de entrada.
    def capacidad_personas(self, value: int) -> None:
        # Explicacion linea 55: Documenta el objetivo y el uso de este bloque.
        """Setter para capacidad con validación."""
        # Explicacion linea 56: Evalua una condicion para elegir el camino de ejecucion.
        if value <= 0:
            # Explicacion linea 57: Informa de una condicion de error mediante una excepcion.
            raise ValueError("La capacidad debe ser mayor a 0")
        # Explicacion linea 58: Asigna un valor, configura un argumento o actualiza un dato del escenario.
        self._capacidad_personas = value

    # Explicacion linea 60: Aplica un decorador a la funcion que aparece a continuacion.
    @property
    # Explicacion linea 61: Declara la funcion y sus parametros de entrada.
    def tiene_respaldo(self) -> bool:
        # Explicacion linea 62: Documenta el objetivo y el uso de este bloque.
        """Getter para si tiene respaldo."""
        # Explicacion linea 63: Devuelve al llamador el resultado construido por este metodo.
        return self._tiene_respaldo

    # Explicacion linea 65: Aplica un decorador a la funcion que aparece a continuacion.
    @tiene_respaldo.setter
    # Explicacion linea 66: Declara la funcion y sus parametros de entrada.
    def tiene_respaldo(self, value: bool) -> None:
        # Explicacion linea 67: Documenta el objetivo y el uso de este bloque.
        """Setter para respaldo."""
        # Explicacion linea 68: Asigna un valor, configura un argumento o actualiza un dato del escenario.
        self._tiene_respaldo = value

    # Explicacion linea 70: Aplica un decorador a la funcion que aparece a continuacion.
    @property
    # Explicacion linea 71: Declara la funcion y sus parametros de entrada.
    def material_tapizado(self) -> str:
        # Explicacion linea 72: Documenta el objetivo y el uso de este bloque.
        """Getter para el material de tapizado."""
        # Explicacion linea 73: Devuelve al llamador el resultado construido por este metodo.
        return self._material_tapizado

    # Explicacion linea 75: Aplica un decorador a la funcion que aparece a continuacion.
    @material_tapizado.setter
    # Explicacion linea 76: Declara la funcion y sus parametros de entrada.
    def material_tapizado(self, value: str) -> None:
        # Explicacion linea 77: Documenta el objetivo y el uso de este bloque.
        """Setter para material de tapizado."""
        # Explicacion linea 78: Asigna un valor, configura un argumento o actualiza un dato del escenario.
        self._material_tapizado = value

    # Explicacion linea 80: Declara la funcion y sus parametros de entrada.
    def calcular_factor_comodidad(self) -> float:
        # Explicacion linea 81: Documenta el objetivo y el uso de este bloque.
        """
        Calcula un factor de comodidad basado en las características del asiento.
        Este es un método concreto que pueden usar las clases hijas.

        Returns:
            float: Factor multiplicador para el precio (1.0 = neutral)
        """
        # Explicacion linea 88: Asigna un valor, configura un argumento o actualiza un dato del escenario.
        factor = 1.0

        # Explicacion linea 90: Evalua una condicion para elegir el camino de ejecucion.
        if self.tiene_respaldo:
            # Explicacion linea 91: Asigna un valor, configura un argumento o actualiza un dato del escenario.
            factor += 0.1

        # Explicacion linea 93: Evalua una condicion para elegir el camino de ejecucion.
        if self.material_tapizado:
            # Explicacion linea 94: Evalua una condicion para elegir el camino de ejecucion.
            if self.material_tapizado.lower() == "cuero":
                # Explicacion linea 95: Asigna un valor, configura un argumento o actualiza un dato del escenario.
                factor += 0.2
            # Explicacion linea 96: Evalua una condicion para elegir el camino de ejecucion.
            elif self.material_tapizado.lower() == "tela":
                # Explicacion linea 97: Asigna un valor, configura un argumento o actualiza un dato del escenario.
                factor += 0.1

        # Factor adicional por capacidad
        # Explicacion linea 100: Asigna un valor, configura un argumento o actualiza un dato del escenario.
        factor += (self.capacidad_personas - 1) * 0.05

        # Explicacion linea 102: Devuelve al llamador el resultado construido por este metodo.
        return factor

    # Explicacion linea 104: Declara la funcion y sus parametros de entrada.
    def obtener_info_asiento(self) -> str:
        # Explicacion linea 105: Documenta el objetivo y el uso de este bloque.
        """
        Obtiene información específica del asiento.
        Método concreto auxiliar para las clases hijas.

        Returns:
            str: Información detallada del asiento
        """
        # Explicacion linea 112: Asigna un valor, configura un argumento o actualiza un dato del escenario.
        info = f"Capacidad: {self.capacidad_personas} personas"
        # Explicacion linea 113: Asigna un valor, configura un argumento o actualiza un dato del escenario.
        info += f", Respaldo: {'Sí' if self.tiene_respaldo else 'No'}"
        # Explicacion linea 114: Evalua una condicion para elegir el camino de ejecucion.
        if self.material_tapizado:
            # Explicacion linea 115: Asigna un valor, configura un argumento o actualiza un dato del escenario.
            info += f", Tapizado: {self.material_tapizado}"
        # Explicacion linea 116: Devuelve al llamador el resultado construido por este metodo.
        return info

    # Explicacion linea 118: Aplica un decorador a la funcion que aparece a continuacion.
    @abstractmethod
    # Explicacion linea 119: Declara la funcion y sus parametros de entrada.
    def calcular_precio(self) -> float:
        # Explicacion linea 120: Documenta el objetivo y el uso de este bloque.
        """
        Método abstracto para calcular el precio del asiento.
        Cada clase concreta debe implementar su propio cálculo.
        """
        # Explicacion linea 124: No realiza ninguna accion en este bloque.
        pass

    # Explicacion linea 126: Aplica un decorador a la funcion que aparece a continuacion.
    @abstractmethod
    # Explicacion linea 127: Declara la funcion y sus parametros de entrada.
    def obtener_descripcion(self) -> str:
        # Explicacion linea 128: Documenta el objetivo y el uso de este bloque.
        """
        Método abstracto para obtener la descripción del asiento.
        Cada clase concreta debe implementar su propia descripción.
        """
        # Explicacion linea 132: No realiza ninguna accion en este bloque.
        pass
