N = int(input())
cnt = 0
   
for i in range(1, 10**6+1):
    if int(str(i)*2) <= N:
        cnt += 1
    elif int(str(i)*2) > N:
        break   
print(cnt)