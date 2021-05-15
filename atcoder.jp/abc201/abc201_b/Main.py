n = int(input())
a = []
for i in range(n):
    b = list(input().split())
    a.append(b)
#print(a)
#昇順でソートする
sorted_data = sorted(a, key=lambda x:int(x[1]))
print(sorted_data[-2][0]) 