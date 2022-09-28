class Node:
    def __init__(self, key, data, child = None, child2 = None):
        self.key = key
        self.data = data
        self.left = child
        self.right = child2
        pass

class BST:
    def __init__(self) -> None:
        self.root = None
        pass

    def insert_(self, node : Node, key, data):
        if node == None: return Node(key,data)
        if key<node.key:
            node.left = self.insert_(node.left, key, data)
            return node
        elif key>node.key:
            node.right = self.insert_(node.right, key, data)
            return node
        else:
            node.data = data
            return node
        pass

    def insert(self,key , data):
        self.root = self.insert_(self.root, key, data)
        pass

    def search_(self, node, key):
        if node == None: return None
        if key<node.key:
            return self.search_(node.left, key)
        elif key>node.key:
            return self.search_(node.right, key)
        else:
            return node.data

    def search(self,key):
        return self.search_(self.root ,key)

    def del_find_rep(self, node : Node ) -> Node:
        temp = node.left
        if temp == None: 
            return node
        if temp.left == None:
            node.left = temp.right
            return temp
        prev = node
        while True:
            prev = temp
            temp = temp.left
            if temp.left == None:
                prev.left = temp.right
                break
        #temp.right = None
        #temp.left = None
        return temp

    def delete_search(self, node : Node, key):
        if node == None: return
        if key<node.key:
            node.left = self.delete_search(node.left, key)
            return node
        elif key>node.key:
            node.right = self.delete_search(node.right, key)
            return node
        else:
            if node.left == None and node.right == None:
                return None
            elif node.left == None:
                node = node.right
                return node
            elif node.right == None:
                node = node.left
                return node
            else:
                temp = self.del_find_rep(node.right)
                temp.left = node.left
                temp.right = node.right if node.right.key != temp.key else temp.right
                return temp


    def delete(self,key):
        self.root = self.delete_search(self.root,key)
        pass

    def print_(self, node : Node):
        return (self.print_(node.left) if node.left != None else '')+ f"{node.key} : {node.data}, "+ (self.print_(node.right) if node.right != None else '')

    def print(self):
        strr = "{ "
        strr += self.print_(self.root)
        strr = strr[:-2]
        strr+='}'
        return strr

    def height_(self,node):
        return max((self.height_(node.left) if node.left != None else 0),(self.height_(node.right) if node.right != None else 0))+1 if node != None else 0

    def height(self):
        return self.height_(self.root)

    def print_tree(self):
        print("==============")
        self._print_tree(self.root, 0)
        print("==============")

    def _print_tree(self, node, lvl):
        if node!=None:
            self._print_tree(node.right, lvl+5)

            print()
            print(lvl*" ", node.key, node.data)
     
            self._print_tree(node.left, lvl+5)

def main():
    bst = BST()
    for key,value in {50:'A', 15:'B', 62:'C', 5:'D', 20:'E', 58:'F', 91:'G', 3:'H', 8:'I', 37:'J', 60:'K', 24:'L'}.items():
        bst.insert(key,value)
    bst.print_tree()
    print(bst.print())
    
    print(bst.search(24))
    bst.insert(20,"AA")
    bst.insert(6,"M")
    bst.delete(62)
    bst.insert(59,"N")
    bst.insert(100,"P")
    bst.delete(8)
    bst.delete(15)
    bst.insert(55,"R")
    bst.delete(50)
    bst.delete(5)
    bst.delete(24)
    print(bst.height())
    print(bst.print())
    bst.print_tree()





if __name__ == '__main__':
    main()