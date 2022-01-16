# Wyświetla graf utworzony w funkcji createTestGraph() w oknie graficznym.

from graphviz import Digraph
from appJar import gui

from os import remove

from production import *
from vertex import *
from graphParser import *
from GUIFormatter import *
from productionExecutor import *

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
        

class MainGraph:
    def __init__(self, verticeArray):
        self.verticeArray = verticeArray

    def applyProduction(self, production):
        self.verticeArray = apply_production(self.verticeArray, production)

# Główny obiekt GUI
APP = gui("Single Push Out Visualisation") #, "800x800"
PPK = ProductionPageKeeper()
PROD_PER_PAGE = 3



def refresh_productions():
    if PPK.currentPage*PROD_PER_PAGE < len(productions): 
        productionToGif(productions[PPK.currentPage*PROD_PER_PAGE], "leftTest", "rightTest")
        APP.reloadImage("ProductionLeft1", "leftTest.gif")
        APP.reloadImage("ProductionRight1", "rightTest.gif")
        APP.setLabel("ProductionIndex1", PPK.currentPage*PROD_PER_PAGE)
    else:
        APP.setLabel("ProductionIndex1", "~")
        APP.reloadImage("ProductionLeft1", "sideGraphBackground.gif")
        APP.reloadImage("ProductionRight1", "sideGraphBackground.gif")
        
    if PPK.currentPage*PROD_PER_PAGE+1 < len(productions): 
        productionToGif(productions[PPK.currentPage*PROD_PER_PAGE+1], "leftTest", "rightTest")
        APP.reloadImage("ProductionLeft2", "leftTest.gif")
        APP.reloadImage("ProductionRight2", "rightTest.gif")
        APP.setLabel("ProductionIndex2", PPK.currentPage*PROD_PER_PAGE+1)
    else:
        APP.setLabel("ProductionIndex2", "~")
        APP.reloadImage("ProductionLeft2", "sideGraphBackground.gif")
        APP.reloadImage("ProductionRight2", "sideGraphBackground.gif")

    if PPK.currentPage*PROD_PER_PAGE+2 < len(productions): 
        productionToGif(productions[PPK.currentPage*PROD_PER_PAGE+2], "leftTest", "rightTest")
        APP.reloadImage("ProductionLeft3", "leftTest.gif")
        APP.reloadImage("ProductionRight3", "rightTest.gif")
        APP.setLabel("ProductionIndex3", PPK.currentPage*PROD_PER_PAGE+2)
    else:
        APP.setLabel("ProductionIndex3", "~")
        APP.reloadImage("ProductionLeft3", "sideGraphBackground.gif")
        APP.reloadImage("ProductionRight3", "sideGraphBackground.gif")
        
    APP.setLabel("PageCounter", PPK.currentPage)


# Funkcja przycisku zmiany strony z produkcjami
def next_production_page():
    if PPK.nextPage():        
        refresh_productions()
        
def applyProductionButtonFunction():
    productionNr = int(APP.getEntry("ProductionInputName"))
    production = productions[productionNr]    
    MAIN_GRAPH.applyProduction(production)
    verticeArrayToGif(MAIN_GRAPH.verticeArray, "TemporaryGraph", dpi=600, size = 1.3)
    APP.reloadImage("MainImage", "TemporaryGraph.gif")

# Funkcja przycisku
def last_production_page():
    if PPK.lastPage():   
        refresh_productions()

# parsing danych
initialVerticies, productions, productionIndicies = parse("./data/initial_graph.txt", "./data/productions.txt", "./data/productions_order.txt")
MAIN_GRAPH = MainGraph(initialVerticies)
PPK.maxPage = int((len(productions))/3)

# dziwne rzeczy aby dopasowac rozmiar okien z produkcjami

# glowne okno z grafem
APP.addImage("MainImage", "mainGraphBackground.gif", 0, 0, 3, 3)
verticeArrayToGif(MAIN_GRAPH.verticeArray, "InitialGraphImage", dpi=600, size = 1.3)
APP.reloadImage("MainImage", "InitialGraphImage.gif")

# produkcje 1
APP.addImage("ProductionLeft1", "sideGraphBackground.gif", 0, 5) # poczatkowy gif celem wymuszenia rozmiaru
APP.addImage("ProductionRight1", "sideGraphBackground.gif", 0, 7)

productionToGif(productions[0], "leftTest", "rightTest")
APP.reloadImage("ProductionLeft1", "leftTest.gif")
APP.addImage("ArrowImage1", "arrow.gif", 0, 6)
APP.reloadImage("ProductionRight1", "rightTest.gif")

# produckcja 2
APP.addImage("ProductionLeft2", "sideGraphBackground.gif", 1, 5) 
APP.addImage("ProductionRight2", "sideGraphBackground.gif", 1, 7)

productionToGif(productions[1], "leftTest", "rightTest")
APP.reloadImage("ProductionLeft2", "leftTest.gif")
APP.addImage("ArrowImage2", "arrow.gif", 1, 6)
APP.reloadImage("ProductionRight2", "rightTest.gif")

# produckcja 3
APP.addImage("ProductionLeft3", "sideGraphBackground.gif", 2, 5)
APP.addImage("ProductionRight3", "sideGraphBackground.gif", 2, 7)

productionToGif(productions[2], "leftTest", "rightTest")
APP.reloadImage("ProductionLeft3", "leftTest.gif")
APP.addImage("ArrowImage3", "arrow.gif", 2, 6)
APP.reloadImage("ProductionRight3", "rightTest.gif")

# numery produkcji
APP.addLabel("ProductionIndex1", PPK.currentPage, 0, 4)
APP.addLabel("ProductionIndex2", PPK.currentPage+1, 1, 4)
APP.addLabel("ProductionIndex3", PPK.currentPage+2, 2, 4)

APP.setLabelWidth("ProductionIndex1", 4)
APP.setLabelWidth("ProductionIndex2", 4)
APP.setLabelWidth("ProductionIndex3", 4)

# przyciski
APP.addButton("Ok", applyProductionButtonFunction, 3, 4)
APP.setButtonWidth("Ok", 10)
APP.addButton("<", last_production_page, 3, 5)
APP.addButton(">", next_production_page, 3, 7)

# Napisy i pola tekstowe
APP.addEntry("ProductionInputName", 3, 0)
APP.setEntryAlign("ProductionInputName", "left")
APP.addLabel("PageCounter", PPK.currentPage, 3, 6)

# uruchomienie
APP.go()

# To do: usuwanie plików w funkcjach

remove("InitialGraphImage.gif")
remove("TemporaryGraph.gif")
remove("leftTest.gif")
remove("rightTest.gif")
remove("baseBackround.gif")
remove("InitialGraphImage")
remove("leftTest")
remove("rightTest")


