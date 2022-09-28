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
    
    def __mul__(self, other):
        if self.size()[1] != other.size()[0]: raise ValueError
        if type(other) != Matrix:
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

a = Matrix([ [1, 0, 2],  [-1, 3, 1] ])
b = Matrix([ [3, 1],
  [2, 1],
  [1, 0]])
c = Matrix((2,3), param=1)
print(transpose(a))
print(a+c)
print(a*b)

