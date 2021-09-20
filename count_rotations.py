def count_rotations(nums):
    print(nums)


    # position = 0
    # while position < len(nums):
    #     low =0
    #     high = len(nums)
    #     mid = (low + high )//2

    #     min_number  = nums[ mid]
        
        
        

        
    #     position +=1
    # return 0


    # position = 0
    # while position < len(nums):

    #     print(nums[position])

    #     if position > 0 and nums[position] < nums[position-1]:
    #         return position 

    #     position +=1
    # return 0



    min_number = min(nums)
    max_number = max(nums)
    lenght = len(nums)

    
    print(f"lenght:{lenght} max index {nums.index(max_number)}")
    if min_number == nums[0] or lenght == 1   :
        return 0   
   
    return nums.index(max_number)+1