import string
p = list(map(int,input().split()))
alpha = string.ascii_lowercase
#print(alpha)
for i in range(len(p)):
    print(alpha[p[i]-1], end = "")

