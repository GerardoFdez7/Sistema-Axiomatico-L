# Gramática del Sistema Axiomático L
# Definición formal de las producciones gramaticales

def mostrar_gramatica_formal():
    """
    Muestra la gramática formal del Sistema L
    """
    gramatica = """
=== GRAMÁTICA DEL SISTEMA AXIOMÁTICO L ===

1. ALFABETO DE L:
   • Variables proposicionales: {p, q, r, s, t, u, v, w, x, y, z}
   • Operadores lógicos: {~, ^, o, =>, <=>}
   • Signos de puntuación: {(, )}
   • Constantes: {0, 1}

2. SÍMBOLOS NO TERMINALES:
   • F (Fórmula)
   • E (Expresión)

3. SÍMBOLO INICIAL:
   • F (Fórmula)

4. PRODUCCIONES GRAMATICALES:

   P1: F → E
       (Una fórmula es una expresión)

   P2: E → VARIABLE
       (Las variables proposicionales son fórmulas bien formadas)
       donde VARIABLE ∈ {p, q, r, s, t, u, v, w, x, y, z}

   P3: E → CONSTANTE
       (Las constantes son fórmulas bien formadas)
       donde CONSTANTE ∈ {0, 1}

   P4: E → ~ E
       (Si E es una fórmula bien formada, ~E es una fórmula bien formada)

   P5: E → E ^ E
       (Si E₁ y E₂ son fórmulas bien formadas, E₁^E₂ es una fórmula bien formada)

   P6: E → E o E
       (Si E₁ y E₂ son fórmulas bien formadas, E₁oE₂ es una fórmula bien formada)

   P7: E → E => E
       (Si E₁ y E₂ son fórmulas bien formadas, E₁=>E₂ es una fórmula bien formada)

   P8: E → E <=> E
       (Si E₁ y E₂ son fórmulas bien formadas, E₁<=>E₂ es una fórmula bien formada)

   P9: E → ( E )
       (Si E es una fórmula bien formada, (E) es una fórmula bien formada)

5. PRECEDENCIA DE OPERADORES (de mayor a menor):
   1. ~ (Negación) - Asociatividad: Derecha
   2. ^ (Conjunción) - Asociatividad: Izquierda
   3. o (Disyunción) - Asociatividad: Izquierda
   4. => (Implicación) - Asociatividad: Izquierda
   5. <=> (Bicondicional) - Asociatividad: Izquierda

6. REGLAS SEMÁNTICAS:
   • Solo las expresiones que pueden ser producidas mediante las
     producciones P1-P9 en un número finito de pasos son fórmulas
     bien formadas del Sistema L.
   • Los paréntesis pueden usarse para alterar la precedencia natural
     de los operadores.
"""
    return gramatica

def generar_ejemplos_derivaciones():
    """
    Genera ejemplos de derivaciones usando la gramática
    """
    ejemplos = """
=== EJEMPLOS DE DERIVACIONES ===

1. Derivación de "p":
   F → E → VARIABLE → p

2. Derivación de "~p":
   F → E → ~E → ~VARIABLE → ~p

3. Derivación de "(p^q)":
   F → E → (E) → (E^E) → (VARIABLE^VARIABLE) → (p^q)

4. Derivación de "p=>q":
   F → E → E=>E → VARIABLE=>VARIABLE → p=>q

5. Derivación de "((p=>q)^p)":
   F → E → (E) → (E^E) → ((E)^E) → ((E=>E)^E) → 
   ((VARIABLE=>VARIABLE)^VARIABLE) → ((p=>q)^p)

6. Derivación de "~(p^q)":
   F → E → ~E → ~(E) → ~(E^E) → ~(VARIABLE^VARIABLE) → ~(p^q)

7. Derivación de "(p<=>~p)":
   F → E → (E) → (E<=>E) → (VARIABLE<=>E) → 
   (VARIABLE<=>~E) → (VARIABLE<=>~VARIABLE) → (p<=>~p)
"""
    return ejemplos

def validar_expresion_gramatica(expresion):
    """
    Valida si una expresión puede ser generada por la gramática
    """
    # Importar el analizador sintáctico
    try:
        from analizador_sintactico import analizar_sintacticamente
        
        ast, grafo = analizar_sintacticamente(expresion)
        if ast is not None:
            return True, "Expresión válida según la gramática del Sistema L"
        else:
            return False, "Expresión inválida según la gramática del Sistema L"
    except Exception as e:
        return False, f"Error al validar: {e}"

def mostrar_tabla_precedencia():
    """
    Muestra la tabla de precedencia de operadores
    """
    tabla = """
=== TABLA DE PRECEDENCIA DE OPERADORES ===

┌─────────────────┬─────────────┬──────────────────┐
│    Operador     │ Precedencia │  Asociatividad   │
├─────────────────┼─────────────┼──────────────────┤
│ ~ (Negación)    │      5      │     Derecha      │
│ ^ (Conjunción)  │      4      │    Izquierda     │
│ o (Disyunción)  │      3      │    Izquierda     │
│ => (Implicación)│      2      │    Izquierda     │
│<=> (Bicondicional)│    1      │    Izquierda     │
└─────────────────┴─────────────┴──────────────────┘

Nota: Mayor número = Mayor precedencia
Los paréntesis () tienen la máxima precedencia
"""
    return tabla

def generar_bnf():
    """
    Genera la gramática en notación BNF (Backus-Naur Form)
    """
    bnf = """
=== GRAMÁTICA EN NOTACIÓN BNF ===

<formula> ::= <expresion>

<expresion> ::= <variable>
              | <constante>
              | "~" <expresion>
              | <expresion> "^" <expresion>
              | <expresion> "o" <expresion>
              | <expresion> "=>" <expresion>
              | <expresion> "<=>" <expresion>
              | "(" <expresion> ")"

<variable> ::= "p" | "q" | "r" | "s" | "t" | "u" | "v" | "w" | "x" | "y" | "z"

<constante> ::= "0" | "1"
"""
    return bnf

def generar_ebnf():
    """
    Genera la gramática en notación EBNF (Extended Backus-Naur Form)
    """
    ebnf = """
=== GRAMÁTICA EN NOTACIÓN EBNF ===

formula = expresion ;

expresion = variable
          | constante
          | "~" expresion
          | expresion "^" expresion
          | expresion "o" expresion
          | expresion "=>" expresion
          | expresion "<=>" expresion
          | "(" expresion ")" ;

variable = "p" | "q" | "r" | "s" | "t" | "u" | "v" | "w" | "x" | "y" | "z" ;

constante = "0" | "1" ;
"""
    return ebnf

if __name__ == "__main__":
    print(mostrar_gramatica_formal())
    print("\n" + "="*60)
    print(generar_ejemplos_derivaciones())
    print("\n" + "="*60)
    print(mostrar_tabla_precedencia())
    print("\n" + "="*60)
    print(generar_bnf())
    print("\n" + "="*60)
    print(generar_ebnf())
    
    # Validar algunas expresiones
    print("\n" + "="*60)
    print("=== VALIDACIÓN DE EXPRESIONES ===")
    
    expresiones_prueba = [
        "p",
        "~~~q",
        "(p^q)",
        "(0=>(ros))",
        "~(p^q)",
        "(p<=>~p)",
        "((p=>q)^p)",
        "(~(p^(qor))os)",
        "abc",  # Inválida
        "p&q",  # Inválida
    ]
    
    for expr in expresiones_prueba:
        valida, mensaje = validar_expresion_gramatica(expr)
        estado = "✓" if valida else "✗"
        print(f"{estado} {expr:15} - {mensaje}")