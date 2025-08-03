# Proyecto de Lógica Matemática - Sistema Axiomático L
# Reconocedor de expresiones del cálculo proposicional
# Utiliza PLY (Python Lex-Yacc) y NetworkX

import sys
import os
import re
from analizador_lexico import analizar_lexicamente, lexer
from analizador_sintactico import analizar_sintacticamente, imprimir_arbol
from generador_grafos import visualizar_grafo, generar_reporte_grafo, exportar_grafo_dot
from automata_finito import crear_automata_alfabeto, visualizar_automata, generar_tabla_transiciones
from gramatica_sistema_L import (
    mostrar_gramatica_formal, 
    generar_ejemplos_derivaciones,
    mostrar_tabla_precedencia,
    validar_expresion_gramatica
)

def limpiar_nombre_archivo(expresion):
    """
    Limpia una expresión para usarla como nombre de archivo válido
    """
    # Reemplazar caracteres especiales por equivalentes seguros
    nombre = expresion.replace('(', 'par_izq_')
    nombre = nombre.replace(')', '_par_der')
    nombre = nombre.replace('=>', '_implica_')
    nombre = nombre.replace('<=>', '_bicondicional_')
    nombre = nombre.replace('^', '_y_')
    nombre = nombre.replace('o', '_o_')
    nombre = nombre.replace('~', 'no_')
    nombre = nombre.replace(' ', '_')
    
    # Remover caracteres no válidos para nombres de archivo
    nombre = re.sub(r'[<>:"/\\|?*]', '_', nombre)
    
    # Limitar la longitud del nombre
    if len(nombre) > 50:
        nombre = nombre[:50]
    
    return nombre

def mostrar_menu():
    """
    Muestra el menú principal del programa
    """
    menu = """
╔══════════════════════════════════════════════════════════════╗
║              SISTEMA AXIOMÁTICO L - MENÚ PRINCIPAL           ║
║              Reconocedor de Expresiones Proposicionales      ║
╠══════════════════════════════════════════════════════════════╣
║ 1. Analizar expresión completa                               ║
║ 2. Solo análisis léxico                                      ║
║ 3. Solo análisis sintáctico                                  ║
║ 4. Mostrar gramática del Sistema L                           ║
║ 5. Mostrar autómata finito del alfabeto                      ║
║ 6. Probar expresiones de ejemplo                             ║
║ 7. Validar múltiples expresiones                             ║
║ 8. Exportar grafo en formato DOT                             ║
║ 9. Mostrar ayuda                                              ║
║ 0. Salir                                                      ║
╚══════════════════════════════════════════════════════════════╝
"""
    print(menu)

def analizar_expresion_completa(expresion):
    """
    Realiza el análisis completo de una expresión
    """
    print(f"\n{'='*60}")
    print(f"ANÁLISIS COMPLETO DE: {expresion}")
    print(f"{'='*60}")
    
    # 1. Análisis Léxico
    print("\n1. ANÁLISIS LÉXICO:")
    print("-" * 30)
    tokens = analizar_lexicamente(expresion)
    if tokens:
        print("Tokens encontrados:")
        for i, (tipo, valor) in enumerate(tokens, 1):
            print(f"  {i:2d}. {tipo:12} -> '{valor}'")
    else:
        print("No se encontraron tokens válidos")
        return False
    
    # 2. Análisis Sintáctico
    print("\n2. ANÁLISIS SINTÁCTICO:")
    print("-" * 30)
    ast, grafo = analizar_sintacticamente(expresion)
    
    if ast is None:
        print("❌ Error en el análisis sintáctico")
        return False
    
    print("✅ Expresión sintácticamente correcta")
    print("\nÁrbol Sintáctico:")
    imprimir_arbol(ast)
    
    # 3. Generación del Grafo
    print("\n3. GRAFO DIRIGIDO:")
    print("-" * 30)
    if grafo:
        print(generar_reporte_grafo(grafo, expresion))
        
        # Preguntar si mostrar el grafo
        respuesta = input("\n¿Desea visualizar el grafo? (s/n): ").lower().strip()
        if respuesta in ['s', 'si', 'sí', 'y', 'yes']:
            try:
                nombre_archivo = f"grafo_{limpiar_nombre_archivo(expresion)}.png"
                visualizar_grafo(grafo, expresion, nombre_archivo)
            except Exception as e:
                print(f"Error al visualizar el grafo: {e}")
    else:
        print("❌ No se pudo generar el grafo")
        return False
    
    return True

