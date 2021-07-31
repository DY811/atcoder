#https://github.com/ryusuke920/kyopro_educational_90_python

n, l = map(int,input().split())
k = int(input())
a = list(map(int,input().split()))
a.append(l)#右端を追加
#print(a)

dif = [a[0]] # 切り口の差を計算
for i in range(n):
    dif.append(a[i + 1]  - a[i])

#x以上の長さになったら切る
def is_ok(x):
    length = 0
    cnt = 0
    for i in dif:
        length += i
        if length >= x:
            length = 0
            cnt += 1
    return cnt # 分割する領域の個数

def meguru_bisect(ng, ok):
    while ng - ok > 1: #切り分けられない長さの最小ー切り分けることのできる長さの最大
        mid = (ng + ok) // 2
        if is_ok(mid) >= k + 1: # k＋１はようかんの個数
            ok = mid
        else:
            ng = mid # 小さくしなければいけない
    return ok

print(meguru_bisect(l, 1))#最大Lセンチを１センチずつに分けられる