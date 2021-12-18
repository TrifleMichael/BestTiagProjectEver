# Wyświetla graf utworzony w funkcji createTestGraph() w oknie graficznym.

from graphviz import Digraph
from appJar import gui

from os import remove

from production import *
from vertex import *
from graphParser import *
from GUIFormatter import *


# Główny obiekt GUI
APP = gui("Single Push Out Visualisation") #, "800x800"

# Funkcja przycisku
def changeImageButtonFunction():
    imageName = APP.getEntry("ImageName")
    print("Loading image", imageName)
    APP.reloadImage("MainImage", imageName)

# Funkcja przycisku
def changeGraphButtonFunction():
    graphName = APP.getEntry("GraphInputName")
    print("Interpreting graph")
    textFormGraphToGif(graphName, "TemporaryGraph")
    APP.reloadImage("MainImage", "TemporaryGraph.gif")


def testShowProduction():
    graph1 = textFormGraphToGif("pl.txt", "PL")    
    graph2 = textFormGraphToGif("pr.txt", "PR")
    APP.reloadImage("ProductionLeft", "PL.gif")
    APP.reloadImage("ProductionRight", "PR.gif")

    
# parsing danych

initialVerticies, productions, productionIndicies = parse("./data/initial_graph.txt", "./data/productions.txt", "./data/productions_order.txt")

# graf początkowy
verticeArrayToGif(initialVerticies, "InitialGraphImage")
APP.addImage("MainImage", "InitialGraphImage.gif", 0, 0)

# produkcje
productionToGif(productions[0], "leftTest", "rightTest")
APP.addImage("ProductionLeft1", "leftTest.gif", 0, 1)
APP.addImage("ArrowImage1", "arrow.gif", 0, 2)
APP.addImage("ProductionRight1", "rightTest.gif", 0, 3)


productionToGif(productions[1], "leftTest", "rightTest")
APP.addImage("ProductionLeft2", "leftTest.gif", 1, 1)
APP.addImage("ArrowImage2", "arrow.gif", 1, 2)
APP.addImage("ProductionRight2", "rightTest.gif", 1, 3)

# przyciski

APP.addButton("Wpisz nazwę pliku z grafem a następnie naciśnij ten przycisk", changeGraphButtonFunction, 2, 0)
APP.addEntry("GraphInputName", 2, 1)

APP.addButton("(Work in progress) wybierz numer produkcji i wciśnij ten przycisk", testShowProduction, 3, 0)
APP.addEntry("ProductionInputName", 3, 1)


# uruchomienie

APP.go()

# To do: usuwanie plików w funkcjach

remove("InitialGraphImage.gif")
remove("leftTest.gif")
remove("rightTest.gif")
remove("InitialGraphImage")
remove("leftTest")
remove("rightTest")


