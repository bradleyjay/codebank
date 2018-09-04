# https://www.youtube.com/watch?v=_fgjrs570YE

def coin_change(amount, coins):

    # Step 1: Make array: 0 -> in target value columns, one row per "allowed" coin
    combos = [[ 0 for j in range(0,amount+1)] for i in coins]
    
    # Step 2: Need both index, and coin value
    for i,coin in enumerate(coins):

        # Step 3: Iterate through column values
        for j in range(0,amount+1):

            # initialize '0' value slot
            if j == 0:
                print((i,j))
                combos[i][j] = 1  

            # if current amount > coin val
            # if no previous row, just use a 0 
            elif j >= coins[i]:
                if i == 0:
                    combos[i][j] =        0        + combos[i][j-coins[i]]
                else:
                    combos[i][j] =  combos[i-1][j] + combos[i][j-coins[i]]
                    

            # if current amount < coin val
            else:
                combos[i][j] = combos[i-1][j]

    for row in combos:
        print(row)
    return combos


coins = [1,3,4]
coin_change(6, coins)