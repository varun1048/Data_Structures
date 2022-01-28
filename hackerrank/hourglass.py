def split(arr:list)->list:
    mid = len(arr) // 2
    return [arr[:mid], arr[mid:]]

def hourglass(arr:list)->None:
    
    nums = [] 
    # In matrix
    for x in  range(len(arr)):
        temp = arr[x]
        nums.append([ temp[0:3], temp[1:4],temp[2:5] ,temp[3:6] ])
    
    for x in nums:
        print(x)
  
    print()
    mid =[]
    for x in range(1,5):
        tem = []
        for y in range(0,4):
            tem.append(nums[x][y][1])
        mid.append(tem)
   
    
    
    
    sum_of = []
    for x in nums:
        temp = []
        for y in x:
            temp.append(sum(y))
        sum_of.append(temp)
    print("\nsum of")
    for x in sum_of:
        print(x)    
    

    max_out = []
    A = []
    B = []
    
    for x in range( len(sum_of)-2 ):
        print(f" {x}  - { x+2}")
        A.append( sum_of[x] )
        B.append( sum_of[x+2] )


    print("\nA and B")
    for x in range( len(A) ):
        print(f" {x} index {A[x]}  {B[x]}  "  )                
    
    print("\nOut")
    for x in range( len(A) ):
        temp = []
        for y in range( len(B)):
            # print(f" {A[x][y]}   {B[x][y]}"  )                
            max_out.append(A[x][y] + B[x][y] + mid[x][y])
            temp.append(A[x][y] + B[x][y] + mid[x][y])
        print(temp)
    
    
    print(f"\nMax {max(max_out)}")
    
    
    
    
    
    
        

def start()->list:
    arr = [[1, 1, 1, 0, 0, 0], [0, 1, 0, 0, 0, 0], [1, 1, 1, 0, 0, 0], [0, 0, 2, 4, 4, 0], [0, 0, 0, 2, 0, 0], [0, 0, 1, 2, 4, 0]]
    return hourglass(arr)