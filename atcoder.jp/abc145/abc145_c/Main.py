n = int(input())
town = []
cnt = 0
dist = 0
for i in range(n):
    x, y = map(int, input().split())
    town.append((x, y))
for i in range(n-1):
    for j in range(i+1, n):
        dist += pow((pow(town[i][0]-town[j][0], 2) + pow(town[i][1]-town[j][1], 2)), 0.5)
        cnt += 1

#各街間の距離の平均(dist/cnt)に全部街を回った時の移動回数n-1をかける
print((n-1)*dist/cnt)