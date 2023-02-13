from csv import *
names = ('Имя', 'Фамилия', 'Возраст', 'Вес', 'Рост')
data = [('Константин','Тарасов',17,66,178)
]

dat = input('Введите данные:')
data.append(tuple(dat.split()))
with open('База данных.csv', 'w') as f:
    f.write(','.join(names) + '\n')
    for i in data:
        i = [str(line) for line in i]
        f.write(','.join(i) + '\n')

with open('База данных.csv') as f:
    name = list(f.readline().split(','))
    #name[-1] = name[-1][:-1]
    name = tuple(name)
    dan = [s.split(',') for s in f]
