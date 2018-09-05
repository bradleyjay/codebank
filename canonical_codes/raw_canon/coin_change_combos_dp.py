# https://www.youtube.com/watch?v=_fgjrs570YE

def coin_change(amount, coins):

    # Step 1: Initialize matrix 'combos'
    #         One column in 1's up to target value
    #         One row per coin "allowed yet" 
    #         0's everywhere, except 0 value column gets 1's

    combos = [[ 0 for j in range(0,amount+1)] for i in coins]
    for i in range(0, len(coins)):
        combos[i][0] = 1

    # Step 2: Iterate over coins, iterate over values
    #         Need both index, and coin value

    for i,coin in enumerate(coins):
        for j in range(0,amount+1):

            # Step 3: # combos is:
            #               whatever you could have done, with just prevoiusly allowed coins
            #               plus combos of this val - this denom (since this that val, plus this denom)
            #
            # if current amount > coin val
            # if no previous row, just use a 0 

            if j >= coins[i]:
                if i == 0:
                    combos[i][j] =        0        + combos[i][j-coins[i]]
                else:
                    combos[i][j] =  combos[i-1][j] + combos[i][j-coins[i]]
                    

            # Step 4: This coin too big? Same as row before, when this coin wasn't allowed
            # if current amount < coin val
            # (why doesnt this go out of index if the coin is too small, and row = 0...?)
            else:
                combos[i][j] = combos[i-1][j]



    for row in combos:
        print(row)

    # Step 5: return
    return combos


coins = [1,3,4]
coin_change(6, coins)