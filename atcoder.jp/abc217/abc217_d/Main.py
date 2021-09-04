import bisect

l, q = map(int,input().split())
cut1 = [0]
cut2 = [l]
x1 = []
for i in range(q):
    ci,xi = map(int,input().split())
    if ci == 1:
        if xi <l//2:
            bisect.insort_left(cut1, xi)
        else:
            bisect.insort_left(cut2, xi)
    else:
        
        if xi < cut1[-1]:
            xin = bisect.bisect_left(cut1, xi)
            print(cut1[xin]-cut1[xin-1])
        elif xi > cut1[-1] and xi < cut2[0]:
            print(cut2[0]-cut1[-1])
        else:
            xin = bisect.bisect_left(cut2, xi)
            print(cut2[xin]-cut2[xin-1])