## MIN HEAPS attempt 2, with study.

"""
NEEDS:
1) Constructor

2) Insert
3) Perc Up

4) Del Min
5) Perc Down
6) Min Child

- no pointers, use list on head, list[0] = 0 and size = 0, perc loops check for 
valid child or parent by 2i, i // 2 method.
- current_size important

"""

class BinHeap():
    def __init__(self):
        self.hl = [0]
        self.size = 0

    def insert(self, data):
        self.hl.append(data)
        self.size += 1
        self.perc_up(self.size)

    def perc_up(self,i):

        while i // 2 > 0:
            if self.hl[i // 2] > self.hl[i]:
                tmp = self.hl[i//2]
                self.hl[i//2] = self.hl[i]
                self.hl[i] = tmp
            i = i // 2

    def del_min(self):
        saved = self.hl[1]
        self.hl[1] = self.hl[self.size]
        self.size -= 1
        self.hl.pop()
        self.perc_down(1)
        return saved

    def perc_down(self,i):
        while (i * 2 <= self.size):
            mc = self.min_child(i)
            if self.hl[mc] < self.hl[i]:
                tmp = self.hl[i]
                self.hl[i] = self.hl[mc]
                self.hl[mc] = tmp
            i = mc
    def min_child(self,i):
        if self.size < (2*i + 1):
            return 2 * i
        else:
            if self.hl[2*i] < self.hl[2*i + 1]:
                return 2* i

            else:
                return 2*i+1

A = BinHeap()
A.insert(2)
A.insert(5)
A.insert(6)
A.insert(25)
print(A.del_min())

## trick is where you actually gate for the child, parent. on the percs,
## they should act until there isn't a parent (i // 2 = 0), or isn't a
## child (2 * i > size)
