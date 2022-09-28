
from stringprep import b1_set
from typing import List,Tuple
class matrix:
    def __init__(self,tou,par=0)->None:
        if isinstance(tou,tuple):
            self.lista__=[[par for j in range(tou[1])] for i in range(tou[0])]
        else:
            self.lista__=tou
    def __add__(self,other):
        if(matrix.size(self)==matrix.size(other)):
            lst=matrix(matrix.size(self))
            for i in range(len(self.lista__)):
                for j in range(len(self.lista__[i])):
                    lst[i][j]=self.lista__[i][j]+other.lista__[i][j]
            return matrix(lst)
        else:
            return "rozne wymiary macierzy"
    def __mul__(self, other):
        if(matrix.size(self)[1]==matrix.size(other)[0]):
            lst=matrix((self.size()[0],other.size()[1]))
            for i in range(len(self.lista__)):
                for j in range(len(other.lista__[1])):
                    t = []
                    for n in range(len(self.lista__[i])):
                        t.append(self.lista__[i][n]*other.lista__[n][j])
                    lst[i][j]=sum(t)
            return lst
        else:
            return "rozne wymiary macierzy"
    def __getitem__(self,index):
        return self.lista__[index]
    def __str__(self):
        stri = []
        for i in self.lista__:
            stri.append(str(i))
        return '\n'.join(stri)
    def size(self):
        return len(self.lista__),len(self.lista__[0])

def transpose(mat:matrix):
    g=mat.size()
    gt=tuple([g[1],g[0]])
    wyn=matrix(gt)
    for i in range(g[0]):
        for j in range(g[1]):
            wyn[j][i]=mat[i][j]
    return wyn


a=matrix([[1, 0, 2],[-1, 3, 1]])
b=matrix((2,3),1)
c=matrix([[3,1],[2,1],[1,0]])

print(a+b,"\n")
print(a*c,"\n")
print(transpose(a),"\n")
