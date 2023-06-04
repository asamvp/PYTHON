'''
Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями). Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
Пользователь вводит 2 числа. n — кол-во элементов первого множества. m — кол-во элементов второго множества. Затем пользователь вводит сами элементы множеств.
'''
print('Введите элементы 1 множества через пробел')
mn1 = set(input().split())
print('Введите элементы 2 множества через пробел')
mn2 = set(input().split())
print(f'Итоговое множество {sorted(mn1.intersection(mn2))}')