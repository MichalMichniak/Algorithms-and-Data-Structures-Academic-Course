from math import inf
import random
import time

def shell_sort(lst):
    h = len(lst)//2
    while h != 0:
        for i in range(h):
            idx = i+h
            while idx<len(lst):
                if lst[idx] < lst[idx-h]:
                    temp = idx
                    while temp-h>=0 and lst[temp] < lst[temp-h]:
                        lst[temp],lst[temp-h] = lst[temp-h],lst[temp]
                        temp -= h
                idx+=h
        h = h//2
    return lst

def sort_test(lst):
    for i in range(1, len(lst)):
        if lst[i]<lst[i-1]:
            print("NIEE")
            return
    print("TAK")
    return

def main():
    lst = [random.randint(0,99) for i in range(10000)]
    t_start = time.perf_counter()
    # testowana metoda
    shell_sort(lst)
    t_stop = time.perf_counter()
    print("Czas obliczeń:", "{:.7f}".format(t_stop - t_start))
    for i in range(10):
        lst = [random.randint(0,99) for i in range(10000)]
        sort_test(shell_sort(lst))
    pass


if __name__ == '__main__':
    main()