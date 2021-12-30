class Vertex:
    def __init__(self, label, index, edges, edges_names):
        self.label = label
        self.index = index
        self.edges = edges
        self.edges_names = edges_names
        
    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return (
                self.label == other.label and
                self.index == other.index and
                self.edges == other.edges and
                self.edges_names == other.edges_names
                
            )
        else:
            return False

    def __ne__(self, other):
        return not self.__eq__(other)