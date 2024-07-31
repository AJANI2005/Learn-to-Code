import os
# return masked string
def maskify(cc : str):
    return str("#"*(len(cc)-4)) + cc[-4:]

import curses

class Node:
    def __init__(self,value):
        self.value = value
        self.children = {}
        self.isWord = False
        
        
class Trie : 
    
    def __init__(self):
        self.head : Node = Node('Head')
       
            
    def insert(self,str : str):
        curr : Node = self.head
        for c in str.upper():
            if curr.children.get(c) is not None:
                curr = curr.children[c]
            else:
                node : Node = Node(c)
                curr.children[c] = node
                curr = node
        curr.isWord = True     
    
      
    def search(self,str : str):
        curr : Node = self.head
        for c in str.upper():
            if curr.children.get(c) is not None:
                curr = curr.children[c]
            else:
                return False
        return curr.isWord   
               
    def log_node(self,node : Node, parent : Node):
        output = ""
        if (parent is not None) and (node is not None): 
            output += parent.value + " ==> " + node.value
            print(output)
        
      
        for key in node.children:
            self.log_node(node.children[key],node)    
            
    def log(self,node = None):
        if node is None: node = self.head
        self.log_node(node,None)
        
        
def main():
    tree = Trie()
    with open("C:\\Software Development\\Software-Dev-RoadMap\\Coding Exploration\\words.txt",'r') as file:
        for line in file.readlines():
            tree.insert(line.strip())
            
    words = input("Test String: ").split(" ")
    for w in words:
        print(w +" --> "+ str(tree.search(w.strip())))
   
    
    


if __name__ == "__main__":
    main()


