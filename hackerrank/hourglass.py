def split(arr:list)->list:
    mid = len(arr) // 2
    return [arr[:mid], arr[mid:]]

def hourglass(arr:list)->None:
    
    nums = [] 
    
    for x in  range(len(arr)):
        temp = arr[x]
        nums.append([ temp[0:3], temp[1:4],temp[2:5] ,temp[3:6] ])
    
    for x in nums:
        print(x)
        
    print()
    mid = []    
    for x in range(1,5):
        mid.append(nums[x][1])
        print(mid[x-1])
    
    print()
    for x in range(len(nums)):
        print(nums[x])
    
    
    
    
    
    
    
    
    
    
    
        

def start()->list:
    arr = [[1, 1, 1, 0, 0, 0], [0, 1, 0, 0, 0, 0], [1, 1, 1, 0, 0, 0], [0, 0, 2, 4, 4, 0], [0, 0, 0, 2, 0, 0], [0, 0, 1, 2, 4, 0]]
    return hourglass(arr)