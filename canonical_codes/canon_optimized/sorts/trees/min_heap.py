## min heap - canonnical

'''
Binary Min Heap: 

Essentially LIST, kind of a tree. Smallest values float up to root (index 1). 
UN-USED 0 index. Parents always smaller than children.

-No pointers, just index. 2*i = lc, 2*i + 1 = rc, i // 2 = parent. Root = 1
-On Insert, new value appended, then perc up
-On del_min, min (root) value returned, last value in list moved to root, perc down
-Always update size!

1) Constructor: head list, size
2) Insert, del_min
3) Perc Up, Perc Down
4) Min Child

'''

class Bin_Heap():

    # 1) Constructor: headlist, size
    def __init__(self):
        self.head_list = [0]
        self.size = 0



    # 2) insert, del_min

    def insert(self,data):

        # 1) append to list, 
        # 2) increment size, 
        # 3) perc up new value

        self.head_list.append(data)
        self.size += 1
        self.perc_up(self.size)

    
    def del_min(self):
        # 1) save root
        # 2) copy last value in list to root, pop last value, size -= 1
        # 3) perc down new root

        saved = self.head_list[1]                              # save root value

        self.head_list[1] = self.head_list[self.size]          # copy last value to root
        self.head_list.pop()                                   # pop last value
        self.size -= 1                                         # deincriment size
        
        self.perc_down(1)                                      # perc down new root
        return saved



    # 3) Perc Up, Perc Down

    def perc_up(self,i):
        # 1) While not root, 
        # 2) if parent > child, swap. 
        # 3 )Move index to parent.

        while i // 2 > 0:      # while not root
            if self.head_list[i//2] > self.head_list[i]:      # parent > child? swap
                tmp = self.head_list[i//2]                 # save parent
                self.head_list[i//2] = self.head_list[i]   # set parent to child
                self.head_list[i] = tmp                    # set child to tmp
            i = i // 2                                     # move up to the parent

    def perc_down(self,i):
        # 1) i * 2 is still in list (child exists)
        # 2) min child < i? swap
        # 3) set i to min child index

        while (i * 2 <= self.size):
            mc = self.min_child(i)

            if self.head_list[mc] < self.head_list[i]:     # if min child val smaller than current
                tmp = self.head_list[i]                    # swap
                self.head_list[i] = self.head_list[mc]
                self.head_list[mc] = tmp
            i = mc                                         # set to min child index


    def min_child(self,i):
        # 1) no rc? return lc
        # 2) lc < rc? return lc
        # 3) lc > rc, return rc

        if self.size < (2*i+1):                             # if theres no rc
            return 2 * i                                    # return lc
        else:
            if self.head_list[2*i] < self.head_list[2*i + 1]:   #if lc < rc, return lc
                return 2 * i
            else:   
                return 2*i + 1                                  # since lc > rc, return rc.



#tests

A = Bin_Heap()
A.insert(2)
A.insert(4)
A.insert(7)
A.insert(33)
A.insert(1)
print(A.del_min())
