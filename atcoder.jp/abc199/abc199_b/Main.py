n = int(input())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
if min(b)-max(a)+1 >= 0:
    print(min(b)-max(a)+1)
else:
    print(0)