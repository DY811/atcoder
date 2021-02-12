# 整数の入力
a, b, c = map(int, input())
# 1の個数＝合計
# print(a + b + c)
# countで1の個数
d = str(a)+str(b)+str(c)
print(d.count("1"))