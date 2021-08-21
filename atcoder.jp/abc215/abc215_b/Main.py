import math
n = int(input())
#print(int(math.log2(n)//1))

for i in range(100):
    if n == 1:
        print(0)
        exit()
    elif 2**i <= n:
        continue
    else:
        print(i-1)
        exit()
    

