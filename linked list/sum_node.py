from Linked_Node import nums_node ,Node
import display

def sum_nodes(head:Node)->int:
    values = [] 
    crt = head
    while crt != None:
        values.append(crt.val)
        crt = crt.next
    return sum(values)    

def sum_nodes_recursion(head:Node)->int:
    if head == None:
        return 0
    return head.val + sum_nodes_recursion(head.next)

def start():
    # print( sum_nodes( nums_node() ) )
    print( sum_nodes_recursion( nums_node() ) )
