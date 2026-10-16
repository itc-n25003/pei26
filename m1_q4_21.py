# 次のプログラムを実行した結果として、正しいものはどれか。
num = 12
list_s = []
s = 2
while s <= num:
    if num % s == 0:
        num //= s
        if s not in list_s:
            list_s.append(s)
    else:
        s += 1
print(list_s)
# ANSWER エ:[2, 3]
