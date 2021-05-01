from decimal import Decimal
n,d,h = map(int,input().split())
D = [list(map(Decimal,input().split())) for _ in range(n)]
#print(d,D)
slope = Decimal(h)/Decimal(d)
for i in range(n):
    tmp = (D[i][1] - h)/(D[i][0] - d)
    slope = min(tmp,slope)
#y = slope*x + b
b = h - slope*d
print(b)