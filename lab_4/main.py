class Pair:
    def __init__(self,key,data) -> None:
        self.key = key
        self.data = data
        pass
class Hash_table:
    def __init__(self, size, c1=1, c2=0) -> None:
        self.size = size
        self.tab = [None for i in range(size)]
        self.c1 = c1
        self.c2 = c2        
        pass

    def hash_func(self,key):
        if type(key) == str:
            return sum([ord(i) for i in key])%self.size
        else:
            return key%self.size
    
    def colision(self, key, data, index_hash):
        i_begin = 0
        i = 1
        counter = 0
        first_index = index_hash
        while i != i_begin:
            index_hash = first_index + self.c1 * i + self.c2* i**2
            index_hash %= self.size
            if self.tab[index_hash] != None:
                if (self.tab[index_hash].data == None and self.tab[index_hash].key == None) or self.tab[index_hash].key == key:
                    self.tab[index_hash] = Pair(key,data)
                    return
                else:
                    i+=1
            else:
                self.tab[index_hash] = Pair(key,data)
                return
            counter += 1
            if counter>self.size: 
                raise ValueError("Brak miejsca")
        else:
            raise ValueError("Brak miejsca")



    def insert(self,key, data):
        index_hash = self.hash_func(key)
        if self.tab[index_hash] != None:
            if (self.tab[index_hash].data == None and self.tab[index_hash] == None) or self.tab[index_hash].key == key:
                self.tab[index_hash] = Pair(key,data)
            else:
                self.colision(key, data, index_hash)
        else:
            self.tab[index_hash] = Pair(key,data)
        pass
    
    def search(self,key):
        i = 0
        i_begin = 0
        counter = 0
        index_hash = self.hash_func(key)
        if self.tab[index_hash] == None: raise ValueError("Brak danej")
        if self.tab[index_hash].key != key:
            i += 1
            index_hash += self.c1 * i + self.c2* i**2
            index_hash %= self.size
            counter+=1
        else:
            return self.tab[index_hash].data
        while i!=i_begin:
            if self.tab[index_hash] == None: raise ValueError("Brak danej")
            if self.tab[index_hash].key != key:
                i += 1
                index_hash += self.c1 * i + self.c2* i**2
                index_hash %= self.size
            else:
                return self.tab[index_hash].data
            counter +=1
            if counter>self.size: raise ValueError("Brak danej")
        else:
            raise ValueError("Brak danej")
        
    def remove(self, key):
        i = 0
        i_begin = 0
        counter = 0
        index_hash = self.hash_func(key)
        if self.tab[index_hash] == None: raise ValueError("Brak danej")
        if self.tab[index_hash].key != key:
            i += 1
            index_hash += self.c1 * i + self.c2* i**2
            index_hash %= self.size
        else:
            self.tab[index_hash] = Pair(None,None)
            return
        while i!=i_begin:
            if self.tab[index_hash] == None: raise ValueError("Brak danej")
            if self.tab[index_hash].key != key:
                i += 1
                index_hash += self.c1 * i + self.c2* i**2
                index_hash %= self.size
            else:
                self.tab[index_hash] = Pair(None,None)
                return
            if counter > self.size: raise ValueError("Brak danej")
            counter += 1 
        else:
            raise ValueError("Brak danej")


    def __str__(self):
        strr = '{'

        for i in self.tab:
            if i != None:
                if i.data != None and i.key != None:
                    strr += f"{i.key}:{i.data},"
        if strr[-1] != '{' : strr = strr[:-1]
        strr += '}'
        return strr
    
    def str_debug(self):
        strr = '{'
        for i in self.tab:
            if i != None:
                strr += f"{i.key}:{i.data},"
            else:
                strr += 'None,'
        if strr[-1] != '{' : strr = strr[:-1]
        strr += '}'
        return strr

alphabet = " ABCDEFGHIJKLMNOPRST"

def test_func(c1, c2):
    htable = Hash_table(13,c1,c2)
    
    for i in range(1,14):
        try:
            htable.insert(i*13,alphabet[i])
        except ValueError as msg:
            print(msg)
    print(htable.str_debug())

def test_func_1(c1, c2):
    htable = Hash_table(13,c1,c2)
    try:
        for i in range(1,16):
            if i != 6 and i!=7:
                try:
                    htable.insert(i,alphabet[i])
                except ValueError as msg:
                    print(msg)
            elif i == 6:
                try:
                    htable.insert(18,alphabet[i])
                except ValueError as msg:
                    print(msg)
            elif i == 7:
                try:
                    htable.insert(31,alphabet[i])
                except ValueError as msg:
                    print(msg)
    except ValueError as msg:
        print(msg)
    print(htable.search(5))
    try:
        print(htable.search(14))
    except ValueError as msg:
        print(msg)
    htable.insert(5, 'Z')
    print(htable.search(5))
    print(htable.str_debug())
    htable.remove(5)
    print(htable.str_debug())
    print(htable.search(31))
    htable.insert('test', 'W')
    print(htable)

def main():
    test_func_1(1,0)
    test_func(1,0)
    test_func(0,1)
    test_func_1(0,1)


if __name__ == '__main__':
    main()