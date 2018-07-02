# couple of things. gotta be careful with whats a name, and whats an
# instance pointer. Referring to edges by name is easier, while
# actually manipulating everything is easier via pointer. You
# really need both.


class Vertex:
    def __init__(self, name):
        self.name = name
        self.neighbors = []
        self.distance = 9999
        self.color = 'black'

    def add_neighbor(self,v):
        if v not in self.neighbors:
            self.neighbors.append(v)
            

class Graph:
    v_dict = {}
    def add_vertex(self,vertex):
        if vertex.name not in self.v_dict:
            self.v_dict[vertex.name] = vertex
            return True
        else:
            return False

    def add_edge(self, u, v):

        if u in self.v_dict and v in self.v_dict:
            for key,value in self.v_dict.items():
                if key == u:
                    value.add_neighbor(self.v_dict[v])
                if key == v:
                    value.add_neighbor(self.v_dict[u])
            return True
        else:
            return False

    def print_graph(self):
        for key, value in sorted(self.v_dict.items()):
            print(key + "   " + str(value.distance))


    def bfs(self,vertex):

        q = []
        q.append(self.v_dict[vertex.name])
        vertex.distance = 0 ## set starting point as distance 0

        while q:
            node = q.pop(0)

            if node.neighbors:
                for neighbor in node.neighbors:
                    if neighbor.color == 'black':
                        q.append(neighbor)
                        if neighbor.distance > node.distance + 1:
                            neighbor.distance = node.distance + 1

            node.color = 'red'
            print(node.name)



g = Graph()

for i in range(ord('A'), ord('K')):
    g.add_vertex(Vertex(chr(i)))

edges = ['AB', 'AE', 'BF', 'CG', 'DE','DH', 'EH', 'FG', 'FI', 'FJ', 'GJ', 'HI']

for edge in edges:
    g.add_edge(edge[:1], edge[1:])


g.print_graph()
g.bfs(g.v_dict['G'])
g.print_graph()
