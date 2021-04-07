n = int(input())
a = [int(input()) for i in range(n)]
b = sorted(a, reverse = True)
#print(b[:2])

for i in range(len(a)):
    #print(a[i])
    if a[i] == b[0]:
        print(b[1])
    else:
        print(b[0])