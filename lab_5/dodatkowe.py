class Node:
    def __init__(self, key, data, child = None, bastard = None):
        self.key = key
        self.data = data
        self.left = child
        self.right = bastard
        self.wsp_wyw = 0
        pass

class AVL:
    def __init__(self) -> None:
        self.root = None
        pass

    def insert_(self, node : Node, key, data):
        if node == None: 
            temp = Node(key,data)
            temp.wsp_wyw = 0
            return temp
        if key<node.key:
            node.left = self.insert_(node.left, key, data)
            node.wsp_wyw =  self.height_(node.left) - self.height_(node.right)
            if node.wsp_wyw ==-2:
                if node.right.wsp_wyw == 1:
                    node = self.RL(node)
                    return node
                if node.right.wsp_wyw == -1:
                    node = self.RR(node)
                    return node
            elif node.wsp_wyw ==2:
                if node.left.wsp_wyw == 1:
                    node = self.LL(node)
                    return node
                if node.left.wsp_wyw == -1:
                    node = self.LR(node)
                    return node
            return node
        elif key>node.key:
            node.right = self.insert_(node.right, key, data)
            node.wsp_wyw = self.height_(node.left) - self.height_(node.right)
            if node.wsp_wyw ==-2:
                if node.right.wsp_wyw == 1:
                    node = self.RL(node)
                    return node
                if node.right.wsp_wyw == -1:
                    node = self.RR(node)
                    return node
            elif node.wsp_wyw ==2:
                if node.left.wsp_wyw == 1:
                    node = self.LL(node)
                    return node
                if node.left.wsp_wyw == -1:
                    node = self.LR(node)
                    return node
            return node
        else:
            node.data = data
            node.wsp_wyw = 0
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
        prev = temp
        temp = temp.left
        if temp.left == None:
            prev.left = temp.right
            return temp
        #temp.right = None
        #temp.left = None
        node = self.del_find_rep(temp)
        node.wsp_wyw =  self.height_(node.left) - self.height_(node.right)
        if node.wsp_wyw ==-2:
            if node.right.wsp_wyw == 1:
                node = self.RL(node)
                return node
            if node.right.wsp_wyw == -1:
                node = self.RR(node)
                return node
        elif node.wsp_wyw ==2:
            if node.left.wsp_wyw == 1:
                node = self.LL(node)
                return node
            if node.left.wsp_wyw == -1:
                node = self.LR(node)
                return node
        return node

    def delete_search(self, node : Node, key):
        if node == None: return
        if key<node.key:
            node.left = self.delete_search(node.left, key)
            node.wsp_wyw =  self.height_(node.left) - self.height_(node.right)
            if node.wsp_wyw ==-2:
                if node.right.wsp_wyw == 1:
                    node = self.RL(node)
                    return node
                if node.right.wsp_wyw == -1:
                    node = self.RR(node)
                    return node
            elif node.wsp_wyw ==2:
                if node.left.wsp_wyw == 1:
                    node = self.LL(node)
                    return node
                if node.left.wsp_wyw == -1:
                    node = self.LR(node)
                    return node
            return node
        elif key>node.key:
            node.right = self.delete_search(node.right, key)
            node.wsp_wyw = self.height_(node.left) - self.height_(node.right)
            if node.wsp_wyw ==-2:
                if node.right.wsp_wyw == 1:
                    node = self.RL(node)
                    return node
                if node.right.wsp_wyw == -1:
                    node = self.RR(node)
                    return node
            elif node.wsp_wyw ==2:
                if node.left.wsp_wyw == 1:
                    node = self.LL(node)
                    return node
                if node.left.wsp_wyw == -1:
                    node = self.LR(node)
                    return node
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
                node = temp
                node.wsp_wyw = self.height_(node.left) - self.height_(node.right)
                if node.wsp_wyw ==-2:
                    if node.right.wsp_wyw == 1:
                        node = self.RL(node)
                        return node
                    if node.right.wsp_wyw == -1:
                        node = self.RR(node)
                        return node
                elif node.wsp_wyw ==2:
                    if node.left.wsp_wyw == 1:
                        node = self.LL(node)
                        return node
                    if node.left.wsp_wyw == -1:
                        node = self.LR(node)
                        return node
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
        return (max((self.height_(node.left) if node.left != None else 0),(self.height_(node.right) if node.right != None else 0))+1) if node != None else 0

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
    
    def LL(self,node):
        B : Node = node.left
        node.left = B.right
        B.right = node
        node = B
        node.wsp_wyw = self.height_(node.left) - self.height_(node.right)
        if node.right != None:
            node.right.wsp_wyw = self.height_(node.right.left) - self.height_(node.right.right)
        if node.left != None:
            node.left.wsp_wyw = self.height_(node.left.left) - self.height_(node.left.right)
        return node

    def RR(self,node):
        B : Node = node.right
        node.right = B.left
        B.left = node
        node = B
        node.wsp_wyw = self.height_(node.left) - self.height_(node.right)
        if node.right != None:
            node.right.wsp_wyw = self.height_(node.right.left) - self.height_(node.right.right)
        if node.left != None:
            node.left.wsp_wyw = self.height_(node.left.left) - self.height_(node.left.right)
        return node

    def RL(self,node):
        B = node.right.left
        node.right.left = B.right
        B.right = node.right
        node.right = B
        return self.RR(node)

    def LR(self,node):
        B = node.left.right
        node.left.right = B.left
        B.left = node.left
        node.left = B
        return self.LL(node)


def main():
    avl = AVL()
    for key,value in {50:'A', 15:'B', 62:'C', 5:'D', 2:'E', 1:'F', 11:'G', 100:'H', 7:'I', 6:'J', 55:'K', 52:'L', 51:'M', 57:'N', 8:'O', 9:'P', 10:'R', 99:'S', 12:'T'}.items():
        avl.insert(key,value)
    avl.print_tree()
    print(avl.print())
    print(avl.search(10))
    avl.delete(50)
    avl.delete(52)
    avl.delete(11)
    avl.delete(57)
    avl.delete(1)
    avl.delete(12)
    avl.insert(3,"AA")
    avl.insert(4,"M")
    avl.delete(7)
    avl.delete(8)
    avl.print_tree()
    print(avl.print())





if __name__ == '__main__':
    main()