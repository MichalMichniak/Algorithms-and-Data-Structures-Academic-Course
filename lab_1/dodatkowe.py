
from typing import List, Tuple

class Matrix:
    def __init__(self, t, param=0) -> None:
        if type(t) is tuple:
            self.__lst = [[param for j in range(t[1])] for i in range(t[0])]
        else:
            self.__lst = t[:][:]
        pass
    
    def __add__(self,other):
        if self.size() != other.size(): raise ValueError
        return Matrix([[ self.__lst[i][j]+other.__lst[i][j] for j in range(len(self.__lst[i]))] for i in range(len(self.__lst))])
    
    def __getitem__(self, index):
        return self.__lst[index]
    
    def __mul__(self, other): ## dodane mnożenie przez skalar 
        if type(other) != Matrix:
            if self.size()[1] != other.size()[0]: raise ValueError
            return Matrix([[other*self[i][j] for j in range(len(self.__lst[0]))] for i in range(len(self.__lst))])
        return Matrix([[sum([self.__lst[i][n]*other.__lst[n][j] for n in range(len(self.__lst[i]))]) for j in range(len(other.__lst[0]))] for i in range(len(self.__lst))])
    
    def __str__(self):
        s = ""
        for i in self.__lst:
            for j in i:
                s+=str(j)+" "
            s += "\n"
        return s
    
    def size(self):
        return len(self.__lst), len(self.__lst[0])

    def __len__(self):
        return len(self.__lst)

def transpose(m : Matrix) -> Matrix:
    t = m.size()
    return Matrix([[m[j][i] for j in range(t[0])] for i in range(t[1])])


def det2x2(a1,a2,a3,a4):
    return a1*a4 - a3*a2

def chio(m : Matrix):
    if m.size()[0] == 2:
        return det2x2(m[0][0],m[0][1],m[1][0],m[1][1])
    sign_change = 1
    i = 1
    n = m
    while n[0][0] == 0:
        m0 = m[0][:]
        n = Matrix([m[j][:] if (j!=0) and (j!=i) else m0 if j==i else m[i][:] for j in range(len(m))])
        i+=1
        sign_change = -1
        if i > len(m):
            return 0
    m = n
    m_new = Matrix([[det2x2(m[0][0],m[0][j],m[i][0],m[i][j]) for j in range(1,len(m[0]))] for i in range(1,len(m))])
    return (chio(m_new)*((1/m[0][0])**(len(m)-2))) * sign_change


m = Matrix([

[5 , 1 , 1 , 2 , 3],

[4 , 2 , 1 , 7 , 3],

[2 , 1 , 2 , 4 , 7],

[9 , 1 , 0 , 7 , 0],

[1 , 4 , 7 , 2 , 2]

])
print(chio(m))

m = Matrix([
     [0 , 1 , 1 , 2 , 3],
     [4 , 2 , 1 , 7 , 3],
     [2 , 1 , 2 , 4 , 7],
     [9 , 1 , 0 , 7 , 0],
     [1 , 4 , 7 , 2 , 2]
    ])

print(chio(m))