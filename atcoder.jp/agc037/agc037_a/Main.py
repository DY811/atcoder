import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)

S = input().rstrip()
#print(S[-4:-2],S[-2:])

if len(S) == 1:
    print(1)
    exit()

# s-1の区切り位置のリスト
separate = [0]*(len(S))

separate[0] = 1
separate[1] = 1
if S[1] != S[0]:
    separate[1] = 1
    
for i in range(2,len(S)):
    #print(i)
    if separate[i-1]==1 and separate[i-2]==1: #直前が1文字
        if S[i-1] != S[i-2]: #文字が異なる
            separate[i] = 1
            #print("A")
        else:
            #print("B")
            separate[i] = 0
    if separate[i-1]==0 and separate[i-2]==1: #直前が2文字
        separate[i] = 1
        #print("C")
    if separate[i-1]==1 and separate[i-2]==0: #直前が2文字
        separate[i] = 1
        #print("C")        

if separate[-1] == 1 and separate[-2] == 1 and S[-1] == S[-2]:
    separate[-1] = 0
if separate[-1] == 0 and separate[-3] == 0:
    if "".join(S[-4:-2]) == "".join(S[-2:]):
        #print("D")
        separate[-2] = 0
        separate[-1] = 1
#print(separate)
answer = sum(separate)
print(answer)