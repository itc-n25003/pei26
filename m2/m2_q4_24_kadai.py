'''
変数aにfunc(-5,-6)の戻り値を代入し、リストzに格納したうえで出力してください
また、bool関数について、簡単な説明をコード内コメントでまとめておきましょう

【解答例】
[True, False, True]
'''

def func(a ,b):
    if a ** b <=64:
        return 1
    else:
        return 0 

x = func(4, 3)
y = func(3 , 4)
z = [bool(x), bool(y)] # 0以外の数値や文字列、要素の入ってリストなどをTrue、空のリスト0や無効な値をFalseとして出力する
a = func(-5,-6)
z.append(bool(a))
print(z)

## 解答 ウ.[「True, False」]が表示される。
