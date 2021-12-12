# Wyświetla graf utworzony w funkcji createTestGraph() w oknie graficznym.

from graphviz import Digraph
from appJar import gui

# Funkcja do testowania, tymczasowa
def createTestGraph():
    graph = Digraph(name="TemporaryGraph")

    graph.node('A', 'Ziemniak')
    graph.node('B', 'Frytki')
    graph.node('C', 'Chipsy')
    graph.edges(['AB', 'AC'])

    graph.graph_attr['dpi']='400'
    return graph

# Tworzy plik .gif na podstawie grafu w formacie .dot lub .gv
# (czyli domyślnych formatów graphviz, takie jak tworzy funkcja createTestGraph powyżej)
def generateGraphImage(graph, fileName):
    print(graph.source)
    graph.render(filename=fileName, format="gif", view=False)


# Tworzy okno aplikacji i wyświetla pierwszy graf
def runApp(graphName):
    # create a GUI variable called app
    app = gui()

    # add & configure widgets - widgets get a name, to help referencing them later
    app.addLabel("title", "Tymczasowy tytuł grafu")
    app.setLabelBg("title", "grey")
    app.addImage("Graf", graphName)

    # start the GUI
    app.go()
    return app


# Główna funkcja testująca
def TheMainestMain():
    graph = createTestGraph()
    generateGraphImage(graph, "a")
    APP = runApp("a.gif")

TheMainestMain()
