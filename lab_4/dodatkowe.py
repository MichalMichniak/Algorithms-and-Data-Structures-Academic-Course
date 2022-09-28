from random import random
from typing import List
class Skip_lst_elem:
    def __init__(self,height,key,data) -> None:
        self.pointers : List[Skip_lst_elem] = [None for i in range(height)]
        self.key = key
        self.data = data
        pass

def randomLevel(p, maxLevel):
    lvl = 1   
    while random() < p and lvl <maxLevel:
        lvl = lvl + 1
    return lvl

class Skip_lst:
    def __init__(self, height) -> None:
        self.head = Skip_lst_elem(height , None, None)
        self.max_height = height
        pass

    def search(self,key):
        temp = self.head
        for i in list(range(self.max_height))[::-1]:
            while temp.pointers[i] != None:
                if temp.pointers[i].key<key:
                    temp = temp.pointers[i]
                elif temp.pointers[i].key == key:
                    return temp.pointers[i].data
                else:
                    break
        else:
            raise ValueError("nie znaleziono danych")
    
    def insert(self, key, data):
        ## TODO: takie same klucze
        new_height = randomLevel(0.5 , self.max_height)
        new_elem = Skip_lst_elem(new_height,key, data)
        temp : Skip_lst_elem = self.head
        pointers_t = [None for i in range(self.max_height)]
        for i in list(range(self.max_height))[::-1]:
            while temp.pointers[i] != None:
                if temp.pointers[i].key < key:
                    temp = temp.pointers[i]
                elif temp.pointers[i].key == key:
                    temp.pointers[i].data = data
                    return
                else:
                    pointers_t[i] = temp
                    break
            else:
                pointers_t[i] = temp
        pointers_t = pointers_t[:new_height]
        for i in range(new_height):
            new_elem.pointers[i] = pointers_t[i].pointers[i]
            pointers_t[i].pointers[i] = new_elem

    def remove(self,key):
        temp = self.head
        pointers_t = [None for i in range(self.max_height)]
        for i in list(range(self.max_height))[::-1]:
            while temp.pointers[i] != None:
                if temp.pointers[i].key<key:
                    temp = temp.pointers[i]
                elif temp.pointers[i].key == key:
                    pointers_t[i] = temp
                    if i == 0:
                        for i in range(len(pointers_t)):
                            if pointers_t[i] != None:
                                #if pointers_t[i].pointers[i] != None:
                                    if pointers_t[i].pointers[i].key == key:
                                        pointers_t[i].pointers[i] = pointers_t[i].pointers[i].pointers[i]
                        return
                    break
                else:
                    break
        else:
            raise ValueError("nie znaleziono danych")

    def __str__(self) -> str:
        temp = self.head.pointers[0]
        strr = '{'
        while temp != None:
            strr += f" {temp.key}: {temp.data},"
            temp = temp.pointers[0]
        strr = strr[:-1]
        strr += '}'
        return strr


    def displayList_(self):
        node = self.head.pointers[0]  # pierwszy element na poziomie 0
        keys = []                           # lista kluczy na tym poziomie
        while(node != None):
            keys.append(node.key)
            node = node.pointers[0]

        for lvl in range(self.max_height-1, -1, -1):
            print("{}: ".format(lvl), end=" ")
            node = self.head.pointers[lvl]
            idx = 0
            while(node != None):                
                while node.key>keys[idx]:
                    print("  ", end=" ")
                    idx+=1
                idx+=1
                print("{:2d}".format(node.key), end=" ")     
                node = node.pointers[lvl]    
            print("")

alphabet = " ABCDEFGHIJKLMNOPRST"

def main():
    slst = Skip_lst(4)
    for i in range(1,16):
        slst.insert(i, alphabet[i])
    print(slst)
    print(slst.search(2))
    slst.insert(2,'Z')
    print(slst.search(2))
    slst.remove(5)
    slst.remove(6)
    slst.remove(7)
    slst.displayList_()
    slst.insert(6,'W')
    slst.displayList_()

if __name__ == '__main__':
    main()