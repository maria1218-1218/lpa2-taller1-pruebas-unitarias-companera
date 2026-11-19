# Explicacion linea 1: Documenta el objetivo y el uso de este bloque.
"""
Clase SofaCama que implementa herencia múltiple.
Esta clase hereda tanto de Sofa como de Cama.
"""

# Explicacion linea 6: Importa las herramientas o clases usadas en este modulo.
from .sofa import Sofa
# Explicacion linea 7: Importa las herramientas o clases usadas en este modulo.
from .cama import Cama


# Explicacion linea 10: Declara una clase que organiza atributos y operaciones del dominio.
class SofaCama(Sofa, Cama):
    # Explicacion linea 11: Documenta el objetivo y el uso de este bloque.
    """
    Clase que implementa herencia múltiple heredando de Sofa y Cama.

    Un sofá-cama es un mueble que funciona tanto como asiento durante el día
    como cama durante la noche.

    Conceptos OOP aplicados:
    - Herencia múltiple: Hereda de Sofa y Cama
    - Resolución MRO: Maneja el orden de resolución de métodos
    - Polimorfismo: Implementa comportamientos únicos combinando funcionalidades
    - Super(): Usa super() para resolver conflictos de herencia
    """

    # Explicacion linea 24: Declara la funcion y sus parametros de entrada.
    def __init__(
        # Explicacion linea 25: Continua la expresion del bloque anterior o ejecuta esta instruccion.
        self,
        # Explicacion linea 26: Continua la expresion del bloque anterior o ejecuta esta instruccion.
        nombre: str,
        # Explicacion linea 27: Continua la expresion del bloque anterior o ejecuta esta instruccion.
        material: str,
        # Explicacion linea 28: Continua la expresion del bloque anterior o ejecuta esta instruccion.
        color: str,
        # Explicacion linea 29: Continua la expresion del bloque anterior o ejecuta esta instruccion.
        precio_base: int,
        # Explicacion linea 30: Asigna un valor, configura un argumento o actualiza un dato del escenario.
        capacidad_personas: int = 3,
        # Explicacion linea 31: Asigna un valor, configura un argumento o actualiza un dato del escenario.
        material_tapizado: str = "tela",
        # Explicacion linea 32: Asigna un valor, configura un argumento o actualiza un dato del escenario.
        tamaño_cama: str = "matrimonial",
        # Explicacion linea 33: Asigna un valor, configura un argumento o actualiza un dato del escenario.
        incluye_colchon: bool = True,
        # Explicacion linea 34: Asigna un valor, configura un argumento o actualiza un dato del escenario.
        mecanismo_conversion: str = "plegable",
    # Explicacion linea 35: Cierra la expresion o estructura iniciada anteriormente.
    ):
        # Explicacion linea 36: Documenta el objetivo y el uso de este bloque.
        """
        Constructor del sofá-cama.

        Args:
            mecanismo_conversion: Tipo de mecanismo de conversión (plegable, extensible, etc.)
            Otros argumentos se pasan a las clases padre
        """
        # Usar super() para llamar al constructor de Sofa (primer padre en MRO)
        # Explicacion linea 44: Continua la expresion del bloque anterior o ejecuta esta instruccion.
        Sofa.__init__(
            # Explicacion linea 45: Continua la expresion del bloque anterior o ejecuta esta instruccion.
            self,
            # Explicacion linea 46: Continua la expresion del bloque anterior o ejecuta esta instruccion.
            nombre,
            # Explicacion linea 47: Continua la expresion del bloque anterior o ejecuta esta instruccion.
            material,
            # Explicacion linea 48: Continua la expresion del bloque anterior o ejecuta esta instruccion.
            color,
            # Explicacion linea 49: Continua la expresion del bloque anterior o ejecuta esta instruccion.
            precio_base,
            # Explicacion linea 50: Continua la expresion del bloque anterior o ejecuta esta instruccion.
            capacidad_personas,
            # Explicacion linea 51: Continua la expresion del bloque anterior o ejecuta esta instruccion.
            True,
            # Explicacion linea 52: Continua la expresion del bloque anterior o ejecuta esta instruccion.
            material_tapizado,
        # Explicacion linea 53: Cierra la expresion o estructura iniciada anteriormente.
        )
        # Inicializar atributos específicos de cama
        # Explicacion linea 55: Asigna un valor, configura un argumento o actualiza un dato del escenario.
        self._tamaño = tamaño_cama
        # Explicacion linea 56: Asigna un valor, configura un argumento o actualiza un dato del escenario.
        self._incluye_colchon = incluye_colchon
        # Atributos específicos del sofá-cama
        # Explicacion linea 58: Asigna un valor, configura un argumento o actualiza un dato del escenario.
        self._mecanismo_conversion = mecanismo_conversion
        # Explicacion linea 59: Asigna un valor, configura un argumento o actualiza un dato del escenario.
        self._modo_actual = "sofa"

    # Explicacion linea 61: Declara la funcion y sus parametros de entrada.
    def calcular_precio(self) -> float:
        # Explicacion linea 62: Documenta el objetivo y el uso de este bloque.
        """
        Calcula el precio final del sofá cama.
        Combina características de ambas clases padre.
        """
        # Precio base del sofá usando super() para resolución MRO
        # Explicacion linea 67: Asigna un valor, configura un argumento o actualiza un dato del escenario.
        precio_sofa = super().calcular_precio()

        # Agregar costos específicos de cama
        # Explicacion linea 70: Evalua una condicion para elegir el camino de ejecucion.
        if self._tamaño == "matrimonial":
            # Explicacion linea 71: Asigna un valor, configura un argumento o actualiza un dato del escenario.
            precio_sofa += 300
        # Explicacion linea 72: Evalua una condicion para elegir el camino de ejecucion.
        elif self._tamaño == "queen":
            # Explicacion linea 73: Asigna un valor, configura un argumento o actualiza un dato del escenario.
            precio_sofa += 500
        # Explicacion linea 74: Evalua una condicion para elegir el camino de ejecucion.
        elif self._tamaño == "king":
            # Explicacion linea 75: Asigna un valor, configura un argumento o actualiza un dato del escenario.
            precio_sofa += 700

        # Explicacion linea 77: Evalua una condicion para elegir el camino de ejecucion.
        if self.incluye_colchon:
            # Explicacion linea 78: Asigna un valor, configura un argumento o actualiza un dato del escenario.
            precio_sofa += 250

        # Costo del mecanismo de conversión
        # Explicacion linea 81: Evalua una condicion para elegir el camino de ejecucion.
        if self._mecanismo_conversion == "hidraulico":
            # Explicacion linea 82: Asigna un valor, configura un argumento o actualiza un dato del escenario.
            precio_sofa += 150
        # Explicacion linea 83: Evalua una condicion para elegir el camino de ejecucion.
        elif self._mecanismo_conversion == "electrico":
            # Explicacion linea 84: Asigna un valor, configura un argumento o actualiza un dato del escenario.
            precio_sofa += 300

        # Explicacion linea 86: Devuelve al llamador el resultado construido por este metodo.
        return round(precio_sofa, 2)

    # Explicacion linea 88: Aplica un decorador a la funcion que aparece a continuacion.
    @property
    # Explicacion linea 89: Declara la funcion y sus parametros de entrada.
    def mecanismo_conversion(self) -> str:
        # Explicacion linea 90: Documenta el objetivo y el uso de este bloque.
        """Getter para el mecanismo de conversión."""
        # Explicacion linea 91: Devuelve al llamador el resultado construido por este metodo.
        return self._mecanismo_conversion

    # Explicacion linea 93: Aplica un decorador a la funcion que aparece a continuacion.
    @property
    # Explicacion linea 94: Declara la funcion y sus parametros de entrada.
    def modo_actual(self) -> str:
        # Explicacion linea 95: Documenta el objetivo y el uso de este bloque.
        """Getter para el modo actual (sofa o cama)."""
        # Explicacion linea 96: Devuelve al llamador el resultado construido por este metodo.
        return self._modo_actual

    # Redefinir tamaño para compatibilidad con ambas clases
    # Explicacion linea 99: Aplica un decorador a la funcion que aparece a continuacion.
    @property
    # Explicacion linea 100: Declara la funcion y sus parametros de entrada.
    def tamaño(self) -> str:
        # Explicacion linea 101: Documenta el objetivo y el uso de este bloque.
        """Getter para tamaño (compatible con clase Cama)."""
        # Explicacion linea 102: Devuelve al llamador el resultado construido por este metodo.
        return self._tamaño

    # Explicacion linea 104: Aplica un decorador a la funcion que aparece a continuacion.
    @property
    # Explicacion linea 105: Declara la funcion y sus parametros de entrada.
    def tamaño_cama(self) -> str:
        # Explicacion linea 106: Documenta el objetivo y el uso de este bloque.
        """Alias para tamaño específico de cama."""
        # Explicacion linea 107: Devuelve al llamador el resultado construido por este metodo.
        return self._tamaño

    # Explicacion linea 109: Declara la funcion y sus parametros de entrada.
    def convertir_a_cama(self) -> str:
        # Explicacion linea 110: Documenta el objetivo y el uso de este bloque.
        """
        Convierte el sofá en cama.
        Método específico del sofá-cama.

        Returns:
            str: Mensaje del resultado de la conversión
        """
        # Explicacion linea 117: Evalua una condicion para elegir el camino de ejecucion.
        if self._modo_actual == "cama":
            # Explicacion linea 118: Devuelve al llamador el resultado construido por este metodo.
            return "El sofá-cama ya está en modo cama"

        # Explicacion linea 120: Asigna un valor, configura un argumento o actualiza un dato del escenario.
        self._modo_actual = "cama"
        # Explicacion linea 121: Devuelve al llamador el resultado construido por este metodo.
        return f"Sofá convertido a cama usando mecanismo {self.mecanismo_conversion}"

    # Explicacion linea 123: Declara la funcion y sus parametros de entrada.
    def convertir_a_sofa(self) -> str:
        # Explicacion linea 124: Documenta el objetivo y el uso de este bloque.
        """
        Convierte la cama en sofá.
        Método específico del sofá-cama.

        Returns:
            str: Mensaje del resultado de la conversión
        """
        # Explicacion linea 131: Evalua una condicion para elegir el camino de ejecucion.
        if self._modo_actual == "sofa":
            # Explicacion linea 132: Devuelve al llamador el resultado construido por este metodo.
            return "El sofá-cama ya está en modo sofá"

        # Explicacion linea 134: Asigna un valor, configura un argumento o actualiza un dato del escenario.
        self._modo_actual = "sofa"
        # Explicacion linea 135: Devuelve al llamador el resultado construido por este metodo.
        return f"Cama convertida a sofá usando mecanismo {self.mecanismo_conversion}"
        # Explicacion linea 136: No realiza ninguna accion en este bloque.
        pass

    # Explicacion linea 138: Declara la funcion y sus parametros de entrada.
    def obtener_descripcion(self) -> str:
        # Explicacion linea 139: Documenta el objetivo y el uso de este bloque.
        """
        Retorna una descripción detallada del sofá cama.
        Combina información de ambas funcionalidades.
        """
        # Explicacion linea 143: Asigna un valor, configura un argumento o actualiza un dato del escenario.
        desc = f"Sofá-Cama: {self.nombre}\n"
        # Explicacion linea 144: Asigna un valor, configura un argumento o actualiza un dato del escenario.
        desc += f"  Material: {self.material}\n"
        # Explicacion linea 145: Asigna un valor, configura un argumento o actualiza un dato del escenario.
        desc += f"  Color: {self.color}\n"
        # Explicacion linea 146: Asigna un valor, configura un argumento o actualiza un dato del escenario.
        desc += f"  {self.obtener_info_asiento()}\n"
        # Explicacion linea 147: Asigna un valor, configura un argumento o actualiza un dato del escenario.
        desc += f"  Tamaño como cama: {self.tamaño_cama}\n"
        # Explicacion linea 148: Asigna un valor, configura un argumento o actualiza un dato del escenario.
        desc += f"  Incluye colchón: {'Sí' if self.incluye_colchon else 'No'}\n"
        # Explicacion linea 149: Asigna un valor, configura un argumento o actualiza un dato del escenario.
        desc += f"  Mecanismo: {self.mecanismo_conversion}\n"
        # Explicacion linea 150: Asigna un valor, configura un argumento o actualiza un dato del escenario.
        desc += f"  Modo actual: {self.modo_actual}\n"
        # Explicacion linea 151: Asigna un valor, configura un argumento o actualiza un dato del escenario.
        desc += f"  Precio final: ${self.calcular_precio()}"
        # Explicacion linea 152: Devuelve al llamador el resultado construido por este metodo.
        return desc

    # Explicacion linea 154: Declara la funcion y sus parametros de entrada.
    def obtener_capacidad_total(self) -> dict:
        # Explicacion linea 155: Documenta el objetivo y el uso de este bloque.
        """
        Obtiene la capacidad tanto como sofá como cama.
        Método único del sofá-cama.

        Returns:
            dict: Capacidades en ambos modos
        """
        # Explicacion linea 162: Asigna un valor, configura un argumento o actualiza un dato del escenario.
        capacidades = {
            # Explicacion linea 163: Continua la expresion del bloque anterior o ejecuta esta instruccion.
            "como_sofa": self.capacidad_personas,
            # Explicacion linea 164: Continua la expresion del bloque anterior o ejecuta esta instruccion.
            "como_cama": 2
            # Explicacion linea 165: Evalua una condicion para elegir el camino de ejecucion.
            if self.tamaño_cama in ["matrimonial", "queen", "king"]
            # Explicacion linea 166: Continua la expresion del bloque anterior o ejecuta esta instruccion.
            else 1,
        # Explicacion linea 167: Cierra la expresion o estructura iniciada anteriormente.
        }
        # Explicacion linea 168: Devuelve al llamador el resultado construido por este metodo.
        return capacidades

    # TODO: Implementar método para verificar compatibilidad de modo
    # def puede_usar_como_cama(self) -> bool:
    #     """Verifica si actualmente puede usarse como cama."""
    #     return self._modo_actual == "cama"

    # def puede_usar_como_sofa(self) -> bool:
    #     """Verifica si actualmente puede usarse como sofá."""
    #     return self._modo_actual == "sofa"

    # Explicacion linea 179: Declara la funcion y sus parametros de entrada.
    def __str__(self) -> str:
        # Explicacion linea 180: Documenta el objetivo y el uso de este bloque.
        """
        Representación en cadena del sofá-cama.
        Sobrescribe el método heredado para mostrar información específica.
        """
        # Explicacion linea 184: Devuelve al llamador el resultado construido por este metodo.
        return f"Sofá-cama {self.nombre} (modo: {self.modo_actual})"
