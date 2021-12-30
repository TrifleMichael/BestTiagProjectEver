# Wyświetla graf utworzony w funkcji createTestGraph() w oknie graficznym.

from graphviz import Digraph

from production import *
from vertex import *
from graphParser import *


# Zamienia tablice obiektow vertex na graf w formacie .gv
def graphFromVertexList(vertexList):
    graph = Digraph(name = "TemporaryGraph")
    
    for v in vertexList:
        graph.node(str(v.index), str(v.label))
        
    for v in vertexList:
        for e in v.edges:
            graph.edge(str(v.index), str(e.index))

    graph.graph_attr['dpi']='200' # poprawa rozdzielczosci
    graph.graph_attr['size']='2' # dopasowanie maxymalnego wymiaru
    return graph
        
# Tworzy plik .gif na podstawie grafu w formacie .gv
def generateGraphImage(graph, fileName):
    graph.render(filename=fileName, format="gif", view=False)

# Zamienia tablice vertex na gif
def verticeArrayToGif(verticeArray, gifName):
    graph = graphFromVertexList(verticeArray)
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


    
