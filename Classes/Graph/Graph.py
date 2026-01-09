import math
from Noeud import Noeud

class Graph:
    def __init__(self):
        self.nodes = {}
    
    def add_node(self, name, coords=None):
        if name not in self.nodes:
            self.node[name] = Noeud(name, coords)
        else:
            print(f"Node {name} already exists.")
    
    def add_edge(self, name1, name2, weight=None, bidirectional=True):
        if name1 not in self.nodes or name2 not in self.nodes:
            print("Error: One or both nodes not found.")
            return
        
        node_1 = self.nodes[name1]
        node_2 = self.nodes[name2]
        
        if weight is None:
            if node_1.coordinates is not None and node_2.coordinates is not None:
                weight = self._get_distance(node_1, node_2)
            else:
                weight = 1
        
        node_1.add_neighbor(node_2, weight)
        
        if bidirectional:
            node_2.add_neighbor(node_1, weight)
            
    def _get_distance(self, node_1, node_2):
        x1, y1 = node_1.coordinates
        x2, y2 = node_2.coordinates
        return round(math.sqrt((x1 - x2)**2 + (y1-y2)**2), 2)
    
    def reset_visits(self):
        for node in self.nodes.values():
            node.visited = False
        
        print("Visited nodes have been reset.")