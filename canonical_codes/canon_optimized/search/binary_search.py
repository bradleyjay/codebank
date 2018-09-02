# Binary Search

'''

-Requires sorted array. Log(N) time.
-Uses pointers: check mid, move pointer to one side of mid (ditch midpoint)

Step 1: Initialize FIRST, LAST pointers, FOUND = FALSE
Step 2: While Loop: while first <= last and not found
Step 3: Set Mid Index: mid = (first+last) // 2
Step 4: Check Mid: 
    Found? Done. 
    Val larger? Move first to mid+1. 
    Val smaller? Move last to mid-1.      
Step 5: Return

'''



def bin_search(a_list, val):

    # Step 1: Initialize
    first = 0
    last = len(a_list)-1
    found = False

    # Step 2: While Loop
    while first <= last and not found:

        # Step 3: Set Mid Index
        mid = (first + last) // 2

        # Step 4: Check Mid: Found / move first up to mid+1 / move last down to mid-1

        if a_list[mid] == val: found = True
        elif a_list[mid] < val: first = mid + 1
        elif a_list[mid] > val: last = mid - 1

    # Step 5: Return
    return found

## so, remember. Ditch the midpoint as you reset the window each time.


a_list = list(range(0,50))
print(bin_search(a_list,49))