def probar_expresiones_ejemplo():
    """
    Prueba las expresiones de ejemplo del proyecto
    """
    expresiones_ejemplo = [
        "p",
        "~~~q",
        "(p^q)",
        "(0=>(ros))",
        "~(p^q)",
        "(p<=>~p)",
        "((p=>q)^p)",
        "(~(p^(qor))os)"
    ]
    
    print("\n" + "="*60)
    print("PROBANDO EXPRESIONES DE EJEMPLO")
    print("="*60)
    
    resultados = []
    for i, expr in enumerate(expresiones_ejemplo, 1):
        print(f"\n{i}. Expresión: {expr}")
        print("-" * 40)
        
        # Análisis rápido
        ast, grafo = analizar_sintacticamente(expr)
        if ast:
            print("✅ Válida")
            if grafo:
                print(f"   Nodos en el grafo: {grafo.number_of_nodes()}")
                print(f"   Aristas en el grafo: {grafo.number_of_edges()}")
            resultados.append((expr, True))
        else:
            print("❌ Inválida")
            resultados.append((expr, False))
    
    # Resumen
    print(f"\n{'='*60}")
    print("RESUMEN DE RESULTADOS")
    print(f"{'='*60}")
    validas = sum(1 for _, valida in resultados if valida)
    print(f"Expresiones válidas: {validas}/{len(expresiones_ejemplo)}")
    
    for expr, valida in resultados:
        estado = "✅" if valida else "❌"
        print(f"{estado} {expr}")

def validar_multiples_expresiones():
    """
    Permite al usuario validar múltiples expresiones
    """
    print("\n" + "="*60)
    print("VALIDACIÓN DE MÚLTIPLES EXPRESIONES")
    print("="*60)
    print("Ingrese expresiones una por línea. Escriba 'fin' para terminar.")
    print("Ejemplos: p, ~q, (p^q), p=>q, etc.\n")
    
    expresiones = []
    while True:
        expr = input("Expresión: ").strip()
        if expr.lower() == 'fin':
            break
        if expr:
            expresiones.append(expr)
    
    if not expresiones:
        print("No se ingresaron expresiones.")
        return
    
    print(f"\n{'='*60}")
    print("RESULTADOS DE VALIDACIÓN")
    print(f"{'='*60}")
    
    for i, expr in enumerate(expresiones, 1):
        valida, mensaje = validar_expresion_gramatica(expr)
        estado = "✅" if valida else "❌"
        print(f"{i:2d}. {estado} {expr:20} - {mensaje}")

def mostrar_ayuda():
    """
    Muestra información de ayuda sobre el sistema
    """
    ayuda = """
╔══════════════════════════════════════════════════════════════╗
║                           AYUDA                              ║
╠══════════════════════════════════════════════════════════════╣
║ ALFABETO DEL SISTEMA L:                                      ║
║ • Variables: p, q, r, s, t, u, v, w, x, y, z                 ║
║ • Operadores: ~ (negación), ^ (conjunción), o (disyunción)  ║
║              => (implicación), <=> (bicondicional)           ║
║ • Paréntesis: ( )                                            ║
║ • Constantes: 0 (falso), 1 (verdadero)                      ║
║                                                              ║
║ PRECEDENCIA DE OPERADORES (mayor a menor):                  ║
║ 1. ~ (negación)                                              ║
║ 2. ^ (conjunción)                                            ║
║ 3. o (disyunción)                                            ║
║ 4. => (implicación)                                          ║
║ 5. <=> (bicondicional)                                       ║
║                                                              ║
║ EJEMPLOS VÁLIDOS:                                            ║
║ • p                                                          ║
║ • ~q                                                         ║
║ • (p^q)                                                      ║
║ • p=>q                                                       ║
║ • (p<=>~p)                                                   ║
║ • ((p=>q)^p)                                                 ║
║                                                              ║
║ ARCHIVOS GENERADOS:                                          ║
║ • grafo_[expresion].png - Visualización del grafo           ║
║ • automata_sistema_L.png - Diagrama del autómata            ║
║ • *.dot - Archivos en formato DOT para Graphviz             ║
╚══════════════════════════════════════════════════════════════╝
"""
    print(ayuda)

