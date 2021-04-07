import sys

a,b = map(int,input().split())
low = int(min(a//0.08,b//0.1))
high = int(max((a+1)//0.08,(b+1)//0.1))
for i in range(low,high+1):
  if int(i*0.08)==a and int(i*0.1)==b:
    print(i)
    sys.exit()
print(-1)