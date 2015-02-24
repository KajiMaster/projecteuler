primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43]
factors = []
def prime_factors(n):
    for prime in primes:
        if n % prime == 0:
            factors.append(prime)
     


print prime_factors(600851475143)
