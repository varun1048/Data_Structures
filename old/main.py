from ProfileInformation import User 
from Database import UserDatabase
from BinaryTree import TreeNode ,BinaryTree

import os
os.system('cls')

varun = User("varun1048",   "varun",        "mk.varun@gmail.com")
aakash = User('aakash',     'Aakash Rai',   'aakash@example.com')
biraj = User('biraj',       'Biraj Das',    'biraj@example.com')
hemanth = User('hemanth',   'Hemanth Jain', 'hemanth@example.com')
jadhesh = User('jadhesh',   'Jadhesh Verma','jadhesh@example.com')
siddhant = User('siddhant', 'Siddhant Sinha','siddhant@example.com')
sonaksh = User('sonaksh',   'Sonaksh Kumar', 'sonaksh@example.com')
vishal = User('vishal',     'Vishal Goel',  'vishal@example.com')

database  = UserDatabase() 
database.insert(varun)
database.insert(aakash)
database.insert(jadhesh)


node0 = TreeNode(3)
node1 = TreeNode(4)
node2 = TreeNode(5)

node0.left=node1
node0.right=node2

tree = node0

tree_tuple = ((1,3,None),2,((None,3,4),5,(6,7,8)))
tree= BinaryTree.parse_tuple(tree_tuple)
print(tree.height())





























# from evaluate_test_cases import evaluate_test_cases
# from tests import test_cases

# from count_rotations import count_rotations  as function
# from  locate_card import locate_card
    # result = locate_card(
    #     x['inputs']['cards'] ,
    #     x['inputs']['query']
    #     )


# chosen = test_cases[:1]
# for x in chosen: 

#     result = function(x['input']['nums']) 
#     evaluate_test_cases(test_cases.index(x),result,x['output'])





