# 次のプログラムを実行した結果として、正しいものはどれか。
a = [1, 2, 3, 4]
id_a = id(a)
b = a.copy()
id_b = id(b)
if id_a == id_b:
    result = "A"
elif id(a) == id(b):
    result = "B"
elif id_a == id(a):
    result = "C"
else:
    result = "D"
print(result)

# ANSWER ウ:C
