

class Node : 
    def __init__(self,data):
        self.data : int = data
        self.next : Node = None

class LinkedList:
    head : Node
    def __init__(self,_head):
        self.head : Node = _head

    def countNodes(self) -> int:
        next : Node = self.head.next
        count : int = 1
        while(next != None):
            next = next.next
            count += 1
        return count
 
nodeA : Node = Node(6)
nodeB : Node = Node(3)
nodeC : Node = Node(4)
nodeD : Node = Node(2)
nodeE : Node = Node(1)

nodeA.next = nodeB
nodeB.next = nodeC
nodeC.next = nodeD
nodeD.next = nodeE

link = LinkedList(nodeA)
print(link.countNodes())

