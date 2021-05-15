s = input()
o_list = [i for i, x in enumerate(s) if x == 'o']
x_list = [i for i, x in enumerate(s) if x == 'x']
q_list = [i for i, x in enumerate(s) if x == '?']

cnt = 0

def is_ok(a):
    ans = str(a[0])+str(a[1])+str(a[2])+str(a[3])
    for i in o_list:
        if str(i) in ans:
            continue
        else:
            return False   
    for i in x_list:
        if str(i) in ans:
            return False
    return True
#print(is_ok("0123"))  
for i in range(10):
    for j in range(10):
        for k in range(10):
            for l in range(10):
                test = str(i)+str(j)+str(k)+str(l)
                if is_ok(test):
                    cnt += 1
print(cnt)
