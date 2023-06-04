"""
st = "1  2 \t3 \n4"  # -> [1, 2, 3, 4]
sp = st.split()
print(sp)
st = "1234"
sp = list(st)
print(sp)

st = "1  2 \t3 \n4"  # -> [1, 2, 3, 4]
sp = st.split()
print(sp)
st1 = "-".join(sp)
print(st1)
""" """
a = "aassddd"
sl = {}
for i in a:
    sl[i] = sl.get(i, 0) + 1
    # if i not in sl:
    #     sl[i] = 1
    # else:
    #     sl[i] += 1
print(sl)"""
"""
sl["g"] = 100
print(sl)
for key, value in sl.items():
    print(key, value)

sl = {"ABC": 1, ("A", "B", "C"): 4}
b = "a"
for k, v in sl.items():
    if b in k:
        print(v)"""

"""
Напишите программу, которая принимает на вход
строку, и отслеживает, сколько раз каждый символ
уже встречался. Количество повторов добавляется к
символам с помощью постфикса формата _n.
Input: a a a b c a a d c d d
Output: a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2

sp = input().split()
sl = {}
res = ''
for i in sp:
    if i not in sl:
        res += i + ' '
        sl[i] = 1
    else:
        res += i + '_' + str(sl[i]) + ' '
        sl[i] += 1
print(res)
"""
"""
sp = input().split()
sl = {}
res = ''
for i in sp:
    if i not in sl:
        res += f"{i} "
    else:
        res += f"{i}_{sl[i]} "
    sl[i] = sl.get(i, 0) + 1
print(res.strip())"""

"""
Задача №27. Общее обсуждение
Пользователь вводит текст(строка). Словом считается
последовательность непробельных символов идущих
подряд, слова разделены одним или большим числом
пробелов или символами конца строки.Определите,
сколько различных слов содержится в этом тексте.

Input: She sells sea shells on the sea shore;The shells
that she sells are sea shells I'm sure.So if she sells sea
shells on the sea shore,I'm sure that the shells are sea
shore shells.
Output: 19
""" """
st='''She sells sea shells on the sea shore;The shells
that she sells are sea shells I'm sure.So if she sells sea
shells on the sea shore,I'm sure that the shells are sea
shore shells.'''
st=st.replace('.',' ').replace(',',' ').replace("'",' ').replace(';',' ').lower()
sp = st.split()
mn = set(sp) #делает набор уникальных значений
print(mn)
print(len(mn))
"""

n = int(input())
max_number = n
while n != 0:
    if max_number < n:
        max_number = n
    n = int(input())
print(max_number)
