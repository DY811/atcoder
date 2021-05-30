n = int(input())
a = list(map(int,input().split()))
cnt = 1
#全てか奇数になる組み合わせを数える
for i in range(n):
    if a[i]%2 == 0:
        cnt *= 2
#すべての数列から、奇数になる数列（偶数の時は2通りある）を引く
print(3**n-cnt)