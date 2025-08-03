# Generador de Grafos Dirigidos para Expresiones del Sistema L
# Utiliza NetworkX para crear y visualizar grafos

import hashlib
import networkx as nx
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.patches import FancyBboxPatch

def crear_grafo_expresion(ast, grafo_nx):
    """
    Crea un grafo dirigido a partir del árbol sintáctico
    """
    if grafo_nx is None:
        return None
    
    return grafo_nx

def visualizar_grafo(grafo, expresion, guardar_archivo=None):
    """
    Visualiza el grafo dirigido usando matplotlib
    """
    if grafo is None or len(grafo.nodes()) == 0:
        print("No hay grafo para visualizar")
        return
    
    # Configurar el layout del grafo de forma determinística
    # Usar un seed basado en la expresión para consistencia
    seed = int(hashlib.md5(expresion.encode()).hexdigest()[:8], 16) % (2**32)
    pos = nx.spring_layout(grafo, k=2, iterations=50, seed=seed)
    
    # Crear la figura
    plt.figure(figsize=(12, 8))
    plt.title(f"Grafo Dirigido de la Expresión: {expresion}", fontsize=14, fontweight='bold')
    
    # Dibujar las aristas con espacio entre flecha y nodo
    nx.draw_networkx_edges(grafo, pos, 
                          edge_color='black', 
                          arrows=True, 
                          arrowsize=20, 
                          arrowstyle='->', 
                          width=2,
                          alpha=0.7,
                          connectionstyle="arc3,rad=0.1",
                          min_source_margin=15,
                          min_target_margin=15)
    
    # Obtener las etiquetas de los nodos
    labels = nx.get_node_attributes(grafo, 'label')
    tipos = nx.get_node_attributes(grafo, 'tipo')
    
    # Definir colores según el tipo de nodo
    colores_nodos = []
    for nodo in grafo.nodes():
        tipo = tipos.get(nodo, 'UNKNOWN')
        if tipo == 'VARIABLE':
            colores_nodos.append('#87CEEB')  # Azul claro
        elif tipo == 'CONSTANTE':
            colores_nodos.append('#98FB98')  # Verde claro
        elif tipo in ['NEGACION', 'CONJUNCION', 'DISYUNCION', 'IMPLICACION', 'BICONDICIONAL']:
            colores_nodos.append('#FFB6C1')  # Rosa claro
        else:
            colores_nodos.append('#D3D3D3')  # Gris claro
    
    # Dibujar los nodos
    nx.draw_networkx_nodes(grafo, pos, 
                          node_color=colores_nodos, 
                          node_size=1500, 
                          alpha=0.9,
                          edgecolors='black',
                          linewidths=2)
    
    # Dibujar las etiquetas de los nodos
    nx.draw_networkx_labels(grafo, pos, labels, 
                           font_size=12, 
                           font_weight='bold',
                           font_color='black')
    
    # Agregar leyenda
    legend_elements = [
        patches.Patch(color='#87CEEB', label='Variables'),
        patches.Patch(color='#98FB98', label='Constantes'),
        patches.Patch(color='#FFB6C1', label='Operadores')
    ]
    plt.legend(handles=legend_elements, loc='upper right')
    
    # Configurar el gráfico
    plt.axis('off')
    plt.tight_layout()
    
    # Guardar o mostrar
    if guardar_archivo:
        plt.savefig(guardar_archivo, dpi=300, bbox_inches='tight')
        print(f"Grafo guardado en: {guardar_archivo}")
    
    plt.show()

def generar_reporte_grafo(grafo, expresion):
    """
    Genera un reporte detallado del grafo
    """
    if grafo is None:
        return "No hay grafo para reportar"
    
    reporte = f"\n=== REPORTE DEL GRAFO ===\n"
    reporte += f"Expresión analizada: {expresion}\n"
    reporte += f"Número de nodos: {grafo.number_of_nodes()}\n"
    reporte += f"Número de aristas: {grafo.number_of_edges()}\n\n"
    
    reporte += "Nodos del grafo:\n"
    for nodo, datos in grafo.nodes(data=True):
        etiqueta = datos.get('label', 'Sin etiqueta')
        tipo = datos.get('tipo', 'Sin tipo')
        reporte += f"  Nodo {nodo}: {etiqueta} (Tipo: {tipo})\n"
    
    reporte += "\nAristas del grafo (Padre -> Hijo):\n"
    for padre, hijo in grafo.edges():
        etiqueta_padre = grafo.nodes[padre].get('label', padre)
        etiqueta_hijo = grafo.nodes[hijo].get('label', hijo)
        reporte += f"  {etiqueta_padre} -> {etiqueta_hijo}\n"
    
    return reporte

def exportar_grafo_dot(grafo, expresion, archivo):
    """
    Exporta el grafo en formato DOT para Graphviz
    """
    if grafo is None:
        return
    
    with open(archivo, 'w', encoding='utf-8') as f:
        f.write(f"// Grafo dirigido para la expresión: {expresion}\n")
        f.write("digraph G {\n")
        f.write("  rankdir=TB;\n")
        f.write("  node [shape=circle, style=filled];\n\n")
        
        # Escribir nodos
        for nodo, datos in grafo.nodes(data=True):
            etiqueta = datos.get('label', str(nodo))
            tipo = datos.get('tipo', 'UNKNOWN')
            
            # Asignar colores según el tipo
            if tipo == 'VARIABLE':
                color = 'lightblue'
            elif tipo == 'CONSTANTE':
                color = 'lightgreen'
            else:
                color = 'lightpink'
            
            f.write(f'  {nodo} [label="{etiqueta}", fillcolor={color}];\n')
        
        f.write("\n")
        
        # Escribir aristas
        for padre, hijo in grafo.edges():
            f.write(f"  {padre} -> {hijo};\n")
        
        f.write("}\n")
    
    print(f"Grafo exportado en formato DOT: {archivo}")

if __name__ == "__main__":
    # Ejemplo de uso
    from analizador_sintactico import analizar_sintacticamente
    
    expresion = "((p=>q)^p)"
    print(f"Analizando expresión: {expresion}")
    
    ast, grafo = analizar_sintacticamente(expresion)
    if grafo:
        print(generar_reporte_grafo(grafo, expresion))
        visualizar_grafo(grafo, expresion)
    else:
        print("Error al generar el grafo")