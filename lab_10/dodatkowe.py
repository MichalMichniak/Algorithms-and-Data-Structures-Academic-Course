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
                    G.getEdge(parent[v],v, not tab[n][1].resztowa,tab[n][1].weight).flow+=min_
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

def cut1():
    I = cv2.imread('min_cut_seg_1.png', cv2.IMREAD_GRAYSCALE)
    YY,XX = I.shape
    scrible_FG = np.zeros((YY,XX),dtype=np.ubyte)
    scrible_FG[100:120, 100:120] = 255

    scrible_BG = np.zeros((YY,XX),dtype=np.ubyte)
    scrible_BG[0:20, 0:20] = 255

    I = cv2.resize(I,(32,32))
    scrible_BG = cv2.resize(scrible_BG,(32,32))
    scrible_FG = cv2.resize(scrible_FG,(32,32))
    hist_FG = cv2.calcHist([I],[0],scrible_FG,[256],[0,256])
    hist_FG = hist_FG/sum(hist_FG)

    hist_BG = cv2.calcHist([I],[0],scrible_BG,[256],[0,256])
    hist_BG = hist_BG/sum(hist_BG)

    YY,XX = I.shape
    G = Graph_List()
    for i in range(len(I)):
        for j in range(len(I[0])):
            G.insertVertex(Vertex(YY*i + j))
    G.insertVertex(Vertex('s'))
    G.insertVertex(Vertex('t'))
    for i in range(len(I)):
        for j in range(len(I[0])):
            if scrible_FG[i,j] == 255:
                G.insertEdge(Vertex('s'),Vertex(YY*(i) + (j)),Edge(inf))
                G.insertEdge(Vertex(YY*(i) + (j)),Vertex('t'),Edge(0))
            elif scrible_BG[i,j] == 255:
                G.insertEdge(Vertex('s'),Vertex(YY*(i) + (j)),Edge(0))
                G.insertEdge(Vertex(YY*(i) + (j)),Vertex('t'),Edge(inf))
            else:
                G.insertEdge(Vertex('s'),Vertex(YY*(i) + (j)),Edge(hist_FG[I[i,j]]))
                G.insertEdge(Vertex(YY*(i) + (j)),Vertex('t'),Edge(hist_BG[I[i,j]]))

    for i in range(1,len(I)-1):
        for j in range(1,len(I[0])-1):
            for k in [(l,m) for l in range(-1,2) for m in range(-1,2) if (m!=0 or l!=0)]:
                weight = np.exp(-0.5*abs(I[i+k[0],j+k[1]].astype(int) - I[i,j].astype(int)))
                G.insertEdge(Vertex(YY*(i+k[0]) + (j+k[1])),Vertex(YY*(i) + (j)),Edge(weight))
                G.insertEdge(Vertex(YY*(i) + (j)),Vertex(YY*(i+k[0]) + (j+k[1])),Edge(weight))
    f,G = ford_fulkerson(G,'s','t')
    res = np.zeros((YY,XX))
    for i in range(len(I)):
        for j in range(len(I[0])):
            if G.getEdge(G.getVertexIdx(Vertex(YY*(i) + (j))),G.getVertexIdx(Vertex('t'))).flow>0:
                res[i,j] = 255
    plt.imshow(res)
    plt.gray()
    plt.show()

def cut2():
    I = cv2.imread('min_cut_seg_2.png', cv2.IMREAD_GRAYSCALE)
    YY,XX = I.shape
    # korpus smiglowca
    scrible_FG = np.zeros((YY,XX),dtype=np.ubyte)
    scrible_FG[29:38, 30:43] = 255

    # dol i gora obrazka
    scrible_BG = np.zeros((YY,XX),dtype=np.ubyte)
    scrible_BG[0:10, 0:63] = 255
    scrible_BG[50:62, 0:62] = 255

    I = cv2.resize(I,(32,32))
    scrible_BG = cv2.resize(scrible_BG,(32,32))
    scrible_FG = cv2.resize(scrible_FG,(32,32))
    hist_FG = cv2.calcHist([I],[0],scrible_FG,[256],[0,256])
    hist_FG = hist_FG/sum(hist_FG)

    hist_BG = cv2.calcHist([I],[0],scrible_BG,[256],[0,256])
    hist_BG = hist_BG/sum(hist_BG)

    YY,XX = I.shape
    G = Graph_List()
    for i in range(len(I)):
        for j in range(len(I[0])):
            G.insertVertex(Vertex(YY*i + j))
    G.insertVertex(Vertex('s'))
    G.insertVertex(Vertex('t'))
    for i in range(len(I)):
        for j in range(len(I[0])):
            if scrible_FG[i,j] == 255:
                G.insertEdge(Vertex('s'),Vertex(YY*(i) + (j)),Edge(inf))
                G.insertEdge(Vertex(YY*(i) + (j)),Vertex('t'),Edge(0))
            elif scrible_BG[i,j] == 255:
                G.insertEdge(Vertex('s'),Vertex(YY*(i) + (j)),Edge(0))
                G.insertEdge(Vertex(YY*(i) + (j)),Vertex('t'),Edge(inf))
            else:
                G.insertEdge(Vertex('s'),Vertex(YY*(i) + (j)),Edge(hist_FG[I[i,j]]))
                G.insertEdge(Vertex(YY*(i) + (j)),Vertex('t'),Edge(hist_BG[I[i,j]]))

    for i in range(1,len(I)-1):
        for j in range(1,len(I[0])-1):
            for k in [(-1,-1),(1,1),(1,-1),(-1,1)]:#[(l,m) for l in range(-1,2) for m in range(-1,2) if (m!=0 or l!=0)]:
                weight = np.exp(-0.5*abs(I[i+k[0],j+k[1]].astype(int) - I[i,j].astype(int)))
                G.insertEdge(Vertex(YY*(i+k[0]) + (j+k[1])),Vertex(YY*(i) + (j)),Edge(weight))
                G.insertEdge(Vertex(YY*(i) + (j)),Vertex(YY*(i+k[0]) + (j+k[1])),Edge(weight))
    f,G = ford_fulkerson(G,'s','t')
    res = np.zeros((YY,XX))
    for i in range(len(I)):
        for j in range(len(I[0])):
            if G.getEdge(G.getVertexIdx(Vertex('t')),G.getVertexIdx(Vertex(YY*(i) + (j)))).flow>0:
                res[i,j] = 255
    plt.imshow(res)
    plt.show()

def main():
    cut1()
    cut2()
    pass

if __name__=='__main__':
    main()