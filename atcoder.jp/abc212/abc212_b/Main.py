p = str(input())

def weak_num(x):
    if int(x) == 9:
        return "0"
    else:
        return str(int(x) + 1)

if p[0] == p[1] == p[2] == p[3]:
    print("Weak")
elif p[1] == weak_num(p[0]) and p[2] == weak_num(p[1]) and p[3] == weak_num(p[2]):
    print("Weak")
else: 
    print("Strong")
#print(weak_num(p[0]),weak_num(p[1]),weak_num(p[2]))