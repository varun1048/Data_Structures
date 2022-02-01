from Linked_Node import alphabet_node,Node,c
import display

def find_node_TF(target:int or str ,head:Node)->bool:
    crt = head
    while  crt != None:
        if crt.val ==  target:
            return True        
        crt = crt.next
    return False

def find_node_TF_recursion(target:int or str ,head:Node)->bool:
    
    if head == None:
        return False
    if head.val == target:
        return True
    
    return False or find_node_TF_recursion('x',head.next)


def find_node(target:Node,head:Node):
    
    if head == None:
        return False
    if head.val == target.val:
        return head
    
    return find_node(target,head.next)

def find_node_value(target:Node,head:Node):
    
    if head == None:
        raise Exception(f"Sorry,there is  no data like  {target}   ")
    if head.val == target:
        return head
    
    return find_node_value(target,head.next)







def start():
    # print( finding_node("z",   alphabet_node())  )
    print( find_node_TF_recursion("z",   alphabet_node())  )
