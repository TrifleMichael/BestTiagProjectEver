# Wyświetla graf utworzony w funkcji createTestGraph() w oknie graficznym.

from graphviz import Digraph

from production import *
from vertex import *
from parserer import *


# Zamienia tablice obiektow vertex na graf w formacie .dot
def graphFromVertexList(vertexList):
    graph = Digraph(name = "TemporaryGraph")
    
    for v in vertexList:
        graph.node(str(v.index), str(v.label))
        
    for v in vertexList:
        for e in v.edges:
            graph.edge(str(v.index), str(e.index))

    graph.graph_attr['dpi']='200' # poprawa rozdzielczosci
    return graph
        
# Tworzy plik .gif na podstawie grafu w formacie .dot lub .gv
def generateGraphImage(graph, fileName):
    graph.render(filename=fileName, format="gif", view=False)


# Zamienia plik tekstowy z graf jako txt na plik gif
def textFormGraphToGif(inputTextFileName, outputGifName):
    vertexList = parse_graph(inputTextFileName)
    graph = graphFromVertexList(vertexList)
    generateGraphImage(graph, outputGifName)


    
