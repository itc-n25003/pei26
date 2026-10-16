'''
繰り返しの中でtotalの値はどのように変化しているか観察したいです
そのためのprint(total)関数をどこに挿入したら良いでしょう？

【実行例】
totalの値は0
totalの値は3
totalの値は6
totalの値は8
totalの値は13
13
'''

animals = ["Dog", "Cat", "Rabbit", "Horse", "Dolphin"]
total = 0
for animal in animals:
    from_D = animal.startswith("D")
    is_long = len(animal) > 5
    print(f'totalの値は{total}')
    if from_D and is_long:
        break
    elif not from_D and is_long:
        total += animal.find("b")
    else:
        total += len(animal)
print(total)
# ANSWER ウ:13
