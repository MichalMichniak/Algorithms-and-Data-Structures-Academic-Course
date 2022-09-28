from copy import deepcopy
class Elem_:
    def __init__(self,data) -> None:
        self.next = None
        self.data = data
        pass

def nil():
    return None

def cons(el, lst : Elem_):
    el = Elem_(el)
    el.next = lst
    return el

def first(lst : Elem_):
    return lst.data if lst != None else None

def rest(lst : Elem_):
    if lst == None: raise Exception("there is no rest")
    return lst.next if lst != None else None

def create():
    return nil()

def destroy(lst : Elem_):
    return nil()

def is_empty(lst : Elem_):
    return lst == None

def add(lst : Elem_ ,data ):
    return cons(data, lst)

def lenght(lst : Elem_,count = 0):
    return lenght(rest(lst) ,count)+1 if first(lst) != None else 0 

def remove(lst : Elem_):
    if not is_empty(lst):
        return rest(lst)
    else:
        raise Exception("out of range")

def get(lst : Elem_):
    return first(lst)

def str_(lst : Elem_) -> str:
        return str(first(lst)) + " "+str_(rest(lst)) if lst != None else ""

def drop(lst,n):
        if n>lenght(lst):raise Exception("index out of range")
        return drop(rest(lst),n-1) if n-1!=0 else deepcopy(rest(lst))

def take(lst, n):
    if n == 0:
        return nil()
    else:
        first_el   = first(lst)     
        rest_lst  = rest(lst)      
        recreated_lst = take(rest_lst, n-1 )
        return cons(first_el, recreated_lst) 
    pass

def append(data, lst):
    if is_empty(lst):
        return cons(data, lst)  
    else:
        first_el = first(lst)     
        rest_lst = rest(lst)      
        recreated_lst = append(data, rest_lst)
        return cons(first_el, recreated_lst) 
    
def drop_back(lst : Elem_):
    if is_empty(lst):
        raise Exception("empty list")
    if is_empty(rest(lst)):
        return nil() 
    else:
        first_el = first(lst)     
        rest_lst = rest(lst)      
        recreated_lst = drop_back( rest_lst)
        return cons(first_el, recreated_lst) 

def main():
    head = nil()
    data = [('AGH', 'Kraków', 1919),
    ('UJ', 'Kraków', 1364),
    ('PW', 'Warszawa', 1915),
    ('UW', 'Warszawa', 1915),
    ('UP', 'Poznań', 1919),
    ('PG', 'Gdańsk', 1945)]
    for i in data[::-1]:
        head = cons(i , head)
    print(lenght(head))
    print(str_(head))
    head = remove(head)
    print(str_(head))
    print(lenght(head))
    print(str_(head))
    print(str_(drop(head , 2)))
    head = append(1,head)
    print(str_(head))
    head = add(head,2)
    print(str_(head))
    head = drop_back(head)
    print(str_(head))
    print(str_(take(head,3)))
    print(get(head))



if __name__ == '__main__':
    main()