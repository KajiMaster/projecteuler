primes = [2, 3, 5, 7, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71]
prime_factors = []
extra = 0
the_number = 13195

def break_down(x):
    for prime in primes:
        if x % prime == 0:
            prime_factors.append(prime)
            extra = x / prime
            
def main():
    break_down(the_number)
    print "The prime factors of %s are: " % the_number
    #prime_factors.sort()
    print prime_factors
    print "The largest prime factor of the group is: "
    print max(prime_factors)

main()
