# Proyecto de Lógica Matemática - Sistema Axiomático L

## Descripción

Este proyecto implementa un reconocedor de expresiones del cálculo proposicional reducido (Sistema Axiomático L) utilizando técnicas de análisis léxico y sintáctico. El sistema está desarrollado en Python usando PLY (Python Lex-Yacc) para el análisis y NetworkX para la visualización de grafos.

## Objetivos

- Aplicar conceptos de autómatas, expresiones regulares y gramáticas
- Implementar un analizador léxico y sintáctico para el Sistema L
- Generar grafos dirigidos que representen la estructura de las expresiones
- Crear diagramas de autómatas finitos para el reconocimiento del alfabeto

## Características del Sistema L

### Alfabeto

- **Variables proposicionales**: p, q, r, s, t, u, v, w, x, y, z
- **Operadores lógicos**: 
  - `~` (negación)
  - `^` (conjunción)
  - `o` (disyunción)
  - `=>` (implicación)
  - `<=>` (bicondicional)
- **Signos de puntuación**: `(`, `)`
- **Constantes**: `0` (falso), `1` (verdadero)

### Gramática

1. Las variables proposicionales y constantes son fórmulas bien formadas
2. Si `a` es una fórmula bien formada, `~a` es una fórmula bien formada
3. Si `a` y `b` son fórmulas bien formadas, entonces `a^b`, `aob`, `a=>b`, `a<=>b` son fórmulas bien formadas
4. Si `a` es una fórmula bien formada, entonces `(a)` es una fórmula bien formada
5. Solo las expresiones producidas mediante los incisos anteriores son fórmulas bien formadas

### Precedencia de Operadores

1. `~` (negación) - Mayor precedencia, asociatividad derecha
2. `^` (conjunción) - Asociatividad izquierda
3. `o` (disyunción) - Asociatividad izquierda
4. `=>` (implicación) - Asociatividad izquierda
5. `<=>` (bicondicional) - Menor precedencia, asociatividad izquierda

## Estructura del Proyecto

```
Proy 1/
├── requirements.txt          # Dependencias del proyecto
├── main.py                   # Programa principal con interfaz de usuario
├── analizador_lexico.py      # Analizador léxico usando PLY
├── analizador_sintactico.py  # Analizador sintáctico usando PLY
├── generador_grafos.py       # Generación y visualización de grafos
├── automata_finito.py        # Diagrama del autómata finito
├── gramatica_sistema_L.py    # Documentación formal de la gramática
└── README.md                 # Este archivo
```

## Instalación

1. **Clonar o descargar el proyecto**

2. **Instalar las dependencias**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Ejecutar el programa principal**:
   ```bash
   python main.py
   ```

## Dependencias

- **PLY (Python Lex-Yacc) 3.11**: Para análisis léxico y sintáctico
- **NetworkX 3.2.1**: Para creación y manipulación de grafos
- **Matplotlib 3.8.2**: Para visualización de grafos y diagramas

## Uso del Sistema

### Interfaz Principal

El programa principal (`main.py`) ofrece un menú interactivo con las siguientes opciones:

1. **Analizar expresión completa**: Realiza análisis léxico, sintáctico y genera el grafo
2. **Solo análisis léxico**: Muestra los tokens identificados
3. **Solo análisis sintáctico**: Verifica la sintaxis y muestra el árbol
4. **Mostrar gramática**: Documentación formal del Sistema L
5. **Mostrar autómata finito**: Diagrama del autómata para el alfabeto
6. **Probar expresiones de ejemplo**: Ejecuta casos de prueba predefinidos
7. **Validar múltiples expresiones**: Permite validar varias expresiones
8. **Exportar grafo en formato DOT**: Para usar con Graphviz
9. **Mostrar ayuda**: Información sobre el uso del sistema

### Ejemplos de Expresiones Válidas

- `p` - Variable simple
- `~~~q` - Negación múltiple
- `(p^q)` - Conjunción con paréntesis
- `(0=>(ros))` - Implicación con constante
- `~(p^q)` - Negación de conjunción
- `(p<=>~p)` - Bicondicional con negación
- `((p=>q)^p)` - Expresión compleja anidada
- `(~(p^(qor))os)` - Expresión con múltiples operadores

## Componentes del Sistema

### 1. Analizador Léxico (`analizador_lexico.py`)

<mcreference link="https://www.ericknavarro.io/2020/02/10/24-Mi-primer-proyecto-utilizando-PLY/" index="1">1</mcreference>

