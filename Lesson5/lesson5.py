"""
print('Введите элементы 1 множества через пробел')
mn1 = set(input().split())
print('Введите элементы 2 множества через пробел')
mn2 = set(input().split())
print(f'Итоговое множество {mn1.difference(mn2)}')
"""
'''
from random import randint
from typing import List

def get_list(number: int) -> List[int]:
    return [randint(1, 10) for _ in range(number)]

num_1 = int(input("введите число элементов 1-го массива: "))
numbers_1 = get_list(num_1)
print(numbers_1)

num_2 = int(input("введите число элементов 2-го массива: "))
numbers_2 = get_list(num_2)
print(numbers_2)

for elem in numbers_1:
    if elem not in numbers_2:
        print(elem, end=" ")


n = int(input('Введите n: '))
lst_one = [int(input(f'Введите {i + 1}-е число первого массива: ')) for i in range(n)]
m = int(input('Введите m: '))
lst_two = [int(input(f'Введите {i + 1}-е число: второго массива')) for i in range(m)]

print(*[num for num in lst_one if num not in lst_two])

'''
'''
Дан массив, состоящий из целых чисел. Напишите
программу, которая в данном массиве определит
количество элементов, у которых два соседних и, при
этом, оба соседних элемента меньше данного. Сначала
вводится число N — количество элементов в массиве
Далее записаны N чисел — элементы массива. Массив
состоит из целых чисел.
Ввод: Ввод:
5 5
1 2 3 4 5 1 5 1 5 1
Вывод: Вывод:
0 2
(каждое число вводится с новой строки)
'''

n = int(input('Введите n: '))
lst = [int(input(f'Введите {i + 1}-е число массива: ')) for i in range(n)]

print(len([i for i in range(1,len(lst)-1) if lst[i] > lst[i - 1] and lst[i] > lst[i + 1]]))