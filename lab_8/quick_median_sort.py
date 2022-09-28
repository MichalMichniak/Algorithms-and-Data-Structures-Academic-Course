import random
import time
def median_3(a, b, c):
    return max(min(a,b),min(c,max(a,b)))

def median_5(a, b, c, d, e):
      f=max(min(a,b),min(c,d)) # usuwa najmniejsza z 4
      g=min(max(a,b),max(c,d)) # usuwa największą z 4
      return median_3(e,f,g)

def median_4(a,b,c,d):
    one = max(min(a,b),min(c,d))
    two = min(max(a,b),max(c,d))
    return (one + two)/2

def median_2(a,b):
    return (a+b)/2

def median(lst):
    if len(lst) == 5:
        return median_5(*lst)
    if len(lst) == 4:
        return median_4(*lst)
    if len(lst) == 3:
        return median_3(*lst)
    if len(lst) == 2:
        return median_2(*lst)
    if len(lst) == 1:
        return lst[0]

def magiczne_wtorki(lst):
    if len(lst)%5!=0:
        tab = [median(lst[5*i:5*i+5]) if i!=len(lst)//5 else median(lst[5*i:]) for i in range(len(lst)//5+1)]
    else:
        tab = [median(lst[5*i:5*i+5]) for i in range(len(lst)//5)]
    return magiczne_wtorki(tab) if len(tab) != 1 else tab[0]

def quicksort_magiczne_piatki(lst):
    if len(lst) <= 1: return lst
    
    pivot = magiczne_wtorki(lst)
    bigger = []
    equal = []
    lower = []
    for i in lst:
        if i<pivot:
            lower.append(i)
        elif i>pivot:
            bigger.append(i)
        else:
            equal.append(i)
    return quicksort(lower) + equal + quicksort(bigger)
    pass


def quicksort(lst):
    if len(lst) <= 1: return lst
    pivot = lst[0]
    bigger = []
    equal = []
    lower = []
    for i in lst:
        if i<pivot:
            lower.append(i)
        elif i>pivot:
            bigger.append(i)
        else:
            equal.append(i)
    return quicksort(lower) + equal + quicksort(bigger)
    pass

def sort_test(lst):
    for i in range(1, len(lst)):
        if lst[i]<lst[i-1]:
            print("NIEE")
            return "NIEE"
    print("TAK")
    return

def main():
    lst = [random.randint(0,99) for i in range(10000)]
    t_start = time.perf_counter()
    # testowana metoda
    quicksort(lst)
    t_stop = time.perf_counter()
    print("Czas obliczeń:", "{:.7f}".format(t_stop - t_start))
    t_start = time.perf_counter()
    # testowana metoda
    quicksort_magiczne_piatki(lst)
    t_stop = time.perf_counter()
    print("Czas obliczeń:", "{:.7f}".format(t_stop - t_start))
    pass


if __name__ == '__main__':
    main()