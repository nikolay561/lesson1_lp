# a = 2
# b = 0.5
# print (a + b)
# name = 'Nick'
# print(f'Hello {name}!')
# print(f'Длинна имени - {len(name)} буквы.')
# print(len(name) > 2)
# print(len(name) + 4 != 8)
# print(name.lower().replace('n', 'N'))
# print(type(a))
# v = int(input('Введите число: '))
# print(f'Вы ввели {v + 10} - {type(v)}')
# user_name = input('Введите Ваше имя: ')
# print(f'Привет, {user_name.upper()}! Как дела?')
# print(type(float('1')), float('1'))
# print(type(int(float('2.5'))), int(float('2.5')))
# print(type(bool(1)), bool(1))
# print(type(bool('')), bool(''))
# print(type(bool(0)), bool(0))
# x = [3, 5, 7, 9, 10.5]
# x.append('Python')
# print(x)
# print(len(x))
# print(x[0])
# print(x[-1])
# print(x[1:4])
# # del x[-1]
# x.remove('Python')
# print(x)
my_list = {'city': 'Москва', 'temperature': '20'}
print(my_list['city'])
my_list['temperature'] = int(my_list['temperature']) - 5
print(my_list)
print(my_list.get('country', 'Россия'))
my_list['date'] = '27.05.2019'
print(my_list)
print(len(my_list))