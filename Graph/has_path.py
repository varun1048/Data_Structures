from Graph_Data import clear , graph_has
clear()
def has_path(graph,scr,dst):
    stack = [scr]
    values = []
    while len(stack) > 0 :
        crt = stack.pop()
        values.append(crt)        
        if dst == crt:
            return True 
        for node in graph[crt]:
            stack.append(node)       
    print(values)
    return False   
# print(has_path(graph_has,'f','i'))

def has_path_recursion(graph,scr,dst):
    if scr == dst:
        return True
    for key in graph[scr]:
        if has_path_recursion(graph,key,dst) == True:
            return True
        
    return False        
print(has_path_recursion(graph_has,'f','i'))

 
