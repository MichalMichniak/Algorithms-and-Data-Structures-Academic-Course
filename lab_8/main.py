import random
import time

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
    
    def __repr__(self):
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

    def repair(self,temp):
        while self.left(temp) < len(self.tab):
                if self.right(temp) < len(self.tab):
                    if (self.tab[self.right(temp)]<self.tab[self.left(temp)]):
                        if self.tab[temp]<self.tab[self.left(temp)]:
                            self.tab[temp],self.tab[self.left(temp)] = self.tab[self.left(temp)],self.tab[temp]
                            temp = self.left(temp)
                            continue
                        else:
                            break
                    elif self.tab[temp]<self.tab[self.right(temp)]:
                        self.tab[temp],self.tab[self.right(temp)] = self.tab[self.right(temp)],self.tab[temp]
                        temp = self.right(temp)
                        continue
                    else:
                        break
                else:
                    if (self.tab[temp]<self.tab[self.left(temp)]):
                        self.tab[temp],self.tab[self.left(temp)] = self.tab[self.left(temp)],self.tab[temp]
                        temp = self.left(temp)
                        break
                    else:
                        break

    def heapify(self):
        root_idx = self.parent(len(self.tab)-1)
        #temp = root_idx
        while root_idx!= -1:
            self.repair(root_idx)
            root_idx -= 1
            #temp = root_idx
        pass


    def sort_from_heap(self):
        if self.tab == []: return None
        lenght = len(self.tab)
        while lenght!=0:
            self.tab[0],self.tab[lenght-1] = self.tab[lenght-1],self.tab[0]
            lenght -= 1
            indx = 0
            while self.right(indx) < lenght:
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
            else:
                if self.left(indx) < lenght:
                    if self.tab[self.left(indx)] > self.tab[indx]:
                        self.tab[self.left(indx)],self.tab[indx] = self.tab[indx],self.tab[self.left(indx)]
        return self.tab

    def __init__(self,tab = None):
        if tab == None: 
            self.tab = []
            return
        self.tab = tab
        self.heapify()

def sort_test(lst):
    for i in range(1, len(lst)):
        if lst[i]<lst[i-1]:
            print("NIEE")
            return
    print("TAK")
    return
        

def main():
    heap = Heap([Elem(i[0],i[1]) for i in [(5,'A'), (5,'B'), (7,'C'), (2,'D'), (5,'E'), (1,'F'), (7,'G'), (5,'H'), (1,'I'), (2,'J')]])
    heap.print_tab()
    print(heap.sort_from_heap())
    heap = Heap([random.randint(0,99) for i in range(10000)])
    print(heap.sort_from_heap())
    lst = [random.randint(0,99) for i in range(10000)]
    t_start = time.perf_counter()
    # testowana metoda
    heap = Heap(lst)
    heap.sort_from_heap()
    t_stop = time.perf_counter()
    print("Czas obliczeń:", "{:.7f}".format(t_stop - t_start))
    for i in range(50):
        lst = [random.randint(0,99) for i in range(10000)]
        heap = Heap(lst)
        sort_test(heap.sort_from_heap())
    pass


if __name__ == '__main__':
    main()