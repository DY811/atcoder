n,a,b = map(int,input().split())

if (a+b)%2 == 0:#偶数奇数が一緒
    print(int((b-a)//2))
else:
    print(int(min(a-1,n-b)+1+(b-a-1)//2))#端に行くまで＋調整１回＋出会うまで