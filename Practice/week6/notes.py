import time

# A Fibonacci sequence is the integer sequence of 0, 1, 1, 2, 3, 5, 8....
# The first two terms are 0 and 1. All other terms are obtained by adding the preceding two terms.
# This means to say the nth term is the sum of (n-1)th and (n-2)ith term.     F    F      F
#                                                                       ie:    n =  n-1 +  n-2

# Recursive Fibonacci Function

def fibonacci (n) :
    if n <= 1:
        return n
    else:
        return fibonacci (n-1) + fibonacci (n-2)


nthTerm = 6

start_time = time.time()
print(fibonacci(nthTerm))
end_time = time.time()
print(f"The excution time is: {end_time-start_time}")

# The algorithm below sacrifices space complexity for time, as it uses the memory to store the results to the function calls.

def dyna_fib(n, lookup) :
    if n <= 2:
        lookup[n] = 1
    
    if lookup[n] is None:
        lookup[n] = dyna_fib(n-1, lookup) + dyna_fib(n-2, lookup)

    return lookup[n]

fibonacci_values = [None] * (10000)
nthTerm = 6
start_time = time.time()
print(dyna_fib(nthTerm, fibonacci_values))
end_time = time.time()
print(f"The execution time is: {end_time-start_time}")

# Greedy Algorithms
# Coin Change problem - Example of Greedy Algorithm

coins = [1, 5, 10, 25]
changeNeeded = 46


def changeDue(change):
    coinsUsed = []
    coins.reverse()
    for coin in coins:
        while coin <= change:
            change -= coin
            coinsUsed.append(coin)
        if change == 0:
            break
    return coinsUsed
    
print(changeDue(changeNeeded))