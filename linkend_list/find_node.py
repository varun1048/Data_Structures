from Linked_Node import alphabet_node,Node,c
import display

def finding_node(target:int or str ,head:Node)->bool:
    crt = head
    while  crt != None:
        if crt.val ==  target:
            return True        
        crt = crt.next
    return False

def finding_node_recursion(target:int or str ,head:Node)->bool:
    
    if head == None:
        return False
    if head.val == target:
        return True
    
    return False or finding_node_recursion('x',head.next)




def start():
    # print( finding_node("z",   alphabet_node())  )
    print( finding_node_recursion("z",   alphabet_node())  )
