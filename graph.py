import pprint

class Vertex:
    def __init__(self, name):
        self.name = name
        self.connections = []
    
    def add_edge(self,obj):
        self.connections.append(obj)

class Edge:
    def __init__(self):
        self.connections = []
    
    def add_edge(self,from_ver,to_ver):
        self.connections.append(from_ver.name)
        self.connections.append(to_ver.name)

class Graph:
    def __init__(self):
        self.graph = {}

    def add_vertices(self,obj):
        self.graph.update({obj.name:obj.connections})

v1 = Vertex("1")
v2 = Vertex("2")
v3 = Vertex("3")
v4 = Vertex("4")

e1 = Edge()
e1.add_edge(v1,v2)

e2 = Edge()
e2.add_edge(v1,v3)

e3 = Edge()
e3.add_edge(v2,v3)

e4 = Edge()
e4.add_edge(v3,v4)

e5 = Edge()
e5.add_edge(v4,v1)

#v1
v1.add_edge(e1.connections)
v1.add_edge(e2.connections)

#v2
v2.add_edge(e3.connections)

#v3
v3.add_edge(e4.connections)

#v4
v4.add_edge(e5.connections)

g1 = Graph()

g1.add_vertices(v1)
g1.add_vertices(v2)
g1.add_vertices(v3)
g1.add_vertices(v4)


pprint.pprint(g1.graph)