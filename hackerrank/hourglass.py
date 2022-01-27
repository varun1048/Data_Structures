def hourglass(arr:list)->None:
    for x in arr:
        print(f"{x}")
            
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
        

def start()->list:
    arr = [[1, 1, 1, 0, 0, 0], [0, 1, 0, 0, 0, 0], [1, 1, 1, 0, 0, 0], [0, 0, 2, 4, 4, 0], [0, 0, 0, 2, 0, 0], [0, 0, 1, 2, 4, 0]]
    return hourglass(arr)