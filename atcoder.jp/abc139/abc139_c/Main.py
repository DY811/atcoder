n = int(input())
h = list(map(int,input().split()))
streak = []
max_streak = 0

for i in range(len(h)-1):
    if h[i] >= h[i+1]:
        streak.append(1)
        max_streak = max(len(streak),max_streak)
    else:
        streak = []
print(max_streak)