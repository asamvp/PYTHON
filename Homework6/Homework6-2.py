"""
Задача 32: Определить индексы элементов массива
 (списка), значения которых принадлежат заданному диапазону
   (т.е. не меньше заданного минимума и не больше заданного максимума)
"""
import random

list1 = [0] * 20
for i in range(0, len(list1)):
    list1[i] = random.randint(0, 30)
print(list1)

min_num = int(input())
max_num = int(input())
for i in range(len(list1)):
    if min_num <= list1[i] <= max_num:
        print(list1[i])
