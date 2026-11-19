#!/usr/bin/env python3
# Explicacion linea 2: Documenta el objetivo y el uso de este bloque.
"""
Punto de entrada principal para la aplicación Tienda de Muebles.
Este archivo inicializa la aplicación y proporciona datos de ejemplo.
"""

# Explicacion linea 7: Importa las herramientas o clases usadas en este modulo.
from services.tienda import TiendaMuebles
# Explicacion linea 8: Importa las herramientas o clases usadas en este modulo.
from ui.menu import MenuTienda

# Explicacion linea 10: Importa las herramientas o clases usadas en este modulo.
from models.concretos.silla import Silla
# Explicacion linea 11: Importa las herramientas o clases usadas en este modulo.
from models.concretos.sillon import Sillon
# Explicacion linea 12: Importa las herramientas o clases usadas en este modulo.
from models.concretos.sofa import Sofa
# Explicacion linea 13: Importa las herramientas o clases usadas en este modulo.
from models.concretos.mesa import Mesa
# Explicacion linea 14: Importa las herramientas o clases usadas en este modulo.
from models.concretos.armario import Armario
# Explicacion linea 15: Importa las herramientas o clases usadas en este modulo.
from models.concretos.cama import Cama
# Explicacion linea 16: Importa las herramientas o clases usadas en este modulo.
from models.concretos.escritorio import Escritorio
# Explicacion linea 17: Importa las herramientas o clases usadas en este modulo.
from models.concretos.cajonera import Cajonera
# Explicacion linea 18: Importa las herramientas o clases usadas en este modulo.
from models.concretos.sofacama import SofaCama
# Explicacion linea 19: Importa las herramientas o clases usadas en este modulo.
from models.composicion.comedor import Comedor


