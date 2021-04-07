n = int(input())
mina = 100000
minb = 100000
tmp0 = 0
tmp1 = 0
tmp2 = 0
time = 200000
for i in range(n):
    a, b = map(int, input().split()) 
    tmp0 = a + b
    tmp1 = max(a,minb)
    tmp2 = max(mina,b)
    time = min(time, tmp0, tmp1, tmp2)
    #print(tmp0,tmp1,tmp2)
    mina = min(mina,a)
    minb = min(minb,b)
print(time)