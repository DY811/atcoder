n,m = map(int,input().split())
ac_num = [0]*n
wa_num = [0]*n
for i in range(m):
    p, s = input().split()
    if ac_num[int(p)-1] == 0:
        if s == "AC":
            ac_num[int(p)-1] += 1
        elif s == "WA":
            wa_num[int(p)-1] += 1
for i in range(n):
    if ac_num[i] == 0:
        wa_num[i] = 0
print(sum(ac_num),sum(wa_num))