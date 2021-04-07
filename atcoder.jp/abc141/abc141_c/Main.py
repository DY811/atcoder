n,k,q = map(int,input().split())
#point = [k]*n
score = [0]*n

for i in range(1,q+1):
    a = int(input())-1
    score[a] += 1
#print(score)

score = [k+(-1)*q+j for j in score]
#print(score)
for i in range(n):
    if score[i] > 0:
        print("Yes")
    else:
        print("No")