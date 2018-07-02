'''

Binary Tree: basic, + insert check n' swap if present.
                - No node class, self-symmetric everywhere


1) Constructor: value, lc, rc
2) Insert method: add, or create/attach lc to new/attach new at self.lc
3) Get lc, get rc

'''

class bin_tree():

# 1) Constructor: value, left child, right child

    def __init__(self,value):
        self.value = value
        self.left_child = None
        self.right_child = None


# 2) Insert left, right

    def insert_left(self,value):

        # None? Create as new tree at self.left_child
        if self.left_child == None:
            self.left_child = bin_tree(value)

        else:
            # create
            n = bin_tree(value)

            # attach current -> new
            n.left_child = self.left_child

            # attach new -> self
            self.left_child = n


    def insert_right(self,value):
        if self.right_child == None:
            self.right_child = bin_tree(value)
        else:
            n = bin_tree(value)
            n.right_child = self.right_child
            self.right_child = n


# 3) Get left, right
    def get_left_child(self):
        return self.left_child

    def get_right_child(self):
        return self.right_child


# tests
bt = bin_tree(4)
bt.insert_left(5)
bt.insert_right(3)
bt.insert_left(45)

print(bt.get_left_child().value)
