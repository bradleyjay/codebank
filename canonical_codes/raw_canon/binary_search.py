
def binary_search(a_list,val):
    first = 0
    last = len(a_list)-1
    found = False

    while first <= last and not found:
        midpoint = (first + last) // 2
        if a_list[midpoint] == val: found = True
        elif a_list[midpoint] > val: last = midpoint - 1 ## already checked midpoint!!
        elif a_list[midpoint] < val: first = midpoint + 1

    return found

a_list = list(range(0,50))
print(binary_search(a_list,7))

## so, remember. Ditch the midpoint as you reset the window each time, and it doesn't
## need recursion. Dope!