# Explicacion linea 22: Declara la funcion y sus parametros de entrada.
def crear_catalogo_inicial(tienda: "TiendaMuebles") -> None:
    # Explicacion linea 23: Documenta el objetivo y el uso de este bloque.
    """
    Crea un catálogo inicial de muebles para demostrar el funcionamiento del sistema.
    Esta función muestra cómo instanciar diferentes tipos de muebles y agregarlos a la tienda.

    Args:
        tienda: Instancia de TiendaMuebles donde agregar los muebles
    """
    # Explicacion linea 30: Muestra informacion al usuario en la consola.
    print("🔨 Creando catálogo inicial de muebles...")

    # Explicacion linea 32: Asigna un valor, configura un argumento o actualiza un dato del escenario.
    sillas = [
        # Explicacion linea 33: Continua la expresion del bloque anterior o ejecuta esta instruccion.
        Silla(
            # Explicacion linea 34: Asigna un valor, configura un argumento o actualiza un dato del escenario.
            nombre="Silla Clásica",
            # Explicacion linea 35: Asigna un valor, configura un argumento o actualiza un dato del escenario.
            material="Madera",
            # Explicacion linea 36: Asigna un valor, configura un argumento o actualiza un dato del escenario.
            color="Café",
            # Explicacion linea 37: Asigna un valor, configura un argumento o actualiza un dato del escenario.
            precio_base=150.0,
            # Explicacion linea 38: Asigna un valor, configura un argumento o actualiza un dato del escenario.
            tiene_respaldo=True,
            # Explicacion linea 39: Asigna un valor, configura un argumento o actualiza un dato del escenario.
            material_tapizado="tela",
        # Explicacion linea 40: Cierra la expresion o estructura iniciada anteriormente.
        ),
        # Explicacion linea 41: Continua la expresion del bloque anterior o ejecuta esta instruccion.
        Silla(
            # Explicacion linea 42: Asigna un valor, configura un argumento o actualiza un dato del escenario.
            nombre="Silla de Oficina Ejecutiva",
            # Explicacion linea 43: Asigna un valor, configura un argumento o actualiza un dato del escenario.
            material="Metal",
            # Explicacion linea 44: Asigna un valor, configura un argumento o actualiza un dato del escenario.
            color="Negro",
            # Explicacion linea 45: Asigna un valor, configura un argumento o actualiza un dato del escenario.
            precio_base=350.0,
            # Explicacion linea 46: Asigna un valor, configura un argumento o actualiza un dato del escenario.
            tiene_respaldo=True,
            # Explicacion linea 47: Asigna un valor, configura un argumento o actualiza un dato del escenario.
            material_tapizado="cuero",
            # Explicacion linea 48: Asigna un valor, configura un argumento o actualiza un dato del escenario.
            altura_regulable=True,
            # Explicacion linea 49: Asigna un valor, configura un argumento o actualiza un dato del escenario.
            tiene_ruedas=True,
        # Explicacion linea 50: Cierra la expresion o estructura iniciada anteriormente.
        ),
        # Explicacion linea 51: Continua la expresion del bloque anterior o ejecuta esta instruccion.
        Silla(
            # Explicacion linea 52: Asigna un valor, configura un argumento o actualiza un dato del escenario.
            nombre="Silla Moderna Minimalista",
            # Explicacion linea 53: Asigna un valor, configura un argumento o actualiza un dato del escenario.
            material="Plástico",
            # Explicacion linea 54: Asigna un valor, configura un argumento o actualiza un dato del escenario.
            color="Blanco",
            # Explicacion linea 55: Asigna un valor, configura un argumento o actualiza un dato del escenario.
            precio_base=80.0,
            # Explicacion linea 56: Asigna un valor, configura un argumento o actualiza un dato del escenario.
            tiene_respaldo=True,
        # Explicacion linea 57: Cierra la expresion o estructura iniciada anteriormente.
        ),
    # Explicacion linea 58: Cierra la expresion o estructura iniciada anteriormente.
    ]

    # Explicacion linea 60: Asigna un valor, configura un argumento o actualiza un dato del escenario.
    mesas = [
        # Explicacion linea 61: Continua la expresion del bloque anterior o ejecuta esta instruccion.
        Mesa(
            # Explicacion linea 62: Asigna un valor, configura un argumento o actualiza un dato del escenario.
            nombre="Mesa de Comedor Familiar",
            # Explicacion linea 63: Asigna un valor, configura un argumento o actualiza un dato del escenario.
            material="Madera",
            # Explicacion linea 64: Asigna un valor, configura un argumento o actualiza un dato del escenario.
            color="Roble",
            # Explicacion linea 65: Asigna un valor, configura un argumento o actualiza un dato del escenario.
            precio_base=500.0,
            # Explicacion linea 66: Asigna un valor, configura un argumento o actualiza un dato del escenario.
            forma="rectangular",
            # Explicacion linea 67: Asigna un valor, configura un argumento o actualiza un dato del escenario.
            capacidad_personas=6,
        # Explicacion linea 68: Cierra la expresion o estructura iniciada anteriormente.
        ),
        # Explicacion linea 69: Continua la expresion del bloque anterior o ejecuta esta instruccion.
        Mesa(
            # Explicacion linea 70: Asigna un valor, configura un argumento o actualiza un dato del escenario.
            nombre="Mesa de Centro Redonda",
            # Explicacion linea 71: Asigna un valor, configura un argumento o actualiza un dato del escenario.
            material="Vidrio",
            # Explicacion linea 72: Asigna un valor, configura un argumento o actualiza un dato del escenario.
            color="Transparente",
            # Explicacion linea 73: Asigna un valor, configura un argumento o actualiza un dato del escenario.
            precio_base=300.0,
            # Explicacion linea 74: Asigna un valor, configura un argumento o actualiza un dato del escenario.
            forma="redonda",
            # Explicacion linea 75: Asigna un valor, configura un argumento o actualiza un dato del escenario.
            capacidad_personas=4,
        # Explicacion linea 76: Cierra la expresion o estructura iniciada anteriormente.
        ),
        # Explicacion linea 77: Continua la expresion del bloque anterior o ejecuta esta instruccion.
        Mesa(
            # Explicacion linea 78: Asigna un valor, configura un argumento o actualiza un dato del escenario.
            nombre="Mesa de Trabajo Industrial",
            # Explicacion linea 79: Asigna un valor, configura un argumento o actualiza un dato del escenario.
            material="Metal",
            # Explicacion linea 80: Asigna un valor, configura un argumento o actualiza un dato del escenario.
            color="Gris",
            # Explicacion linea 81: Asigna un valor, configura un argumento o actualiza un dato del escenario.
            precio_base=450.0,
            # Explicacion linea 82: Asigna un valor, configura un argumento o actualiza un dato del escenario.
            forma="rectangular",
            # Explicacion linea 83: Asigna un valor, configura un argumento o actualiza un dato del escenario.
            capacidad_personas=4,
        # Explicacion linea 84: Cierra la expresion o estructura iniciada anteriormente.
        ),
    # Explicacion linea 85: Cierra la expresion o estructura iniciada anteriormente.
    ]

    # Explicacion linea 87: Asigna un valor, configura un argumento o actualiza un dato del escenario.
    asientos_grandes = [
        # Explicacion linea 88: Continua la expresion del bloque anterior o ejecuta esta instruccion.
        Sillon(
            # Explicacion linea 89: Asigna un valor, configura un argumento o actualiza un dato del escenario.
            nombre="Sillón Reclinable de Lujo",
            # Explicacion linea 90: Asigna un valor, configura un argumento o actualiza un dato del escenario.
            material="Cuero",
            # Explicacion linea 91: Asigna un valor, configura un argumento o actualiza un dato del escenario.
            color="Marrón",
            # Explicacion linea 92: Asigna un valor, configura un argumento o actualiza un dato del escenario.
            precio_base=800.0,
            # Explicacion linea 93: Asigna un valor, configura un argumento o actualiza un dato del escenario.
            tiene_respaldo=True,
            # Explicacion linea 94: Asigna un valor, configura un argumento o actualiza un dato del escenario.
            material_tapizado="cuero",
            # Explicacion linea 95: Asigna un valor, configura un argumento o actualiza un dato del escenario.
            es_reclinable=True,
            # Explicacion linea 96: Asigna un valor, configura un argumento o actualiza un dato del escenario.
            tiene_reposapiés=True,
        # Explicacion linea 97: Cierra la expresion o estructura iniciada anteriormente.
        ),
        # Explicacion linea 98: Continua la expresion del bloque anterior o ejecuta esta instruccion.
        Sofa(
            # Explicacion linea 99: Asigna un valor, configura un argumento o actualiza un dato del escenario.
            nombre="Sofá Modular de 3 Plazas",
            # Explicacion linea 100: Asigna un valor, configura un argumento o actualiza un dato del escenario.
            material="Tela",
            # Explicacion linea 101: Asigna un valor, configura un argumento o actualiza un dato del escenario.
            color="Gris",
            # Explicacion linea 102: Asigna un valor, configura un argumento o actualiza un dato del escenario.
            precio_base=1200.0,
            # Explicacion linea 103: Asigna un valor, configura un argumento o actualiza un dato del escenario.
            capacidad_personas=3,
            # Explicacion linea 104: Asigna un valor, configura un argumento o actualiza un dato del escenario.
            tiene_respaldo=True,
            # Explicacion linea 105: Asigna un valor, configura un argumento o actualiza un dato del escenario.
            material_tapizado="tela",
            # Explicacion linea 106: Asigna un valor, configura un argumento o actualiza un dato del escenario.
            es_modular=True,
            # Explicacion linea 107: Asigna un valor, configura un argumento o actualiza un dato del escenario.
            incluye_cojines=True,
        # Explicacion linea 108: Cierra la expresion o estructura iniciada anteriormente.
        ),
        # Explicacion linea 109: Continua la expresion del bloque anterior o ejecuta esta instruccion.
        Sofa(
            # Explicacion linea 110: Asigna un valor, configura un argumento o actualiza un dato del escenario.
            nombre="Sofá Chesterfield Clásico",
            # Explicacion linea 111: Asigna un valor, configura un argumento o actualiza un dato del escenario.
            material="Cuero",
            # Explicacion linea 112: Asigna un valor, configura un argumento o actualiza un dato del escenario.
            color="Verde",
            # Explicacion linea 113: Asigna un valor, configura un argumento o actualiza un dato del escenario.
            precio_base=2000.0,
            # Explicacion linea 114: Asigna un valor, configura un argumento o actualiza un dato del escenario.
            capacidad_personas=2,
            # Explicacion linea 115: Asigna un valor, configura un argumento o actualiza un dato del escenario.
            tiene_respaldo=True,
            # Explicacion linea 116: Asigna un valor, configura un argumento o actualiza un dato del escenario.
            material_tapizado="cuero",
            # Explicacion linea 117: Asigna un valor, configura un argumento o actualiza un dato del escenario.
            es_modular=False,
            # Explicacion linea 118: Asigna un valor, configura un argumento o actualiza un dato del escenario.
            incluye_cojines=False,
        # Explicacion linea 119: Cierra la expresion o estructura iniciada anteriormente.
        ),
    # Explicacion linea 120: Cierra la expresion o estructura iniciada anteriormente.
    ]

    # Explicacion linea 122: Asigna un valor, configura un argumento o actualiza un dato del escenario.
    almacenamiento = [
        # Explicacion linea 123: Continua la expresion del bloque anterior o ejecuta esta instruccion.
        Armario(
            # Explicacion linea 124: Asigna un valor, configura un argumento o actualiza un dato del escenario.
            nombre="Armario Ropero 4 Puertas",
            # Explicacion linea 125: Asigna un valor, configura un argumento o actualiza un dato del escenario.
            material="Madera",
            # Explicacion linea 126: Asigna un valor, configura un argumento o actualiza un dato del escenario.
            color="Blanco",
            # Explicacion linea 127: Asigna un valor, configura un argumento o actualiza un dato del escenario.
            precio_base=600.0,
            # Explicacion linea 128: Asigna un valor, configura un argumento o actualiza un dato del escenario.
            num_puertas=4,
            # Explicacion linea 129: Asigna un valor, configura un argumento o actualiza un dato del escenario.
            num_cajones=2,
            # Explicacion linea 130: Asigna un valor, configura un argumento o actualiza un dato del escenario.
            tiene_espejos=True,
        # Explicacion linea 131: Cierra la expresion o estructura iniciada anteriormente.
        ),
        # Explicacion linea 132: Continua la expresion del bloque anterior o ejecuta esta instruccion.
        Cajonera(
            # Explicacion linea 133: Asigna un valor, configura un argumento o actualiza un dato del escenario.
            nombre="Cajonera Vintage 5 Cajones",
            # Explicacion linea 134: Asigna un valor, configura un argumento o actualiza un dato del escenario.
            material="Madera",
            # Explicacion linea 135: Asigna un valor, configura un argumento o actualiza un dato del escenario.
            color="Vintage",
            # Explicacion linea 136: Asigna un valor, configura un argumento o actualiza un dato del escenario.
            precio_base=300.0,
            # Explicacion linea 137: Asigna un valor, configura un argumento o actualiza un dato del escenario.
            num_cajones=5,
            # Explicacion linea 138: Asigna un valor, configura un argumento o actualiza un dato del escenario.
            tiene_ruedas=False,
        # Explicacion linea 139: Cierra la expresion o estructura iniciada anteriormente.
        ),
        # Explicacion linea 140: Continua la expresion del bloque anterior o ejecuta esta instruccion.
        Cajonera(
            # Explicacion linea 141: Asigna un valor, configura un argumento o actualiza un dato del escenario.
            nombre="Cajonera Oficina con Ruedas",
            # Explicacion linea 142: Asigna un valor, configura un argumento o actualiza un dato del escenario.
            material="Metal",
            # Explicacion linea 143: Asigna un valor, configura un argumento o actualiza un dato del escenario.
            color="Gris",
            # Explicacion linea 144: Asigna un valor, configura un argumento o actualiza un dato del escenario.
            precio_base=180.0,
            # Explicacion linea 145: Asigna un valor, configura un argumento o actualiza un dato del escenario.
            num_cajones=3,
            # Explicacion linea 146: Asigna un valor, configura un argumento o actualiza un dato del escenario.
            tiene_ruedas=True,
        # Explicacion linea 147: Cierra la expresion o estructura iniciada anteriormente.
        ),
    # Explicacion linea 148: Cierra la expresion o estructura iniciada anteriormente.
    ]

    # Explicacion linea 150: Asigna un valor, configura un argumento o actualiza un dato del escenario.
    dormitorio_oficina = [
        # Explicacion linea 151: Continua la expresion del bloque anterior o ejecuta esta instruccion.
        Cama(
            # Explicacion linea 152: Asigna un valor, configura un argumento o actualiza un dato del escenario.
            nombre="Cama King Size de Lujo",
            # Explicacion linea 153: Asigna un valor, configura un argumento o actualiza un dato del escenario.
            material="Madera",
            # Explicacion linea 154: Asigna un valor, configura un argumento o actualiza un dato del escenario.
            color="Nogal",
            # Explicacion linea 155: Asigna un valor, configura un argumento o actualiza un dato del escenario.
            precio_base=1000.0,
            # Explicacion linea 156: Asigna un valor, configura un argumento o actualiza un dato del escenario.
            tamaño="king",
            # Explicacion linea 157: Asigna un valor, configura un argumento o actualiza un dato del escenario.
            incluye_colchon=True,
            # Explicacion linea 158: Asigna un valor, configura un argumento o actualiza un dato del escenario.
            tiene_cabecera=True,
        # Explicacion linea 159: Cierra la expresion o estructura iniciada anteriormente.
        ),
        # Explicacion linea 160: Continua la expresion del bloque anterior o ejecuta esta instruccion.
        Cama(
            # Explicacion linea 161: Asigna un valor, configura un argumento o actualiza un dato del escenario.
            nombre="Cama Individual Juvenil",
            # Explicacion linea 162: Asigna un valor, configura un argumento o actualiza un dato del escenario.
            material="Metal",
            # Explicacion linea 163: Asigna un valor, configura un argumento o actualiza un dato del escenario.
            color="Azul",
            # Explicacion linea 164: Asigna un valor, configura un argumento o actualiza un dato del escenario.
            precio_base=400.0,
            # Explicacion linea 165: Asigna un valor, configura un argumento o actualiza un dato del escenario.
            tamaño="individual",
            # Explicacion linea 166: Asigna un valor, configura un argumento o actualiza un dato del escenario.
            incluye_colchon=False,
            # Explicacion linea 167: Asigna un valor, configura un argumento o actualiza un dato del escenario.
            tiene_cabecera=True,
        # Explicacion linea 168: Cierra la expresion o estructura iniciada anteriormente.
        ),
        # Explicacion linea 169: Continua la expresion del bloque anterior o ejecuta esta instruccion.
        Escritorio(
            # Explicacion linea 170: Asigna un valor, configura un argumento o actualiza un dato del escenario.
            nombre="Escritorio Ejecutivo L-Shape",
            # Explicacion linea 171: Asigna un valor, configura un argumento o actualiza un dato del escenario.
            material="Madera",
            # Explicacion linea 172: Asigna un valor, configura un argumento o actualiza un dato del escenario.
            color="Caoba",
            # Explicacion linea 173: Asigna un valor, configura un argumento o actualiza un dato del escenario.
            precio_base=750.0,
            # Explicacion linea 174: Asigna un valor, configura un argumento o actualiza un dato del escenario.
            forma="L",
            # Explicacion linea 175: Asigna un valor, configura un argumento o actualiza un dato del escenario.
            tiene_cajones=True,
            # Explicacion linea 176: Asigna un valor, configura un argumento o actualiza un dato del escenario.
            num_cajones=4,
        # Explicacion linea 177: Cierra la expresion o estructura iniciada anteriormente.
        ),
        # Explicacion linea 178: Continua la expresion del bloque anterior o ejecuta esta instruccion.
        Escritorio(
            # Explicacion linea 179: Asigna un valor, configura un argumento o actualiza un dato del escenario.
            nombre="Escritorio Gaming RGB",
            # Explicacion linea 180: Asigna un valor, configura un argumento o actualiza un dato del escenario.
            material="Metal",
            # Explicacion linea 181: Asigna un valor, configura un argumento o actualiza un dato del escenario.
            color="Negro",
            # Explicacion linea 182: Asigna un valor, configura un argumento o actualiza un dato del escenario.
            precio_base=500.0,
            # Explicacion linea 183: Asigna un valor, configura un argumento o actualiza un dato del escenario.
            forma="rectangular",
            # Explicacion linea 184: Asigna un valor, configura un argumento o actualiza un dato del escenario.
            tiene_cajones=False,
            # Explicacion linea 185: Asigna un valor, configura un argumento o actualiza un dato del escenario.
            tiene_iluminacion=True,
        # Explicacion linea 186: Cierra la expresion o estructura iniciada anteriormente.
        ),
    # Explicacion linea 187: Cierra la expresion o estructura iniciada anteriormente.
    ]

    # Explicacion linea 189: Asigna un valor, configura un argumento o actualiza un dato del escenario.
    sofacama = SofaCama(
        # Explicacion linea 190: Asigna un valor, configura un argumento o actualiza un dato del escenario.
        nombre="SofaCama Convertible Premium",
        # Explicacion linea 191: Asigna un valor, configura un argumento o actualiza un dato del escenario.
        material="Tela",
        # Explicacion linea 192: Asigna un valor, configura un argumento o actualiza un dato del escenario.
        color="Beige",
        # Explicacion linea 193: Asigna un valor, configura un argumento o actualiza un dato del escenario.
        precio_base=1500.0,
        # Explicacion linea 194: Asigna un valor, configura un argumento o actualiza un dato del escenario.
        capacidad_personas=3,
        # Explicacion linea 195: Asigna un valor, configura un argumento o actualiza un dato del escenario.
        material_tapizado="tela",
        # Explicacion linea 196: Asigna un valor, configura un argumento o actualiza un dato del escenario.
        tamaño_cama="matrimonial",
        # Explicacion linea 197: Asigna un valor, configura un argumento o actualiza un dato del escenario.
        incluye_colchon=True,
        # Explicacion linea 198: Asigna un valor, configura un argumento o actualiza un dato del escenario.
        mecanismo_conversion="hidraulico",
    # Explicacion linea 199: Cierra la expresion o estructura iniciada anteriormente.
    )

    # Explicacion linea 201: Asigna un valor, configura un argumento o actualiza un dato del escenario.
    todos_los_muebles = (
        # Explicacion linea 202: Continua la expresion del bloque anterior o ejecuta esta instruccion.
        sillas
        # Explicacion linea 203: Continua la expresion del bloque anterior o ejecuta esta instruccion.
        + mesas
        # Explicacion linea 204: Continua la expresion del bloque anterior o ejecuta esta instruccion.
        + asientos_grandes
        # Explicacion linea 205: Continua la expresion del bloque anterior o ejecuta esta instruccion.
        + almacenamiento
        # Explicacion linea 206: Continua la expresion del bloque anterior o ejecuta esta instruccion.
        + dormitorio_oficina
        # Explicacion linea 207: Continua la expresion del bloque anterior o ejecuta esta instruccion.
        + [sofacama]
    # Explicacion linea 208: Cierra la expresion o estructura iniciada anteriormente.
    )

    # Explicacion linea 210: Recorre los elementos de una coleccion para procesarlos.
    for mueble in todos_los_muebles:
        # Explicacion linea 211: Asigna un valor, configura un argumento o actualiza un dato del escenario.
        resultado = tienda.agregar_mueble(mueble)
        # Explicacion linea 212: Muestra informacion al usuario en la consola.
        print(f"  ✓ {resultado}")

    # Explicacion linea 214: Muestra informacion al usuario en la consola.
    print(f"✅ Catálogo inicial creado con éxito!")


