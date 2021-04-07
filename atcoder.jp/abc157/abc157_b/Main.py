# abc 157 B Bingo
row1 = list(map(int, input().split()))
row2 = list(map(int, input().split()))
row3 = list(map(int, input().split()))
n = int(input())

ans1 = [0,0,0]
ans2 = [0,0,0]
ans3 = [0,0,0]

for i in range(1,n+1):
    #print(i)
    b = int(input())
    for j in range(0,3):
        if row1[j] == b:
            ans1[j] = 1
        if row2[j] == b:
            ans2[j] = 1            
        if row3[j] == b:
            ans3[j] = 1
#print(ans1)
#print(ans2)
#print(ans3)

if ans1 == [1,1,1]:
    print("Yes")
elif ans2 == [1,1,1]:
    print("Yes")
elif ans3 == [1,1,1]:
    print("Yes")     
elif ans1[0] == 1 and ans2[0] == 1 and ans3[0] == 1:
    print("Yes")   
elif ans1[1] == 1 and ans2[1] == 1 and ans3[1] == 1:
    print("Yes")    
elif ans1[2] == 1 and ans2[2] == 1 and ans3[2] == 1:
    print("Yes")

elif ans1[0] == 1 and ans2[1] == 1 and ans3[2] == 1:
    print("Yes")    
elif ans1[2] == 1 and ans2[1] == 1 and ans3[0] == 1:
    print("Yes")
else:
    print("No")
    