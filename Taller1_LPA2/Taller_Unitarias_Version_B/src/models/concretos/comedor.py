# Explicacion linea 1: Importa las herramientas o clases usadas en este modulo.
from typing import List
# Explicacion linea 2: Importa las herramientas o clases usadas en este modulo.
from ..concretos.mesa import Mesa
# Explicacion linea 3: Importa las herramientas o clases usadas en este modulo.
from ..concretos.silla import Silla


# Explicacion linea 6: Declara una clase que organiza atributos y operaciones del dominio.
class Comedor:
    # Explicacion linea 7: Declara la funcion y sus parametros de entrada.
    def calcular_precio_total(self) -> float:
        # Explicacion linea 8: Asigna un valor, configura un argumento o actualiza un dato del escenario.
        total = self.mesa.calcular_precio()
        # Explicacion linea 9: Asigna un valor, configura un argumento o actualiza un dato del escenario.
        total += sum(silla.calcular_precio() for silla in self.sillas)
        # Explicacion linea 10: Devuelve al llamador el resultado construido por este metodo.
        return total

    # Explicacion linea 12: Documenta el objetivo y el uso de este bloque.
    """
	Clase que representa un conjunto de comedor compuesto por una mesa y varias sillas.
	"""

    # Explicacion linea 16: Declara la funcion y sus parametros de entrada.
    def __init__(self, mesa: Mesa, sillas: List[Silla] = None):
        # Explicacion linea 17: Asigna un valor, configura un argumento o actualiza un dato del escenario.
        self.mesa = mesa
        # Explicacion linea 18: Asigna un valor, configura un argumento o actualiza un dato del escenario.
        self.sillas = sillas if sillas is not None else []

    # Explicacion linea 20: Declara la funcion y sus parametros de entrada.
    def agregar_silla(self, silla: Silla):
        # Explicacion linea 21: Ejecuta una operacion del objeto dentro del flujo.
        self.sillas.append(silla)

    # Explicacion linea 23: Declara la funcion y sus parametros de entrada.
    def quitar_silla(self, silla: Silla):
        # Explicacion linea 24: Evalua una condicion para elegir el camino de ejecucion.
        if silla in self.sillas:
            # Explicacion linea 25: Ejecuta una operacion del objeto dentro del flujo.
            self.sillas.remove(silla)

    # Explicacion linea 27: Declara la funcion y sus parametros de entrada.
    def cantidad_sillas(self) -> int:
        # Explicacion linea 28: Devuelve al llamador el resultado construido por este metodo.
        return len(self.sillas)

    # Explicacion linea 30: Declara la funcion y sus parametros de entrada.
    def descripcion(self) -> str:
        # Explicacion linea 31: Asigna un valor, configura un argumento o actualiza un dato del escenario.
        desc = f"Comedor con mesa: {self.mesa.obtener_descripcion()}\n"
        # Explicacion linea 32: Asigna un valor, configura un argumento o actualiza un dato del escenario.
        desc += f"y {len(self.sillas)} sillas:\n"
        # Explicacion linea 33: Recorre los elementos de una coleccion para procesarlos.
        for idx, silla in enumerate(self.sillas, 1):
            # Explicacion linea 34: Asigna un valor, configura un argumento o actualiza un dato del escenario.
            desc += f"  {idx}. {silla.obtener_descripcion()}\n"
        # Explicacion linea 35: Devuelve al llamador el resultado construido por este metodo.
        return desc
