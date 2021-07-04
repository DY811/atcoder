import math
p = int(input())
yen = []
for i in range(1,11):
    yen.append(math.factorial(i))
#print(yen)
cnt = 0
for i in range(1,11):
    cnt += p//yen[-i]
    p = p%yen[-i]
print(cnt)
    

