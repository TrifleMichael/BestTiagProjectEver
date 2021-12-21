from vertex import Vertex
from production import Production

def find_vertex_with_index(vertices, index):
    for v in vertices:
        if v.index == index:
            return v

def parse_graph(tab):
    vertices = [None for _ in range(len(tab))]
    for i in range(len(tab)):
        vertices[i] = Vertex(tab[i][1], int(tab[i][0]), [], [])
    for i in range(len(tab)):
        for v in tab[i][2:]:
            to_add = v.split(":")
            e = find_vertex_with_index(vertices, int(to_add[0]))
            vertices[i].edges.append(e)
            vertices[i].edges_names.append(to_add[1])
    return vertices

def parse_initial_graph(initial_graph_path):
    with open(initial_graph_path, "r") as f:
        temp = [row.split() for row in f.read().splitlines()]
    return parse_graph(temp)

def parse_left_and_right(left_and_right_path):
    with open(left_and_right_path, "r") as f:
        temp = [row.split() for row in f.read().splitlines()]
    left = []
    right = []
    i = 0
    while temp[i][0] != '=':
        left.append(temp[i])
        i += 1
    i += 1
    for j in range(i, len(temp)):
        right.append(temp[j])
    return (parse_graph(left), parse_graph(right)) 

def parse_productions(productions_path):
    with open(productions_path, "r") as f:
        temp = [prod.split() for prod in f.read().splitlines()]
    productions = [None for _ in range(len(temp))]
    for i in range(len(temp)):
        (left, right) = parse_left_and_right(temp[i][1])
        productions[i] = Production(temp[i][0], left, right)
    return productions

def parse_order(order_path):
    with open(order_path, "r") as f:
        order = [int(prod) for prod in f.read().split()]
    return order

def parse(initial_graph_path, productions_path, order_path):
    return (parse_initial_graph(initial_graph_path), parse_productions(productions_path), parse_order(order_path))

(a,b,c) = parse("./data/initial_graph.txt", "./data/productions.txt", "./data/productions_order.txt")
'''
parse("./data/initial_graph.txt", "./data/productions.txt", "./data/productions_order.txt")
zwróci krotkę składającą się z (a,b,c):
a - tablicy wierzchołków początkowego grafu (z wpisanymi odpowiednimi krawędziami i ich nazwami)
b - tablicy produkcji (składających się z nazwy, lewego i prawego grafu)
c - tablicy porządku wywoływania kolejnych produkcji (po ich indeksach z b)
'''
