
class Node:
    def __init__(self,val) -> None:
        self.val = val
        self.next = None
    def __str__(self) -> str:
        return f"Node {self.val}"




def Display(head : Node)->None:
    # recursion
    if head == None:
        return    
    print(head.val)
    Display(head.next)
    
    # normal way 
    # current = head
    # while current != None:
    #     print(current.val)
    #     current = current.next

def  Sum(head: Node)->int:
    if head == None:
        return 0
    return head.val + Sum(head.next)
    
    #normal way
    # current = head
    # count = 0
    # while current != None:
    #     count += current.val
    #     current = current.next
    # return count

def exist_val(val:str,head:Node)->bool:
    if head == None:
        return False    
    if head.val == val:
        return True    
    return False or exist_val(val,head.next)

    #normal
    # while head != None:
    #     if head.val == val:
    #         return True
    #     head = head.next
    # return False

def exist_node(node:Node,head:Node)->bool:
    if head == None:
        return False    
    if head == node:
        return True    
    return False or exist_node(node,head.next)


def find_node(node:Node,head:Node)->Node:
    if head == None:
        return None
    if head == node:
        return head
    return find_node(node,head.next)


def find_val(val,head:Node)->Node:
    if head == None:
        return None
    if head.val == val:
        return head
    return find_val(val,head.next)






def reverse(head:Node,out=None)->Node:
    if head == None:
        return out
    
    Next = head.next
    head.next = out
    out = head
    return reverse(Next,out) 

    #normal way
    # while head != None:        
    #     Next = head.next
    #     head.next = out
    #     out = head
    #     head = Next
    # return out


def zip_i(node1:Node ,node2:Node)->Node:
    tail = node1
    current1 = node1.next
    current2 = node2
    count = 0
    
    while current1 and current2:
        if count %2 == 0:
            tail.next = current2
            current2 = current2.next 
        else:
            tail.next = current1
            current1 = current1.next
        
        tail = tail.next
        count += 1
        
        if current1:
            tail.next = current1
        else:
            tail.next = current2
             
            
    return node1

def zip_r(node1:Node ,node2:Node,tail=None)->Node:
    return zip_r(node1,node2,tail.next)


















def numbers()->Node:
        A = Node(1)
        B = Node(2)
        C = Node(3)
        D = Node(4)
        E = Node(5)
        
        A.next = B
        B.next = C
        C.next = D
        D.next = E
        
        return A

def alphabet()->Node:
    X = Node('X')
    Y = Node('Y')
    Z = Node('Z')
    X.next = Y
    Y.next = Z
    return X


def start()-> None:

    A = Node('A')
    B = Node('B')
    C = Node('C')
    D = Node('D')
    E = Node('E')
    
    A.next = B
    # B.next = C
    # C.next = D
    # D.next = E
        

    # Display(numbers())
    # out = Sum(numbers())
    # out = exist_val("D", A) 
    # out = exist_node(C, A) 
    # out = find_node(C, A) 
    # out = find_val("aC", A) 
    # print(out)
    
    # Display( reverse(A) )
    out = zip_r(A,numbers())
    Display( out )
    
    