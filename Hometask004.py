'''
Написать функцию same_by(characteristic, objects)
Если список пустой или характеристики элементов одинаковы True
В противном слувае  - False'''

def same_by(characteristic, objects):
    characteristic = True
    for i in objects:
        if i % 2 != 0:
            characteristic = not characteristic
            break
    return characteristic


values = [1, 2, 3, 4]  # [0, 2, 10, 6]
if same_by(lambda x: x % 2, values):
    print('same')
else:
    print('different')
