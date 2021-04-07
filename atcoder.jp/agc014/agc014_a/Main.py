# agc014 A Cookie Exchanges
a, b, c = map(int,input().split())
def cookie(x,y,z,cnt=0):
    if x == y and y == z and x%2 == 0:
        return -1
    elif x % 2 == 0 and y % 2 == 0 and z % 2 == 0:
        return cookie(y/2+z/2,x/2+z/2,x/2+y/2,cnt+1)
    else:
        return cnt
print(cookie(a,b,c,0))  