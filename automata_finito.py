# Diagrama de Autómata Finito para el Alfabeto del Sistema L
# Reconoce el alfabeto: variables, operadores, paréntesis y constantes

import networkx as nx
import matplotlib.pyplot as plt
import matplotlib.patches as patches

def crear_automata_alfabeto():
    """
    Crea el autómata finito para reconocer el alfabeto del sistema L
    """
    # Crear grafo dirigido
    automata = nx.DiGraph()
    
    # Estados del autómata
    estados = {
        'q0': 'Estado Inicial',
        'q1': 'Variable/Constante',
        'q2': 'Negación',
        'q3': 'Conjunción',
        'q4': 'Disyunción',
        'q5': 'Paréntesis Izq',
        'q6': 'Paréntesis Der',
        'q7': 'Igual (=)',
        'q8': 'Implicación (=>)',
        'q9': 'Menor (<)',
        'q10': 'Bicondicional (<=>)',
        'qf': 'Estado Final'
    }
    
    # Agregar nodos
    for estado, descripcion in estados.items():
        automata.add_node(estado, label=estado, descripcion=descripcion)
    
    # Transiciones del autómata
    transiciones = [
        # Desde estado inicial
        ('q0', 'q1', 'p,q,r,s,t,u,v,w,x,y,z'),  # Variables
        ('q0', 'q1', '0,1'),                      # Constantes
        ('q0', 'q2', '~'),                        # Negación
        ('q0', 'q3', '^'),                        # Conjunción
        ('q0', 'q4', 'o'),                        # Disyunción
        ('q0', 'q5', '('),                        # Paréntesis izquierdo
        ('q0', 'q6', ')'),                        # Paréntesis derecho
        ('q0', 'q7', '='),                        # Inicio de implicación
        ('q0', 'q9', '<'),                        # Inicio de bicondicional
        
        # Desde q7 (después de '=')
        ('q7', 'q8', '>'),                        # Completar implicación '=>'
        
        # Desde q9 (después de '<')
        ('q9', 'q7', '='),                        # Ir a '=' para formar '<=>'
        
        # Desde q8 (implicación completa)
        ('q8', 'qf', 'ε'),                        # Aceptar implicación
        
        # Completar bicondicional desde q7 cuando viene de q9
        ('q7', 'q10', '> (desde <)'),             # Completar bicondicional
        ('q10', 'qf', 'ε'),                       # Aceptar bicondicional
        
        # Estados finales para tokens simples
        ('q1', 'qf', 'ε'),                        # Variables y constantes
        ('q2', 'qf', 'ε'),                        # Negación
        ('q3', 'qf', 'ε'),                        # Conjunción
        ('q4', 'qf', 'ε'),                        # Disyunción
        ('q5', 'qf', 'ε'),                        # Paréntesis izquierdo
        ('q6', 'qf', 'ε'),                        # Paréntesis derecho
    ]
    
    # Agregar aristas
    for origen, destino, simbolo in transiciones:
        automata.add_edge(origen, destino, label=simbolo)
    
    return automata, estados

