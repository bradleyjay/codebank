## RADIX SORT

## note - LSD version

# 1) Create buckets for each digit in base
# 2) Iterate through list, add numbers to buckets
# 3) Move up a digit, repeat

# for iteration 0 to start, 

def radix_sort(an_array, base = 10):
    def list_to_buckets(an_array, base, iteration):
        ## list of lists
        buckets = [[] for x in range(base)]
            for number in an_array:
                ## isolate base digit from number. This is say, 12 // 10**0 = 12.
                ## then, 12 % 10 = 2, or the base digit.
                digit = (number // base ** iteration) % base

                #drop that sucker in the right bucket:
                buckets[digit].append(number)
                
            return buckets

    def buckets_to_list(buckets):
        numbers = []
        for bucket in buckets:
            ##append numbers to a bucket sequentially (!) to the array
            for number in bucket:
                numbers.append(number)
        return numbers

    maxval = max(array)

    it = 0
    # iterate, sorting the array by each base-digit:
    while base ** it <= maxval:
        array = buckets_to_list(list_to_buckets(array, base, it))
        it += 1

    return array
