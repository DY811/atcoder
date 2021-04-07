# abc088 B Card Game for Two
n = int(input())
a = list(map(int,input().split()))
a.sort() #昇順
#print(a)
#print(a[0::2])
ans = sum(a[0::2])-sum(a[1::2]) #nから2個飛ばしで
ans = abs(ans)
print(ans)