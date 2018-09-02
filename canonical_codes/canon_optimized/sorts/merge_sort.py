
# https://stackoverflow.com/questions/18761766/mergesort-python
# uses 2N space in calc, but 2N = N for large N (this applies for space..?)

''' 

Recursive splits (logN), merge back together (N) -> (N log N)

1) Base case: len(x) < 2: return x
2) Set mid, call recursive on L, R
3) Add smaller val from each side to RESULT with position indicies
4) Add remaining elements
5) return RESULT

'''

def merge_sort(x):

    # Step 1: Base Case
    if len(x) < 2: return x

    # Step 2: Set mid, call recursives on L, R

    mid = len(x)//2

    L = merge_sort(x[:mid])
    R = merge_sort(x[mid:])

    # Step 3: Add smaller val from each side to RESULT using position indicies

    i = 0
    j = 0
    result = []

    while i < len(L) and j < len(R):

        if L[i] < R[j]:
            result.append(L[i])
            i += 1

        else:
            result.append(R[j])
            j += 1

    # Step 4: Add remaining elements
    result += L[i:]
    result += R[j:]

    # Step 5: Return RESULT
    return result

a = [5,2,3,77,22,55,33]
print(merge_sort(a))
