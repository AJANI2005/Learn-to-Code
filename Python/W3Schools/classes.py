

class Node:
    data : int = 0
    next : 'Node' = None

    @classmethod
    def update(cls):
        cls.data = 5
        
a : Node = Node()
b : Node = Node()

Node.update()

print(a.data,b.data)