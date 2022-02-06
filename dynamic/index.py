import os
from  fibonacci import febonecci
from grid_traveler import grid_traveler
def out(inner:any):
    os.system('cls')
    print(inner)
    
if __name__=="__main__":
    # out  = febonecci(10)
    out( grid_traveler(18,18) )