from collections import deque
n = int(input())
a = list(map(int,input().split()))
a.sort()
#print(a)
d = deque(a)
second = 0
for i in range(1,n+1):
    d.pop()#1
    second += d.pop() #2
    d.popleft() #3
print(second)