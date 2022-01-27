import os
clear =  lambda : os.system('cls')

graph_has ={
    'f':['g',"i"],
    'g':["h"],
    'h':[],
    'i':['g','k'],
    'k':[],
    'j':[]
}


# depth first search
Graph = {
    'a':['c','b'],
    'b':['d',],
    'd':['f'],
    'f':[],    
    'c':['e'],
    'e':[],
}