class Elem:
    def __init__(self,key , data) -> None:
        self.key = key
        self.data = data
        pass

    def __lt__(self, other):
        return other.key > self.key
    
    def __gt__(self, other):
        return other.key < self.key
    
    def __eq__(self, other):
        return other.key == self.key
    
    def __str__(self):
        return f"{self.key}:{self.data}"

class Heap:
    def __init__(self) -> None:
        self.tab = []
        pass

    def is_empty(self):
        return self.tab == []

    def peek(self):
        if self.is_empty(): raise ValueError("brak danej do zwrocenia")
        return self.tab[0].data
    
    def enqueue(self, key, data):
        indx = len(self.tab)
        self.tab.append(Elem(key,data))
        while self.parent(indx)>=0:
            if self.tab[self.parent(indx)]<self.tab[indx]:
                self.tab[self.parent(indx)],self.tab[indx] = self.tab[indx],self.tab[self.parent(indx)] 
                indx = self.parent(indx)
            else:
                break

    def left(self, i):
        return (2*(i+1)) -1

    def right(self, i):
        return 2*(i+1)

    def parent(self,i):
        return (i-1)//2

    def dequeue(self):
        if self.tab == []: return None
        res = self.peek()
        self.tab[0] = self.tab[-1]
        self.tab.pop()
        indx = 0
        while self.right(indx) < self.tab.__len__():
            if self.tab[indx] < self.tab[self.left(indx)]:
                if self.tab[self.left(indx)] > self.tab[self.right(indx)]:
                    self.tab[self.left(indx)],self.tab[indx] = self.tab[indx],self.tab[self.left(indx)] 
                    indx = self.left(indx)
                else:
                    self.tab[self.right(indx)],self.tab[indx] = self.tab[indx],self.tab[self.right(indx)] 
                    indx = self.right(indx)
            elif self.tab[indx] < self.tab[self.right(indx)]:
                self.tab[self.right(indx)],self.tab[indx] = self.tab[indx],self.tab[self.right(indx)] 
                indx = self.right(indx)
            else:
                break
        return res

    def print_tab(self):
        if self.tab == []: 
            print("{}")
            return
        print ('{', end=' ')
        for i in range(self.tab.__len__()-1):
            print(self.tab[i], end = ', ')
        if self.tab[self.tab.__len__()-1]: print(self.tab[self.tab.__len__()-1] , end = ' ')
        print( '}')

    def print_tree(self, idx, lvl):
        if idx<self.tab.__len__():           
            self.print_tree(self.right(idx), lvl+1)
            print(2*lvl*'  ', self.tab[idx] if self.tab[idx] else None)           
            self.print_tree(self.left(idx), lvl+1)

def main():
    heap = Heap()
    s = "ALGORYTM"
    k = [4, 7, 6, 7, 5, 2, 2, 1]
    for i,j in zip(k,s):
        heap.enqueue(i,j)
    heap.print_tree(0,0)
    heap.print_tab()
    print(heap.dequeue())
    print(heap.peek())
    heap.print_tab()
    while not heap.is_empty():
        print(heap.dequeue())
    heap.print_tab()
    pass


if __name__ == '__main__':
    main()