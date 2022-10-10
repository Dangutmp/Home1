"""
Вам дана переменная n, в которую записано целое число.

Создайте массив a длины n, в котором каждое следующее число так же
генерируется функцией get_integer().

Выведите по очереди:
- сам массив
    > уже написано за вас
- [a] первый, медианный (центральный) и последний элемент массива через пробел
- [b] минимальный и максимальный элементы массива через пробел
- [c] сумму всех элементов массива
- [d] массив, состоящий из квадратов всех четных элементов a
- [e] позицию первого вхождения минимального элемента в a/*когда впервые встречается тот или иной элемент в списке. Возращаем индекс этого элемента*/
- [f] развернутый массив a
    > подсказка: используйте встроенную функцию или срез
- [g] массив, состоящий из всех элементов a на четных позициях
    > подсказка: используйте срез
"""
import copy


def First_occurrence(s, x):
    j = -1
    i = 0
    Len = len(s)
    while i < Len:
        if s[i] == x:
            j = i
    if j < 0:
        return N
def Sum_list(s):
    out = 0
    i = 0
    Len = len(s)
    while i < Len:
        out += s[i]
        i += 1
    return out

def square(s):
    out = list()
    i = 0
    Len = len(s)
    while i <Len:
        out.append(s[i] * s[i])
        i += 2
    return out
def mirror_list(s):
    out = list()
    Len = len(s)
    for i in range(1, Len):
        out.append(s[Len - i])
    return out
def even_elements(s):
    Len = len(s)
    out = list()
    i = 0
    while i < Len:
        out.append(s[i])
        i += 2
    return out

def Max_element(s):
    Len = len(s)
    out = s[0]
    for i in range(1, Len):
        if out > s[i]:
            out = s[i]
    return out
def Min_element(s):
    Len = len(s)
    out = s[0]
    for i in range(1, Len):
        if out < s[i]:
            out = s[i]
    return out

from test.common.context import get_integer

n = get_integer()
n = 5
a = list()
i = 0
while i < n:
    a.append(get_integer())
    i += 1

print(a)
# b = a.sort()
# print(b)
print(str(a[0]) + " " + str(a[int(n / 2)]) + " " + str(a[n - 1]))
print(str(Min_element(a)) + " " + str(Max_element(a)))
print(Sum_list(a))
print(square(a))# тут проблема
print()
print(mirror_list(a))
print(even_elements(a))