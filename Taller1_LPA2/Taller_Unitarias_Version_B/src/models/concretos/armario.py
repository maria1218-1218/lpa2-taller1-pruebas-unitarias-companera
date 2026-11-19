# Explicacion linea 1: Documenta el objetivo y el uso de este bloque.
"""
Clase concreta Armario.
Representa un armario genérico.
"""

# from ..mueble import Mueble


# Explicacion linea 9: Declara una clase que organiza atributos y operaciones del dominio.
class Armario:
    # Explicacion linea 10: Documenta el objetivo y el uso de este bloque.
    """
    Clase concreta que representa un armario.
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
        precio_base: int,
        # Explicacion linea 20: Asigna un valor, configura un argumento o actualiza un dato del escenario.
        num_puertas: int = 2,
        # Explicacion linea 21: Asigna un valor, configura un argumento o actualiza un dato del escenario.
        num_cajones: int = 0,
        # Explicacion linea 22: Asigna un valor, configura un argumento o actualiza un dato del escenario.
        tiene_espejos: bool = False,
    # Explicacion linea 23: Cierra la expresion o estructura iniciada anteriormente.
    ):
        # Explicacion linea 24: Asigna un valor, configura un argumento o actualiza un dato del escenario.
        self.nombre = nombre
        # Explicacion linea 25: Asigna un valor, configura un argumento o actualiza un dato del escenario.
        self.material = material
        # Explicacion linea 26: Asigna un valor, configura un argumento o actualiza un dato del escenario.
        self.color = color
        # Explicacion linea 27: Asigna un valor, configura un argumento o actualiza un dato del escenario.
        self.precio_base = int(precio_base) if precio_base is not None else 0
        # Explicacion linea 28: Asigna un valor, configura un argumento o actualiza un dato del escenario.
        self.num_puertas = num_puertas
        # Explicacion linea 29: Asigna un valor, configura un argumento o actualiza un dato del escenario.
        self.num_cajones = num_cajones
        # Explicacion linea 30: Asigna un valor, configura un argumento o actualiza un dato del escenario.
        self.tiene_espejos = tiene_espejos

    # Explicacion linea 32: Declara la funcion y sus parametros de entrada.
    def calcular_precio(self) -> int:
        # Explicacion linea 33: Documenta el objetivo y el uso de este bloque.
        """Calcula el precio final del armario."""
        # Explicacion linea 34: Asigna un valor, configura un argumento o actualiza un dato del escenario.
        precio = self.precio_base
        # Explicacion linea 35: Asigna un valor, configura un argumento o actualiza un dato del escenario.
        precio += self.num_puertas * 50
        # Explicacion linea 36: Asigna un valor, configura un argumento o actualiza un dato del escenario.
        precio += self.num_cajones * 30
        # Explicacion linea 37: Evalua una condicion para elegir el camino de ejecucion.
        if self.tiene_espejos:
            # Explicacion linea 38: Asigna un valor, configura un argumento o actualiza un dato del escenario.
            precio += 100
        # Explicacion linea 39: Devuelve al llamador el resultado construido por este metodo.
        return int(round(precio))

    # Explicacion linea 41: Declara la funcion y sus parametros de entrada.
    def obtener_descripcion(self) -> str:
        # Explicacion linea 42: Documenta el objetivo y el uso de este bloque.
        """
        Retorna una descripción detallada del armario.
        """
        # Explicacion linea 45: Devuelve al llamador el resultado construido por este metodo.
        return (
            # Explicacion linea 46: Asigna un valor, configura un argumento o actualiza un dato del escenario.
            f"Armario '{self.nombre}': Material={self.material}, Color={self.color}, "
            # Explicacion linea 47: Asigna un valor, configura un argumento o actualiza un dato del escenario.
            f"Puertas={self.num_puertas}, Cajones={self.num_cajones}, Espejos={'Sí' if self.tiene_espejos else 'No'}, "
            # Explicacion linea 48: Asigna un valor, configura un argumento o actualiza un dato del escenario.
            f"Precio base=${self.precio_base}"
        # Explicacion linea 49: Cierra la expresion o estructura iniciada anteriormente.
        )
