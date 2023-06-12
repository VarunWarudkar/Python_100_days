import itertools

def prime():
    # handle first part 
    yield 2

    #handle second part
    prime_cache = [2]
    #loop over all odd numbers
    for n in itertools.count(3, 2):
        is_prime = True
        
        #check any prime number devides n
        for p in prime_cache:
            if n % p == 0:
                is_prime = False
                break
            
        if is_prime:
            prime_cache.append(n)
            yield n


for p in prime():
    if p > 10:
        break
    print(p)
    
