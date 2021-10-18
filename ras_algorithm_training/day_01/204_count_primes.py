"""
Count the number of prime numbers less than a non-negative number, n.
notes:
- less than only, n is not included
"""

def countPrimes(n: int) -> int:
    if n < 3:
        return 0
    primes = [True] * n            # make a list of n True by default
    primes[0] = primes[1] = False  # cancel 0 and 1 as they are not primes 
        
"""
loop from first prime(0) up to sqrt(n) why is that ?
If a number n is not a prime, it can be factored into two factors a and b: n = a * b
Now a and b can't be both greater than the square root of n, since then the product a * b would be greater than sqrt(n) * sqrt(n) = n
So in any factorization of n, at least one of the factors must be smaller than the square root of n, and if we can't find any factors less than or equal to the square root, n must be a prime.
"""    
    for i in range(2, int(n ** 0.5) + 1):  
        if primes[i]:
            for j in range(i * i, n, i):  # set all multiple of first none-prime to false
                primes[j] = False

    return sum(primes)


print(countPrimes(21))
