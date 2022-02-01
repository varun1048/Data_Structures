from Linked_Node import *
import display
def insert_node(target :Node,val:Node)->None:
    
    temp = target.next
    target.next = val
    val.next = temp

def start():
    insert_node(c,q)
    display.display_linkend_list(a)
