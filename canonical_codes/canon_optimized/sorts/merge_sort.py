
# https://stackoverflow.com/questions/18761766/mergesort-python
# uses 2N space in calc, but 2N = N for large N (this applies for space..?)

''' 
merge sort:

1) base case
2) Save recursive call on L, R
3) Add smaller value from each side to temp list using pos indicies, Result
4) Add remaining
5) Return result

'''

def msort3(x):

    # 1) base case (array size)
    
    if len(x) < 2:
        return x
    
    # 2) Call recursives on L, R

    mid = len(x) // 2
    
    left_half = msort3(x[:mid])
    right_half = msort3(x[mid:])

    #3) Add smaller value from each side to RESULT using pos indicies

    result = []
    i = 0
    j = 0

    while i < len(left_half) and j < len(right_half):
        
        if left_half[i] > right_half[j]:
            result.append(right_half[j])
            j += 1
        else:
            result.append(left_half[i])
            i += 1

    # 4) Add remaining elements

    result += left_half[i:]
    result += right_half[j:]

    # 5) return RESULT
    return result

a = [5,2,3,77,22,55,33]
print(msort3(a))
