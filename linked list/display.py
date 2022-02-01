from  Linked_Node import *

def display_linkend_list(head:Node ):
    
    current = head
    while current != None:
        print(current.val)
        current = current.next
    
def display_linkend_list_recursion(head:Node ):
    if head == None:
        return
    print(head.val)
    display_linkend_list(head.next)    

def start():
    display_linkend_list_recursion( alphabet_node() )