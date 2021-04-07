n,m = map(int,input().split())
food = list(range(1,m+1))
#print(food)
k = list(map(int,input().split()))
#suki = [a for a in k if a in food]
suki = k[1:]

for i in range(n-1):
    k = list(map(int,input().split()))
    k = k[1:]
    common = [b for b in k if b in suki]
    if len(common) == 0:
        print(0)
        break
    suki = common
else: #for loopまわりきったら
    print(len(suki))