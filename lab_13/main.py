import numpy as np
import cv2
import cmath
from math import inf

def string_compare(P, T, i, j):
    if i == 0:
         return j
    if j == 0:
        return i
    zamian    = string_compare(P,T,i-1,j-1) + int(P[i]!=T[j])
    wstawien = string_compare(P,T,i,j-1) + 1
    usuniec   = string_compare(P,T,i-1,j) + 1
    najnizszy_koszt = min(min(zamian, wstawien), usuniec)
    return najnizszy_koszt

def string_compare_PD(P, T):
    # if i == 0:
    #      return j
    # if j == 0:
    #     return i
    D = np.zeros([len(P),len(T)])
    tab_rodzic = np.array([['X' for i in range(len(T))] for i in range(len(P))])
    D[0,:] = np.array([i for i in range(len(T))])
    D[:,0] = np.array([i for i in range(len(P))])
    tab_rodzic[0,1:] = np.array(['I' for i in range(len(T)-1)])
    tab_rodzic[1:,0] = np.array(['D' for i in range(len(P)-1)])
    for i in range(1,len(P)):
        for j in range(1,len(T)):
            zamian = D[i-1,j-1] + (P[i]!=T[j])
            wstawien = D[i,j-1] + 1
            usuniec = D[i-1,j] + 1
            najnizszy_koszt = min(zamian, wstawien, usuniec)
            D[i,j] = najnizszy_koszt
            tab_rodzic[i,j] = ('S' if P[i]!=T[j] else 'M') if zamian == najnizszy_koszt else ('D' if najnizszy_koszt == usuniec else 'I')
    # zamian = string_compare(P,T,i-1,j-1) + int(P[i]!=T[j])
    # wstawień = string_compare(P,T,i,j-1) + 1
    # usunięć = string_compare(P,T,i-1,j) + 1
    return D[-1,-1]

def string_compare_PD_strategy(P, T):
    # if i == 0:
    #      return j
    # if j == 0:
    #     return i
    D = np.zeros([len(P),len(T)])
    tab_rodzic = np.array([['X' for i in range(len(T))] for i in range(len(P))])
    D[0,:] = np.array([i for i in range(len(T))])
    D[:,0] = np.array([i for i in range(len(P))])
    tab_rodzic[0,1:] = np.array(['I' for i in range(len(T)-1)])
    tab_rodzic[1:,0] = np.array(['D' for i in range(len(P)-1)])
    for i in range(1,len(P)):
        for j in range(1,len(T)):
            zamian = D[i-1][j-1] + (P[i]!=T[j])
            wstawien = D[i][j-1] + 1
            usuniec = D[i-1][j] + 1
            najnizszy_koszt = min(zamian, wstawien, usuniec)
            D[i,j] = najnizszy_koszt
            tab_rodzic[i,j] = ('S' if P[i]!=T[j] else 'M') if zamian == najnizszy_koszt else ('D' if najnizszy_koszt == usuniec else 'I')
    # zamian = string_compare(P,T,i-1,j-1) + int(P[i]!=T[j])
    # wstawień = string_compare(P,T,i,j-1) + 1
    # usunięć = string_compare(P,T,i-1,j) + 1
    strr = ''
    while i !=0 and j!=0:
        strr=tab_rodzic[i,j]+strr
        if tab_rodzic[i,j] == 'I':
            j-=1
        elif tab_rodzic[i,j] == 'D':
            i-=1
        else:
            i-=1
            j-=1
    strr=tab_rodzic[i,j]+strr
    return  strr


def string_compare_PD_subsequence(P, T):
    # if i == 0:
    #      return j
    # if j == 0:
    #     return i
    D = np.zeros([len(P),len(T)])
    tab_rodzic = np.array([['X' for i in range(len(T))] for i in range(len(P))])
    #D[0,:] = np.array([i for i in range(len(T))])
    D[:,0] = np.array([i for i in range(len(P))])
    #tab_rodzic[0,1:] = np.array(['I' for i in range(len(T)-1)])
    tab_rodzic[1:,0] = np.array(['D' for i in range(len(P)-1)])
    for i in range(1,len(P)):
        for j in range(1,len(T)):
            zamian = D[i-1][j-1] + (P[i]!=T[j])
            wstawien = D[i][j-1] + 1
            usuniec = D[i-1][j] + 1
            najnizszy_koszt = min(zamian, wstawien, usuniec)
            D[i,j] = najnizszy_koszt
            tab_rodzic[i,j] = ('S' if P[i]!=T[j] else 'M') if zamian == najnizszy_koszt else ('D' if najnizszy_koszt == usuniec else 'I')
    # zamian = string_compare(P,T,i-1,j-1) + int(P[i]!=T[j])
    # wstawień = string_compare(P,T,i,j-1) + 1
    # usunięć = string_compare(P,T,i-1,j) + 1
    i =len(P)-1
    j = 0
    for k in range(len(T)):
            if ( D[i][k] < D[i][j] ):
                    j = k
    return  j - len(P) + 1