def visualizar_automata(automata, estados, guardar_archivo=None):
    """
    Visualiza el autómata finito
    """
    plt.figure(figsize=(16, 12))
    plt.title("Autómata Finito para el Alfabeto del Sistema L", fontsize=16, fontweight='bold')
    
    # Layout del grafo
    pos = nx.spring_layout(automata, k=3, iterations=100, seed=42)
    
    # Ajustar posiciones manualmente para mejor visualización
    pos_ajustadas = {
        'q0': (0, 0),
        'q1': (-2, 2),
        'q2': (-2, 1),
        'q3': (-2, 0),
        'q4': (-2, -1),
        'q5': (-2, -2),
        'q6': (0, -2),
        'q7': (2, 0),
        'q8': (4, 1),
        'q9': (2, -1),
        'q10': (4, -1),
        'qf': (6, 0)
    }
    
    # Usar posiciones ajustadas si están disponibles
    for nodo in automata.nodes():
        if nodo in pos_ajustadas:
            pos[nodo] = pos_ajustadas[nodo]
    
    # Colores para diferentes tipos de estados
    colores_nodos = []
    for nodo in automata.nodes():
        if nodo == 'q0':
            colores_nodos.append('#90EE90')  # Verde claro para inicial
        elif nodo == 'qf':
            colores_nodos.append('#FFB6C1')  # Rosa para final
        else:
            colores_nodos.append('#87CEEB')  # Azul claro para intermedios
    
    # Dibujar nodos
    nx.draw_networkx_nodes(automata, pos,
                          node_color=colores_nodos,
                          node_size=2000,
                          alpha=0.9,
                          edgecolors='black',
                          linewidths=2)
    
    # Dibujar etiquetas de nodos
    labels = {nodo: nodo for nodo in automata.nodes()}
    nx.draw_networkx_labels(automata, pos, labels,
                           font_size=12,
                           font_weight='bold')
    
    # Dibujar aristas
    nx.draw_networkx_edges(automata, pos,
                          edge_color='black',
                          arrows=True,
                          arrowsize=20,
                          arrowstyle='->',
                          width=1.5,
                          alpha=0.7,
                          connectionstyle="arc3,rad=0.1")
    
    # Dibujar etiquetas de aristas
    edge_labels = nx.get_edge_attributes(automata, 'label')
    # Simplificar etiquetas largas
    edge_labels_simple = {}
    for edge, label in edge_labels.items():
        if len(label) > 15:
            edge_labels_simple[edge] = label[:12] + "..."
        else:
            edge_labels_simple[edge] = label
    
    nx.draw_networkx_edge_labels(automata, pos, edge_labels_simple,
                                font_size=8,
                                bbox=dict(boxstyle="round,pad=0.2", facecolor="white", alpha=0.8))
    
    # Agregar leyenda
    legend_elements = [
        patches.Patch(color='#90EE90', label='Estado Inicial'),
        patches.Patch(color='#87CEEB', label='Estados Intermedios'),
        patches.Patch(color='#FFB6C1', label='Estado Final')
    ]
    plt.legend(handles=legend_elements, loc='upper left')
    
    # Agregar descripción
    descripcion = (
        "Alfabeto del Sistema L:\n"
        "• Variables: p,q,r,s,t,u,v,w,x,y,z\n"
        "• Operadores: ~, ^, o, =>, <=>\n"
        "• Paréntesis: (, )\n"
        "• Constantes: 0, 1"
    )
    
    plt.text(0.02, 0.98, descripcion, transform=plt.gca().transAxes,
             fontsize=10, verticalalignment='top',
             bbox=dict(boxstyle="round,pad=0.5", facecolor="lightyellow", alpha=0.8))
    
    plt.axis('off')
    plt.tight_layout()
    
    if guardar_archivo:
        plt.savefig(guardar_archivo, dpi=300, bbox_inches='tight')
        print(f"Diagrama del autómata guardado en: {guardar_archivo}")
    
    plt.show()

def generar_tabla_transiciones(automata):
    """
    Genera la tabla de transiciones del autómata
    """
    print("\n=== TABLA DE TRANSICIONES DEL AUTÓMATA ===")
    print("Estado Origen -> Estado Destino [Símbolo]")
    print("-" * 50)
    
    for origen, destino, datos in automata.edges(data=True):
        simbolo = datos.get('label', 'ε')
        print(f"{origen:>10} -> {destino:<10} [{simbolo}]")

def exportar_automata_dot(automata, archivo):
    """
    Exporta el autómata en formato DOT
    """
    with open(archivo, 'w', encoding='utf-8') as f:
        f.write("// Autómata Finito para el Alfabeto del Sistema L\n")
        f.write("digraph Automata {\n")
        f.write("  rankdir=LR;\n")
        f.write("  node [shape=circle];\n")
        f.write("  q0 [shape=circle, style=filled, fillcolor=lightgreen];\n")
        f.write("  qf [shape=doublecircle, style=filled, fillcolor=lightpink];\n\n")
        
        # Escribir transiciones
        for origen, destino, datos in automata.edges(data=True):
            simbolo = datos.get('label', 'ε')
            f.write(f'  {origen} -> {destino} [label="{simbolo}"];\n')
        
        f.write("}\n")
    
    print(f"Autómata exportado en formato DOT: {archivo}")

if __name__ == "__main__":
    print("=== AUTÓMATA FINITO PARA EL ALFABETO DEL SISTEMA L ===")
    
    # Crear y visualizar el autómata
    automata, estados = crear_automata_alfabeto()
    
    print(f"\nEstados del autómata: {len(estados)}")
    for estado, desc in estados.items():
        print(f"  {estado}: {desc}")
    
    # Mostrar tabla de transiciones
    generar_tabla_transiciones(automata)
    
    # Visualizar el autómata
    visualizar_automata(automata, estados, "automata_sistema_L.png")
    
    # Exportar en formato DOT
    exportar_automata_dot(automata, "automata_sistema_L.dot")