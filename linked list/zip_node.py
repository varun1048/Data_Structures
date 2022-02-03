from Linked_Node import Node,alphabet_node_2
from display import display_linkend_list

def zip_node(node1 :Node,node2 :Node)->Node:
    
    current1 = node1
    current2 = node2
    new_node = None
    while current1 != None or current2 != None :
        # print(current1)
        # print(current2)
        
        
        temp = current1.next
        current1 = current2
        current1.next = temp

        if current1:
            current1 = current1.next 
        if current2:
            current2 = current2.next 
            
    return node2

def start():
    out = zip_node(*alphabet_node_2())
    display_linkend_list( out )
    