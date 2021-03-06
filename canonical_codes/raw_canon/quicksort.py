## QUICK SORT
## Similar speed to MERGE SORT, but takes no extra space. However,
## it's worst case is O(n^2)

## Gist of it is, you split each list, then recursively move down into the 
## less than and greater than lists. by the time you're done, you've sorted each
## sublist et. al., and the wrinkle: you've been sorting ON THE LIST the whole
## time. So no merging or copying, the sublists are sorted so the LIST is sorted!!


def quick_sort(a_list):
    ## this keeps initial call from being recursive, so that we start with the 
    ## whole list.
    quick_sort_helper(a_list,0,len(a_list)-1)

def quick_sort_helper(a_list, first, last):
    
     ## Start here. Recursive bit: do this if til base case, where list length 
     ## is 0 or 1.
    if first < last:

       
        split_point = partition(a_list,first, last)

        ## Ok, we're back. STEP 3: Now, quicksort the below-split-point list and
        ## above-split-point list.

        quick_sort_helper(a_list, first, split_point -1)
        quick_sort_helper(a_list, split_point + 1, last)

def partition(a_list, first, last):
    ## STEP 1: Choose pivot value (arbitary, here)
    pivot_value = a_list[first]

    ## STEP 2: Partition Process - find split point, exchange items to be on
    ## correct side of it til you do. By incrementing leftmarker, find 
    ## element on left of pivot that's LARGER than pivot value. By de-incrementing
    ## right marker, find element on right of pivot that's SMALLER than pivot.
    ## Swap.

    left_mark = first+1 ## because first is pivot
    right_mark = last

    done = False
    while not done:

        # while left and right mark haven't crossed sides yet, advance left
        # mark til you find a larger value than pivot
        while left_mark <=right_mark and a_list[left_mark] <= pivot_value:
            left_mark = left_mark + 1

        # while left and right mark haven't crossed sides yet, decrease right
        # mark til you find a smaller value than pivot
        while a_list[right_mark] <= pivot_value and right_mark >= left_mark:
            right_mark = right_mark - 1

        # if marks have crossed, you're done. Don't do anything else.
        if right_mark < left_mark:
            done= True

        # otherwise, exchange values at left and right marks. repeat this til
        # they cross

        else:
            temp = a_list[left_mark]
            a_list[left_mark] = a_list[right_mark]
            a_list[right_mark] = temp

    ## finally, exchange value at right mark (the split point) with our pivot
    ## value.

    temp = a_list[first]
    a_list[first] = a_list[right_mark]
    a_list[right_mark] = temp

    return right_mark

a_list = [24, 52, 82, 93, 20, 33, 22, 54, 64, 32]
quick_sort(a_list)
print(a_list)
