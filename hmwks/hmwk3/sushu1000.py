def era(limit):  
    primes = [True] * (limit + 1)  
    primes[0] = primes[1] = False  
    for i, is_prime in enumerate(primes):  
        if is_prime:  
            yield i  
            for n in range(i*i, limit + 1, i):  
                primes[n] = False  
  
def print_primes(limit):  
    for prime in era(limit):  
        print(prime)  
  
print_primes(1000)