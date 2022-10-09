"""
FizzBuzz

Реализуйте функцию, которая принимает на вход начало и конец
полуинтервала и выводит для каждого числа в нем в отдельную строку
- fizz, если число делится на 3, но не на 5
- buzz, если число делится на 5, но не на 3
- fizzbuzz, если число делится на 15
- само число иначе

Например, fizzbuzz(11, 16) должен вывести
11
fizz
13
14
fizzbuzz
"""


def fizzbuzz(a: int, b: int):
    if b < a:
        c = a
        a = b
        b = c
    i = a
    b += 1
    while i < b:
        if i % 15
            print("fizzbuzz")
        elif i % 5
            print("buzz")
        elif i % 3
            print("fizz")
        else
            print(i)
        i += 1


