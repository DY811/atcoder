# abc068 B Break Number
n = int(input())

def division(m,cycle=0):
    if m % 2 != 0:
        return cycle
    return division(m/2, cycle+1)

max_num = 0
ans = 1
for i in range(1,n+1):
    if division(i) > max_num:
        max_num = division(i)
        ans = i
        #print(i)
print(ans)