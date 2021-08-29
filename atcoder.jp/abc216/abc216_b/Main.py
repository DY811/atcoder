n = int(input())
member = []
for i in range(n):
    name = input()
    if name in member:
        print("Yes")
        break
    member.append(name)
else:
    print("No")