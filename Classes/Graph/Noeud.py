from Arrete import Arrete

class Noeud:
    
    def __init__(self, name, coords=None):
        self.name = name
        self.coordinates = coords
        self.neighbors = []
        self.visited = False
    
    def add_neighbor(self, neighbor_noeud, weight):
        new_arrete = Arrete(self, neighbor_noeud, weight)
        self.neighbors.append(new_arrete)
        
    def __repr__(self):
        return f"Node({self.name})"