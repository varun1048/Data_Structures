def febonecci(num,memo ={})-> int:
    if num in memo :
        return memo[num]
    if num<=2:
        return 1
    memo[num] =  febonecci(num -1,memo) + febonecci(num - 2,memo)
    return  memo[num]









# def febonecci(num:int,a =0 ,b=1)->int:    
#     if a == 0:
#         num -= 1
#     # print(a+b)
#     if num == 0:
#         return b
#     return febonecci(num-1,b,a+b)
    



# def febonecci(num:int)->None:
#     a ,b = 0 ,1
    
#     for _ in range(num):
#         c = a+b
#         print(f"{c}")
#         a , b = b ,c 
    