import string
alpha = string.ascii_lowercase
#print(alpha)
x = input()
n = int(input())

renamed = []
for _ in range(n):
    tmp = input()
    rename = ''
    for i in range(len(tmp)):
        rename += alpha[x.index(tmp[i])]
    renamed.append([rename,tmp])
renamed.sort()
for i in range(n):
    print(renamed[i][1])