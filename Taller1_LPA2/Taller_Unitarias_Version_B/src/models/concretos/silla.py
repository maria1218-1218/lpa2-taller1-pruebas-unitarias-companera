# Explicacion linea 1: Documenta el objetivo y el uso de este bloque.
"""
Clase concreta Silla.
Implementa un mueble de asiento específico para una persona.
"""

# Explicacion linea 6: Importa las herramientas o clases usadas en este modulo.
from ..categorias.asientos import Asiento


# Explicacion linea 9: Declara una clase que organiza atributos y operaciones del dominio.
class Silla(Asiento):
    # Explicacion linea 10: Documenta el objetivo y el uso de este bloque.
    """
    Clase concreta que representa una silla.

    Una silla es un asiento individual con características específicas
    como altura regulable, ruedas, etc.

    Conceptos OOP aplicados:
    - Herencia: Hereda de Asiento
    - Polimorfismo: Implementa métodos abstractos de manera específica
    - Encapsulación: Protege atributos específicos de la silla
    """

    # Explicacion linea 22: Declara la funcion y sus parametros de entrada.
    def __init__(
        # Explicacion linea 23: Continua la expresion del bloque anterior o ejecuta esta instruccion.
        self,
        # Explicacion linea 24: Continua la expresion del bloque anterior o ejecuta esta instruccion.
        nombre: str,
        # Explicacion linea 25: Continua la expresion del bloque anterior o ejecuta esta instruccion.
        material: str,
        # Explicacion linea 26: Continua la expresion del bloque anterior o ejecuta esta instruccion.
        color: str,
        # Explicacion linea 27: Continua la expresion del bloque anterior o ejecuta esta instruccion.
        precio_base: float,
        # Explicacion linea 28: Asigna un valor, configura un argumento o actualiza un dato del escenario.
        tiene_respaldo: bool = True,
        # Explicacion linea 29: Asigna un valor, configura un argumento o actualiza un dato del escenario.
        material_tapizado: str = None,
        # Explicacion linea 30: Asigna un valor, configura un argumento o actualiza un dato del escenario.
        altura_regulable: bool = False,
        # Explicacion linea 31: Asigna un valor, configura un argumento o actualiza un dato del escenario.
        tiene_ruedas: bool = False,
    # Explicacion linea 32: Cierra la expresion o estructura iniciada anteriormente.
    ):
        # Silla siempre tiene capacidad de 1 persona
        # Explicacion linea 34: Continua la expresion del bloque anterior o ejecuta esta instruccion.
        super().__init__(
            # Explicacion linea 35: Continua la expresion del bloque anterior o ejecuta esta instruccion.
            nombre, material, color, precio_base, 1, tiene_respaldo, material_tapizado
        # Explicacion linea 36: Cierra la expresion o estructura iniciada anteriormente.
        )
        # Explicacion linea 37: Asigna un valor, configura un argumento o actualiza un dato del escenario.
        self._altura_regulable = altura_regulable
        # Explicacion linea 38: Asigna un valor, configura un argumento o actualiza un dato del escenario.
        self._tiene_ruedas = tiene_ruedas

    # Explicacion linea 40: Aplica un decorador a la funcion que aparece a continuacion.
    @property
    # Explicacion linea 41: Declara la funcion y sus parametros de entrada.
    def altura_regulable(self) -> bool:
        # Explicacion linea 42: Documenta el objetivo y el uso de este bloque.
        """Getter para altura regulable."""
        # Explicacion linea 43: Devuelve al llamador el resultado construido por este metodo.
        return self._altura_regulable

    # Explicacion linea 45: Aplica un decorador a la funcion que aparece a continuacion.
    @altura_regulable.setter
    # Explicacion linea 46: Declara la funcion y sus parametros de entrada.
    def altura_regulable(self, value: bool) -> None:
        # Explicacion linea 47: Documenta el objetivo y el uso de este bloque.
        """Setter para altura regulable."""
        # Explicacion linea 48: Asigna un valor, configura un argumento o actualiza un dato del escenario.
        self._altura_regulable = value

    # Explicacion linea 50: Aplica un decorador a la funcion que aparece a continuacion.
    @property
    # Explicacion linea 51: Declara la funcion y sus parametros de entrada.
    def tiene_ruedas(self) -> bool:
        # Explicacion linea 52: Documenta el objetivo y el uso de este bloque.
        """Getter para ruedas."""
        # Explicacion linea 53: Devuelve al llamador el resultado construido por este metodo.
        return self._tiene_ruedas

    # Explicacion linea 55: Aplica un decorador a la funcion que aparece a continuacion.
    @tiene_ruedas.setter
    # Explicacion linea 56: Declara la funcion y sus parametros de entrada.
    def tiene_ruedas(self, value: bool) -> None:
        # Explicacion linea 57: Documenta el objetivo y el uso de este bloque.
        """Setter para ruedas."""
        # Explicacion linea 58: Asigna un valor, configura un argumento o actualiza un dato del escenario.
        self._tiene_ruedas = value

    # Explicacion linea 60: Declara la funcion y sus parametros de entrada.
    def calcular_precio(self) -> float:
        # Explicacion linea 61: Documenta el objetivo y el uso de este bloque.
        """
        Implementa el cálculo de precio específico para sillas.
        Returns:
            float: Precio final de la silla
        """
        # Explicacion linea 66: Asigna un valor, configura un argumento o actualiza un dato del escenario.
        precio = self.precio_base

        # Aplicar factor de comodidad
        # Explicacion linea 69: Asigna un valor, configura un argumento o actualiza un dato del escenario.
        factor_comodidad = self.calcular_factor_comodidad()
        # Explicacion linea 70: Asigna un valor, configura un argumento o actualiza un dato del escenario.
        precio *= factor_comodidad

        # Características específicas de silla
        # Explicacion linea 73: Evalua una condicion para elegir el camino de ejecucion.
        if self.altura_regulable:
            # Explicacion linea 74: Asigna un valor, configura un argumento o actualiza un dato del escenario.
            precio += 30
        # Explicacion linea 75: Evalua una condicion para elegir el camino de ejecucion.
        if self.tiene_ruedas:
            # Explicacion linea 76: Asigna un valor, configura un argumento o actualiza un dato del escenario.
            precio += 20

        # Explicacion linea 78: Devuelve al llamador el resultado construido por este metodo.
        return round(precio, 2)

    # Explicacion linea 80: Declara la funcion y sus parametros de entrada.
    def obtener_descripcion(self) -> str:
        # Explicacion linea 81: Documenta el objetivo y el uso de este bloque.
        """
        Retorna una descripción detallada de la silla, incluyendo nombre y características principales.
        Returns:
            str: Descripción completa de la silla
        """
        # Explicacion linea 86: Asigna un valor, configura un argumento o actualiza un dato del escenario.
        desc = f"Silla: {self.nombre}\n"
        # Explicacion linea 87: Asigna un valor, configura un argumento o actualiza un dato del escenario.
        desc += f"  Material: {self.material}\n"
        # Explicacion linea 88: Asigna un valor, configura un argumento o actualiza un dato del escenario.
        desc += f"  Color: {self.color}\n"
        # Explicacion linea 89: Asigna un valor, configura un argumento o actualiza un dato del escenario.
        desc += f"  {self.obtener_info_asiento()}\n"
        # Explicacion linea 90: Asigna un valor, configura un argumento o actualiza un dato del escenario.
        desc += f"  Altura regulable: {'Sí' if self.altura_regulable else 'No'}\n"
        # Explicacion linea 91: Asigna un valor, configura un argumento o actualiza un dato del escenario.
        desc += f"  Ruedas: {'Sí' if self.tiene_ruedas else 'No'}\n"
        # Explicacion linea 92: Asigna un valor, configura un argumento o actualiza un dato del escenario.
        desc += f"  Precio final: ${self.calcular_precio()}"
        # Explicacion linea 93: Devuelve al llamador el resultado construido por este metodo.
        return desc

    # Explicacion linea 95: Declara la funcion y sus parametros de entrada.
    def regular_altura(self, nueva_altura: int) -> str:
        # Explicacion linea 96: Documenta el objetivo y el uso de este bloque.
        """
        Simula la regulación de altura de la silla.
        Método específico de la clase Silla.

        Args:
            nueva_altura: Nueva altura en centímetros

        Returns:
            str: Mensaje del resultado de la operación
        """
        # Explicacion linea 106: Evalua una condicion para elegir el camino de ejecucion.
        if not self.altura_regulable:
            # Explicacion linea 107: Devuelve al llamador el resultado construido por este metodo.
            return "Esta silla no tiene altura regulable"

        # Explicacion linea 109: Evalua una condicion para elegir el camino de ejecucion.
        if nueva_altura < 40 or nueva_altura > 100:
            # Explicacion linea 110: Devuelve al llamador el resultado construido por este metodo.
            return "La altura debe estar entre 40 y 100 cm"

        # Explicacion linea 112: Devuelve al llamador el resultado construido por este metodo.
        return f"Altura ajustada a {nueva_altura} cm"

    # Explicacion linea 114: Declara la funcion y sus parametros de entrada.
    def es_silla_oficina(self) -> bool:
        # Explicacion linea 115: Documenta el objetivo y el uso de este bloque.
        """
        Determina si la silla es adecuada para oficina.

        Returns:
            bool: True si es silla de oficina
        """
        # Explicacion linea 121: Devuelve al llamador el resultado construido por este metodo.
        return self.altura_regulable and self.tiene_ruedas
