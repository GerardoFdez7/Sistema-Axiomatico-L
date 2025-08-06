#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script de Demostración para la Presentación
Sistema Axiomático L - Reconocedor de Expresiones Proposicionales

Este script ejecuta demostraciones organizadas para cada sección de la presentación.
"""

import sys
import time
from analizador_lexico import analizar_lexicamente
from analizador_sintactico import analizar_sintacticamente, imprimir_arbol
from generador_grafos import visualizar_grafo, generar_reporte_grafo, exportar_grafo_dot
from automata_finito import crear_automata_alfabeto, generar_tabla_transiciones
from gramatica_sistema_L import mostrar_gramatica_formal
from main import limpiar_nombre_archivo

def pausa(mensaje="Presiona Enter para continuar..."):
    """Pausa la ejecución para permitir explicaciones"""
    input(f"\n{mensaje}")

def separador(titulo):
    """Imprime un separador visual"""
    print("\n" + "="*60)
    print(f"  {titulo}")
    print("="*60)

def demo_introduccion():
    """Demostración para Alex - Introducción"""
    separador("DEMO 1: INTRODUCCIÓN AL SISTEMA")
    
    print("\n🎯 OBJETIVO DEL PROYECTO:")
    print("   Reconocedor completo de expresiones del cálculo proposicional")
    
    print("\n📚 ALFABETO DEL SISTEMA L:")
    print("   • Variables: p, q, r, s, t, u, v, w, x, y, z")
    print("   • Operadores: ~, ^, o, =>, <=>")
    print("   • Paréntesis: ( )")
    print("   • Constantes: 0, 1")
    
    print("\n🛠️ TECNOLOGÍAS UTILIZADAS:")
    print("   • Python 3.x")
    print("   • PLY (Python Lex-Yacc) - Análisis léxico y sintáctico")
    print("   • NetworkX - Generación de grafos")
    print("   • Matplotlib - Visualización")
    
    print("\n✨ FUNCIONALIDADES PRINCIPALES:")
    print("   1. Análisis léxico (tokenización)")
    print("   2. Análisis sintáctico (validación gramatical)")
    print("   3. Generación de grafos dirigidos")
    print("   4. Visualización de autómatas finitos")
    
    pausa("Alex: Explica el contexto y objetivos...")

def demo_analisis_lexico():
    """Demostración para Juan Diego - Análisis Léxico"""
    separador("DEMO 2: ANÁLISIS LÉXICO")
    
    expresiones_demo = [
        "p",
        "(p^q)",
        "p=>q",
        "(p<=>~r)"
    ]
    
    print("\n🔍 TOKENIZACIÓN DE EXPRESIONES:")
    print("\nEl analizador léxico convierte texto en tokens...")
    
    for expr in expresiones_demo:
        print(f"\n📝 Expresión: '{expr}'")
        tokens = analizar_lexicamente(expr)
        print("   Tokens generados:")
        for i, (tipo, valor) in enumerate(tokens, 1):
            print(f"      {i}. {tipo:12} -> '{valor}'")
        
        if expr != expresiones_demo[-1]:
            pausa("Continuar con siguiente expresión...")
    
    print("\n💡 CARACTERÍSTICAS DEL ANALIZADOR LÉXICO:")
    print("   • Reconoce operadores multi-carácter (=>, <=>)")
    print("   • Valida caracteres del alfabeto")
    print("   • Detecta errores léxicos")
    print("   • Genera secuencia de tokens para análisis sintáctico")
    
    pausa("Juan Diego: Explica el proceso de tokenización...")

def demo_analisis_sintactico():
    """Demostración para Diego - Análisis Sintáctico"""
    separador("DEMO 3: ANÁLISIS SINTÁCTICO")
    
    expresion_demo = "((p=>q)^p)"
    
    print(f"\n🌳 ANÁLISIS SINTÁCTICO DE: '{expresion_demo}'")
    print("\nLa gramática del Sistema L define 9 producciones:")
    print("   P1: F → E")
    print("   P2: E → VARIABLE")
    print("   P3: E → CONSTANTE")
    print("   P4: E → ~ E")
    print("   P5: E → E ^ E")
    print("   P6: E → E o E")
    print("   P7: E → E => E")
    print("   P8: E → E <=> E")
    print("   P9: E → ( E )")
    
    pausa("Continuar con análisis...")
    
    print(f"\n🔍 Analizando '{expresion_demo}'...")
    ast, grafo = analizar_sintacticamente(expresion_demo)
    
    if ast:
        print("\n✅ Expresión VÁLIDA")
        print("\n📊 ÁRBOL SINTÁCTICO GENERADO:")
        imprimir_arbol(ast)
        
        print("\n📈 PRECEDENCIA DE OPERADORES (mayor a menor):")
        print("   1. ~ (negación)")
        print("   2. ^ (conjunción)")
        print("   3. o (disyunción)")
        print("   4. => (implicación)")
        print("   5. <=> (bicondicional)")
    else:
        print("\n❌ Error en el análisis sintáctico")
    
    pausa("Diego: Explica la gramática y el AST...")

def demo_grafos():
    """Demostración para Gerardo - Generación de Grafos"""
    separador("DEMO 4: GENERACIÓN Y VISUALIZACIÓN DE GRAFOS")
    
    expresion_demo = "(p^~q)"
    
    print(f"\n📊 GENERACIÓN DE GRAFO PARA: '{expresion_demo}'")
    
    ast, grafo = analizar_sintacticamente(expresion_demo)
    
    if grafo:
        print("\n✅ Grafo generado exitosamente")
        
        # Mostrar reporte del grafo
        reporte = generar_reporte_grafo(grafo, expresion_demo)
        print(reporte)
        
        print("\n🎨 CARACTERÍSTICAS DE VISUALIZACIÓN:")
        print("   • Nodos coloreados por tipo:")
        print("     - Azul claro: Variables (p, q, r, ...)")
        print("     - Verde claro: Constantes (0, 1)")
        print("     - Rosa claro: Operadores (~, ^, o, =>, <=>)")
        print("   • Aristas direccionales con espaciado optimizado")
        print("   • Layout determinístico (mismo resultado siempre)")
        print("   • Leyenda explicativa")
        
        pausa("¿Generar visualización del grafo? (Enter para sí)")
        
        try:
            nombre_archivo = f"demo_grafo_{limpiar_nombre_archivo(expresion_demo)}.png"
            visualizar_grafo(grafo, expresion_demo, nombre_archivo)
            print(f"\n💾 Grafo guardado como: {nombre_archivo}")
        except Exception as e:
            print(f"\n⚠️ Error al visualizar: {e}")
        
        # Exportar a DOT
        try:
            archivo_dot = f"demo_grafo_{limpiar_nombre_archivo(expresion_demo)}.dot"
            exportar_grafo_dot(grafo, expresion_demo, archivo_dot)
            print(f"\n💾 Archivo DOT generado: {archivo_dot}")
        except Exception as e:
            print(f"\n⚠️ Error al exportar DOT: {e}")
    
    pausa("Gerardo: Explica la visualización...")

def demo_automata():
    """Demostración para Juarez - Autómata Finito"""
    separador("DEMO 5: AUTÓMATA FINITO")
    
    print("\n🤖 AUTÓMATA FINITO PARA EL ALFABETO DEL SISTEMA L")
    print("\nEl autómata reconoce todos los símbolos válidos del alfabeto:")
    
    # Crear el autómata
    automata, estados = crear_automata_alfabeto()
    
    print(f"\n📊 ESTADOS DEL AUTÓMATA ({len(estados)} estados):")
    for estado, descripcion in estados.items():
        print(f"   {estado}: {descripcion}")
    
    pausa("Continuar con tabla de transiciones...")
    
    print("\n🔄 TABLA DE TRANSICIONES:")
    generar_tabla_transiciones(automata)
    
    print("\n💡 CARACTERÍSTICAS DEL AUTÓMATA:")
    print("   • AFD (Autómata Finito Determinista)")
    print("   • Reconoce operadores multi-carácter")
    print("   • Maneja todos los símbolos del alfabeto")
    print("   • Base teórica para el análisis léxico")
    
    print("\n🎯 EJEMPLO DE RECONOCIMIENTO:")
    print("   Para reconocer '=>':")
    print("   q0 --[=]--> q7 --[>]--> q8 --[ε]--> qf")
    
    pausa("Juarez: Explica el autómata y las transiciones...")

def demo_interfaz():
    """Demostración para Jose - Interfaz y Funcionalidades"""
    separador("DEMO 6: INTERFAZ Y FUNCIONALIDADES")
    
    print("\n🖥️ INTERFAZ DE USUARIO DEL SISTEMA")
    print("\nEl sistema ofrece un menú interactivo con 9 opciones:")
    print("\n   1. 🔍 Analizar expresión completa")
    print("   2. 📝 Solo análisis léxico")
    print("   3. 🌳 Solo análisis sintáctico")
    print("   4. 📚 Mostrar gramática del Sistema L")
    print("   5. 🤖 Mostrar autómata finito del alfabeto")
    print("   6. 🧪 Probar expresiones de ejemplo")
    print("   7. ✅ Validar múltiples expresiones")
    print("   8. 💾 Exportar grafo en formato DOT")
    print("   9. ❓ Mostrar ayuda")
    print("   0. 🚪 Salir")
    
    pausa("Continuar con demostración de validación...")
    
    print("\n🧪 DEMOSTRACIÓN: VALIDACIÓN DE EXPRESIONES")
    
    expresiones_test = [
        ("p", "Variable simple"),
        ("(p^q)", "Conjunción con paréntesis"),
        ("((p=>q)^p)", "Expresión compleja anidada"),
        ("p&q", "Expresión inválida (operador no reconocido)"),
        ("(p^", "Expresión incompleta")
    ]
    
    print("\nValidando expresiones de ejemplo:")
    for expr, descripcion in expresiones_test:
        try:
            ast, grafo = analizar_sintacticamente(expr)
            estado = "✅" if ast else "❌"
            print(f"   {estado} {expr:15} - {descripcion}")
        except:
            print(f"   ❌ {expr:15} - {descripcion}")
    
    print("\n🎯 CARACTERÍSTICAS DE LA INTERFAZ:")
    print("   • Menú intuitivo y organizado")
    print("   • Validación de entrada del usuario")
    print("   • Manejo robusto de errores")
    print("   • Retroalimentación visual clara")
    print("   • Exportación en múltiples formatos")
    print("   • Casos de prueba predefinidos")
    
    pausa("Jose: Explica la interfaz y funcionalidades...")

def demo_completo():
    """Ejecuta toda la demostración"""
    print("🎓 DEMOSTRACIÓN COMPLETA DEL SISTEMA AXIOMÁTICO L")
    print("   Reconocedor de Expresiones Proposicionales")
    print("\n👥 Presentadores:")
    print("   • Alex - Introducción")
    print("   • Juan Diego - Análisis Léxico")
    print("   • Diego - Análisis Sintáctico")
    print("   • Gerardo - Generación de Grafos")
    print("   • Juarez - Autómata Finito")
    print("   • Jose - Interfaz y Funcionalidades")
    
    pausa("Comenzar demostración...")
    
    # Ejecutar cada demo
    demo_introduccion()
    demo_analisis_lexico()
    demo_analisis_sintactico()
    demo_grafos()
    demo_automata()
    demo_interfaz()
    
    separador("CONCLUSIÓN")
    print("\n🎉 DEMOSTRACIÓN COMPLETADA")
    print("\n✨ El Sistema Axiomático L demuestra la integración de:")
    print("   • Teoría de autómatas y lenguajes formales")
    print("   • Técnicas de análisis léxico y sintáctico")
    print("   • Visualización de estructuras de datos")
    print("   • Aplicación práctica de conceptos teóricos")
    
    print("\n🙏 ¡Gracias por su atención!")
    print("\n❓ ¿Preguntas?")

def menu_demo():
    """Menú para seleccionar demostraciones individuales"""
    while True:
        print("\n" + "="*50)
        print("  MENÚ DE DEMOSTRACIONES")
        print("="*50)
        print("1. Demo completa (todas las secciones)")
        print("2. Introducción (Alex)")
        print("3. Análisis Léxico (Juan Diego)")
        print("4. Análisis Sintáctico (Diego)")
        print("5. Generación de Grafos (Gerardo)")
        print("6. Autómata Finito (Juarez)")
        print("7. Interfaz y Funcionalidades (Jose)")
        print("0. Salir")
        
        opcion = input("\nSeleccione una opción: ").strip()
        
        if opcion == '0':
            print("\n¡Hasta luego!")
            break
        elif opcion == '1':
            demo_completo()
        elif opcion == '2':
            demo_introduccion()
        elif opcion == '3':
            demo_analisis_lexico()
        elif opcion == '4':
            demo_analisis_sintactico()
        elif opcion == '5':
            demo_grafos()
        elif opcion == '6':
            demo_automata()
        elif opcion == '7':
            demo_interfaz()
        else:
            print("\n❌ Opción inválida")

if __name__ == "__main__":
    try:
        menu_demo()
    except KeyboardInterrupt:
        print("\n\n🛑 Demostración interrumpida")
    except Exception as e:
        print(f"\n❌ Error durante la demostración: {e}")