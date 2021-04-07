from collections import deque
n = int(input()) #具材の数
v = list(map(int,input().split()))#具材の価値
v.sort()
v = deque(v)
def mix(v):
    if len(v) == 1:
        return v[0]
    smallest = v.popleft()
    v[0] = (smallest + v[0])/2
    return mix(v)
print(mix(v))    