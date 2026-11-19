# Explicacion linea 1: Documenta el objetivo y el uso de este bloque.
"""
Clase concreta Cajonera.
Representa una cajonera genérica.
"""

# from ..mueble import Mueble


# Explicacion linea 9: Declara una clase que organiza atributos y operaciones del dominio.
class Cajonera:
    # Explicacion linea 10: Documenta el objetivo y el uso de este bloque.
    """
    Clase concreta que representa una cajonera.
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
        num_cajones: int = 3,
        # Explicacion linea 21: Asigna un valor, configura un argumento o actualiza un dato del escenario.
        tiene_ruedas: bool = False,
    # Explicacion linea 22: Cierra la expresion o estructura iniciada anteriormente.
    ):
        # Explicacion linea 23: Asigna un valor, configura un argumento o actualiza un dato del escenario.
        self.nombre = nombre
        # Explicacion linea 24: Asigna un valor, configura un argumento o actualiza un dato del escenario.
        self.material = material
        # Explicacion linea 25: Asigna un valor, configura un argumento o actualiza un dato del escenario.
        self.color = color
        # Explicacion linea 26: Asigna un valor, configura un argumento o actualiza un dato del escenario.
        self.precio_base = int(precio_base) if precio_base is not None else 0
        # Explicacion linea 27: Asigna un valor, configura un argumento o actualiza un dato del escenario.
        self.num_cajones = num_cajones
        # Explicacion linea 28: Asigna un valor, configura un argumento o actualiza un dato del escenario.
        self.tiene_ruedas = tiene_ruedas

    # Explicacion linea 30: Declara la funcion y sus parametros de entrada.
    def calcular_precio(self) -> int:
        # Explicacion linea 31: Documenta el objetivo y el uso de este bloque.
        """Calcula el precio final de la cajonera."""
        # Explicacion linea 32: Asigna un valor, configura un argumento o actualiza un dato del escenario.
        precio = self.precio_base
        # Explicacion linea 33: Asigna un valor, configura un argumento o actualiza un dato del escenario.
        precio += self.num_cajones * 20
        # Explicacion linea 34: Evalua una condicion para elegir el camino de ejecucion.
        if self.tiene_ruedas:
            # Explicacion linea 35: Asigna un valor, configura un argumento o actualiza un dato del escenario.
            precio += 30
        # Explicacion linea 36: Devuelve al llamador el resultado construido por este metodo.
        return int(round(precio))

    # Explicacion linea 38: Declara la funcion y sus parametros de entrada.
    def obtener_descripcion(self) -> str:
        # Explicacion linea 39: Documenta el objetivo y el uso de este bloque.
        """
        Retorna una descripción detallada de la cajonera.
        """
        # Explicacion linea 42: Devuelve al llamador el resultado construido por este metodo.
        return (
            # Explicacion linea 43: Asigna un valor, configura un argumento o actualiza un dato del escenario.
            f"Cajonera '{self.nombre}': Material={self.material}, Color={self.color}, "
            # Explicacion linea 44: Asigna un valor, configura un argumento o actualiza un dato del escenario.
            f"Cajones={self.num_cajones}, Ruedas={'Sí' if self.tiene_ruedas else 'No'}, "
            # Explicacion linea 45: Asigna un valor, configura un argumento o actualiza un dato del escenario.
            f"Precio base=${self.precio_base}"
        # Explicacion linea 46: Cierra la expresion o estructura iniciada anteriormente.
        )
