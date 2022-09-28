from cmath import inf
from typing import List
import numpy as np
from copy import deepcopy
import cv2
import warnings
import matplotlib.pyplot as plt
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
    def __init__(self,weight,resztowa : bool = False):
        self.weight = weight
        self.resztowa : bool= resztowa
        if resztowa:
            self.flow = weight
        else:
            self.flow = 0
        

    def __repr__(self):
        return "("+str(self.weight)+" "+str(self.flow)+" "+str(self.resztowa)+")"
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
        if egde.resztowa:
            self.graph[self.dic[vertex1]].append([self.dic[vertex2],egde])
            return
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

    def getEdge(self, vertex1_idx, vertex2_idx,resz = None , weight = None):
        if resz == None: 
            temp = list(filter(lambda x: vertex2_idx==x[0] ,self.graph[vertex1_idx]))
        else:
            if weight == None: temp = list(filter(lambda x: vertex2_idx==x[0] and (x[1].resztowa == resz) ,self.graph[vertex1_idx]))
            if weight != None: temp = list(filter(lambda x: vertex2_idx==x[0] and (x[1].resztowa == resz) and (x[1].weight == weight) ,self.graph[vertex1_idx]))
        
        if temp == []: return 
        if len(temp)>1: return temp
        else: temp=temp[0]
        return temp[1]


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

def BFS(G:Graph_List, source, destination):
    visited = [0 for i in range(G.order())]
    parent = [-1 for i in range(G.order())]
    Q : List[int]= []
    Q.append(G.getVertexIdx(Vertex(source)))
    destination_idx = G.getVertexIdx(Vertex(destination))
    while Q != []:
        v = Q[0]
        Q.pop(0)
        visited[v] = 1
        for i in G.neighbours(v):
            if visited[i[0]] == 0 and G.getEdge(i[0],v,not i[1].resztowa).flow>0:
                Q.append(i[0])
                parent[i[0]] = v
                if i[0] == destination_idx:
                    return parent
    raise ValueError()

def min_weight(G:Graph_List, parent, source, destination ):
    v = G.getVertexIdx(Vertex(destination))
    source = G.getVertexIdx(Vertex(source))
    min_ = inf
    while v != source:
        max_ = 0
        if type(G.getEdge(v,parent[v]))==list:
            for i in G.getEdge(v,parent[v]):
                max_ = max(max_,i[1].flow)
        else:
            max_ = G.getEdge(v,parent[v]).flow
        min_ = min(max_,min_)
        v = parent[v]
    return min_
        
def augment(G:Graph_List, parent, source, destination ):
    min_ = min_weight(G,parent,source,destination)
    v = G.getVertexIdx(Vertex(destination))
    source = G.getVertexIdx(Vertex(source))
    while v != source:
        if type(G.getEdge(v,parent[v]))==list:
            tab = G.getEdge(v,parent[v])
            for n,i in enumerate(tab):
                if i[1].flow>= min_:
                    tab[n][1].flow -=min_
                    G.getEdge(parent[v],v,not tab[n][1].resztowa,tab[n][1].weight).flow+=min_
                    break
        else:
            tab = G.getEdge(v,parent[v])
            tab.flow -=min_
            G.getEdge(parent[v],v,not tab.resztowa,tab.weight).flow+=min_
        v = parent[v]
    return min_

def ford_fulkerson(G:Graph_List, source, destination):
    G_copy = deepcopy(G)
    for k1,k2,w in G_copy.edges():
        G_copy.insertEdge(Vertex(k1),Vertex(k2),Edge(w.weight,True))
    maxflow = 0
    try:
        while True:
            maxflow += augment(G_copy,BFS(G_copy,source,destination),source,destination)
    except ValueError:
        return maxflow,G_copy


def main():
    graf_0 = [ ('s','u',2), ('u','t',1), ('u','v',3), ('s','v',1), ('v','t',2)]
    G = Graph_List()
    for i in graf_0:
        G.insertVertex(Vertex(i[0]))
        G.insertVertex(Vertex(i[1]))
        G.insertEdge(Vertex(i[0]),Vertex(i[1]),Edge(i[2]))
    max,G_copy = ford_fulkerson(G,'s','t')
    print(max)
    printGraph(G_copy)
    graf_1 = [ ('s', 'a', 16), ('s', 'c', 13), ('a', 'c', 10), ('c', 'a', 4), ('a', 'b', 12), ('b', 'c', 9), ('b', 't', 20), ('c', 'd', 14), ('d', 'b', 7), ('d', 't', 4) ]
    G = Graph_List()
    for i in graf_1:
        G.insertVertex(Vertex(i[0]))
        G.insertVertex(Vertex(i[1]))
        G.insertEdge(Vertex(i[0]),Vertex(i[1]),Edge(i[2]))
    max,G_copy = ford_fulkerson(G,'s','t')
    print(max)
    printGraph(G_copy)
    graf_2 = [ ('s', 'a', 3), ('s', 'c', 3), ('a', 'b', 4), ('b', 's', 3), ('b', 'c', 1), ('b', 'd', 2), ('c', 'e', 6), ('c', 'd', 2), ('d', 't', 1), ('e', 't', 9)]
    G = Graph_List()
    for i in graf_2:
        G.insertVertex(Vertex(i[0]))
        G.insertVertex(Vertex(i[1]))
        G.insertEdge(Vertex(i[0]),Vertex(i[1]),Edge(i[2]))
    max,G_copy = ford_fulkerson(G,'s','t')
    print(max)
    printGraph(G_copy)
    graf_3 = [('s', 'a', 8), ('s', 'd', 3), ('a', 'b', 9), ('b', 'd', 7), ('b', 't', 2), ('c', 't', 5), ('d', 'b', 7), ('d', 'c', 4)]
    G = Graph_List()
    for i in graf_3:
        G.insertVertex(Vertex(i[0]))
        G.insertVertex(Vertex(i[1]))
        G.insertEdge(Vertex(i[0]),Vertex(i[1]),Edge(i[2]))
    max,G_copy = ford_fulkerson(G,'s','t')
    print(max)
    printGraph(G_copy)
    pass

if __name__=='__main__':
    main()