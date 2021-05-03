def solve():
    n, m = list(map(int, input().split()))
    next_list = [0] * n
    for i in range(m):
        x, y = map(int, input().split())
        #xのウサギの後にどのウサギが着いたか
        next_list[x - 1] |= 1 << (y - 1)
    #print(next_list)
    bt_list = [1 << i for i in range(n)]
    dp = [0] * (1 << n)
    dp[0] = 1
    for i in range(1 << n):
    #ウサギの集合のすべてのパターン（2bitで表す）
        for j in range(n):
        #jのウサギが追加できるか？
            if i & bt_list[j] == 0 and i & next_list[j] == 0:
            #集合のなかにjのウサギがいない＆集合の中にまだ後続のウサギがいない
                dp[i + bt_list[j]] += dp[i]
                #jを追加したウサギの集合は、iの状態を作れるパターン分ある                
    print(dp[-1])
    #最終的に、11111（Nの数だけ）になるパターンを求める
if __name__ == '__main__':
    solve()