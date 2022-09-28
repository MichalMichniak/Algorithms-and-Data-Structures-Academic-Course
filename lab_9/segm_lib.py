import numpy as np
from copy import deepcopy
class Vertex:
    def __init__(self, key ,data = None, color = None) -> None:
        self.key = key
        self.data = data
        self.color = color
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

    def set_color(self,vertex_idx, color):
        self.lst[vertex_idx].color = color

    def get_color(self,vertex):
        return self.lst[self.getVertexIdx(vertex)].color

    def neighbours(self, vertex_idx):
        return self.graph[vertex_idx].copy()

    def order(self):
        return len(self.lst)

    def size(self):
        return len([(self.lst[j].key,self.lst[i].key) for i in range(len(self.graph)) for j in self.graph[i]])//2

    def edges(self):
        return [(self.lst[self.graph[i][j][0]].key,self.lst[i].key, self.graph[i][j][1]) for i in range(len(self.graph)) for j in range(len(self.graph[i]))]

    def getEdge(self, vertex1_idx, vertex2_idx):
        temp = list(filter(lambda x: vertex2_idx==x[0] ,self.graph[vertex1_idx]))
        if temp == []: return 
        else: temp=temp[0]
        return deepcopy(temp[1])

def PrimMST(G:Graph_List):
    if G.order() == 0: return Graph_List()
    intree = [0 for i in range(G.order())]
    distance = [np. float64('inf') for i in range(G.order())]
    parent = [-1 for i in range(G.order())]
    rozmiar = np. float64('inf')
    res = Graph_List()
    for i in range(G.order()):
        res.insertVertex(Vertex(G.getVertex(i)))
    v_idx = 0
    while intree[v_idx] == 0:
        intree[v_idx] = 1
        for i in G.neighbours(v_idx):
            if i[1].weight < distance[i[0]]:
                distance[i[0]] = i[1].weight
                parent[i[0]] = v_idx
        min = np. float64('inf')
        for i in range(len(distance)):
            if distance[i]<min and intree[i]!=1:
                min = distance[i]
                v_idx = i
        if parent[v_idx] == -1: print("graf niespojny")
        res.insertEdge(G.getVertex(v_idx),G.getVertex(parent[v_idx]), G.getEdge(v_idx,parent[v_idx]))
        res.insertEdge(G.getVertex(parent[v_idx]),G.getVertex(v_idx), G.getEdge(v_idx,parent[v_idx]))
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

