# Analizador Léxico para el Sistema Axiomático L
# Reconoce expresiones del cálculo proposicional

import ply.lex as lex

# Lista de tokens
tokens = (
    'VARIABLE',      # Variables proposicionales: p,q,r,s,t,u,v,w,x,y,z
    'NEGACION',      # Operador de negación: ~
    'CONJUNCION',    # Operador de conjunción: ^
    'DISYUNCION',    # Operador de disyunción: o
    'IMPLICACION',   # Operador de implicación: =>
    'BICONDICIONAL', # Operador bicondicional: <=>
    'PARIZQ',        # Paréntesis izquierdo: (
    'PARDER',        # Paréntesis derecho: )
    'CONSTANTE',     # Constantes: 0, 1
)

# Reglas de tokens usando expresiones regulares

# Variables proposicionales (solo letras específicas)
def t_VARIABLE(t):
    r'[pqrstuvwxyz]'
    return t

# Operador bicondicional (debe ir antes que implicación)
def t_BICONDICIONAL(t):
    r'<=>'
    return t

# Operador de implicación
def t_IMPLICACION(t):
    r'=>'
    return t

# Operador de negación
def t_NEGACION(t):
    r'~'
    return t

# Operador de conjunción
def t_CONJUNCION(t):
    r'\^'
    return t

# Operador de disyunción
def t_DISYUNCION(t):
    r'o'
    return t

# Paréntesis
def t_PARIZQ(t):
    r'\('
    return t

def t_PARDER(t):
    r'\)'
    return t

# Constantes (0 y 1)
def t_CONSTANTE(t):
    r'[01]'
    t.value = int(t.value)
    return t

# Caracteres ignorados (espacios y tabs)
t_ignore = ' \t'

# Manejo de saltos de línea
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# Manejo de errores
def t_error(t):
    print(f"Carácter ilegal '{t.value[0]}' en la línea {t.lineno}")
    t.lexer.skip(1)

# Construir el analizador léxico
lexer = lex.lex()

# Función para probar el analizador léxico
def analizar_lexicamente(entrada):
    lexer.input(entrada)
    tokens_encontrados = []
    
    while True:
        tok = lexer.token()
        if not tok:
            break
        tokens_encontrados.append((tok.type, tok.value))
    
    return tokens_encontrados

if __name__ == "__main__":
    # Pruebas del analizador léxico
    expresiones_prueba = [
        "p",
        "~~~q",
        "(p^q)",
        "(0=>(ros))",
        "~(p^q)",
        "(p<=>~p)",
        "((p=>q)^p)",
        "(~(p^(qor))os)"
    ]
    
    print("=== ANÁLISIS LÉXICO ===")
    for expr in expresiones_prueba:
        print(f"\nExpresión: {expr}")
        tokens = analizar_lexicamente(expr)
        print(f"Tokens: {tokens}")