X = int(input())
num = [0]*(X+1)

if X == 1:
    print(1)
    exit()
else:
    for i in range(1,X+1): #b
        for j in range(2,X+1): #p
            if i**j <= X:
                num[i**j] = 1
            else:
                break
rev_num = num[::-1]
minus_index = rev_num.index(1)
print(X-minus_index)