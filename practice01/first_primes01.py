print("Hello, world!, 30 September, post dinner session")
import math
from math import sqrt
primes_in = 1000
check_limit = int(1+sqrt(1000))
prime_list=[2]
print (check_limit)
def prime_or_not(n):
    # 1. Reject numbers less than 2
    if n < 2:
        return False

    # 2. Only check divisors up to sqrt(n)
    limit = int(sqrt(n)) + 1

    # 3. Loop through possible divisors
    for i in range(2, limit):
        # 4. If divisible, it's not prime
        if n % i == 0:
            return False

    # 5. If no divisors found, it's prime
    return True
        
        
                
#print(prime_or_not(12))


for m in range(3, 1001):
    if prime_or_not(m):
        prime_list.append(m)
        

             
print(prime_list)            
                          