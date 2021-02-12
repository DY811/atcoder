# スペース区切りの整数の入力
a, b = map(int, input().split())
# 確認
# print(str(b) + " & " + str(c))
if a * b % 2 == 0:
    print("Even")
else:
    print("Odd")