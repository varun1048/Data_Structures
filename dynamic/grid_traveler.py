def grid_traveler(m:int,n:int,memo={})->int:
    key_to = str(m)+','+str(n)
    if key_to in memo:
        return memo[key_to]
    if m == 0 and n == 0:
        return 0
    if m == 1 or n == 1 :
        return 1
    
    memo[key_to] =grid_traveler(m -1,n,memo) + grid_traveler(m,n-1,memo)
    
    return memo[key_to]
    
    