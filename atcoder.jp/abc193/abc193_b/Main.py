n = int(input())
price = [0]*n

for i in range(n):
    #print(i)
    a, p, x = map(int, input().split()) # 所要分、価格、在庫
    if x - (a+0.5) > 0: # in stock
        price[i] = p
    else:
        price[i] = float('inf')
if min(price) == float('inf'):
    print(-1)
else:
    print(min(price))