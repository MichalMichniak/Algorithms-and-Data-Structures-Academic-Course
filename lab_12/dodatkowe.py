
import time
import numpy as np

def hash1(x)->int:
    hw = 0
    d = 256
    q = 101
    for i in range(len(x)):
        hw = (hw*d + ord(x[i])) % q
    return hw

def hash2(x)->int:
    hw = 0
    d = 256
    q = 103
    for i in range(len(x)):
        hw = (hw*d + ord(x[i])) % q 
    return hw


def next_hash(hS,Sm,Smn,h,q):
    d = 256
    x = ((d * (hS - ord(Sm) * h) + ord(Smn)) % q)
    return x if x > 0 else x+q

def hash_maker(f1,f2,n,b):
    return lambda x: (f1(x)+n*f2(x))%b

def check_if_in_set(el, set):
    for i in set:
        for n,j in enumerate(i):
            if el[n] != j:
                break
        else:
            return True
    return False


def bloom_filter(txt,elem):
    n = len(elem)
    P = 0.001
    b = -n*np.log(P)/((np.log(2))**2)
    k = int(np.ceil(np.log(2)*(b/n)))
    b = int(np.ceil(b))
    g = []

    h1 = 1
    h2 = 1
    d = 256
    q1 = 101
    q2 = 103
    for i in range(len(elem[0])-1):
        h1 = (h1*d) % q1
        h2 = (h2*d) % q2

    # funkcje hashujące poprzez kombinację liniową g_{i}
    for i in range(k):
        g.append(hash_maker(hash1,hash2,i,b))
    hsubs = [0 for i in range(b)]
    for n in range(k):
        for i in elem:
            hsubs[g[n](i)%b] = 1
    hs_temp = [hash1(txt[0:0+len(elem[0])]),hash2(txt[0:0+len(elem[0])])]
    hs = [g[i](txt[:len(elem[0])]) for i in range(k)]
    hs2 = [g[i](txt[:len(elem[0])]) for i in range(k)]
    counter = 0
    false_counter = 0
    true_counter = 0
    for m in range(len(txt)-len(elem[0])):
        p = 0
        for i in hs:
            if hsubs[i%b]!=1:
                break
        else:
            if check_if_in_set(txt[m:m+len(elem[0])], elem):
                true_counter +=1
            else:
                false_counter+=1
            counter += 1
        if m+len(elem[0])+1 < len(txt):
            hs_temp[0] = next_hash(hs_temp[0],txt[m],txt[m+len(elem[0])],h1,q1)
            hs_temp[1] = next_hash(hs_temp[1],txt[m],txt[m+len(elem[0])],h2,q2)
        for n,i in enumerate(hs):
            if m+len(elem[0])+1 < len(txt):
                hs[n] = (hs_temp[0] + n*hs_temp[1])%b
    return true_counter,false_counter


def main():
    elem1 = ['gandalf', 'looking', 'blocked', 'comment', 'pouring', 'finally', 'hundred', 'hobbits', 'however', 'popular', 'nothing', 'enjoyed', 'stuffed', 'relaxed', 'himself', 'present', 'deliver', 'welcome', 'baggins', 'further']
    with open("lotr.txt", encoding='utf-8') as f:
        text = f.readlines()
    S = ' '.join(text).lower()
    t_start = time.perf_counter()
    bloom_filter(S,elem1)
    t_stop = time.perf_counter()
    print("Czas obliczeń:", "{:.7f}".format(t_stop - t_start))
    print(bloom_filter(S,elem1))
    
    


if __name__ == '__main__':
    main()