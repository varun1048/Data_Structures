class Node:
    
    def __init__(self,val) -> None:
        self.val = val
        self.next = None
    
    def __str__(self) -> str:
        return f"Node {str.upper(self.val)}"
    
a = Node("a")
b = Node("b")
c = Node("c")
# d = Node("d")

q = Node("q")

a.next = b
b.next = c
# c.next = d

def alphabet_node()->Node:
    a = Node("a")
    b = Node("b")
    c = Node("c")
    d = Node("d")
    e = Node("e")
    f = Node("f")
    
    a.next = b
    b.next = c
    # c.next = d
    # d.next = e
    # e.next = f
    
    return a

def alphabet_node_2()->Node:
    q = Node("q")
    r = Node("r")
    s = Node("s")

    
    q.next = r
    r.next = s

    a = Node("a")
    b = Node("b")
    
    a.next = b
    b.next = c
    
    return a , q

def nums_node()->Node:
    a = Node(2)
    b = Node(8)
    c = Node(3)
    d = Node(7)

    a.next = b
    b.next = c
    c.next = d
    return  a
