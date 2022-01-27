class Node:
    def __init__(self,val):
        self.val = val
        self.right = None
        self.left = None

# a = Node('a')
# b = Node('b')
# c = Node('c')
# d = Node('d')
# e = Node('e')
# f = Node('f')


a = Node(1)
b = Node(1)
c = Node(12)
d = Node(17)
# e = Node('e')
# f = Node('f')# x = Node('x')



a.left = b
a.right = c
b.left = d
# b.right = e
# c.right = f
# d.right = x

