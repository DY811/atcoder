x,y,z = map(int,input().split())
ta = y/x
su = int(ta*z)/z
if ta > su and su >= 0:
    print(int(ta*z))
elif ta == su and su >= 0:
    print(int(ta*z)-1)
else:
    print(0)