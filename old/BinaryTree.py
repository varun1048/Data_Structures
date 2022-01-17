class TreeNode:
    def __init__(self,key) -> None:
        self.key = key
        self.left = None
        self.right = None
        
    # def __repr__(self):
    #     return f"""key:{self.key} 
    #     Right:{self.right} Lift:{self.left}"""
    
    # def __str__(self):
    #     return self.__repr__()


class BinaryTree():
    def __init__(self, key):
        self.key, self.left, self.right = key, None, None
    
    def height(self):
        if self is None:
            return 0
        return 1 + max(BinaryTree.height(self.left), BinaryTree.height(self.right))
    
    def size(self):
        if self is None:
            return 0
        return 1 + BinaryTree.size(self.left) + BinaryTree.size(self.right)

    def traverse_in_order(self):
        if self is None: 
            return []
        return (BinaryTree.traverse_in_order(self.left) + 
                [self.key] + 
                BinaryTree.traverse_in_order(self.right))
    
    def display_keys(self, space='\t', level=0):
        # If the node is empty
        if self is None:
            print(space*level + '∅')
            return   

        # If the node is a leaf 
        if self.left is None and self.right is None:
            print(space*level + str(self.key))
            return

        # If the node has children
        self.display_keys(self.right, space, level+1)
        print(space*level + str(self.key))
        self.display_keys(self.left,space, level+1)    
    
    def to_tuple(self):
        if self is None:
            return None
        if self.left is None and self.right is None:
            return self.key
        return BinaryTree.to_tuple(self.left),  self.key, BinaryTree.to_tuple(self.right)
    
    def __str__(self):
        return "BinaryTree <{}>".format(self.to_tuple())
    
    def __repr__(self):
        return "BinaryTree <{}>".format(self.to_tuple())
    
    @staticmethod    
    def parse_tuple(data):
        if data is None:
            node = None
        elif isinstance(data, tuple) and len(data) == 3:
            node = BinaryTree(data[1])
            node.left = BinaryTree.parse_tuple(data[0])
            node.right = BinaryTree.parse_tuple(data[2])
        else:
            node = BinaryTree(data)
        return node