# Wyświetla graf utworzony w funkcji createTestGraph() w oknie graficznym.

from graphviz import Digraph
from appJar import gui

from os import remove

from production import *
from vertex import *
from graphParser import *
from GUIFormatter import *

class ProductionPageKeeper:
    def __init__(self):
        self.currentPage = 0
        self.maxPage = 0
        
    def nextPage(self):
        if self.currentPage + 1 <= self.maxPage:
            self.currentPage += 1
            return True
        return False
    
    def lastPage(self):
        if self.currentPage > 0:
            self.currentPage -= 1
            return True
        return False
        

# Główny obiekt GUI
APP = gui("Single Push Out Visualisation") #, "800x800"
PPK = ProductionPageKeeper()

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

# Funkcja przycisku
def testShowProduction():
    graph1 = textFormGraphToGif("pl.txt", "PL")    
    graph2 = textFormGraphToGif("pr.txt", "PR")
    APP.reloadImage("ProductionLeft", "PL.gif")
    APP.reloadImage("ProductionRight", "PR.gif")

# Funkcja przycisku
def next_production_page():
    if PPK.nextPage():        
        productionToGif(productions[PPK.currentPage*2], "leftTest", "rightTest")
        APP.reloadImage("ProductionLeft1", "leftTest.gif")
        APP.reloadImage("ProductionRight1", "rightTest.gif")
        
        productionToGif(productions[PPK.currentPage*2+1], "leftTest", "rightTest")
        APP.reloadImage("ProductionLeft2", "leftTest.gif")
        APP.reloadImage("ProductionRight2", "rightTest.gif")
        
        APP.setLabel("PageCounter", PPK.currentPage)

# Funkcja przycisku
def last_production_page():
    if PPK.lastPage():        
        productionToGif(productions[PPK.currentPage*2], "leftTest", "rightTest")
        APP.reloadImage("ProductionLeft1", "leftTest.gif")
        APP.reloadImage("ProductionRight1", "rightTest.gif")
        
        productionToGif(productions[PPK.currentPage*2+1], "leftTest", "rightTest")
        APP.reloadImage("ProductionLeft2", "leftTest.gif")
        APP.reloadImage("ProductionRight2", "rightTest.gif")
        
        APP.setLabel("PageCounter", PPK.currentPage)

# parsing danych
initialVerticies, productions, productionIndicies = parse("./data/initial_graph.txt", "./data/productions.txt", "./data/productions_order.txt")
PPK.maxPage = int((len(productions)-1)/2) # TO DO - NIE WYSWIETLA OSTATNIEJ PRODUCJI JESLI NIEPARZYSTE

# dziwne rzeczy aby dopasowac rozmiar okien z produkcjami
productionToGif(productions[0], "leftTest", "baseBackround")

# graf początkowy
verticeArrayToGif(initialVerticies, "InitialGraphImage")
APP.addImage("MainImage", "InitialGraphImage.gif", 0, 0)

# produkcje 1

APP.addImage("ProductionLeft1", "baseBackround.gif", 0, 1) # dziwne rzeczy
APP.addImage("ProductionRight1", "baseBackround.gif", 0, 3)

productionToGif(productions[0], "leftTest", "rightTest")
APP.reloadImage("ProductionLeft1", "leftTest.gif")
APP.addImage("ArrowImage1", "arrow.gif", 0, 2)
APP.reloadImage("ProductionRight1", "rightTest.gif")

# produckcja 2
APP.addImage("ProductionLeft2", "baseBackround.gif", 1, 1) # dziwne rzeczy
APP.addImage("ProductionRight2", "baseBackround.gif", 1, 3)

productionToGif(productions[1], "leftTest", "rightTest")
APP.reloadImage("ProductionLeft2", "leftTest.gif")
APP.addImage("ArrowImage2", "arrow.gif", 1, 2)
APP.reloadImage("ProductionRight2", "rightTest.gif")

# przyciski

APP.addButton("Wpisz nazwę pliku z grafem a następnie naciśnij ten przycisk", changeGraphButtonFunction, 2, 0)
APP.addEntry("GraphInputName", 2, 1)

APP.addButton("(Work in progress) wybierz numer produkcji i wciśnij ten przycisk", testShowProduction, 3, 0)
APP.addEntry("ProductionInputName", 3, 1)


APP.addLabel("PageInfo", "Current production page: ", 2, 2)
APP.addLabel("PageCounter", PPK.currentPage, 2, 3)
APP.addButton("<", last_production_page, 3, 2)
APP.addButton(">", next_production_page, 3, 3)

# uruchomienie

APP.go()

# To do: usuwanie plików w funkcjach

remove("InitialGraphImage.gif")
remove("leftTest.gif")
remove("rightTest.gif")
remove("baseBackround.gif")
remove("InitialGraphImage")
remove("leftTest")
remove("rightTest")


