import polska

class Vertex:
    def __init__(self, key ,data = None) -> None:
        self.key = key
        self.data = data
        pass

    def __hash__(self):
        return hash(self.key)

    def __eq__(self, other):
        return self.key == other

class Edge:
    def __init__(self):
        pass


class Graph_List:
    def __init__(self) -> None:
        self.dic = {}
        self.lst = []
        self.graph = []
        self.edge_lst = []

    def  insertVertex(self,vertex):
        if vertex in self.dic.keys(): 
            self.lst[self.dic[vertex]] = vertex
            return
        self.dic[vertex] = len(self.lst)
        self.lst.append(vertex)
        self.graph.append([])

    def insertEdge(self, vertex1, vertex2, egde):
        if self.dic[vertex2] not in self.graph[self.dic[vertex1]]: self.graph[self.dic[vertex1]].append(self.dic[vertex2])
        if self.dic[vertex1] not in self.graph[self.dic[vertex2]]: self.graph[self.dic[vertex2]].append(self.dic[vertex1])
        # na zapas nie wiem po co
        self.edge_lst.append(egde)

    def deleteVertex(self, vertex):
        del self.graph[self.dic[vertex]]
        for i in range(self.graph.__len__()):
            try:
                self.graph[i].remove(self.dic[vertex])
            except ValueError:
                pass
        for i in range(self.graph.__len__()):
            for j in range(len(self.graph[i])):
                if self.graph[i][j] > self.dic[vertex]:
                    self.graph[i][j] -= 1
        del self.lst[self.dic[vertex]]
        for i in self.lst:
            if self.dic[i] > self.dic[vertex]:
                self.dic[i] -= 1
        self.dic.pop(vertex)

    def deleteEdge(self, vertex1, vertex2):
        try:
            self.graph[self.dic[vertex1]].remove(self.dic[vertex2])
        except ValueError:
            pass
        try:
            self.graph[self.dic[vertex2]].remove(self.dic[vertex1])
        except ValueError:
            pass

    def getVertexIdx(self, vertex):
        return self.dic[vertex]

    def getVertex(self, vertex_idx):
        return self.lst[vertex_idx]

    def neighbours(self, vertex_idx):
        return self.graph[vertex_idx].copy()

    def order(self):
        return len(self.lst)

    def size(self):
        return len([(self.lst[j].key,self.lst[i].key) for i in range(len(self.graph)) for j in self.graph[i]])//2

    def edges(self):
        return [(self.lst[j].key,self.lst[i].key) for i in range(len(self.graph)) for j in self.graph[i]]


class Graph_Matrix:
    def __init__(self) -> None:
        self.dic = {}
        self.lst = []
        self.matrix = []
        pass

    def  insertVertex(self,vertex):
        if vertex in self.dic.keys(): 
            self.lst[self.dic[vertex]] = vertex
            return
        self.dic[vertex] = len(self.lst)
        self.lst.append(vertex)
        self.matrix.append([0 for i in range(len(self.matrix[0]))]) if self.matrix != [] else self.matrix.append([])
        for i in range(len(self.matrix)):
            self.matrix[i].append(0)
        pass

    def insertEdge(self, vertex1, vertex2, egde):
        self.matrix[self.dic[vertex1]][self.dic[vertex2]] = 1
        self.matrix[self.dic[vertex2]][self.dic[vertex1]] = 1
        pass

    def deleteVertex(self, vertex):
        del self.matrix[self.dic[vertex]]
        for i in range(len(self.matrix)):
            del self.matrix[i][self.dic[vertex]]
        del self.lst[self.dic[vertex]]
        for i in self.lst:
            if self.dic[i] > self.dic[vertex]:
                self.dic[i] -= 1
        self.dic.pop(vertex)
        pass

    def deleteEdge(self, vertex1, vertex2):
        self.matrix[self.dic[vertex1]][self.dic[vertex2]] = 0
        self.matrix[self.dic[vertex2]][self.dic[vertex1]] = 0
        pass

    def getVertexIdx(self, vertex):
        return self.dic[vertex]
        pass

    def getVertex(self, vertex_idx):
        return self.lst[vertex_idx]
        pass

    def neighbours(self, vertex_idx):
        return [i for i in range(len(self.matrix[vertex_idx])) if self.matrix[vertex_idx][i]==1]
        pass

    def order(self):
        return len(self.lst)
        pass

    def size(self):
        return len([(self.lst[j].key,self.lst[i].key) for i in range(len(self.matrix)) for j in range(len(self.matrix[i])) if self.matrix[i][j] == 1])//2
        pass

    def edges(self):
        return [(self.lst[j].key,self.lst[i].key) for i in range(len(self.matrix)) for j in range(len(self.matrix[i])) if self.matrix[i][j] == 1]
        pass

def test(g_lst):
    for i in polska.graf:
        a = Vertex(i[0])
        b = Vertex(i[1])
        g_lst.insertVertex(a)
        g_lst.insertVertex(b)
        g_lst.insertEdge(a,b,Edge())
    g_lst.deleteVertex(Vertex('K'))
    g_lst.deleteEdge(Vertex('T'), Vertex('W'))
    polska.draw_map(g_lst.edges())

def main():
    matrix = Graph_Matrix()
    lst = Graph_List()
    test(matrix)
    test(lst) 
    
     
      
if __name__ == "__main__":      
    main()    
