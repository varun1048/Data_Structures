from Linked_Node import Node,alphabet_node
from display import display_linkend_list
def reverse(head:Node)->Node:
    current   = head
    previous = None
    while current != None:
        Next = current.next
                
        current.next = previous
        previous = current
        
        current = Next        
        print(previous)
    return previous

def reverse_recursion(head:Node,previous=None)->Node:
    if head == None:
        return previous
        
    Next = head.next
    head.next = previous
    return reverse_recursion(Next,head)


def valkai_oru_vattam(head:Node)->Node:
    arr = []
    current = head
    while current != None:
        arr.append(current)
        current = current.next
        
    arr = arr[::-1]
    for i , v in enumerate(arr):
        try:
            v.next = arr[i+1]
        except:
            v.next = None
            
    return arr[0]
    



def start()->None:
    node =  valkai_oru_vattam(alphabet_node())
    display_linkend_list(node) 
    # print(node)
    