def main():
    """
    Función principal del programa
    """
    print("\n" + "="*60)
    print("PROYECTO DE LÓGICA MATEMÁTICA")
    print("Sistema Axiomático L - Reconocedor de Expresiones Proposicionales")
    print("Desarrollado con PLY (Python Lex-Yacc) y NetworkX")
    print("="*60)
    
    while True:
        mostrar_menu()
        
        try:
            opcion = input("\nSeleccione una opción (0-9): ").strip()
            
            if opcion == '0':
                print("\n¡Gracias por usar el Sistema Axiomático L!")
                break
            
            elif opcion == '1':
                expresion = input("\nIngrese la expresión a analizar: ").strip()
                if expresion:
                    analizar_expresion_completa(expresion)
                else:
                    print("❌ Debe ingresar una expresión")
            
            elif opcion == '2':
                expresion = input("\nIngrese la expresión para análisis léxico: ").strip()
                if expresion:
                    print(f"\nAnálisis léxico de: {expresion}")
                    tokens = analizar_lexicamente(expresion)
                    if tokens:
                        for i, (tipo, valor) in enumerate(tokens, 1):
                            print(f"  {i:2d}. {tipo:12} -> '{valor}'")
                    else:
                        print("No se encontraron tokens válidos")
            
            elif opcion == '3':
                expresion = input("\nIngrese la expresión para análisis sintáctico: ").strip()
                if expresion:
                    print(f"\nAnálisis sintáctico de: {expresion}")
                    ast, grafo = analizar_sintacticamente(expresion)
                    if ast:
                        print("✅ Expresión sintácticamente correcta")
                        print("\nÁrbol sintáctico:")
                        imprimir_arbol(ast)
                    else:
                        print("❌ Error en el análisis sintáctico")
            
            elif opcion == '4':
                print(mostrar_gramatica_formal())
                print(generar_ejemplos_derivaciones())
                print(mostrar_tabla_precedencia())
            
            elif opcion == '5':
                print("\nGenerando autómata finito del alfabeto...")
                automata, estados = crear_automata_alfabeto()
                generar_tabla_transiciones(automata)
                
                respuesta = input("\n¿Desea visualizar el autómata? (s/n): ").lower().strip()
                if respuesta in ['s', 'si', 'sí', 'y', 'yes']:
                    try:
                        visualizar_automata(automata, estados, "automata_sistema_L.png")
                    except Exception as e:
                        print(f"Error al visualizar el autómata: {e}")
            
            elif opcion == '6':
                probar_expresiones_ejemplo()
            
            elif opcion == '7':
                validar_multiples_expresiones()
            
            elif opcion == '8':
                expresion = input("\nIngrese la expresión para exportar: ").strip()
                if expresion:
                    ast, grafo = analizar_sintacticamente(expresion)
                    if grafo:
                        archivo = f"grafo_{limpiar_nombre_archivo(expresion)}.dot"
                        exportar_grafo_dot(grafo, expresion, archivo)
                    else:
                        print("❌ No se pudo generar el grafo")
            
            elif opcion == '9':
                mostrar_ayuda()
            
            else:
                print("❌ Opción inválida. Seleccione un número del 0 al 9.")
        
        except KeyboardInterrupt:
            print("\n\nPrograma interrumpido por el usuario.")
            break
        except Exception as e:
            print(f"❌ Error inesperado: {e}")
        
        input("\nPresione Enter para continuar...")

if __name__ == "__main__":
    main()