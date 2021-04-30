n = input()
op_cnt = len(n) - 1 #隙間の数
for i in range(2**op_cnt): #+ or -で2通りずつ存在する（全探索）
    op = ["-"]*op_cnt
    for j in range(op_cnt): #opそれぞれビットシフト
        if ((i >> j)&1): #iの全探索分それぞれで、j bitシフトしてj番目が1かどうか
            op[(op_cnt - 1)-j] = "+" #例えば４つ隙間があったら、３ビットシフトで最初の隙間でop[0]にプラスを入れる
    #ここで計算の隙間が決まる
    formula = ""
    for p_n, p_o in zip(n,op+[""]):
        #zipで２つの行列を同時に回す
        #A+-B+-C+-Dのように繋げる。隙間は１こ少ないので""
        formula += (p_n + p_o)
    #計算式が完成（文字列）
    if eval(formula)==7: #eval()は文字列で計算する
        print(formula + "=7")
        break #必ず解があるから