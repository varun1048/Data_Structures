from Graph_Data import Graph as graph


def depth_first_serach(graph,source):
    values = []
    stack = [ source ]
    
    loop = 0    
    while len(stack) > 0:
        current  = stack.pop(0)
        values.append(current)
        for key in  graph[current]:
            stack.append(key)
        # stack +=graph[key]

        print( f" current {current} key {key} graph {graph[current]} \t stack = {stack}" )
        
    print(f"\n\tResult {values}")

# depth_first_serach(graph,"a")



def depth_first_serach_resursion(graph,source):
    print(source)
    for key  in graph[source]:
        depth_first_serach_resursion(graph,key)

# depth_first_serach_resursion(graph,"a")

def birth_first_serach_resursion(graph,source):
    print(source)
    for key  in graph[source]:
        birth_first_serach_resursion(graph,key)

birth_first_serach_resursion(graph,"a")
