"""
По данному целому неотрицательному n вычислите
значение n!. N! = 1 * 2 * 3 * ... * N (произведение всех
чисел от 1 до N) 0! = 1 Решить задачу используя цикл
while
Input: 5
Output: 120

print("Введите число:")
result = 1
n = int(input())
for i in range(1, n + 1):
    result *= i
print(result)
"""

"""
Дано натуральное число A > 1. Определите, каким по
счету числом Фибоначчи оно является, то есть
выведите такое число n, что φ(n)=A. Если А не
является числом Фибоначчи, выведите число -1.
Input: 5
Output: 6
""" """
print("Введите число")
number = int(input())
i = 1
sum = 1
while i <= number:
    sum = sum * i
    i = i + 1
print(f"Факториал числа {number}={sum}")
print(f"порядковый номер {i}")

input_num = int(input('Введите число: '))
n1, n2 = 0, 1
f_id = 2
while n2 < input_num:
    n1, n2 = n2, n1 + n2
    f_id += 1
if input_num != n2:
    f_id = -1
print(f_id)

Input: 6 -> -20 30 -40 50 10 -10
Output: 2


N = int(input("Введите количество дней N:"))
k = 0
maximum = 0
for i in range(0 , N):
    temp = int(input("Введите значение температуры: "))
    if temp >= 0:
        k +=1
        if maximum < k:
            maximum = k
    else:
        k = 0
print(f"Максимальная оттепель составила {maximum} дней")
"""

N = int(input("Введите количество арбузов:"))
minimum = 0
maximum = 0
for i in range(0, N):
    temp = int(input("Введите вес: "))
    if i == 0:
        minimum = temp
    if maximum < temp:
        maximum = temp
    if minimum > temp:
        minimum = temp
print(f"Максимальный арбуз {maximum} ")
print(f"Минимальный арбуз {minimum} ")
