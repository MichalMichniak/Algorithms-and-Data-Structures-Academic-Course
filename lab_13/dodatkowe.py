from typing import List


class Node:
    def __init__(self, sufix):
        self.sufix = sufix
        self.succesors = []
        pass
    def __repr__(self):
        return self.sufix

class Trie:
    def __init__(self):
        self.root = Node('')
        pass

    def add_sufix(self, txt,node = None, i = 0):
        """
        for uncompresed trees
        """
        if node == None:
            node = self.root
        if i == len(txt): return
        for n,j in enumerate(node.succesors):
            if j.sufix == txt[i]:
                self.add_sufix(txt,node.succesors[n],i+1)
                break
        else:
            node.succesors.append(Node(txt[i]))
            self.add_sufix(txt,node.succesors[len(node.succesors)-1],i+1)

    def compress(self,node = None):
        if node == None:
            node = self.root
        if len(node.succesors) == 0: return
        while len(node.succesors) == 1:
            node.sufix += node.succesors[0].sufix
            node.succesors = node.succesors[0].succesors
            self.compress(node)
        for i in range(len(node.succesors)):
            self.compress(node.succesors[i])

    def find(self,mask,node = None,i = 0)->bool:
        if node == None:
            node = self.root
        for n in range(len(node.succesors)):
            if i+len(node.succesors[n].sufix) > len(mask):
                continue
            if mask[i:i+len(node.succesors[n].sufix)] == node.succesors[n].sufix:
                if i+len(node.succesors[n].sufix) == len(mask) and i+len(node.succesors[n].sufix) == len(mask):
                    return True
                return self.find(mask,node.succesors[n],i+len(node.succesors[n].sufix))
        return False

    def recurent_count(self,node : Node = None):
        count = 0
        if len(node.succesors) == 0:
            return 1
        for i in range(len(node.succesors)):
            count+= self.recurent_count(node.succesors[i])
        return count

    def count(self,mask,node = None,i = 0):
        if node == None:
            node = self.root
        for n in range(len(node.succesors)):
            if i+len(node.succesors[n].sufix) > len(mask):
                continue
            if mask[i:i+len(node.succesors[n].sufix)] == node.succesors[n].sufix:
                if i+len(node.succesors[n].sufix) == len(mask):
                    return self.recurent_count(node.succesors[n])
                return self.count(mask,node.succesors[n],i+len(node.succesors[n].sufix))
        return 0


    def _print_tree(self, node, lvl):
        if node!=None:
            for i in range(len(node.succesors)): 	                	
                self._print_tree(node.succesors[i], lvl+1)
                if i<len(node.succesors)-1:
                    print(lvl*'  ', node.succesors[i])

    def print_tree(self):
        print("==============")
        self._print_tree(self.root, 0)
        print("==============")

def build_trie(txt):
    trie = Trie()
    for i in range(len(txt)):
        trie.add_sufix(txt[i:])
    trie.compress()
    return trie



class Suffix_table:
    def __init__(self,tab = None) -> None:
        if tab != None:
            tab = [[n , i] for n,i in enumerate(tab)]
            tab.sort(key = lambda x: x[1])
            self.tab_s = tab
        else:
            self.tab_s = []
        pass
    
    def from_trie(self,trie):
        """
        nie rozumiem :(
        """
        pass

def build_suffix(txt):
    tab = [txt[i:] for i in range(len(txt))]
    trie = Suffix_table(tab)
    return trie

def main():
    txt = "banana\0"
    trie = build_trie(txt)
    trie.print_tree()
    print(trie.find("nana\0"))
    print(trie.find("nan"))
    print(trie.count("na"))
    print(trie.count("nan"))
    sufix =build_suffix(txt)
    p = 0
    pass

if __name__ == '__main__':
    main()