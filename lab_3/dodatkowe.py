


def realloc(tab, size):
    oldSize = len(tab)
    return [tab[i] if i<oldSize else None  for i in range(size)]

class Unroled_linked_lst_elem:
    size = 6
    def __init__(self,next = None) -> None:
        self.act_len = 0
        self.next : Unroled_linked_lst_elem = next
        self.lst = realloc([],self.size)
        pass

    def remove(self,index):
        if index>=self.act_len: 
            self.next.remove(index - (self.act_len))
        else:
            self.lst[index:-1] = self.lst[index+1:]
            self.lst[-1] = None
            self.act_len -=1
            if float(self.act_len) < float(self.size/2) and (not (self.next is None)):
                if float(self.next.act_len - 1) < float(self.size/2):
                    self.lst[self.act_len : self.act_len-1 + self.next.act_len+1] = self.next.lst[:self.next.act_len]
                    self.act_len += self.next.act_len
                    self.next = self.next.next
                else:
                    self.lst[self.act_len] = self.next.lst[0]
                    self.next.remove(0)
                    self.act_len += 1




    def add(self,index,data):
        if index>self.act_len: 
            if self.next is None: self.add(self.act_len, data)
            else:self.next.add(index - (self.act_len), data)
        elif self.act_len == self.size:
            self.next = Unroled_linked_lst_elem(self.next)
            rest = self.size - self.size//2
            self.next.lst[:rest] = self.lst[self.size//2:]
            self.lst[self.size//2:] = realloc([], rest)
            self.next.act_len = rest
            self.act_len = self.size//2
            self.add(index, data)
        else:
            self.lst[index+1:] = self.lst[index:-1]
            self.lst[index] = data
            self.act_len += 1

class Unroled_linked_lst:
    def __init__(self) -> None:
        self.lst = Unroled_linked_lst_elem()
        pass

    def insert(self,index, data):
        self.lst.add(index, data)
    
    def get(self,index):
        l = self.lst
        while index>=l.act_len: 
            index = index - l.act_len
            l = l.next
            if l == None: raise ValueError("unroled linked list out of range")
        return l.lst[index]
        
    def __str__(self) -> str:
        strr = ''
        l = self.lst
        i = 0
        while True:
            if l.act_len <= i:
                l = l.next
                i = 0
                if l == None: break
            strr += str(l.lst[i]) + ' '
            i += 1
        
        return strr
    
    def str_tab_debug(self) -> str:
        strr = '\ndebug unroled linked list: \n{\n'
        l = self.lst
        strr += str(l.lst) + f" actual size: {l.act_len}\n" 
        while True:
            l = l.next
            if l == None: break
            strr += str(l.lst) + f" actual size: {l.act_len}\n" 
        strr += '}'
        return strr

    def delete(self, index):
        self.lst.remove(index)
        pass



def main():
    lst = Unroled_linked_lst()
    for i in range(1,10):
        lst.insert(i-1,i)
    print(lst.get(4))
    lst.insert(1,10)
    lst.insert(8,11)
    print(lst)
    lst.delete(1)
    lst.delete(2)
    print(lst)

    # wypiywanie struktury
    print(lst.str_tab_debug())


if __name__ == '__main__':
    main()



