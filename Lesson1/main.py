"""n = 'Hello\'Hello'
print(n)
x = 5
print(type(x))
a=5
b=5.424
c=n

print(f"{a} - {b} - {c}")
print("{} - {} - {}".format(a,b,c))

print('Введите первое число')
x=input()

print('Введите второе число')
y=input()

print(a,'+',b,'=',a+b)

c=5.87
print(c)
print(type(c))
c=str(c)
print(c+'454')
print(type(c))

import math
n = 100
m = 750
print(math.ceil(m/n))

print('Введите количество парт в 1 классе')
x = int(input())
print('Введите количество парт в 2 классе')
y = int(input())
print('Введите количество парт в 3 классе')
z = int(input())
p1 = x // 2 + x % 2
p2 = y // 2 + y % 2
p3 = z // 2 + z % 2
print(f"всего количество парт {p1+p2+p3}")
"""
"""
Вагоны в электричке пронумерованы натуральными
числами, начиная с 1 (при этом иногда вагоны
нумеруются от «головы» поезда, а иногда – с
«хвоста»; это зависит от того, в какую сторону едет
электричка). В каждом вагоне написан его номер.
Витя сел в i-й вагон от головы поезда и обнаружил,
что его вагон имеет номер j. Он хочет определить,
сколько всего вагонов в электричке. Напишите
программу, которая будет это делать или сообщать,
что без дополнительной информации это сделать
невозможно.
Input: 3 4 (ввод на разных строках)
Output: 6

print('Введите номер вагона по порядку в который сел человек')
i = int(input())
print('Введите фактический номер')
j = int(input())
if i==j :
    print("Недостаточно данных")
else:
    print(i + j - 1)
"""
"""
Задача №7. Общее обсуждение
Дано натуральное число. Требуется определить,
является ли год с данным номером високосным. Если
год является високосным, то выведите YES, иначе
выведите NO. Напомним, что в соответствии с
григорианским календарем, год является
високосным, если его номер кратен 4, но не кратен
100, а также если он кратен 400.
Input: 2016
Output: YES

print('Введите год')
year = int(input())
if (year%4 == 0 and year%100 != 0) or year%400 == 0:
    print("Високос")
else:
    print("нет")
"""

"""
Боря, Вова и Дима спорят, кто из них выше и в каком порядке они должны стоять в шеренге на уроке физкультуры. Напишите программу, которая упорядочивает рост мальчиков по невозрастанию.
Формат ввода
Три строки, на каждой – рост каждого мальчика.
Формат вывода
Три строки, на первой рост самого высокого мальчика, на третьей – самого низкого."""
print('Введите рост 1 чел')
x = int(input())
print('Введите рост 2 чел')
y = int(input())
print('Введите рост 3 чел')
z = int(input())
if x < y:
    buffer = x
    x = y
    y = buffer
    # x, y = y, x
if y < z:
    buffer = y
    y = z
    z = buffer
if x < y:
    buffer = x
    x = y
    y = buffer
print('__________')
print(x)
print(y)
print(z)