# Explicacion linea 217: Declara la funcion y sus parametros de entrada.
def crear_comedores_ejemplo(tienda: "TiendaMuebles") -> None:
    # Explicacion linea 218: Documenta el objetivo y el uso de este bloque.
    """
    Crea comedores de ejemplo para demostrar la composición.

    Args:
        tienda: Instancia de TiendaMuebles donde agregar los comedores
    """
    # Explicacion linea 224: Muestra informacion al usuario en la consola.
    print("\n🍽️ Creando comedores de ejemplo...")

    # Explicacion linea 226: Asigna un valor, configura un argumento o actualiza un dato del escenario.
    mesa_familiar = Mesa(
        # Explicacion linea 227: Asigna un valor, configura un argumento o actualiza un dato del escenario.
        nombre="Mesa Familiar Extensible",
        # Explicacion linea 228: Asigna un valor, configura un argumento o actualiza un dato del escenario.
        material="Madera",
        # Explicacion linea 229: Asigna un valor, configura un argumento o actualiza un dato del escenario.
        color="Roble",
        # Explicacion linea 230: Asigna un valor, configura un argumento o actualiza un dato del escenario.
        precio_base=800.0,
        # Explicacion linea 231: Asigna un valor, configura un argumento o actualiza un dato del escenario.
        forma="rectangular",
        # Explicacion linea 232: Asigna un valor, configura un argumento o actualiza un dato del escenario.
        capacidad_personas=8,
    # Explicacion linea 233: Cierra la expresion o estructura iniciada anteriormente.
    )

    # Explicacion linea 235: Asigna un valor, configura un argumento o actualiza un dato del escenario.
    sillas_familiares = []
    # Explicacion linea 236: Recorre los elementos de una coleccion para procesarlos.
    for i in range(1, 7):  # 6 sillas
        # Explicacion linea 237: Asigna un valor, configura un argumento o actualiza un dato del escenario.
        silla = Silla(
            # Explicacion linea 238: Asigna un valor, configura un argumento o actualiza un dato del escenario.
            nombre=f"Silla Familiar {i}",
            # Explicacion linea 239: Asigna un valor, configura un argumento o actualiza un dato del escenario.
            material="Madera",
            # Explicacion linea 240: Asigna un valor, configura un argumento o actualiza un dato del escenario.
            color="Roble",
            # Explicacion linea 241: Asigna un valor, configura un argumento o actualiza un dato del escenario.
            precio_base=120.0,
            # Explicacion linea 242: Asigna un valor, configura un argumento o actualiza un dato del escenario.
            tiene_respaldo=True,
            # Explicacion linea 243: Asigna un valor, configura un argumento o actualiza un dato del escenario.
            material_tapizado="tela",
        # Explicacion linea 244: Cierra la expresion o estructura iniciada anteriormente.
        )
        # Explicacion linea 245: Continua la expresion del bloque anterior o ejecuta esta instruccion.
        sillas_familiares.append(silla)

    # Explicacion linea 247: Asigna un valor, configura un argumento o actualiza un dato del escenario.
    comedor_familiar = Comedor(
        # Explicacion linea 248: Asigna un valor, configura un argumento o actualiza un dato del escenario.
        nombre="Comedor Familiar Completo", mesa=mesa_familiar, sillas=sillas_familiares
    # Explicacion linea 249: Cierra la expresion o estructura iniciada anteriormente.
    )

    # Explicacion linea 251: Asigna un valor, configura un argumento o actualiza un dato del escenario.
    mesa_moderna = Mesa(
        # Explicacion linea 252: Asigna un valor, configura un argumento o actualiza un dato del escenario.
        nombre="Mesa Moderna Cristal",
        # Explicacion linea 253: Asigna un valor, configura un argumento o actualiza un dato del escenario.
        material="Vidrio",
        # Explicacion linea 254: Asigna un valor, configura un argumento o actualiza un dato del escenario.
        color="Negro",
        # Explicacion linea 255: Asigna un valor, configura un argumento o actualiza un dato del escenario.
        precio_base=600.0,
        # Explicacion linea 256: Asigna un valor, configura un argumento o actualiza un dato del escenario.
        forma="redonda",
        # Explicacion linea 257: Asigna un valor, configura un argumento o actualiza un dato del escenario.
        capacidad_personas=4,
    # Explicacion linea 258: Cierra la expresion o estructura iniciada anteriormente.
    )

    # Explicacion linea 260: Asigna un valor, configura un argumento o actualiza un dato del escenario.
    sillas_modernas = []
    # Explicacion linea 261: Recorre los elementos de una coleccion para procesarlos.
    for i in range(1, 5):  # 4 sillas
        # Explicacion linea 262: Asigna un valor, configura un argumento o actualiza un dato del escenario.
        silla = Silla(
            # Explicacion linea 263: Asigna un valor, configura un argumento o actualiza un dato del escenario.
            nombre=f"Silla Moderna {i}",
            # Explicacion linea 264: Asigna un valor, configura un argumento o actualiza un dato del escenario.
            material="Metal",
            # Explicacion linea 265: Asigna un valor, configura un argumento o actualiza un dato del escenario.
            color="Negro",
            # Explicacion linea 266: Asigna un valor, configura un argumento o actualiza un dato del escenario.
            precio_base=150.0,
            # Explicacion linea 267: Asigna un valor, configura un argumento o actualiza un dato del escenario.
            tiene_respaldo=True,
            # Explicacion linea 268: Asigna un valor, configura un argumento o actualiza un dato del escenario.
            material_tapizado="cuero",
        # Explicacion linea 269: Cierra la expresion o estructura iniciada anteriormente.
        )
        # Explicacion linea 270: Continua la expresion del bloque anterior o ejecuta esta instruccion.
        sillas_modernas.append(silla)

    # Explicacion linea 272: Asigna un valor, configura un argumento o actualiza un dato del escenario.
    comedor_moderno = Comedor(
        # Explicacion linea 273: Asigna un valor, configura un argumento o actualiza un dato del escenario.
        nombre="Comedor Moderno Premium", mesa=mesa_moderna, sillas=sillas_modernas
    # Explicacion linea 274: Cierra la expresion o estructura iniciada anteriormente.
    )

    # Explicacion linea 276: Asigna un valor, configura un argumento o actualiza un dato del escenario.
    comedores = [comedor_familiar, comedor_moderno]
    # Explicacion linea 277: Recorre los elementos de una coleccion para procesarlos.
    for comedor in comedores:
        # Explicacion linea 278: Asigna un valor, configura un argumento o actualiza un dato del escenario.
        resultado = tienda.agregar_comedor(comedor)
        # Explicacion linea 279: Muestra informacion al usuario en la consola.
        print(f"  ✓ {resultado}")

    # Explicacion linea 281: Muestra informacion al usuario en la consola.
    print("✅ Comedores de ejemplo creados!")


