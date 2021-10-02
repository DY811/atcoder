N = int(input())

login = []
for _ in range(N):
    A,B = map(int,input().split())
    login.append([A,1])
    login.append([A+B,-1])

login.sort()

#print(login)

from collections import defaultdict
dict = defaultdict(int)

people = 0
for log in login:
    people += log[1]
    dict[log[0]] = people

ans = [0]*(N+1)
start = login[0][0]

for key in dict:
    ans[dict[start]] += key - start
    start = key

print(*ans[1:])


