import unittest
import copy

from vertex import Vertex 
from production import Production 

def fast_rm(array, id):
    array[id] = array[len(array) - 1]
    array.pop()
    
def find_key(d, val):
    for key, value in d.items():  # for name, age in dictionary.iteritems():  (for Python 2.x)
        if val == value:
            return key
    return -1

def apply_production(graph, production, indexPairs): 
    indexPairs = dict(indexPairs)
    right = copy.deepcopy(production.right)
      
    # przemianowanie prawej strony produkcji
    for id, v in right.items():
        right[id].index = indexPairs[id]
        for i in range(len(v.edges)):
            v.edges[i] = indexPairs[v.edges[i]] 
    
    for id in production.left.keys():
        if indexPairs[id] not in graph.keys(): 
            print(f"Production execution failed: vertex {indexPairs[id]} is in the production left side, but not in the graph")
            return graph 
    
    for id in right.keys():
        if indexPairs[id] in graph.keys() and id not in production.left.keys(): 
            print(f"Production execution failed: vertex {id} (production id) is in the right side and the graph, but not in the left side of the production")
            return graph 
    
    
    for id, v in right.items():
        id = indexPairs[id]
        if id in graph.keys():            
            for edge_v_id, edge_name in zip(graph[id].edges, graph[id].edges_names):
                p_edge_v_id = find_key(indexPairs, edge_v_id)
                if p_edge_v_id not in production.left.keys():
                    v.edges.append(edge_v_id)       
                    v.edges_names.append(edge_name)
        graph.update({id:v})
        
    for id in production.left.keys():
        if id not in right.keys():
            graph.pop(indexPairs[id])
        
    for id, v in graph.items():
        key = find_key(indexPairs, id)
        if key != -1 and key not in production.left.keys():
            to_rm = []
            for i in range(len(v.edges)):
                edge_v_id = v.edges[i]
                p_edge_v_id = find_key(indexPairs, edge_v_id)
                if p_edge_v_id in production.left.keys() and p_edge_v_id not in right.keys():
                    to_rm.append(edge_v_id)
            for eid in to_rm:
                for j in range(len(v.edges)):
                    if v.edges[j] == eid:
                        fast_rm(v.edges, i)
                        fast_rm(v.edges_names, i)
                        break
                    
                    
    return graph

class ProductionExecutionTests(unittest.TestCase): 
    def test_identity_production(self):
        graph = {0:Vertex("a", 0, [], [])} 
        production = Production("P", graph.copy(), graph.copy())

        self.assertEqual(graph, apply_production(graph.copy(), production))

    
    def test_basic_usage(self):
        left = {0: Vertex("a", 0, [], [])} 
        right = {0:Vertex("a", 0, [1], [""]), 1:Vertex("b", 1, [0], [""])}
        
        production = Production(
            "P", 
            left.copy(), 
            right.copy()
        )
        
        self.assertEqual(right, apply_production(left.copy(), production))
        
    def test_vertex_removal(self):
        left = {0:Vertex("a", 0, [1], [""]), 1:Vertex("b", 1, [0], [""])}
        right = {0: Vertex("a", 0, [], [])} 
        
        production = Production(
            "P", 
            left.copy(), 
            right.copy()
        )
        
        self.assertEqual(right, apply_production(left.copy(), production))
        
    def test_edge_removal(self):
        left = {0:Vertex("a", 0, [1], [""]), 1:Vertex("b", 1, [0], [""])}
        right = {0:Vertex("a", 0, [1], [""]), 1:Vertex("b", 1, [], [])}
        
        production = Production(
            "P", 
            left.copy(), 
            right.copy()
        )
        
        self.assertEqual(right, apply_production(left.copy(), production))
        
    def test_vertex_not_included_in_production(self):
        graph_before = {0:Vertex("a", 0, [1], [""]), 1:Vertex("b", 1, [0], [""]), 2:Vertex("c", 2, [0], [""])} 
        graph_expected = {1:Vertex("b", 1, [], []), 2:Vertex("c", 2, [], [])} 
        
        left = {0:Vertex("a", 0, [1], [""]), 1:Vertex("b", 1, [0], [""])}
        right = {1:Vertex("b", 1, [], [])}
        
        production = Production(
            "P", 
            left.copy(), 
            right.copy()
        )
        
        self.assertEqual(graph_expected, apply_production(graph_before.copy(), production))
        
    def test_change_edge_name(self):
        graph_before = {0:Vertex("a", 0, [1], [""]), 1:Vertex("b", 1, [0], [""]), 2:Vertex("c", 2, [0], [""])} 
        graph_expected = {0:Vertex("a", 0, [1], [""]), 1:Vertex("b", 1, [0], ["name"]), 2:Vertex("c", 2, [0], [""])} 
        
        left = {0:Vertex("a", 0, [1], [""]), 1:Vertex("b", 1, [0], [""])}
        right = {0:Vertex("a", 0, [1], [""]), 1:Vertex("b", 1, [0], ["name"])}
        
        production = Production(
            "P", 
            left.copy(), 
            right.copy()
        )
        
        self.assertEqual(graph_expected, apply_production(graph_before.copy(), production))
        
        

if __name__ == '__main__':
    unittest.main()
