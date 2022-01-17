class Node:
    def __init__(self,val):
        self.val = val
        self.right = None
        self.left = None

a = Node('a')
b = Node('b')
c = Node('c')
d = Node('d')
e = Node('e')
f = Node('f')

a.left = b
a.right = c
b.left = d
b.right = d
c.right = f