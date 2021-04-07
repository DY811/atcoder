import math
x = int(input())

# is_prime
def is_prime(n):
    if n == 1: return False
    for k in range(2,int(math.sqrt(n))+1):
        if n%k == 0:
            return False
    return True
  
for i in range(10**5,10**8):
    if is_prime(i):
        max_n = i
        break

prime = [] # prime number 素数
for i in range(2,max_n+1):
    if is_prime(i):
        prime.append(i)
    if x <= prime[-1]:
        print(i)
        break