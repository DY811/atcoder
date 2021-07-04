#https://www.programming-pack.com/entry/2019/11/04/235625
#<>の時は難しい。左右から階段を登ってどちらの頂点が採用されるかを考える
s = list(input())

#不等号の向きを記録する
memo = ""

#不等号の連続した個数を記録する
cnt = 0

#1つ前に数えた不等号の連続した個数を記録する
before_cnt = 0

#出力する答え
ans = 0

#文字列Sの連続した不等号の向きを数える
for x in s:
    #初めはmemoが空白なので,memoに不等号の向きを記録
    if memo == "":
        memo = x
    
    #不等号の向きが同じ場合は、数を1カウントしてループに戻る
    if memo == x:
        cnt += 1
        
    #不等号の向きが異なる場合
    else:
        #ansに和を加算する
        ans += cnt * (cnt+1) // 2
        #print(ans)
        
        #不等号の向きの変化が処理が必要な場合（＜から＞になる時）
        if memo == ">":
            if before_cnt < cnt:#階段の頂点を今のcntに交代するので前回の頂点を引く
                ans -= before_cnt
                #print(ans)
            else:#>の数が小さい時は階段の頂点が相手なので最後のcnt分は引く
                ans -= cnt
                #print(ans)

        before_cnt = cnt
        cnt = 1
        memo = x
ans += cnt * (cnt+1) // 2
#print(ans)
if before_cnt < cnt:
    if memo == ">":
        ans -= before_cnt
        #print(ans)
else:
    if memo == ">":
        ans -= cnt
        #print(ans)
print(ans)