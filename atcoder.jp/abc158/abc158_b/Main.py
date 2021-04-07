n,a,b = map(int,input().split())
mix = a + b 
q = n//mix
r = n%mix
ao = a*q + min(r,a)
print(ao)