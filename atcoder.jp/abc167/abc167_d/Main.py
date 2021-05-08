"""
ダブリングの考え
動的計画法のように、小さい数字からスタートして、
前の状態を使いながら次の状態を作っていく。

2**n = 2**(n-1)+2**(n-1)なので１つ前の状態を見ながら2の累乗分状態を作っていく
k回は2のn乗の組み合わせで表せるので、それぞれの状態を繋いでk回後の状態を求める
"""

def main():
    n, k = map(int, input().split())
    a = list(map(int,input().split()))
    
    dv = []
    for _ in range(60): #2**60 > 10**18だから
        l = [0]*n
        dv.append(l)
    #遷移表
    for i in range(n):
        dv[0][i] = a[i] - 1 #index分１を引く
    for i in range(1,60):
        for j in range(n):
            dv[i][j] = dv[i-1][dv[i-1][j]] #2**i番目の居場所は、2**(i-1)番目の行き先
    #kが2**nならそのままdvを参照できるが、端数がある場合のために２ビット表記を使う
    #kがどんな数でも、2**0,2**1,2**2,,,の足し算で表せる
    
    #kを２ビットで表記した時の1の位置
    b = []
    for i in range(60):
        if k>>i & 1:
            b.append(i)
    now = 0
    for i in b:
        now = dv[i][now]
    print(now+1)#indexにするために１引いたものを戻す
    #print(dv)

if __name__ == "__main__":
    main()