# Explicacion linea 284: Declara la funcion y sus parametros de entrada.
def aplicar_descuentos_ejemplo(tienda: "TiendaMuebles") -> None:
    # Explicacion linea 285: Documenta el objetivo y el uso de este bloque.
    """
    Aplica algunos descuentos de ejemplo para demostrar el sistema.

    Args:
        tienda: Instancia de TiendaMuebles donde aplicar descuentos
    """
    # Explicacion linea 291: Muestra informacion al usuario en la consola.
    print("\n🏷️ Aplicando descuentos de ejemplo...")

    # Explicacion linea 293: Asigna un valor, configura un argumento o actualiza un dato del escenario.
    descuentos = [
        # Explicacion linea 294: Continua la expresion del bloque anterior o ejecuta esta instruccion.
        ("silla", 10),  # 10% de descuento en sillas
        # Explicacion linea 295: Continua la expresion del bloque anterior o ejecuta esta instruccion.
        ("mesa", 15),  # 15% de descuento en mesas
        # Explicacion linea 296: Continua la expresion del bloque anterior o ejecuta esta instruccion.
        ("sofa", 20),  # 20% de descuento en sofás
    # Explicacion linea 297: Cierra la expresion o estructura iniciada anteriormente.
    ]

    # Explicacion linea 299: Recorre los elementos de una coleccion para procesarlos.
    for categoria, porcentaje in descuentos:
        # Explicacion linea 300: Asigna un valor, configura un argumento o actualiza un dato del escenario.
        resultado = tienda.aplicar_descuento(categoria, porcentaje)
        # Explicacion linea 301: Muestra informacion al usuario en la consola.
        print(f"  ✓ {resultado}")

    # Explicacion linea 303: Muestra informacion al usuario en la consola.
    print("✅ Descuentos aplicados!")


