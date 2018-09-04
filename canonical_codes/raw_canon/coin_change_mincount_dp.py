# https://www.youtube.com/watch?v=NJuKJ8sasGk&t=272s

def min_count(amount, coins):

    # Step 1: Initialize arrays
    # 1) min_coins: min number of coins to reach value, thus far
    #               init: large num at each, 0 at i[0]
    # 2) last_taken: when min coins beats current record, save last taken coin
    #               init: -1 (saving index of coin matrix value, start as nonsense)

    
    min_coins = [999] * (amount+1)   # number of coins to reacha given value i (i is also index)
    min_coins[0] = 0
    last_taken = [-1] * (amount+1)

    # Step 2: Iterate over coins
    for j in range(0,len(coins)):  

        # Step 3: Iterate over values up to target amount
        for i in range(0,len(min_coins)):   # 

            # Step 4: If coin is smaller than current value,
            #         and this combo used fewer coins than last best,
            #         1) Save as best score for 1 + (val-curr_coin)
            #         2) Save this coin as last coin taken in last_taken

            if coins[j] <= i and min_coins[i] > 1+min_coins[i-coins[j]]:
                min_coins[i] = 1 + min_coins[i-coins[j]]
                last_taken[i] = j

    # Step 5: 'Coins taken' found by going to target amount, then checking 
    #          last coin used (from last_taken). Subtract off that value,
    #          then check *that* last_taken value, repeat til 0.
    #

    current_val = amount
    which_coins = []

    while current_val > 0:
        which_coins.append(coins[last_taken[current_val]])
        current_val -= coins[last_taken[current_val]]


    # Step 6: return
    return min_coins[amount], which_coins






coins = [7,2,3,6]
print(min_count(13, coins))