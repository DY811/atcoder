n = int(input())
 
a = [0, 0, 0]
for i in range(n):
    t, x, y = map(int, input().split())
    dt = t - a[0]  #　時間
    d = abs(x - a[1]) + abs(y - a[2]) # 距離
    if dt >= d and (dt - d) % 2 == 0: # 距離以上に時間がある（例：3秒で4歩は無理）。偶奇が揃う。
        a = [t, x, y]
    else:
        print("No")        
        break
else: #すべての処理が終わった後に実行(つまりbreakしていない場合)       
    print("Yes")   