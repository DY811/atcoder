n = int(input())

if n%2 == 0:
    for i in range(2**n):#全ての条件
        zero = 0
        one = 0
        ans = ['']*n
        for j in range(n):#各ケタで1か0か
            if one >= zero:
                if ((i>>j)&1):
                    one += 1
                    ans[-j-1] = ')'
                else:
                    zero += 1
                    ans[-j-1] = '('
            else:
                break
        if zero == one and zero == n//2:
            print(*ans, sep = '')#リストを外してスペースなしで出力
else:
    exit()