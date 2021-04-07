import math
n = int(input())
cnt = 0
list = []
for i in range(2,n+1):
    #print(math.floor(math.log(n,i)))
    if math.floor(math.log(n,i)) == 1:
        break
    else:
        cnt = math.floor(math.log(n,i)) 
        for j in range(2, cnt+1):
            #print(i**j)
            list.append(i**j)
print(n - len(set(list)))  