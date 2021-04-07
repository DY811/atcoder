s = list(input())
t = list(input())

cnt = 0
for i in range(0,3):
    if s[i] == t[i]:
        cnt += 1
    else:
        cnt += 0
print(cnt)