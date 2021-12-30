import unittest

from graphParser import parse
from vertex import Vertex 
from production import Production 

def fast_rm(array, id):
    array[id] = array[len(array) - 1]
    array.pop()

def aplay_production(graph, production):
    for id, v in production.right.items():
        if id in graph.keys():            
            for edge_id, edge_name in zip(graph[id].edges, graph[id].edges_names):
                if edge_id not in production.left.keys():
                    production.right.edges.append(edge_id)       
                    production.right.edges_names.append(edge_name)
        graph.update({v.index:v})
        
    for id, v in graph.items():            
        if id not in production.left.keys():
            for i in range(len(graph[id].edges)):
                edge_id = graph[id].edges[i] 
                if edge_id in production.left.keys() and edge_id not in production.right.keys():
                    fast_rm(graph[id].edges, i)
                    fast_rm(graph[id].edges_names, i)
                           
    return graph

class ProductionExecutionTests(unittest.TestCase): 
    def test_identity_production(self):
        graph = {0:Vertex("a", 0, [], [])} 
        production = Production("P", graph.copy(), graph.copy())

        self.assertEqual(graph, aplay_production(graph.copy(), production))

    
    def test_basic_usage(self):
        left = {0: Vertex("a", 0, [], [])} 
        right = {0:Vertex("a", 0, [1], [""]), 1:Vertex("b", 1, [0], [""])}
        
        production = Production(
            "P", 
            left.copy(), 
            right.copy()
        )
        
        self.assertEqual(right, aplay_production(left.copy(), production))
        
        

if __name__ == '__main__':
    unittest.main()