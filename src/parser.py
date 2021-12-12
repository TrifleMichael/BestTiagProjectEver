from vertex import Vertex
from production import Production

def parse_morphisms(L, R, morphisms_path):
    with open(morphisms_path, "r") as f:
        ms = [m.split() for m in f.read().splitlines()]
    morphisms = [None for _ in range(len(ms))]
    for m in range(len(ms)):
        morphisms[m] = (L[int(ms[m][0])], R[int(ms[m][1])])
    return morphisms

def parse_graph(graph_path):
    with open(graph_path, "r") as f:
        temp = [row.split() for row in f.read().splitlines()]
    vertices = [None for _ in range(len(temp))]
    for i in range(len(temp)):
        vertices[i] = Vertex(temp[i][0], i, [])
    for i in range(len(temp)):
        for v in temp[i][1:]:
            vertices[i].edges.append(vertices[int(v)])
    return vertices

def parse_initial_graph(initial_graph_path):
    return parse_graph(initial_graph_path)

def parse_productions(productions_path):
    with open(productions_path, "r") as f:
        temp = [prod.split() for prod in f.read().splitlines()]
    productions = [None for _ in range(len(temp))]
    for i in range(len(temp)):
        L = parse_graph(temp[i][1])
        R = parse_graph(temp[i][2])
        morphisms = parse_morphisms(L, R, temp[i][3])
        productions[i] = Production(temp[i][0], L, R, morphisms)
    return productions

def parse_order(order_path):
    with open(order_path, "r") as f:
        order = [int(prod) for prod in f.read().split()]
    return order

def parse(initial_graph_path, productions_path, order_path):
    return (parse_initial_graph(initial_graph_path), parse_productions(productions_path), parse_order(order_path))

'''
parse("./data/initial_graph.txt", "./data/productions.txt", "./data/productions_order.txt")
zwróci krotkę składającą się z (a,b,c):
a - tablicy wierzchołków początkowego grafu (z wpisanymi odpowiednimi krawędziami)
b - tablicy produkcji (składających się z nazwy, lewego i prawego grafu
oraz tablicy krotek przedstawiających wierzchołkowi lewej strony odpowiadającu mu wierzchołek prawej)
c - tablicy porządku wywoływania kolejnych produkcji (po ich indeksach z b)
'''