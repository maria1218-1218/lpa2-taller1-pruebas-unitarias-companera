# Explicacion linea 1: Documenta el objetivo y el uso de este bloque.
"""
Clase concreta Sofa.
Implementa un mueble de asiento para varias personas, sin brazos reclinables.
"""

# Explicacion linea 6: Importa las herramientas o clases usadas en este modulo.
from ..categorias.asientos import Asiento


# Explicacion linea 9: Declara una clase que organiza atributos y operaciones del dominio.
class Sofa(Asiento):
    # Explicacion linea 10: Documenta el objetivo y el uso de este bloque.
    """
    Clase concreta que representa un sofá.
    Hereda de Asiento y añade características específicas.
    """

    # Explicacion linea 15: Declara la funcion y sus parametros de entrada.
    def __init__(
        # Explicacion linea 16: Continua la expresion del bloque anterior o ejecuta esta instruccion.
        self,
        # Explicacion linea 17: Continua la expresion del bloque anterior o ejecuta esta instruccion.
        nombre: str,
        # Explicacion linea 18: Continua la expresion del bloque anterior o ejecuta esta instruccion.
        material: str,
        # Explicacion linea 19: Continua la expresion del bloque anterior o ejecuta esta instruccion.
        color: str,
        # Explicacion linea 20: Continua la expresion del bloque anterior o ejecuta esta instruccion.
        precio_base: float,
        # Explicacion linea 21: Asigna un valor, configura un argumento o actualiza un dato del escenario.
        capacidad_personas: int = 3,
        # Explicacion linea 22: Asigna un valor, configura un argumento o actualiza un dato del escenario.
        tiene_respaldo: bool = True,
        # Explicacion linea 23: Asigna un valor, configura un argumento o actualiza un dato del escenario.
        material_tapizado: str = None,
        # Explicacion linea 24: Asigna un valor, configura un argumento o actualiza un dato del escenario.
        tiene_brazos: bool = True,
        # Explicacion linea 25: Asigna un valor, configura un argumento o actualiza un dato del escenario.
        es_modular: bool = False,
        # Explicacion linea 26: Asigna un valor, configura un argumento o actualiza un dato del escenario.
        incluye_cojines: bool = False,
    # Explicacion linea 27: Cierra la expresion o estructura iniciada anteriormente.
    ):
        # Explicacion linea 28: Continua la expresion del bloque anterior o ejecuta esta instruccion.
        super().__init__(
            # Explicacion linea 29: Continua la expresion del bloque anterior o ejecuta esta instruccion.
            nombre,
            # Explicacion linea 30: Continua la expresion del bloque anterior o ejecuta esta instruccion.
            material,
            # Explicacion linea 31: Continua la expresion del bloque anterior o ejecuta esta instruccion.
            color,
            # Explicacion linea 32: Continua la expresion del bloque anterior o ejecuta esta instruccion.
            precio_base,
            # Explicacion linea 33: Continua la expresion del bloque anterior o ejecuta esta instruccion.
            capacidad_personas,
            # Explicacion linea 34: Continua la expresion del bloque anterior o ejecuta esta instruccion.
            tiene_respaldo,
            # Explicacion linea 35: Continua la expresion del bloque anterior o ejecuta esta instruccion.
            material_tapizado,
        # Explicacion linea 36: Cierra la expresion o estructura iniciada anteriormente.
        )
        # Explicacion linea 37: Asigna un valor, configura un argumento o actualiza un dato del escenario.
        self._tiene_brazos = tiene_brazos
        # Explicacion linea 38: Asigna un valor, configura un argumento o actualiza un dato del escenario.
        self._es_modular = es_modular
        # Explicacion linea 39: Asigna un valor, configura un argumento o actualiza un dato del escenario.
        self._incluye_cojines = incluye_cojines

    # Explicacion linea 41: Aplica un decorador a la funcion que aparece a continuacion.
    @property
    # Explicacion linea 42: Declara la funcion y sus parametros de entrada.
    def tiene_brazos(self) -> bool:
        # Explicacion linea 43: Documenta el objetivo y el uso de este bloque.
        """Getter para brazos."""
        # Explicacion linea 44: Devuelve al llamador el resultado construido por este metodo.
        return self._tiene_brazos

    # Explicacion linea 46: Aplica un decorador a la funcion que aparece a continuacion.
    @property
    # Explicacion linea 47: Declara la funcion y sus parametros de entrada.
    def es_modular(self) -> bool:
        # Explicacion linea 48: Documenta el objetivo y el uso de este bloque.
        """Getter para modular."""
        # Explicacion linea 49: Devuelve al llamador el resultado construido por este metodo.
        return self._es_modular

    # Explicacion linea 51: Aplica un decorador a la funcion que aparece a continuacion.
    @property
    # Explicacion linea 52: Declara la funcion y sus parametros de entrada.
    def incluye_cojines(self) -> bool:
        # Explicacion linea 53: Documenta el objetivo y el uso de este bloque.
        """Getter para cojines."""
        # Explicacion linea 54: Devuelve al llamador el resultado construido por este metodo.
        return self._incluye_cojines

    # Explicacion linea 56: Declara la funcion y sus parametros de entrada.
    def calcular_precio(self) -> float:
        # Explicacion linea 57: Documenta el objetivo y el uso de este bloque.
        """Calcula el precio final del sofá."""
        # Explicacion linea 58: Asigna un valor, configura un argumento o actualiza un dato del escenario.
        precio = self.precio_base

        # Aplicar factor de comodidad base
        # Explicacion linea 61: Asigna un valor, configura un argumento o actualiza un dato del escenario.
        factor_comodidad = self.calcular_factor_comodidad()
        # Explicacion linea 62: Asigna un valor, configura un argumento o actualiza un dato del escenario.
        precio *= factor_comodidad

        # Características específicas del sofá
        # Explicacion linea 65: Evalua una condicion para elegir el camino de ejecucion.
        if self.tiene_brazos:
            # Explicacion linea 66: Asigna un valor, configura un argumento o actualiza un dato del escenario.
            precio += 150
        # Explicacion linea 67: Evalua una condicion para elegir el camino de ejecucion.
        if self.es_modular:
            # Explicacion linea 68: Asigna un valor, configura un argumento o actualiza un dato del escenario.
            precio += 200
        # Explicacion linea 69: Evalua una condicion para elegir el camino de ejecucion.
        if self.incluye_cojines:
            # Explicacion linea 70: Asigna un valor, configura un argumento o actualiza un dato del escenario.
            precio += 50

        # Explicacion linea 72: Devuelve al llamador el resultado construido por este metodo.
        return round(precio, 2)

    # Explicacion linea 74: Declara la funcion y sus parametros de entrada.
    def obtener_descripcion(self) -> str:
        # Explicacion linea 75: Documenta el objetivo y el uso de este bloque.
        """
        Retorna una descripción detallada del sofá.
        """
        # Explicacion linea 78: Asigna un valor, configura un argumento o actualiza un dato del escenario.
        desc = f"Sofá: {self.nombre}\n"
        # Explicacion linea 79: Asigna un valor, configura un argumento o actualiza un dato del escenario.
        desc += f"  Material: {self.material}\n"
        # Explicacion linea 80: Asigna un valor, configura un argumento o actualiza un dato del escenario.
        desc += f"  Color: {self.color}\n"
        # Explicacion linea 81: Asigna un valor, configura un argumento o actualiza un dato del escenario.
        desc += f"  {self.obtener_info_asiento()}\n"
        # Explicacion linea 82: Asigna un valor, configura un argumento o actualiza un dato del escenario.
        desc += f"  Brazos: {'Sí' if self.tiene_brazos else 'No'}\n"
        # Explicacion linea 83: Asigna un valor, configura un argumento o actualiza un dato del escenario.
        desc += f"  Modular: {'Sí' if self.es_modular else 'No'}\n"
        # Explicacion linea 84: Asigna un valor, configura un argumento o actualiza un dato del escenario.
        desc += f"  Incluye cojines: {'Sí' if self.incluye_cojines else 'No'}\n"
        # Explicacion linea 85: Asigna un valor, configura un argumento o actualiza un dato del escenario.
        desc += f"  Precio final: ${self.calcular_precio()}"
        # Explicacion linea 86: Devuelve al llamador el resultado construido por este metodo.
        return desc
