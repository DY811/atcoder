# abc 086 B 1 21
import math

a, b = input().split()
q = int(a+b)
if math.sqrt(q) % 1 == 0:
    print("Yes")
else:
    print("No")