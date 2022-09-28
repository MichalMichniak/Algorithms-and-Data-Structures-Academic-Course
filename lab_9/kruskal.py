import numpy as np
from copy import deepcopy
class Vertex:
    def __init__(self, key ,data = None, color = None) -> None:
        self.key = key
        self.data = data
        self.color = None
        pass

    def __hash__(self):
        return hash(self.key)

    def __eq__(self, other):
        if type(other) == Vertex:
            return self.key == other.key
        else:
            return self.key == other

    def __repr__(self):
        return str(self.key)

class Edge:
    def __init__(self,weight):
        self.weight = weight
    
    def __repr__(self):
        return str(self.weight)
        pass


class Graph_List:
    def __init__(self) -> None:
        self.dic = {}
        self.lst = []
        self.graph = []


    def  insertVertex(self,vertex):
        if vertex in self.dic.keys(): 
            self.lst[self.dic[vertex]] = vertex
            return
        self.dic[vertex] = len(self.lst)
        self.lst.append(vertex)
        self.graph.append([])

    def insertEdge(self, vertex1, vertex2, egde):
        if self.graph[self.dic[vertex1]] == []:
            self.graph[self.dic[vertex1]].append([self.dic[vertex2],egde])
        elif self.dic[vertex2] not in list(zip(*self.graph[self.dic[vertex1]]))[0]: 
            self.graph[self.dic[vertex1]].append([self.dic[vertex2],egde])
        """if self.graph[self.dic[vertex2]] == []:
            self.graph[self.dic[vertex2]].append([self.dic[vertex1],egde])
        elif self.dic[vertex1] not in list(zip(*self.graph[self.dic[vertex2]]))[0]: 
            self.graph[self.dic[vertex2]].append([self.dic[vertex1],egde])"""
        

    def deleteEdge(self, vertex1, vertex2):
        try:
            temp = list(filter(lambda x: self.dic[vertex2]==x[0] ,self.graph[self.dic[vertex1]]))
            if temp == []: return 
            else: temp=temp[0]
            self.graph[self.dic[vertex1]].remove(temp)

            """temp = list(filter(lambda x: self.dic[vertex1]==x[0] ,self.graph[self.dic[vertex2]]))
            if temp == []: return 
            else: temp=temp[0]
            self.graph[self.dic[vertex2]].remove(temp)"""
        except ValueError:
            pass
    
    def deleteVertex(self, vertex):
        del self.graph[self.dic[vertex]]
        for i in range(self.graph.__len__()):
            try:
                self.deleteEdge(self.lst[i], vertex)
                self.deleteEdge(vertex, self.lst[i])
            except ValueError:
                pass
        for i in range(self.graph.__len__()):
            for j in range(len(self.graph[i])):
                if self.graph[i][j][0] > self.dic[vertex]:
                    self.graph[i][j][0] -= 1
        del self.lst[self.dic[vertex]]
        for i in self.lst:
            if self.dic[i] > self.dic[vertex]:
                self.dic[i] -= 1
        self.dic.pop(vertex)



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

    def getedges(self):
        return [(ni,j[0],j[1]) for ni,i in enumerate(self.graph) for j in i]

    def getEdge(self, vertex1_idx, vertex2_idx):
        temp = list(filter(lambda x: vertex2_idx==x[0] ,self.graph[vertex1_idx]))
        if temp == []: return 
        else: temp=temp[0]
        return deepcopy(temp[1])

class Union_Find:
    def __init__(self,lst):
        self.lst = lst
        self.dic = {i:n for n,i in enumerate(lst)}
        self.size = [1 for i in range(len(lst))]
        self.p = [i for i in range(len(lst))]
        self.n = len(lst)-1

    def find(self,v):
        root = self.dic[v]
        if self.p[root] != root:
            root = self.find(self.lst[self.p[root]])
        return root

    def same_component(self,s1,s2):
        return self.find(s1) == self.find(s2)

    def union_sets(self,s1,s2):
        t1 = self.find(s1)
        t2 = self.find(s2)
        if t1 == t2: return
        if self.size[t1] > self.size[t2]:
            self.p[t2] = t1
            self.n-=1
        elif self.size[t1] == self.size[t2]:
            self.p[t2] = t1
            self.size[t1] +=1
            self.n-=1
        else:
            self.p[t1] = t2
            self.n-=1
        pass



    def __repr__(self):
        return "Union Find: " + str(self.p)

def kruskal(G:Graph_List):
    if G.order() == 0: return Graph_List()
    res = Graph_List()
    ed = G.getedges()
    ed.sort(key=lambda x: x[2].weight)
    UF = Union_Find([i for i in range(G.order())])
    while UF.n !=0:
        t = ed[0]
        ed.pop(0)
        if not UF.same_component(t[0],t[1]):
            UF.union_sets(t[0],t[1])
            res.insertVertex(G.getVertex(t[0]))
            res.insertVertex(G.getVertex(t[1]))
            res.insertEdge(G.getVertex(t[0]),G.getVertex(t[1]), t[2])
            res.insertEdge(G.getVertex(t[1]),G.getVertex(t[0]), t[2])
    return res


def printGraph(g):
    n = g.order()
    print("------GRAPH------",n)
    for i in range(n):
        v = g.getVertex(i)
        print(v, end = " -> ")
        nbrs = g.neighbours(i)
        for (j, w) in nbrs:
            print(g.getVertex(j), w, end=";")
        print()
    print("-------------------")

def test_union():
    test = [1,2,3,4,5]
    UF = Union_Find(test)
    UF.union_sets(1,2)
    UF.union_sets(4,5)
    print(UF.same_component(1,2))
    print(UF.same_component(2,3))
    print(UF.same_component(4,5))
    UF.union_sets(3,1)
    print(UF.same_component(1,2))
    print(UF.same_component(2,3))
    print(UF.same_component(4,5))

def test_kruskal():
    graf = [ ('A','B',4), ('A','C',1), ('A','D',4),
         ('B','E',9), ('B','F',9), ('B','G',7), ('B','C',5),
         ('C','G',9), ('C','D',3),
         ('D', 'G', 10), ('D', 'J', 18),
         ('E', 'I', 6), ('E', 'H', 4), ('E', 'F', 2),
         ('F', 'H', 2), ('F', 'G', 8),
         ('G', 'H', 9), ('G', 'J', 8),
         ('H', 'I', 3), ('H','J',9),
         ('I', 'J', 9)
        ]
    g_list = Graph_List()
    for i in graf:
        g_list.insertVertex(Vertex(i[0]))
        g_list.insertVertex(Vertex(i[1]))
        g_list.insertEdge(Vertex(i[0]),Vertex(i[1]),Edge(i[2]))
        g_list.insertEdge(Vertex(i[1]),Vertex(i[0]),Edge(i[2]))
    temp = kruskal(g_list)
    printGraph(temp)
    pass

def main():
    test_union()
    test_kruskal()
    pass

if __name__=='__main__':
    main()