from typing import List
class B_Tree_Elem:
    def __init__(self,max_size) -> None:
        self.size = 0
        self.keys = [None for i in range(max_size+1)]
        self.children : List[B_Tree_Elem]= [None for i in range(max_size+2)]
        pass
 

class B_Tree:
    def __init__(self,max_size) -> None:
        self.max_size = max_size
        self.root = None
        pass
    
    def split(self,node,n):
        node.keys[n+1:] = node.keys[n:-1]
        node.keys[n] = node.children[n].keys[(self.max_size+1)//2]
        node.size+=1
        node.children[n+1:] = node.children[n:-1]
        node.children[n] = B_Tree_Elem(self.max_size)
        node.children[n].children[:len(node.children[n+1].children[:(self.max_size+1)//2+1])] = node.children[n+1].children[:(self.max_size+1)//2+1]
        node.children[n+1].children[:len(node.children[n+1].children[(self.max_size+1)//2+1:])] = node.children[n+1].children[(self.max_size+1)//2+1:]
        node.children[n].keys[:len(node.children[n+1].keys[:(self.max_size+1)//2])] = node.children[n+1].keys[:(self.max_size+1)//2+1]
        node.children[n+1].keys[:len(node.children[n+1].keys[(self.max_size+1)//2+1:])] = node.children[n+1].keys[(self.max_size+1)//2+1:]
        node.children[n+1].keys[len(node.children[n+1].keys[(self.max_size+1)//2:])-1:] = [None for i in node.children[n+1].keys[len(node.children[n+1].keys[(self.max_size+1)//2:])-1:]]
        node.children[n+1].children[(self.max_size+1)//2+1:] = [None for i in node.children[n+1].children[(self.max_size+1)//2+1:]]
        node.children[n].size = (self.max_size+1)//2
        node.children[n+1].size = (self.max_size+1)//2 - 1

    def insert_rec(self,node : B_Tree_Elem,key, height):
        #print(height)
        #if node.children.__len__() > self.max_size+2: raise ValueError(f"{key}")
        for n,l in enumerate(node.keys):
            if node.size<=n: continue
            if key<l:
                if node.size != self.max_size and all([i is None for i in node.children]):
                    node.keys[n+1:] = node.keys[n:-1]
                    node.keys[n] = key
                    node.size +=1
                    return None
                elif all([i is None for i in node.children]):
                    node.keys[n+1:] = node.keys[n:-1]
                    node.keys[n] = key
                    node.size+=1
                    return True
                else:
                    
                    rest = self.insert_rec(node.children[n],key,height+1)
                    if rest is None: return None
                    if node.size != self.max_size:
                        self.split(node,n)
                        return None
                    else:
                        self.split(node,n)
                        return True
        else:
            n = node.size
            if node.size != self.max_size and all([i is None for i in node.children]):
                node.keys[n+1:] = node.keys[n:-1]
                node.keys[n] = key
                node.size +=1
                return None
            elif all([i is None for i in node.children]):
                node.keys[n+1:] = node.keys[n:-1]
                node.keys[n] = key
                node.size +=1
                return True
            else:
                rest = self.insert_rec(node.children[n],key,height+1)
                if rest is None: return None
                if node.size != self.max_size:
                    self.split(node,n)
                    return None
                else:
                    self.split(node,n)
                    return True
        return 


    def insert(self,key):
        if key == 1:
            g = 0
            pass
        if self.root == None: self.root = B_Tree_Elem(self.max_size)
        t = self.insert_rec(self.root,key,0)
        if t is None: return
        temp = B_Tree_Elem(self.max_size)
        temp.keys[0] = self.root.keys[self.root.size//2]
        temp.size = 1
        temp.children[0] = B_Tree_Elem(self.max_size)
        temp.children[1] = self.root
        temp.children[0].keys[:len(self.root.keys[:self.root.size//2])] = self.root.keys[:self.root.size//2]
        temp.children[1].keys[:len(self.root.keys[self.root.size//2+1:])] = self.root.keys[self.root.size//2+1:]
        temp.children[1].keys[len(self.root.keys[self.root.size//2+1:]):] = [None for i in temp.children[1].keys[len(self.root.keys[self.root.size//2+1:]):]]
        temp.children[0].children[:len(self.root.children[:(self.max_size+1)//2+1])] = self.root.children[:(self.max_size+1)//2+1]
        temp.children[1].children[:len(temp.children[1].children[(self.max_size+1)//2+1:])] = temp.children[1].children[(self.max_size+1)//2+1:]
        temp.children[1].children[len(temp.children[1].children[self.root.size//2+1:]):] = [None for i in temp.children[1].children[len(temp.children[1].children[self.root.size//2+1:]):]]
        temp.children[0].size = (self.max_size+1)//2
        temp.children[1].size = (self.max_size+1)//2 - 1
        self.root = temp










    def print_tree(self):
        print("==============")
        self._print_tree(self.root, 0)
        print("==============")

    def _print_tree(self, node, lvl):
        if node!=None:
            for i in range(node.size+1): 	                	
                self._print_tree(node.children[i], lvl+1)
                if i<node.size:
                    print(lvl*'  ', node.keys[i])


def main():
    # input długość tablicy
    b_tree = B_Tree(3)
    for i in [5, 17, 2, 14, 7, 4, 12, 1, 16, 8, 11, 9, 6, 13, 0, 3, 18 , 15, 10, 19]:
        b_tree.insert(i)
    b_tree.print_tree()
    b_tree2 = B_Tree(3)
    for i in [i for i in range(20)]:
        b_tree2.insert(i)
    b_tree2.print_tree()
    for i in [i for i in range(20,200)]:
        b_tree2.insert(i)
    b_tree2.print_tree()
    b_tree3 = B_Tree(5)
    for i in [i for i in range(200)]:
        b_tree3.insert(i)
    b_tree3.print_tree()
if __name__ == '__main__':
    main()