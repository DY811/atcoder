h,w = map(int,input().split())
for i in range(1,h+2+1):
    if i == 1 or i == h+2:
        print("#"*(w+2))
    else:
        panel = input()
        print("#"+panel+"#")