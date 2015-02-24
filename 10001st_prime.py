primes = [2, 3, 5, 7, 11, 13, 17]
count = 0

def is_prime(x):
    if x % 2 == 0:
        return False
    else:
        for n in range(3, x, 2):
            if x % n == 0:
                return False
        return True

while len(primes) < 10002:
    print count
    if is_prime(count) == True:
        primes.append(count)
        count = primes[-1] + 2
    else:
        count = primes[-1] + 2

print primes[-1]


