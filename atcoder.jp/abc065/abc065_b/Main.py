n = int(input())
a = []
for i in range(n):
    a.append(int(input()))
#print(a)
cnt = 0
num = 1
while cnt <= n:
    if num == 2:
        print(cnt)
        break
    num = a[num-1]
    cnt += 1
if cnt > n:    
    print(-1)