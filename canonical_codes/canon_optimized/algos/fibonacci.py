def fibonacci(i):
    '''
    Fibonacci sequence: sum of last two numbers in sequence. Debatable, can start
    with 0 as the first number, or 1. 

    This calls, recursively, for the sum of the last two numbers in the sequence 
    to produce the *next* fibonacci number. Those calls recurse down until the base
    cases of i = 0 or i = 1.

    '''

    if i <= 0: return 0         # input 0 or below? is ZERO
    if i == 1: return 1         # input 1? is 1 
    return fibonacci(i-1)+fibonacci(i-2)   

print(fibonacci(2))
print(fibonacci(7))