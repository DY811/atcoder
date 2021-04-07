import string
#print(list(string.ascii_lowercase))#alphabet in lower case
#alpha = list(string.ascii_lowercase)
w = input()
for i in w:
    if w.count(i) % 2 == 0:
        continue
    else:
        print("No")
        break
else:
    print("Yes")
