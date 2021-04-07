import string
s = set(list(input()))
#print(s) # unique letters
alpha = list(string.ascii_lowercase)
#print(alpha) #all letters
for i in s:
    rm_index = alpha.index(i)
    rm_chr = alpha.pop(rm_index)
    # print(rm_chr)
if len(alpha)== 0:
    print("None")
else: 
    print(alpha[0])