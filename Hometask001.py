'''
Пример:
values = [1, 23, 42, "asdfg"]
transformed_values = list(map(transformation, values))
if values == transformed_values:
    print('ok')
else:
    print('fail')

'''

transformation = lambda data: data
values = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
transformed_values = list(map(transformation, values))
if values == transformed_values:
    print('ok')
else:
    print('fail')
