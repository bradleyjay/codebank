## Merge Sort
## Recrusively split list until lengh is 1 or empty. Going back up involves
## merging the sorted lists. 


## At most, any list can be split log(n) times, and each one needs a merge, 
## which costs O(n). So together, O(NlogN)

## NOTE: If start and end indicies are passed along with list at recursive call,
## can remove slice. Slice is O(k), so MUST be removed for actual O(nlogn) 
## performance.

def merge_sort(a_list):

    print("Splitting: ")
    print(a_list)
    
    ## base case: right here. If list length ( and successive mergesort calls
    ## are using left or right half as list ) is 1 or 0, you're done.
    ## then move up a level, sort that chunk of the list, and so on.

    if len(a_list) > 1:
        mid = len(a_list) // 2

        ## this is where the storage monstrosity happens. COPYIED here. OHHHH
        ## also, this is happening inside each level.. (Q) so...is that just double?
        ## or lots more?

        left_half = a_list[:mid]
        right_half = a_list[mid:]

        ## this algo marches up funny. first call calls another left half mergesort,
        ## which calls another...no right half merge sort happens til left base
        ## case reached. Then right of last left list, so another single value.
        ## whole main list left half merge_sort occurs before main list right half
        ## begins.

        merge_sort(left_half) 
        merge_sort(right_half)



        ## Part I:
        ## so, this chunk looks at the left most value of left list
        ## and compares to leftmost value of right list.
        ## THE WINNER LIST gets incremeneted only. 
        ## Then, the fullList index gets incremented.
        ## In effect, you're filing the smaller value of left and right
        ## in the main list. 

        ## repeat until you've finished both one of the two lists.


        i = 0   # left half list index
        j = 0   # right half list index
        k = 0   # full list index
        
        while i < len(left_half) and j < len(right_half):

            # value of left[i] < value of right[j]?
            if left_half[i] < right_half[j]:
                
                # then save value of left[i] to fullList[k] 
                a_list[k] = left_half[i]


                i = i + 1

            # if value of left[i] !< value of right[j]
            else:
                
                #save value of right[j] to fullList[k]
                a_list[k] = right_half[j]
                j = j + 1

            # so after filing away either left[i] or right[j], 
            # incremenet fullList k
            k = k + 1

        # Part II:
        ## cleanup - finish the other list.


        while i < len(left_half):

            a_list[k] = left_half[i]
            i = i + 1
            k = k + 1

        while j < len(right_half):

            a_list[k] = right_half[j]
            j = j + 1
            k = k + 1

    print("Merging ", a_list)

a_list = [54, 26, 93, 17, 77, 31, 44, 55,20]
merge_sort(a_list)
print(a_list)
