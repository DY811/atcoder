import heapq

Q = int(input())

balls = []
add_v = 0
for i in range(Q):
    s = list(map(int, input().split()))
    p = s[0]

    if p == 1:
        # add ball
        x = s[1]
        heapq.heappush(balls, x-add_v)
    elif p == 2:
        # add value
        x = s[1]
        add_v += x
    else:
        ball = heapq.heappop(balls)
        print(ball+add_v)