- Implementa el reconocimiento de tokens usando expresiones regulares
- Identifica variables, operadores, paréntesis y constantes
- Maneja errores léxicos y caracteres inválidos

### 2. Analizador Sintáctico (`analizador_sintactico.py`)

<mcreference link="https://www.ericknavarro.io/2020/02/10/24-Mi-primer-proyecto-utilizando-PLY/" index="1">1</mcreference>

- Implementa la gramática del Sistema L usando PLY
- Construye árboles sintácticos abstractos (AST)
- Genera grafos dirigidos durante el análisis
- Maneja precedencia y asociatividad de operadores

### 3. Generador de Grafos (`generador_grafos.py`)

<mcreference link="https://networkx.org/documentation/stable/tutorial.html" index="2">2</mcreference> <mcreference link="https://www.geeksforgeeks.org/python-visualize-graphs-generated-in-networkx-using-matplotlib/" index="5">5</mcreference>

- Crea grafos dirigidos usando NetworkX
- Visualiza grafos con Matplotlib
- Exporta grafos en formato DOT para Graphviz
- Genera reportes detallados de la estructura

### 4. Autómata Finito (`automata_finito.py`)

- Implementa el diagrama de estados para el alfabeto
- Visualiza las transiciones del autómata
- Exporta diagramas en múltiples formatos

### 5. Gramática Formal (`gramatica_sistema_L.py`)

- Documentación completa de la gramática
- Ejemplos de derivaciones
- Notaciones BNF y EBNF
- Validación de expresiones

## Archivos Generados

El sistema genera varios archivos durante su ejecución:

- `grafo_[expresion].png` - Visualización del grafo dirigido
- `automata_sistema_L.png` - Diagrama del autómata finito
- `*.dot` - Archivos en formato DOT para Graphviz
- `parser.out` - Archivo de depuración de PLY
- `parsetab.py` - Tabla de análisis sintáctico generada por PLY

## Ejemplos de Uso

### Análisis de una Expresión

```python
from analizador_sintactico import analizar_sintacticamente
from generador_grafos import visualizar_grafo

# Analizar expresión
expresion = "((p=>q)^p)"
ast, grafo = analizar_sintacticamente(expresion)

if grafo:
    # Visualizar el grafo
    visualizar_grafo(grafo, expresion)
```

### Validación Léxica

```python
from analizador_lexico import analizar_lexicamente

# Obtener tokens
tokens = analizar_lexicamente("p^q")
print(tokens)  # [('VARIABLE', 'p'), ('CONJUNCION', '^'), ('VARIABLE', 'q')]
```

## Características Técnicas

### Análisis Léxico
- Reconocimiento basado en expresiones regulares
- Manejo de caracteres especiales y secuencias multi-carácter
- Detección y reporte de errores léxicos

### Análisis Sintáctico
- Gramática libre de contexto implementada con PLY
- Construcción de árboles sintácticos abstractos
- Manejo de precedencia y asociatividad
- Generación automática de grafos dirigidos

### Visualización
- Grafos dirigidos con nodos coloreados por tipo
- Layouts automáticos para mejor legibilidad
- Exportación en múltiples formatos (PNG, DOT)
- Leyendas y etiquetas descriptivas

## Limitaciones

- Solo acepta las variables proposicionales especificadas (p-z)
- Los operadores deben escribirse exactamente como se define
- No soporta espacios dentro de los operadores multi-carácter
- La visualización puede ser compleja para expresiones muy grandes

## Casos de Prueba

El sistema incluye casos de prueba predefinidos que cubren:

- Variables simples
- Operadores unarios y binarios
- Expresiones con paréntesis
- Precedencia de operadores
- Expresiones anidadas complejas
- Casos de error comunes

## Autor

Proyecto desarrollado como parte del curso de Lógica Matemática, implementando conceptos de:
- Teoría de autómatas
- Análisis léxico y sintáctico
- Gramáticas formales
- Visualización de estructuras de datos

## Referencias

<mcreference link="https://www.ericknavarro.io/2020/02/10/24-Mi-primer-proyecto-utilizando-PLY/" index="1">1</mcreference> <mcreference link="https://networkx.org/documentation/stable/tutorial.html" index="2">2</mcreference> <mcreference link="https://www.geeksforgeeks.org/python-visualize-graphs-generated-in-networkx-using-matplotlib/" index="5">5</mcreference>

- PLY (Python Lex-Yacc) Documentation
- NetworkX Documentation
- Matplotlib Documentation
- Teoría de Compiladores - Aho, Sethi, Ullman
- Lógica Matemática y Fundamentos