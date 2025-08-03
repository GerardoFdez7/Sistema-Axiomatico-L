# Analizador Sintáctico para el Sistema Axiomático L
# Implementa la gramática del cálculo proposicional

import ply.yacc as yacc
from analizador_lexico import tokens
import networkx as nx

# Clase para representar nodos del árbol sintáctico
class NodoAST:
    def __init__(self, tipo, valor=None, hijos=None):
        self.tipo = tipo
        self.valor = valor
        self.hijos = hijos if hijos else []
        self.id = None  # ID único para el grafo
    
    def __str__(self):
        if self.valor is not None:
            return f"{self.tipo}({self.valor})"
        return self.tipo

# Variable global para el grafo
grafo_expresion = None
contador_nodos = 0

# Función para generar IDs únicos para nodos
def generar_id():
    global contador_nodos
    contador_nodos += 1
    return contador_nodos

# Función para agregar nodo al grafo
def agregar_nodo_grafo(nodo):
    global grafo_expresion
    if grafo_expresion is None:
        grafo_expresion = nx.DiGraph()
    
    nodo.id = generar_id()
    etiqueta = nodo.valor if nodo.valor is not None else nodo.tipo
    grafo_expresion.add_node(nodo.id, label=str(etiqueta), tipo=nodo.tipo)
    
    # Agregar aristas a los hijos
    for hijo in nodo.hijos:
        if hijo.id is None:
            agregar_nodo_grafo(hijo)
        grafo_expresion.add_edge(nodo.id, hijo.id)
    
    return nodo

# Precedencia de operadores (de menor a mayor precedencia)
precedence = (
    ('left', 'BICONDICIONAL'),
    ('left', 'IMPLICACION'),
    ('left', 'DISYUNCION'),
    ('left', 'CONJUNCION'),
    ('right', 'NEGACION'),
)

# Reglas de la gramática

# Regla inicial
def p_formula(p):
    '''formula : expresion'''
    global grafo_expresion, contador_nodos
    grafo_expresion = None
    contador_nodos = 0
    p[0] = agregar_nodo_grafo(p[1])

# Variables proposicionales y constantes son fórmulas bien formadas
def p_expresion_variable(p):
    '''expresion : VARIABLE'''
    p[0] = NodoAST('VARIABLE', p[1])

def p_expresion_constante(p):
    '''expresion : CONSTANTE'''
    p[0] = NodoAST('CONSTANTE', p[1])

# Negación: Si a es una fórmula bien formada, ~a es una fórmula bien formada
def p_expresion_negacion(p):
    '''expresion : NEGACION expresion %prec NEGACION'''
    p[0] = NodoAST('NEGACION', '~', [p[2]])

# Operadores binarios: Si a y b son fórmulas bien formadas, entonces a^b, aob, a=>b, a<=>b son fórmulas bien formadas
def p_expresion_conjuncion(p):
    '''expresion : expresion CONJUNCION expresion'''
    p[0] = NodoAST('CONJUNCION', '^', [p[1], p[3]])

def p_expresion_disyuncion(p):
    '''expresion : expresion DISYUNCION expresion'''
    p[0] = NodoAST('DISYUNCION', 'o', [p[1], p[3]])

def p_expresion_implicacion(p):
    '''expresion : expresion IMPLICACION expresion'''
    p[0] = NodoAST('IMPLICACION', '=>', [p[1], p[3]])

def p_expresion_bicondicional(p):
    '''expresion : expresion BICONDICIONAL expresion'''
    p[0] = NodoAST('BICONDICIONAL', '<=>', [p[1], p[3]])

# Paréntesis: Si a es una fórmula bien formada, entonces (a) es una fórmula bien formada
def p_expresion_parentesis(p):
    '''expresion : PARIZQ expresion PARDER'''
    p[0] = p[2]  # Los paréntesis no cambian la estructura del árbol

# Manejo de errores sintácticos
def p_error(p):
    if p:
        print(f"Error sintáctico en el token '{p.value}' (tipo: {p.type}) en la línea {p.lineno}")
    else:
        print("Error sintáctico: fin de entrada inesperado")

# Construir el analizador sintáctico
parser = yacc.yacc()

# Función para analizar una expresión
def analizar_sintacticamente(expresion):
    global grafo_expresion
    try:
        resultado = parser.parse(expresion)
        return resultado, grafo_expresion
    except Exception as e:
        print(f"Error durante el análisis sintáctico: {e}")
        return None, None

# Función para imprimir el árbol sintáctico
def imprimir_arbol(nodo, nivel=0):
    if nodo is None:
        return
    
    indentacion = "  " * nivel
    print(f"{indentacion}{nodo}")
    
    for hijo in nodo.hijos:
        imprimir_arbol(hijo, nivel + 1)

if __name__ == "__main__":
    # Pruebas del analizador sintáctico
    expresiones_prueba = [
        "p",
        "~~~q",
        "(p^q)",
        "~(p^q)",
        "(p<=>~p)",
        "((p=>q)^p)"
    ]
    
    print("=== ANÁLISIS SINTÁCTICO ===")
    for expr in expresiones_prueba:
        print(f"\n--- Expresión: {expr} ---")
        ast, grafo = analizar_sintacticamente(expr)
        if ast:
            print("Árbol sintáctico:")
            imprimir_arbol(ast)
            if grafo:
                print(f"Nodos en el grafo: {list(grafo.nodes(data=True))}")
                print(f"Aristas en el grafo: {list(grafo.edges())}")
        else:
            print("Error en el análisis")