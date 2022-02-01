from Linked_Node import alphabet_node ,Node ,a,c
import display
from find_node import find_node, find_node_value

def insert_node(nodes  ,target :Node ,node:Node)->Node:
    
    target = find_node(target,nodes)
    temp = target.next
    target.next = node
    node.next = temp
    
    return nodes
    

def start():  
    
    z = Node("insert node")
    
    out =  insert_node(alphabet_node(),c,z)
    
    
    display.display_linkend_list(out)
