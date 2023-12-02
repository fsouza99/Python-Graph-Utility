from abc import ABC, abstractmethod
INFINITE = 2**31-1

class Node():

    __slots__ = ['data', 'key', 'parent', 'adjacency']

    def __init__(self, data):
        self.data = data
        self.parent = None
        self.key = None
        self.adjacency = []

class UndirectedEdge():
    
    __slots__ = ['u', 'v', 'w']

    def __init__(self, u, v, w=1):
        self.u = u
        self.v = v
        self.w = w

class DirectedEdge():

    __slots__ = ['u', 'v', 'w']

    def __init__(self, u, v, w=1):
        self.u = u
        self.v = v
        self.w = w

class Graph(ABC):
    
    __slots__ = ['vertices', 'edges']

    def __init__(self):
        self.vertices = []
        self.edges = []

    def searchForData(self, data: str) -> Node: # returns the node with a certain content.
        for node in self.vertices:
            if node.data == data:
                return node
        return None

    def insert(self, data):  # inserts a vertex to the graph.
        self.vertices.append(Node(data))
        return None

    def insertAll(self, values: list):  # inserts a whole list of new vertices.
        for data in values:
            self.vertices.append(Node(data))
        return None

    def extractMin(self, vertices:list) -> Node: # returns, from a list, the node with minimum key value, removes this node from the list.
        selected = min(vertices, key=lambda v : v.key)
        vertices.remove(selected)
        return selected

    @abstractmethod
    def connect(self, data_A: str, data_B: str, cost=None):
        pass
        
class DirectedGraph(Graph):

    def connect(self, data_A: str, data_B: str, cost=None): # connect two vertices of datas data_A and data_B, respectively.
        node_A = self.searchForData(data_A)
        node_B = self.searchForData(data_B)
        if not (node_B, cost) in node_A.adjacency:
            node_A.adjacency.append((node_B, cost))
            self.edges.append(DirectedEdge(node_A, node_B, cost))
        return None

    def initializeSingleSource(self, s:Node): # prepares for future procedures.
        for vertex in self.vertices:
            vertex.key = INFINITE
            vertex.parent = None
        s.key = 0
        return None
    
    def relax(self, u:Node, v:Node, w:float):
        if v.key > u.key + w:
            v.key = u.key + w
            v.parent = u
        return None

    def dijkstra(self, data:str): # Dijkstra's Algorithm: computes the shortest path from single source.
        s = self.searchForData(data)
        self.initializeSingleSource(s)
        Q = self.vertices.copy()
        c = 0
        while Q:
            u = self.extractMin(Q)
            for adjencency in u.adjacency:
                self.relax(u, adjencency[0], adjencency[1])
            c += 1
        return None

class UndirectedGraph(Graph):

    def connect(self, data_A: str, data_B: str, cost=None): # connect two vertices of datas data_A and data_B, respectively.
        node_A = self.searchForData(data_A)
        node_B = self.searchForData(data_B)
        if not (node_B, cost) in node_A.adjacency:
            node_A.adjacency.append((node_B, cost))
            node_B.adjacency.append((node_A, cost))
            self.edges.append(UndirectedEdge(node_A, node_B, cost))
        return None

    def findSet(self, edge:UndirectedEdge, forest:list) -> set:
        for tree in forest:
            if edge in tree:
                return tree
        return None

    def kruskalMST(self) -> set: # Kruskal's Algorithm for the Minimum Spanning Tree problem.
        A = set()
        forest = []
        for v in self.vertices:
            tree = set()
            tree.add(v)
            forest.append(tree)
        self.edges.sort(key=lambda e : e.w)
        for edge in self.edges:
            uset = self.findSet(edge.u, forest)
            vset = self.findSet(edge.v, forest)
            if uset != vset:
                A.add(edge)
                uset |= vset
                forest.remove(vset)
        return A

    def primMST(self) -> Node: # Prim's Algorithm for the Minimum Spanning Tree problem.
        for v in self.vertices:
            v.key = INFINITE
            v.parent = None
        self.vertices[0].key = 0
        path = []
        Q = self.vertices.copy()
        while Q:
            u = self.extractMin(Q)
            for neighbor in u.adjacency:
                w = neighbor[1]
                if neighbor[0] in Q and neighbor[0].key > w:
                    neighbor[0].parent = u
                    neighbor[0].key = w
                    path.append(neighbor)
        return path





