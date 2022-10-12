"""
Считайте с клавиатуры две строки.

Выведите по очереди:
- [a] произведение длин этих строк
- [b] обе эти строки, разделенные пробелом
- [c] обе эти строки, разделенные запятой и табуляцией
- [d] строку вида "Hello, {первая строка}! Just wanted to say: '{вторая строка}'"
    > подсказка: используйте форматную строку (f-string)
- [e] первые "слова" из каждой строки через пробел
    > под "словами" имеются в виду части строки, разделенные друг от друга пробелами
- [f] количество "слов" в первой строке
- [g] первую позицию вхождения первой строки во вторую (или -1, если их нет)
"""
def First_word(s):
    Len = len(s)
    i = 0
    out = ""
    while s[i] != " " and i < Len:
        out += s[i]
        i += 1
    return out

def Word_count(s):
    Len = len(s)
    i = 0
    j = 0
    out = 0
    while i < Len:
        if s[i] == " ":
            j = 1
        else:
            if j == 1:
                out += 1
                j = 0
        i += 1
    if s[0] != " ":
        out += 1
    return out
#где то засел вечный цикл
s1 = input()
s2 = input()

print(len(s1) * len(s2))
print(s1, s2)
print(s1 + "," + "  " + s2)
print("Hello, " + s1 + "! Just wanted to say:" + s2)
print(First_word(s1), First_word(s2))
print(Word_count(s1))

print("end")
# Место для вашего кода
