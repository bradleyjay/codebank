'''

Top Down Memoized Knapsack

Tuskar's way was bottom up: do the table out, then find your answers.
CS dojo's way was just be recursive. Together, calc relevant value, memoize
values you've seen, then at end step back down to tell what items you took.


top_down_ks:
1) items table, item count and Capacity
2) blank matrix
3) KS function
4) items taken


'''

# 1) Items Table

items = (0,0), (1,1), (3,4), (4,5), (5,7)          # wt, val
n = 4
c = 7

# 2) blank matrix

matrix = [[None for col in range(c+1)] for row in range(n+1)]

# 3) KS function

def ks(i,w):
    if matrix[i][w] != None: return matrix[i][w]      # check memo
    elif i == 0 or w == 0: result = 0                 # base case
    elif items[i][0] > w: result = ks(i-1,w)          # can't take it bc space? same as i-1
    else:
        tmp1 = ks(i-1,w)                              # if you don't take vs...
        tmp2 = items[i][1] + ks(i-1,w-items[i][0])    # if you take
        result = max(tmp1, tmp2)                      # max of both
    matrix[i][w] = result                             # save to memo

    return result

# 4) items taken:

def which():
    i = n
    w = c

    knapsack = []

    while i > 0 and w > 0:
        if ks(i,w) != ks(i-1,w):           # if same, couldn't take.  otherwise, did!
            knapsack.append(i)              
            w = w - items[i][0]
            i = i - 1
        else:
            i = i - 1                      # since we didnt, go down an item. try again.

    return knapsack

print(which())
print(matrix)
