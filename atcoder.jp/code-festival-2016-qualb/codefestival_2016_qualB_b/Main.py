# code festival 2016 qual B
n, a, b = map(int, input().split())
s = input()
b_tmp = 0
pass_tmp = 0

for i in range(n):
    #print(pass_tmp)
    if s[i] == "a" and pass_tmp < (a+b):
        print("Yes")
        pass_tmp += 1
    elif s[i] == "b" and pass_tmp < (a+b) and b_tmp < b:
        print("Yes")
        pass_tmp += 1
        b_tmp += 1
    else:
        print("No")        