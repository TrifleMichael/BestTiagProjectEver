# Wyświetla graf utworzony w funkcji createTestGraph() w oknie graficznym.

from graphviz import Digraph
from appJar import gui

from production import *
from vertex import *
from parserer import *
from GUIFormatter import *


# Główny obiekt GUI
APP = gui()

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




# początkowy stan aplikacji
APP.addLabel("title", "Tymczasowy tytuł grafu")
APP.setLabelBg("title", "grey")
APP.addImage("MainImage", "defaultBackground.gif")

APP.addButton("Wpisz nazwę pliku z obrazem a następnie naciśnij ten przycisk", changeImageButtonFunction)
APP.addEntry("ImageName")

APP.addButton("Wpisz nazwę pliku z grafem a następnie naciśnij ten przycisk", changeGraphButtonFunction)
APP.addEntry("GraphInputName")

APP.go()

# Tutaj powinna być funkcja czyszcząca pliki tymczasowe

