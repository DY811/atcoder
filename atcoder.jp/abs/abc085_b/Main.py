n = int(input())
# 整数のｎ個の羅列（改行して与えられる）
a = list(int(input()) for _ in range(n))
# a.sort(reverse=True)
# print(a)
print(len(set(a)))