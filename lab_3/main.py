
def realloc(tab, size):
    oldSize = len(tab)
    return [tab[i] if i<oldSize else None  for i in range(size)]

class Cyclic_list:
    def __init__(self) -> None:
        self.lst = realloc([],5)
        self.begin = 0
        self.end = 0 
        self.size = 5
        pass

    def is_empty(self):
        return self.begin == self.end
    
    def peek(self):
        return self.lst[self.begin] if self.end != self.begin else None
    
    def dequeue(self):
        if self.end == self.begin: return None
        res = self.lst[self.begin]
        self.lst[self.begin] = None
        self.begin = (self.begin + 1)%self.size
        return res
    
    def enqueue(self, data):
        self.lst[self.end] = data
        self.end = (self.end + 1)%self.size
        if self.end == self.begin:
            new = realloc(self.lst[:self.end], 2*self.size)
            len_begin_lst = self.size-self.end
            new[2*self.size-len_begin_lst:] = self.lst[self.end:]
            self.begin = 2*self.size-len_begin_lst
            self.lst = new
            self.size = self.size * 2

    def __str__(self) -> str:
        temp = self.begin
        strr = ""
        while temp != self.end:
            strr += str(self.lst[temp]) + ' '
            temp = (temp + 1)%self.size
        return strr

    def str_full_lst(self):
        return str(self.lst)

clst = Cyclic_list()
for i in range(1,5):
    clst.enqueue(i)
print(clst.dequeue())
print(clst.peek())
print(clst)
for i in range(5,9):
    clst.enqueue(i)
print(clst.str_full_lst())
while not clst.is_empty():
    print(clst.dequeue())
print(clst)
