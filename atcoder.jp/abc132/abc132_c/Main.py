import statistics
n = int(input()) # 問題の個数
d = list(map(int,input().split()))
cnt = 0

d.sort()
m = len(d)
k_index = int(m/2)
if d[k_index] != d[k_index-1]:
    max_k = d[k_index]
    low_k = d[k_index-1]
    cnt = max_k - low_k
else:
    cnt = 0
print(cnt)