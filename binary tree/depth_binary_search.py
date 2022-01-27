import os
from turtle import left
os.system('cls')
from Node_class import *

def depth_search(node):
    stack = [node]
    values = []
    while len (stack) >0:
        current = stack.pop()
        values.append(current.val)
        
        if current.right: # same ass current.right != None: 
            stack.append(current.right)
        if current.left:
            stack.append(current.left)            
            
    return values 

    
# print(depth_search(a))


def depth_recursion(node):
    if node == None :
        return []
    return [node.val] + depth_recursion(node.left)  + depth_recursion(node.right)

# print(depth_recursion(a))










def sum_tree(node):
    if node == None :
        return 0
    return node.val + sum_tree(node.left)  + sum_tree(node.right)

# print(sum_tree(a))



# def min_vlaue(node):
#     if not node:
#         return 0    
#     return min( node.val , min_vlaue(node.right) , min_vlaue(node.left) )

# print(min_vlaue(a))

def max_root(node):   
    if not node:
        return 0
    return node.val + ( max_root(node.right) if max_root(node.right) < max_root(node.left) else max_root(node.right))
        
     
    
print(max_root(a))