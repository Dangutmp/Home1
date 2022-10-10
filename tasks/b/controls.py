"""
Вам даны три переменные x, y и s, в которые записаны два случайных целых числа и
случайная строка длины 30, соответственно.

Выведите по очереди:
- сами x, y и z через пробел
    > уже написано за вас
- [a] сколько целых чисел находятся строго между x и y по значению
- [b] количество шагов в гипотезе Коллатца, необходимое, чтобы получить из x единицу
    > если число x четное, оно заменяется половину от себя
    > если число x нечетное, оно заменяется на 3x + 1
- [c] количество четных букв ('a', 'e', 'i', 'o', 'u') в строке s
"""
def Collarts(x):
    n = 0
    while x != 1:
        if x % 2 == 0:
            x /= 2
        else:
            x = 3 * x + 1
        #print(x)
        n += 1
    return n
def even_2(s):
    i = 0
    out = ""
    Len = len(s)
    while i < Len:
        if i % 2 == 0:
            out += s[i]
            i += 2
    return out
def even_1(s):
    i = 0
    out = ""
    Len = len(s)
    while i < Len:
        if i % 2 == 0:
            out += s[i]
        i += 1
    return out


from test.common.context import get_integer, get_string

x = get_integer()
y = get_integer()
s = get_string()

print(x, y, s)
# x = 12
# y = 15
print(abs((int(x) - int(y))) - 1)
print(Collarts(x))
print(even_2(s))

# Место для вашего кода
