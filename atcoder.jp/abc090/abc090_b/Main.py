a, b = map(int,input().split())
cnt = 0

for i in range(a,b+1):
    mae = str(i)
    ushiro = mae[::-1] #reversed
    if mae == ushiro:
        cnt += 1
print(cnt)