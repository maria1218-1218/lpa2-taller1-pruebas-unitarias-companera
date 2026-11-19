# MUEBLES AURORA | Laboratorio de calidad de software

> **LPA2 - Taller 1**  /  Version B  /  Python + pytest
>
> Este proyecto conserva el sistema de tienda de muebles del ejercicio del docente y presenta una suite de pruebas documentada por escenarios de uso.

## Panel del proyecto

| Area de verificacion | Que se comprueba | Evidencia |
| :-- | :-- | :-- |
| Abstraccion y POO | Interfaces abstractas, metodos y herencia | `tests/unit/models/` |
| Herencia multiple | Comportamiento de SofaCama | `tests/unit/models/concretos/` |
| Composicion | Comedores compuestos por mesa y sillas | `tests/unit/models/composicion/` |
| Reglas de negocio | Descuentos, inventario, venta y errores | `tests/unit/services/` |
| Datos reutilizables | Fixtures independientes | `tests/conftest.py` |
| Aislamiento | Objetos Mock y patch | Pruebas de servicios e integracion |
| TDD | Validaciones de funcionalidades de inventario | `tests/unit/services/test_tdd_inventario.py` |
| Integracion | Recorrido entre varias capas del sistema | `tests/integration/` |
| Cobertura | Umbral minimo de 80 por ciento | `htmlcov/index.html` |

## Guia rapida para Windows (VS Code)

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python -m pytest
```

Si PowerShell bloquea la activacion, no necesitas modificar la seguridad de Windows:

```powershell
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe -m pytest
```

## Comandos de evaluacion

```bash
python -m pytest -v
python -m pytest tests/unit -v
python -m pytest tests/integration -m integration -v
python -m pytest --cov=src --cov-branch --cov-report=term-missing --cov-report=html
```

El reporte navegable esta en `htmlcov/index.html`. La portada alternativa del informe esta en `informe_aurora.html`.

## Metodo AAA

- **Preparar:** crear muebles, tienda y datos de entrada.
- **Actuar:** invocar una operacion del sistema.
- **Comprobar:** comparar el resultado real con el esperado.

## TDD

1. RED: escribir primero un escenario que inicialmente falle.
2. GREEN: implementar solo el comportamiento necesario para aprobar.
3. REFACTOR: mejorar la implementacion manteniendo la prueba en verde.

La suite incluye pruebas de inventario pensadas para este ciclo. No se afirma que el historial de Git documente los tres pasos.

## Estructura

```text
src/                 Codigo original de la aplicacion, con comentarios de apoyo
  models/            Categorias, tipos concretos y composicion
  services/          Tienda e inventario
  ui/                Interfaz de consola
  main.py            Punto de entrada
tests/
  conftest.py        Datos compartidos
  unit/              Casos unitarios organizados por dominio
  integration/       Escenarios de varias capas
htmlcov/             Reporte automatico de cobertura
informe_aurora.html   Portada visual diferenciada
pytest.ini           Configuracion de pruebas
.coveragerc          Reglas de medicion
GUIA_COMENTARIOS.txt  Guia de lectura en texto simple
```

## Notas de mantenimiento

Los archivos HTML de `htmlcov/` son generados por `pytest-cov` y se pueden volver a crear con los comandos anteriores. El codigo productivo no fue reescrito: solo se agregaron comentarios explicativos para evitar alterar la logica del docente. Los comentarios agregados se escribieron sin tildes.

## Entregables

- [x] Pruebas separadas por modulos
- [x] Cobertura minima del 80 por ciento (validar nuevamente en el equipo local)
- [x] Casos limite y condiciones de error
- [x] Fixtures, mocks y pruebas independientes
- [x] Reporte HTML generado
- [x] README con comandos y explicaciones
