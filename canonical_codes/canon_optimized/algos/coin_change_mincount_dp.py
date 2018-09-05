# Problem: Make Change
# Goal: Min Coin Count

'''
Recipe:

1) Initialize Two Arrays
    1 - min_count   length = target val + 1
                    all = 999 (something big), except i[0] = 0

    2 - last_coin   length = target val + 1
                    all = -1

2) Iterate over each coin:  (j)
    Iterate over each value:    (i)

3) save min(min_count[i], 1 + min_count[i-coin[j]])
        if you do, save last used coin in last_coin

4) Get coins used:
    - start with target value, last coin taken
    - take target_value - value of that coin
    - now check for remaining value

5) Return

'''



# Make Change, MIN COUNT
def make_change_MINCOUNT(target_val, coins):

# Step 1: Initialize Two Arrays
    min_count = [9999] * (target_val + 1)
    min_count[0] = 0

    last_coin = [-1] * (target_val + 1)

# Step 2: Iterate over each coin, over all values:
    for j in range(0,len(coins)):
        for i in range(0,len(min_count)):

            # Step 3: take min(min_count[i], 1 + min_count[i-coins[j]])
            #              if you update it, save last used coin
            #           (because 1 + min_count[value-thisCoin) is one coin of that
            #            denom in value, off the current value. The coin count
            #            at that spot, + 1, is the number of coins to reach this spot, with
            #           these allowed coins so far.)

            if coins[j] <= i and min_count[i] > 1 + min_count[i-coins[j]]:
                min_count[i] = 1+ min_count[i-coins[j]]
                last_coin[i] = j

 # Step 4: Get coins used:
 #  - Start at target val
 #  - Subtract off last coin used at that value 
 #  - repeat til 0
 
    current_val = target_val
    coins_used = []

    while current_val > 0:
        coins_used.append(coins[last_coin[current_val]])
        current_val -= coins[last_coin[current_val]]


# Step 5: Report min coin count to hit target val, what those coins were:

    return min_count[target_val], coins_used


coins = [7,2,3,6]
print(make_change_MINCOUNT(13, coins))