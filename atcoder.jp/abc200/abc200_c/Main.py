n= int(input())
a = list(map(int, input().split()))

amari = [0]*200
#２つの数字の差が200の倍数ならそれらの余りは同じになる

for x in a:
  amari[x%200] += 1

#print(amari)

ans = 0
for x in amari:
  ans += x*(x-1)//2 #nC2

print(ans)