n = int(input())
a = list(map(int,input().split()))
if len(set(a)) == n:
    print('Yes')
else:
    print('No')