# Explicacion linea 306: Declara la funcion y sus parametros de entrada.
def mostrar_estadisticas_iniciales(tienda: "TiendaMuebles") -> None:
    # Explicacion linea 307: Documenta el objetivo y el uso de este bloque.
    """
    Muestra estadísticas iniciales de la tienda.

    Args:
        tienda: Instancia de TiendaMuebles para obtener estadísticas
    """
    # Explicacion linea 313: Muestra informacion al usuario en la consola.
    print("\n📊 Estadísticas iniciales de la tienda:")

    # Explicacion linea 315: Asigna un valor, configura un argumento o actualiza un dato del escenario.
    stats = tienda.obtener_estadisticas()
    # Explicacion linea 316: Muestra informacion al usuario en la consola.
    print(f"  📦 Total de muebles: {stats.get('total_muebles', 0)}")
    # Explicacion linea 317: Muestra informacion al usuario en la consola.
    print(f"  🍽️ Total de comedores: {stats.get('total_comedores', 0)}")
    # Explicacion linea 318: Muestra informacion al usuario en la consola.
    print(f"  💰 Valor del inventario: ${stats.get('valor_inventario', 0):,.2f}")
    # Explicacion linea 319: Muestra informacion al usuario en la consola.
    print(f"  🏷️ Descuentos activos: {stats.get('descuentos_activos', {})}")
    # Explicacion linea 320: Muestra informacion al usuario en la consola.
    print(f"  🛒 Ventas realizadas: {stats.get('ventas_realizadas', 0)}")
    # Explicacion linea 321: Muestra informacion al usuario en la consola.
    print(
        # Explicacion linea 322: Continua la expresion del bloque anterior o ejecuta esta instruccion.
        f"  📈 Total muebles vendidos (acumulado): {stats.get('total_muebles_vendidos', 0)}"
    # Explicacion linea 323: Cierra la expresion o estructura iniciada anteriormente.
    )
    # Explicacion linea 324: Muestra informacion al usuario en la consola.
    print(
        # Explicacion linea 325: Continua la expresion del bloque anterior o ejecuta esta instruccion.
        f"  💵 Valor total de ventas (acumulado): ${stats.get('valor_total_ventas', 0):,.2f}"
    # Explicacion linea 326: Cierra la expresion o estructura iniciada anteriormente.
    )
    # Explicacion linea 327: Muestra informacion al usuario en la consola.
    print("\n  📋 Distribución por tipos:")
    # Explicacion linea 328: Recorre los elementos de una coleccion para procesarlos.
    for tipo, cantidad in (stats.get("tipos_muebles", {}) or {}).items():
        # Explicacion linea 329: Muestra informacion al usuario en la consola.
        print(f"    • {tipo}: {cantidad} unidades")


