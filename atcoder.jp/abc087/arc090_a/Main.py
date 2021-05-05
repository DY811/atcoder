n = int(input())
a1 = list(map(int,input().split()))
a2 = list(map(int,input().split()))
"""
 左上および右下のマスにもアメが置かれており、あなたはこれらのマスに置かれているアメも回収します。
 ↑この設定どこいった？
a1_candies = [0]*n
a2_candies = [0]*n

for i in range(n):
    if i < n-1 and i > 1:
        a1_candies[i] = a1[i] + a2[i+1]
        a2_candies[i] = a1[i-1] + a2[i]
    elif i < n-1 and i == 1:
        a1_candies[i] = a1[i] + a2[i+1]
        a2_candies[i] = a2[i]
    elif i == n-1:
        a1_candies[i] = a1[i]
        a2_candies[i] = a1[i-1] + a2[i]
"""
max_candies = 0
for i in range(n):
    tmp = sum(a1[0:i+1]) + sum(a2[i:])
    max_candies = max(tmp,max_candies)
print(max_candies)