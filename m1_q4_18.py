# 次のプログラムを実行した結果として、正しいものはどれか
phrase = "PythonProgramming"
list_p = []
for p in phrase:
    if p not in list_p:
        list_p.append(p)
print(len(phrase) - len(list_p))
# ANSWER エ:6
