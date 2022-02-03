from Linked_Node import Node,alphabet_node

def find_index_node(index:int,node:Node)->any:
    
    if node == None:
        return None
    
    if index == 0:
        return node.val
    
    return  find_index_node(index - 1,node.next)

def start():
    print(find_index_node(45,alphabet_node()))
