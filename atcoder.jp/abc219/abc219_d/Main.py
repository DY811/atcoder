n=int(input())
x,y=map(int,input().split())
a=[]
b=[]
for _ in range(n):
    A,B=map(int,input().split())
    a.append(A)
    b.append(B)
if sum(a)<x or sum(b)<y:
    print(-1)
    exit
else:
    num=[[False]*(y+1) for _ in range(x+1)]
    #print(num)
    num[0][0]=1
    for i in range(n):
      A=a[i]
      B=b[i]
      for j in range(x,-1,-1):#１ずつ減らす
          for h in range(y,-1,-1):
              #すでに選んでる
              if num[j][h]!=False:
                  #print(j,h)
                  #たこ焼きとたい焼き欲しい数を上限とする
                  if num[min(x,j+A)][min(y,h+B)]==False:
                      num[min(x,A+j)][min(y,B+h)]=num[j][h]+1
                  else:
                      num[min(x,A+j)][min(y,B+h)]=min(num[j][h]+1,num[min(x,A+j)][min(y,B+h)])
    #print(num)
    print(num[x][y]-1)