def string_compare_PD_longest_subsequence(P, T):
    # if i == 0:
    #      return j
    # if j == 0:
    #     return i
    D = np.zeros([len(P),len(T)])
    tab_rodzic = np.array([['X' for i in range(len(T))] for i in range(len(P))])
    D[0,:] = np.array([i for i in range(len(T))])
    D[:,0] = np.array([i for i in range(len(P))])
    tab_rodzic[0,1:] = np.array(['I' for i in range(len(T)-1)])
    tab_rodzic[1:,0] = np.array(['D' for i in range(len(P)-1)])
    for i in range(1,len(P)):
        for j in range(1,len(T)):
            zamian = D[i-1,j-1] + ( inf if P[i]!=T[j] else 0 )
            wstawien = D[i,j-1] + 1
            usuniec = D[i-1,j] + 1
            najnizszy_koszt = min(zamian, wstawien, usuniec)
            D[i,j] = najnizszy_koszt
            tab_rodzic[i,j] = ('S' if P[i]!=T[j] else 'M') if zamian == najnizszy_koszt else ('D' if najnizszy_koszt == usuniec else 'I')
    # zamian = string_compare(P,T,i-1,j-1) + int(P[i]!=T[j])
    # wstawień = string_compare(P,T,i,j-1) + 1
    # usunięć = string_compare(P,T,i-1,j) + 1
    strr = ''
    while i !=0 and j!=0:
        if tab_rodzic[i,j] == 'I':
            j-=1
        elif tab_rodzic[i,j] == 'D':
            i-=1
        else:
            strr = T[j] + strr
            i-=1
            j-=1
    return strr




def string_compare_PD_monotonic_subsequence(T):
    # if i == 0:
    #      return j
    # if j == 0:
    #     return i
    P = [int(i) for i in T[1:]]
    P.sort()
    P = [str(i) for i in P]
    P = ''.join(P)
    P = " "+P
    print(P)
    D = np.zeros([len(P),len(T)])
    tab_rodzic = np.array([['X' for i in range(len(T))] for i in range(len(P))])
    D[0,:] = np.array([i for i in range(len(T))])
    D[:,0] = np.array([i for i in range(len(P))])
    tab_rodzic[0,1:] = np.array(['I' for i in range(len(T)-1)])
    tab_rodzic[1:,0] = np.array(['D' for i in range(len(P)-1)])
    for i in range(1,len(P)):
        for j in range(1,len(T)):
            zamian = D[i-1,j-1] + ( inf if P[i]!=T[j] else 0 )
            wstawien = D[i,j-1] + 1
            usuniec = D[i-1,j] + 1
            najnizszy_koszt = min(zamian, wstawien, usuniec)
            D[i,j] = najnizszy_koszt
            tab_rodzic[i,j] = ('S' if P[i]!=T[j] else 'M') if zamian == najnizszy_koszt else ('D' if najnizszy_koszt == usuniec else 'I')
    # zamian = string_compare(P,T,i-1,j-1) + int(P[i]!=T[j])
    # wstawień = string_compare(P,T,i,j-1) + 1
    # usunięć = string_compare(P,T,i-1,j) + 1
    strr = ''
    while i !=0 and j!=0:
        if tab_rodzic[i,j] == 'I':
            j-=1
        elif tab_rodzic[i,j] == 'D':
            i-=1
        else:
            strr = T[j] + strr
            i-=1
            j-=1
    return strr


def main():
    P = ' kot'
    T = ' pies'
    print(string_compare(P,T,len(P)-1,len(T)-1))
    P = ' biały autobus'
    T = ' czarny autokar'
    print(string_compare_PD(P,T))
    P = ' thou shalt not'
    T = ' you should not'
    print(string_compare_PD_strategy(P,T))
    P = ' bin'
    T = ' mokeyssbanana'
    print(string_compare_PD_subsequence(P, T))
    P = ' democrat'
    T = ' republican'
    print(string_compare_PD_longest_subsequence(P, T))
    T = ' 243517698'
    print(string_compare_PD_monotonic_subsequence(T))
    pass

if __name__ == '__main__':
    main()