'''
実行例を参考に、問題集に記載されている1、3、5の内容（問題文）を実際にコードで作成し、実行確認してみてください。


【実行例】
15
False
<class 'str'>
1.7
'''
# 問2-1
a = int(input())
print(a != 15)

# 問2-3
a = 11
result= type(bin(a))
print(result)

# 問2-5
a = 1.740516
print(f'{a:.2g}')
