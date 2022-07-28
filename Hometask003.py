'''
Винни-ПУХ
Пример:
парам-пам пам-пам-пам -> 'Парам пам-пам'
парам-пам пам-пам -> 'Пам парам'

'''
# Только "а"

res = 'Парам пам-пам' if len(set(map(lambda s: s.count('а'), input('Введите фразу: ').split()))) == 1 else 'Пам парам'
print(res)

###################################################################################################

# Все гласные

sym = ['а', 'е', 'ё', 'и', 'о', 'у', 'ы', 'э', 'ю', 'я']

string = ''
phrase = input('Введите фразу: ').split()
for i in range(len(phrase)):
    if i > 0:
        string += '_'
    for j in range(len(phrase[i])):

        if phrase[i][j] in sym:
            string += 'A'
        else:
            string += phrase[i][j]
string = string.split('_')

res = 'Парам пам-пам' if len(set(map(lambda s: s.count('A'), string))) == 1 else 'Пам парам'
print(res)

###################################################################################################

# Все гласные

sym = ['а', 'е', 'ё', 'и', 'о', 'у', 'ы', 'э', 'ю', 'я']

phrase = input('Введите фразу: ')
for i in range(len(sym)):
    phrase=phrase.replace(sym[i], 'A')

phrase=phrase.split()
res = 'Парам пам-пам' if len(set(map(lambda s: s.count('A'), phrase))) == 1 else 'Пам парам'
print(res)