from copy import deepcopy
class Elem_:
    def __init__(self,data) -> None:
        self.next = None
        self.data = data
        pass


class Linked_Lst:
    def __init__(self, head = None) -> None:
        if head != None:
            self.head = head
        else:
            self.head : Elem_ = None
        pass

    def destroy(self):
        self.head = None
    
    def add(self,data):
        new_elem = Elem_(data)
        new_elem.next = self.head
        self.head = new_elem

    def is_empty(self):
        return self.head == None
    
    def lenght(self):
        count = 0
        temp = self.head
        while temp != None:
            temp = temp.next
            count += 1
        return count

    def remove(self):
        if not self.is_empty():
            self.head = self.head.next
        else:
            raise Exception("out of range")
    
    def get(self):
        return self.head.data
    
    def __str__(self) -> str:
        strr = ""
        temp = self.head
        while temp != None:
            strr += str(temp.data) + " "
            temp = temp.next
        return strr
    
    def take(self,n):
        list_copy = deepcopy(self.head)
        if n>self.lenght():raise Exception("index out of range")
        temp = list_copy
        for i in range(n-1):
            temp = temp.next
        temp.next = None
        return Linked_Lst(list_copy)

    def drop(self,n):
        temp = deepcopy(self.head)
        if n>self.lenght():raise Exception("index out of range")
        for i in range(n):
            temp = temp.next
        return Linked_Lst(temp)
    
    def append(self,data):
        if self.head == None:
            self.head = Elem_(data)
        else:
            temp = self.head
            while temp.next != None:
                temp = temp.next
            temp.next = Elem_(data)
    
    def drop_back(self):
        if self.head == None: raise Exception("empty list")
        temp = self.head
        while temp.next.next != None:
            temp = temp.next
        temp.next = None

lst = Linked_Lst()
data = [('AGH', 'Kraków', 1919),
('UJ', 'Kraków', 1364),
('PW', 'Warszawa', 1915),
('UW', 'Warszawa', 1915),
('UP', 'Poznań', 1919),
('PG', 'Gdańsk', 1945)]
for i in data[::-1]:
    lst.add(i)
print(lst)
print(lst.lenght())
print(lst.is_empty())
print(lst.take(3))
print(lst.drop(3))
print(lst)
lst.drop_back()
print(lst)
lst.append(('AGH', 'Kraków', 1919))
print(lst)
lst_2 = Linked_Lst()
for i in data:
    lst_2.append(i)
print(lst_2)