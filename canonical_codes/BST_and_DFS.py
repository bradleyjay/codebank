## two classes: tree, node. Leaving out deletion for now.
# https://www.youtube.com/watch?v=f5dU3xoE6ms

# for ease, assume integers

# node class
class node:
    def __init__(self,value=None):
        self.value = value
        self.lc = None
        self.rc = None

## bst is WRAPPER of node management
class BST: 
    def __init__(self):
        ## starts empty
        self.root = None

    ## most basic.
    def insert(self,value):

        ## can we insert at root? 
        if self.root == None:
            self.root=node(value)
        else: ## can't insert at root?
            self._insert(value,self.root)      ## means its a "private" fcn. just a convention
                                                ## that says, hey user, don't call this outside the class.
    ## seperate because the private insert will be recursive, and won't have
    ## all that logic hanging on.

    def _insert(self,value,cur_node):
        # less than current node?
        if value<cur_node.value:
            #break into two more cases. 1) no left child. 2) no right child
            if cur_node.lc == None:
                cur_node.lc = node(value)
            else: ## there IS a lc
                ## call recursive insert, but pass current node's left child as new cur node. DOPE
                self._insert(value,cur_node.lc)
        elif value > cur_node.value:  ## ok, so if cur val is larger than right node.
            ## same deal, breaks into two. 
            if cur_node.rc == None:
                cur_node.rc=node(value)
            else:
                self._insert(value,cur_node.rc)

        ## note: leaves out = case. 
        else:
            print("Value already in tree!")  ## no bueno, not for that

        '''
        summary: 
            - if inserted node larger than current node, either insert it, or 
                recurse and try again
            - if inserted node smaller than current node, either insert it or 
                recurse and try again.

            otherwise, error - already have that value
        '''

    def print_tree(self):
        ## first, is the root a node?
        if self.root != None:   ## which is default when tree created
            self._print_tree(self.root)  ## again, splitting into recursive and not 

    def _print_tree(self,cur_node):
        if cur_node!=None:

            ## in order traversal. In order? SORTED ASCENDING!!
            self._print_tree(cur_node.lc)
            print(cur_node.value)
            self._print_tree(cur_node.rc)




     ################## basic function complete. ###############
     
    def height(self):
        if self.root!=None:
            return self._height(self.root,0)
        else:
            return 0

    def _height(self,cur_node,cur_height):
    ## pass integer because we need to store height we've seen on each recursive call      
        if cur_node == None: return cur_height
    ## rest of height from left subtree, then right. Compare, return larger
        left_height = self._height(cur_node.lc, cur_height+1) ## increment in the call
        right_height = self._height(cur_node.rc, cur_height+1)
        return max(left_height, right_height)

        ## so note, this is done at every node of the tree. when you hit leaf, returns 
        ## current node is none at a leaf, so it returns current height. Cool



        ####### search functions - pub and priv, with recursive private #####


    def search(self,value):
        ## go find it. Empty tree? False. Found it?
        if self.root!= None:
            return self._search(value,self.root)
        else:
            return False

    def _search(self,value,cur_node):  ## depth first search!

        ## first, value = to current node val?
        if value == cur_node.value: return True
        elif value < cur_node.value and cur_node.lc != None: ## if smaller, cur HAS lc
        ## then return this fcn, looking at lc
            return self._search(value,cur_node.lc)
        elif value>cur_node.value and cur_node.rc != None: ## and cur HAS right
            ## go serach that right tree
            return self._search(value,cur_node.rc)

        ## now, the other cases. Or, we've finished all this and didn't find it
        ## let's think about this. if you're on a value, and you went left, but are larger,
        ## and there's no next rc, that's it. 
        ## likewise, if you're on a value, you came from left, and you're still smaller
        ## than that node, you're done.

        ## it's awesome. A BST keeps cutting the domain in two, so once you've passed a value,
        ## you're can't pass back past it. Otherwise, the values youre searching would be
        ## in the other tree that you were filtered away from.
        return False




def fill_tree(tree, num_elems=100,max_int=1000):
    from random import randint
    for _ in range(num_elems):
        cur_elem=randint(0,max_int)
        tree.insert(cur_elem)
    return tree

tree = BST()
#tree = fill_tree(tree)

tree.print_tree()
tree.insert(35)
tree.insert(11)
tree.insert(28)
tree.insert(36)
tree.insert(25)
tree.insert(5)
tree.insert(3)

print('Tree height is ' + str(tree.height()))
print(tree.search(25))
print(tree.search(4))
