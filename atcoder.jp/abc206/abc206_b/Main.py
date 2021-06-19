n = int(input())
tmp = (2*n)**(0.5)//1
#print(tmp)

if tmp*(tmp+1) >= 2*n:
    print(int(tmp))
elif (tmp+1)*(tmp+2) >= 2*n:
    print(int(tmp+1))
else:
    print(int(tmp+2))
