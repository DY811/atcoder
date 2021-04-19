A,B,C,X,Y = map(int,input().split())
AB = 2*C
Z = max(X,Y)
cost = [0]*(Z+1)

for i in range(Z+1):
    if i >= X and i >= Y:
        cost[i] = AB*i
    elif i >= X:
        cost[i] = AB*i + B*(Y-i)
    elif i >= Y:
        cost[i] = AB*i + A*(X-i)
    else:
        cost[i] = AB*i + A*(X-i) + B*(Y-i)

print(min(cost))