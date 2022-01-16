# Wyświetla graf utworzony w funkcji createTestGraph() w oknie graficznym.

from graphviz import Digraph

from production import *
from vertex import *
from graphParser import *


# Zamienia tablice obiektow vertex na graf w formacie .gv
def graphFromVertexList(vertexList, dpi = 150, size = 2):
    keys = vertexList.keys()
    graph = Digraph(name = "TemporaryGraph")
    
    for v in keys:
        graph.node(str(vertexList[v].index), str(vertexList[v].label))
        
    for v in keys:
        for e in vertexList[v].edges:
            graph.edge(str(vertexList[v].index), str(e))

    graph.graph_attr['dpi']=str(dpi) # poprawa rozdzielczosci
    graph.graph_attr['size']=str(size) # dopasowanie maxymalnego wymiaru
    return graph
        
# Tworzy plik .gif na podstawie grafu w formacie .gv
def generateGraphImage(graph, fileName):
    graph.render(filename=fileName, format="gif", view=False)

# Zamienia tablice vertex na gif
def verticeArrayToGif(verticeArray, gifName, dpi = 150, size = 2):
    graph = graphFromVertexList(verticeArray, dpi, size)
    generateGraphImage(graph, gifName)

# Zamienia produkcje na dwa gif'y prawej i lewej strony
def productionToGif(production, leftGraphName, rightGraphName):
    verticeArrayToGif(production.left, leftGraphName)
    verticeArrayToGif(production.right, rightGraphName)
    

# Zamienia plik tekstowy z grafem jako txt na plik gif
def textFormGraphToGif(inputTextFileName, outputGifName):
    vertexList = parse_initial_graph(inputTextFileName)
    graph = graphFromVertexList(vertexList)
    generateGraphImage(graph, outputGifName)


    
