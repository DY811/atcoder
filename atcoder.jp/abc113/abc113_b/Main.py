N = int(input())
T, A = map(int,input().split())
H = list(map(int,input().split()))
temp = [0]*N

for i in range(N):
    temp[i] = abs(T - H[i]*0.006 - A)
print(temp.index(min(temp))+1)