from math import inf
import random
import time

class Elem_lst:
    def __init__(self,key,data) -> None:
        self.key = key
        self.data = data
        pass

    def __gt__(self,other):
        if type(other) is Elem_lst:
            return self.key>other.key
        return self.key>other

    def __repr__(self):
        return f"{self.key} : {self.data}"

## niestabilne
def swap(lst):
    for i in range(len(lst)):
        maximum = -inf
        idx = 0
        for j in range(len(lst)-i):
            if lst[j]>maximum:
                idx = j
                maximum = lst[j]
        lst[-i-1],lst[idx] = lst[idx],lst[-i-1]
        maximum = -inf
        idx = 0
    return lst

## niestabilne
def shift(lst):
    for i in range(len(lst)):
        maximum = -inf
        idx = 0
        for j in range(i,len(lst)):
            if lst[j]>maximum:
                idx = j
                maximum = lst[j]
        temp = lst[idx]
        lst.pop(idx)
        lst.insert(0,temp)
        maximum = -inf
        idx = 0
    return lst



def sort_test(lst):
    for i in range(1, len(lst)):
        if lst[i]<lst[i-1]:
            print("NIEE")
            return
    print("TAK")
    return

def main():
    lst = [Elem_lst(i[0],i[1]) for i in [(5,'A'), (5,'B'), (7,'C'), (2,'D'), (5,'E'), (1,'F'), (7,'G'), (5,'H'), (1,'I'), (2,'J')]]
    print(swap(lst))
    print(shift(lst))
    lst = [random.randint(0,1000) for i in range(10000)]
    t_start = time.perf_counter()
    swap(lst)
    t_stop = time.perf_counter()
    print("Czas obliczeń:", "{:.7f}".format(t_stop - t_start))
    lst = [random.randint(0,1000) for i in range(10000)]
    t_start = time.perf_counter()
    shift(lst)
    t_stop = time.perf_counter()
    print("Czas obliczeń:", "{:.7f}".format(t_stop - t_start))
    for i in range(50):
        lst = [random.randint(0,1000) for i in range(100)]
        sort_test(swap(lst))
    pass


if __name__ == '__main__':
    main()