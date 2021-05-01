import math
n = int(input())

#１番おおきいものを買ってバラバラにし、残りをそれぞれ買う
#1+2+3+..+n = n(n+1)/2より
#k(k+1) <= 2*(n+1)となるkを探す

tmp = math.sqrt(2*(n+1))//1
if int(tmp) * (int(tmp)+1) <= 2*(n+1):
    k = int(tmp)
else:
    k = int(tmp) - 1
#残りのそれぞれを買うのがn-k本と一番長いの１本
print(n-k+1)