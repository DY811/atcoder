num = list(map(int,input().split()))
num.sort()
cnt = 0
#１番大きな数字と同じか1小さくなるまで２を足す
if num[2]-num[0]>0:
    cnt += (num[2]-num[0])//2
    num[0] = num[0] + 2*((num[2]-num[0])//2)
if num[2]-num[1]>0:
    cnt += (num[2]-num[1])//2
    num[1] = num[1] + 2*((num[2]-num[1])//2)
#3の倍数−1なら後２回（２を足す、１をそのほか２つに足す）
#3の倍数−2なら後一回
if num[0] == num[1] == num[2]:
    print(cnt)
elif sum(num)%3 == 2:
    print(cnt+2)
else:
    print(cnt+1)
   