# Explicacion linea 332: Declara la funcion y sus parametros de entrada.
def main():
    # Explicacion linea 333: Documenta el objetivo y el uso de este bloque.
    """
    Función principal que inicializa y ejecuta la aplicación.

    Esta función demuestra todos los conceptos de OOP implementados:
    - Creación de objetos de diferentes clases
    - Herencia y polimorfismo al agregar diferentes tipos de muebles
    - Composición con los comedores
    - Herencia múltiple con el sofá-cama
    - Encapsulación y abstracción en toda la jerarquía
    """
    # Explicacion linea 343: Inicia una operacion que puede generar una excepcion.
    try:
        # Explicacion linea 344: Muestra informacion al usuario en la consola.
        print("🏠 Bienvenido a la Tienda de Muebles - Taller OOP 🏠")
        # Explicacion linea 345: Muestra informacion al usuario en la consola.
        print("=" * 50)

        # Explicacion linea 347: Asigna un valor, configura un argumento o actualiza un dato del escenario.
        tienda = TiendaMuebles("Mueblería Moderna OOP")
        # Explicacion linea 348: Muestra informacion al usuario en la consola.
        print(f"🏪 Inicializando {tienda.nombre}...")

        # Explicacion linea 350: Continua la expresion del bloque anterior o ejecuta esta instruccion.
        crear_catalogo_inicial(tienda)

        # Explicacion linea 352: Continua la expresion del bloque anterior o ejecuta esta instruccion.
        crear_comedores_ejemplo(tienda)

        # Explicacion linea 354: Continua la expresion del bloque anterior o ejecuta esta instruccion.
        aplicar_descuentos_ejemplo(tienda)

        # Explicacion linea 356: Continua la expresion del bloque anterior o ejecuta esta instruccion.
        mostrar_estadisticas_iniciales(tienda)

        # Explicacion linea 358: Muestra informacion al usuario en la consola.
        print("\n🎯 Iniciando interfaz de usuario...")
        # Explicacion linea 359: Asigna un valor, configura un argumento o actualiza un dato del escenario.
        menu = MenuTienda(tienda)

        # Explicacion linea 361: Continua la expresion del bloque anterior o ejecuta esta instruccion.
        input("\nPresiona Enter para iniciar el menú interactivo...")

        # Explicacion linea 363: Ejecuta una operacion del objeto dentro del flujo.
        menu.ejecutar()

    # Explicacion linea 365: Controla la excepcion indicada sin detener el flujo principal.
    except KeyboardInterrupt:
        # Explicacion linea 366: Muestra informacion al usuario en la consola.
        print("\n\n👋 Programa interrumpido por el usuario. ¡Hasta luego!")
    # Explicacion linea 367: Controla la excepcion indicada sin detener el flujo principal.
    except Exception as e:
        # Explicacion linea 368: Muestra informacion al usuario en la consola.
        print(f"\n❌ Error inesperado: {e}")
        # Explicacion linea 369: Importa las herramientas o clases usadas en este modulo.
        import traceback

        # Explicacion linea 371: Continua la expresion del bloque anterior o ejecuta esta instruccion.
        traceback.print_exc()
    # Explicacion linea 372: Comienza un nuevo bloque de instrucciones.
    finally:
        # Explicacion linea 373: Muestra informacion al usuario en la consola.
        print("\n" + "=" * 50)
        # Explicacion linea 374: Muestra informacion al usuario en la consola.
        print("✨ Programa finalizado. ¡Gracias por usar la Tienda de Muebles! ✨")


# Explicacion linea 377: Evalua una condicion para elegir el camino de ejecucion.
if __name__ == "__main__":
    # Punto de entrada de la aplicación
    # Explicacion linea 379: Continua la expresion del bloque anterior o ejecuta esta instruccion.
    main()
