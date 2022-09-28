import numpy as np
from copy import copy

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
    
    def get_array(self):
        return np.array(self.matrix)

    def deg(self,vertex_id):
        return np.sum(self.matrix[vertex_id])

def izomorphizm(M,P : Graph_Matrix,G : Graph_Matrix)-> bool:
    return (P.get_array()==M@((M@G.get_array()).T)).all()

def prune(M,G : Graph_Matrix,P : Graph_Matrix, current):
    M_copy = M.copy() * 6
    while not (M_copy == M).all():
        for i in range(current,len(M)):
            for j in range(len(M[0])):
                if M[i,j] == 1:
                    for x in P.neighbours(i):
                        for y in G.neighbours(j):
                            if M[x,y] == 1:
                                break
                        else:
                            M[i,j] = 0
        M_copy = M.copy()
    return M

def M0(G : Graph_Matrix,P : Graph_Matrix):
    M = np.zeros((G.order(),P.order()))
    for i in range(P.order()):
        for j in range(G.order()):
            if P.deg(i) >= G.deg(j):
                M[j,i] = 1
    return M

def ullman1(used_columns, current_row,G : Graph_Matrix,P : Graph_Matrix, M : np.ndarray = None, no_recursion = 0):
    rec = 0 
    rec+=1
    if M is None: M = np.ones((P.order(),G.order()))
    if current_row == len(M):
        if izomorphizm(M,P,G):
            return 1,rec
        return 0,rec
    #M_prim = prune(M.copy(), G, P, current_row)
    M_prim = M.copy()
    count = 0
    
    for i in [j for j in range(M.shape[1]) if (j not in used_columns) and M_prim[current_row,j]==1]:
        u_prim = used_columns.copy()
        u_prim.append(i)
        M_prim_prim = M_prim.copy()
        row = np.array([0 for k in range(len(M[current_row,:]))])
        row[i] = 1
        M_prim_prim[current_row,:] = row
        temp = ullman1(u_prim, current_row+1, G, P, M_prim_prim)
        count += temp[0]
        rec += temp[1]
    return count,rec

def ullman2(used_columns, current_row,G : Graph_Matrix,P : Graph_Matrix, M : np.ndarray = None, no_recursion = 0):
    rec = 0 
    rec+=1
    if M is None: M = M0(P,G)
    if current_row == len(M):
        if izomorphizm(M,P,G):
            return 1,rec
        return 0,rec
    #M_prim = prune(M.copy(), G, P, current_row)
    M_prim = M.copy()
    count = 0
    for i in [j for j in range(M.shape[1]) if (j not in used_columns) and M_prim[current_row,j]==1]:
        u_prim = used_columns.copy()
        u_prim.append(i)
        M_prim_prim = M_prim.copy()
        row = np.array([0 for k in range(len(M[current_row,:]))])
        row[i] = 1
        M_prim_prim[current_row,:] = row
        temp = ullman2(u_prim, current_row+1, G, P, M_prim_prim)
        count += temp[0]
        rec += temp[1]
    return count,rec


def ullman3(used_columns, current_row,G : Graph_Matrix,P : Graph_Matrix, M : np.ndarray = None, no_recursion = 0):
    rec = 0 
    rec+=1
    if M is None: M = M0(P,G)
    if current_row == len(M):
        if izomorphizm(M,P,G):
            return 1,rec
        return 0,rec
    M_prim = prune(M.copy(), G, P, current_row)
    #M_prim = M.copy()
    count = 0
    for i in [j for j in range(M.shape[1]) if (j not in used_columns) and M_prim[current_row,j]==1]:
        u_prim = used_columns.copy()
        u_prim.append(i)
        M_prim_prim = M_prim.copy()
        row = np.array([0 for k in range(len(M[current_row,:]))])
        row[i] = 1
        M_prim_prim[current_row,:] = row
        temp = ullman3(u_prim, current_row+1, G, P, M_prim_prim)
        count += temp[0]
        rec += temp[1]
    return count,rec


def main():
    graph_G = [ ('A','B',1), ('B','F',1), ('B','C',1), ('C','D',1), ('C','E',1), ('D','E',1)]
    graph_P = [ ('A','B',1), ('B','C',1), ('A','C',1)]
    G = Graph_Matrix()
    for i in graph_G:
        G.insertVertex(Vertex(i[0]))
        G.insertVertex(Vertex(i[1]))
        G.insertEdge(Vertex(i[0]),Vertex(i[1]),1)
    P = Graph_Matrix()
    for i in graph_P:
        P.insertVertex(Vertex(i[0]))
        P.insertVertex(Vertex(i[1]))
        P.insertEdge(Vertex(i[0]),Vertex(i[1]),1)
    print(ullman1([],0,G,P))
    print(ullman2([],0,G,P))
    print(ullman3([],0,G,P))
    pass

if __name__ == '__main__':
    main()