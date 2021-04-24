n, m = map(int, input().split())
paths = [(i, []) for i in range(n)]
for _ in range(m):
    a, b = map(int, input().split())
    a, b = a-1, b-1
    paths[a][1].append(b)
    paths[b][1].append(a)
paths.sort(key=lambda path: len(path[1]), reverse=True) #繋がっているものが多い順
#print(paths)

color_map = [0 for _ in range(n)]
def counting(index):
    if index == n:
        return 1
    pos, path = paths[index] #position and linked paths
    if len(path) == 0: #繋がっていないので3通りある
        return 3**(n - index)
    flag = [True for _ in range(4)]
    for node in path:
        flag[color_map[node]] = False
    ret = 0
    for color in range(1,4):
        if flag[color]:
            color_map[pos] = color
            ret += counting(index+1)
    color_map[pos] = 0
    return ret
 
if n > 1:
    color_map[paths[0][0]] = 1
    print(counting(1)*3)
else:
    print(3)