import time
def naiwe_method(txt,mask):
    start = 0
    counter = 0
    porownania = 0
    while start+len(mask) != len(txt)+1:
        for i in range(len(mask)):
            porownania += 1
            if txt[i+start] != mask[i]:
                break
        else:
            counter+=1
        start +=1
    return f"{counter};{porownania}"

def hash(strr):
    hw = 0
    d = 256
    q = 101
    for i in range(len(strr)):
        hw = (hw*d + ord(strr[i])) % q
    return hw



def next_hash(hS,Sm,Smn,h):
    d = 256
    q = 101
    x = ((d * (hS - ord(Sm) * h) + ord(Smn)) % q)
    return x if x > 0 else x+q

def rabin_karp(txt, mask):
    start = 0
    counter = 0
    porownania = 0
    kolizje = 0
    hW = hash(mask)
    h = 1
    d = 256
    q = 101
    for i in range(len(mask)-1):
        h = (h*d) % q 
    hS = hash(txt[0:len(mask)])
    while start+len(mask) != len(txt)+1:
        if hW == hS:
            for i in range(len(mask)):
                porownania += 1
                if txt[i+start] != mask[i]:
                    kolizje +=1
                    break
            else:
                counter+=1
        try:
            porownania += 1
            hS = next_hash(hS,txt[start],txt[start + len(mask)],h)
        except:
            pass
        start +=1
        
    return f"{counter};{porownania};{kolizje}"   

def kmp_table(W):
    pos = 1
    cnd = 0
    n = 0
    T = [0 for i in range(len(W)+1)]
    T[0] = -1
    while pos < len(W):
        n += 1
        if W[pos] == W[cnd]:
            T[pos] = T[cnd]
        else:
            T[pos] = cnd
            n += 1
            while cnd>=0 and W[pos]!=W[cnd]:
                cnd = T[cnd]
        pos += 1
        cnd += 1
    T[pos] = cnd
    return T,n

def KMP(S, W):
    m = 0
    i = 0
    T,n = kmp_table(W)
    nP = 0
    P = []
    while m < len(S):
        n+=1
        if W[i] == S[m]:
            m+=1
            i+=1
            if i == len(W):
                P.append(m-i) 
                nP+=1
                if T[i] != -1:i = T[i] 
        else:
            i = T[i]
            if i<0:
                m+=1
                i+=1
    return f"{nP};{n}"

def main():
    with open("lotr.txt", encoding='utf-8') as f:
        text = f.readlines()
    S = ' '.join(text).lower()
    print(naiwe_method(S,"time."))
    print(rabin_karp(S,"time."))
    print(KMP(S,"time."))



if __name__ == '__main__':
    main()