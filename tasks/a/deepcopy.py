"""
Deepcopy

Реализуйте функцию "глубокого" копирования массива.
Нельзя использовать встроенную функцию deepcopy из модуля copy.

Копировать массивы может быть нужно по следующей причине.
Если рассмотреть код
a = [1, 2, 3]
b = a
b.append(4)
b[0] = 0
print(a)
то будет выведено [0, 2, 3, 4], потому что a и b ссылаются на один и тот же объект.

Требуется сделать "полную" копию массива вложенных массивов, чтобы никакие
изменения в нем не отражались на оригинальном массиве.
"""


def deepcopy(a: list) -> list:
    """
    Функция принимает на вход массив, каждый элемент которого - либо
    число, либо массив такой же структуры, например [[1, 2], [3], 4, [[[5]], [6]]],
    и возвращает точно такой же массив, но занимающий другое место в памяти
    """
    result = a[:]
'''    result = []
    for item in a:
        if type(item) == list:
            ...  # если элемент - тоже массив
        else:
            ...  # если элемент - число'''
    return result


if __name__ == '__main__':
    a = [[1, 2], [3], 4, [[[5]], [6]]]
    b = deepcopy(a)
    b.append(7)
    b[0][1] = 0
    b[3][1][0] = -1
    print(a)  # должен вывести [[1, 2], [3], 4, [[[5]], [6]]]
    print(b)  # должен вывести [[1, 0], [3], 4, [[[5]], [-1]], 7]'''
