from collections import deque
n = int(input())
four = list()
kukan = list()


for i in range(n):
    tmp = deque(list(map(int,input().split())))
    a = tmp.popleft()
    b = list(tmp)
    if a == 2:
        b[1] += -0.1
    elif a == 3:
        b[0] += 0.1
    elif a == 4:
        b[1] += -0.1
        b[0] += 0.1
    four.append(a)
    kukan.append(b)
#print(four)
#print(kukan)
cnt = 0
for i in range(n):
    for j in range(i+1,n):
        if kukan[i][1] < kukan[j][0] or kukan[j][1] < kukan[i][0]:
            cnt += 0
        else:
            cnt += 1
print(cnt)
    