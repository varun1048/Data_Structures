from Linked_Node import Node,alphabet_node_2
from display import display_linkend_list

def zip_node(node1 :Node,node2 :Node)->Node:
    
    current = node1
    while current != None:
        
        current = current.next 
        
    return node1
def start():
    out = zip_node(*alphabet_node_2())
    display_linkend_list( out )
    