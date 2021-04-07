# 三井住友信託銀行プログラミングコンテスト２０１９B
import math
n = int(input())
x = n//1.08 + 1 # 商 Quotient
"""
108//1.08は99になる
"""

if math.floor(x*1.08) == n:
    print(int(x))
else:
    print(":(")