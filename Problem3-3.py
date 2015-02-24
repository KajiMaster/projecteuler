def prime_factors(n):
    i = 2
    factors = []
    while i * i <= n:
        while n > 1:
            while n % i == 0:
                factors.append(i)
                n //= i
            i += 1
    return factors[-1]

print prime_factors(600851475143)
