# Explicacion linea 1: Documenta el objetivo y el uso de este bloque.
"""
Clase concreta Sillón.
Implementa un mueble de asiento para más de una persona, con brazos y respaldo.
"""

# from ..categorias.asientos import Asiento


# Explicacion linea 9: Declara una clase que organiza atributos y operaciones del dominio.
class Sillon:
    # Explicacion linea 10: Documenta el objetivo y el uso de este bloque.
    """
    Clase concreta que representa un sillón.
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
        precio_base: int,
        # Explicacion linea 21: Asigna un valor, configura un argumento o actualiza un dato del escenario.
        capacidad_personas: int = 2,
        # Explicacion linea 22: Asigna un valor, configura un argumento o actualiza un dato del escenario.
        tiene_respaldo: bool = True,
        # Explicacion linea 23: Asigna un valor, configura un argumento o actualiza un dato del escenario.
        material_tapizado: str = None,
        # Explicacion linea 24: Asigna un valor, configura un argumento o actualiza un dato del escenario.
        tiene_brazos: bool = True,
        # Explicacion linea 25: Asigna un valor, configura un argumento o actualiza un dato del escenario.
        es_reclinable: bool = False,
        # Explicacion linea 26: Asigna un valor, configura un argumento o actualiza un dato del escenario.
        tiene_reposapiés: bool = False,
    # Explicacion linea 27: Cierra la expresion o estructura iniciada anteriormente.
    ):
        # Explicacion linea 28: Asigna un valor, configura un argumento o actualiza un dato del escenario.
        self.nombre = nombre
        # Explicacion linea 29: Asigna un valor, configura un argumento o actualiza un dato del escenario.
        self.material = material
        # Explicacion linea 30: Asigna un valor, configura un argumento o actualiza un dato del escenario.
        self.color = color
        # Explicacion linea 31: Asigna un valor, configura un argumento o actualiza un dato del escenario.
        self.precio_base = int(precio_base) if precio_base is not None else 0
        # Explicacion linea 32: Asigna un valor, configura un argumento o actualiza un dato del escenario.
        self.capacidad_personas = capacidad_personas
        # Explicacion linea 33: Asigna un valor, configura un argumento o actualiza un dato del escenario.
        self.tiene_respaldo = tiene_respaldo
        # Explicacion linea 34: Asigna un valor, configura un argumento o actualiza un dato del escenario.
        self.material_tapizado = material_tapizado
        # Explicacion linea 35: Asigna un valor, configura un argumento o actualiza un dato del escenario.
        self.tiene_brazos = tiene_brazos
        # Explicacion linea 36: Asigna un valor, configura un argumento o actualiza un dato del escenario.
        self.es_reclinable = es_reclinable
        # Explicacion linea 37: Asigna un valor, configura un argumento o actualiza un dato del escenario.
        self.tiene_reposapiés = tiene_reposapiés

    # Explicacion linea 39: Declara la funcion y sus parametros de entrada.
    def calcular_precio(self) -> int:
        # Explicacion linea 40: Documenta el objetivo y el uso de este bloque.
        """Calcula el precio final del sillón."""
        # Explicacion linea 41: Asigna un valor, configura un argumento o actualiza un dato del escenario.
        precio = self.precio_base
        # Explicacion linea 42: Evalua una condicion para elegir el camino de ejecucion.
        if self.material_tapizado:
            # Explicacion linea 43: Asigna un valor, configura un argumento o actualiza un dato del escenario.
            precio += 200
        # Explicacion linea 44: Evalua una condicion para elegir el camino de ejecucion.
        if self.tiene_brazos:
            # Explicacion linea 45: Asigna un valor, configura un argumento o actualiza un dato del escenario.
            precio += 100
        # Explicacion linea 46: Evalua una condicion para elegir el camino de ejecucion.
        if self.es_reclinable:
            # Explicacion linea 47: Asigna un valor, configura un argumento o actualiza un dato del escenario.
            precio += 250
        # Explicacion linea 48: Evalua una condicion para elegir el camino de ejecucion.
        if self.tiene_reposapiés:
            # Explicacion linea 49: Asigna un valor, configura un argumento o actualiza un dato del escenario.
            precio += 80
        # Explicacion linea 50: Devuelve al llamador el resultado construido por este metodo.
        return int(round(precio))

    # Explicacion linea 52: Declara la funcion y sus parametros de entrada.
    def obtener_descripcion(self) -> str:
        # Explicacion linea 53: Documenta el objetivo y el uso de este bloque.
        """
        Retorna una descripción detallada del sillón.
        """
        # Explicacion linea 56: Devuelve al llamador el resultado construido por este metodo.
        return (
            # Explicacion linea 57: Asigna un valor, configura un argumento o actualiza un dato del escenario.
            f"Sillón '{self.nombre}': Material={self.material}, Color={self.color}, "
            # Explicacion linea 58: Asigna un valor, configura un argumento o actualiza un dato del escenario.
            f"Capacidad={self.capacidad_personas} personas, Tapizado={self.material_tapizado or 'N/A'}, "
            # Explicacion linea 59: Asigna un valor, configura un argumento o actualiza un dato del escenario.
            f"Brazos={'Sí' if self.tiene_brazos else 'No'}, Reclinable={'Sí' if self.es_reclinable else 'No'}, "
            # Explicacion linea 60: Asigna un valor, configura un argumento o actualiza un dato del escenario.
            f"Reposapiés={'Sí' if self.tiene_reposapiés else 'No'}, Precio base=${self.precio_base}"
        # Explicacion linea 61: Cierra la expresion o estructura iniciada anteriormente.
        )
