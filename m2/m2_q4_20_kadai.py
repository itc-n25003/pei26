'''
5から25までの奇数の合計を求めて出力してください。

【条件】
1. 求める各値はrange()関数を使って生成すること
2. 各値はlist_bにappend()で追加すること
3. 合計はsum()関数を使うこと

【出力例】
165
'''
list_b = []
for i in range(5,26,2):
    list_b.append(i)

result = sum(list_b)
print(result)
