"""
Игра "Быки и коровы"

Компьютер загадывает строку из n цифр.
Каждый ход игрок вводит догадку - тоже строку из n цифр, и получает в ответ
- количество "быков" - верно угаданных цифр на своих позициях
- количество "коров" - верно угаданных цифр, поставленных на неверные позиции

Например, при загаданной строке "4271" и догадке "1234" есть
- 1 бык - цифра "2" на второй позиции
- 2 коровы - цифры "1" и "4"

Реализуйте вспомогательные функции для этой игры:
- [a] create_secret, score, validate
- [b] computer
- [*] сделайте так, чтобы игрок-компьютер опирался на результаты
  предыдущих ходов и пытался делать основанные на них ходы
    > вам придется заметно изменить структуру игры, чтобы
      иметь возможность сообщать игроку результаты по-разному
      в зависимости от того, человек это или компьютер
"""
import random
from typing import Callable


def create_secret(n: int) -> str:
    """
    Функция принимает длину загадываемого числа
    и возвращает случайную строку из цифр указанной длины
    """
    10 ** (n - 1)
    # 10 ** (n - 1) - нижняя граница
    # 10 ** (n) - 1
    return random.randint(10 ** (n - 1), 10 ** n - 1)


def score(secret: str, guess: str, list_2=None) -> tuple[int, int]:
    # cow - корова
    # bull - бык
    cow = 0
    bull= 0
    Len = min(len(secret), len(guess))
    i = int(0)
    while i < Len:
        #print("while 1")
        if secret[i] == guess[i]:
            bull += 1
        i += 1

    i = 0
    List_1 = []
    List_2 = []

    while i < Len:
        #print("while 2")
        List_1.append(0)
        List_2.append(0)
        i += 1

    i = 0
    j = 0

    while i < Len:
        #print("while 3.1")
        while j < 10:
            #print("while 3.2")
            if secret[i] == j:
                List_1[j] = 1
            j += 1
        i += 1

    i = 0
    j = 0

    while i < Len:
        #print("while 4.1")
        while j < 10:
            #print("while 4.2")
            if guess[i] == j:
                List_2[j] = 1
            j += 1
        i += 1

    i = 0

    while i < Len:
        #print("while 5")
        if List_1[i] == List_2[i]:
            cow += 1
        i += 1

    """
    Функция принимает загаданную строку и догадку игрока
    и возвращает пару из количества "быков" и количества "коров"
        > можно для каждой цифры от '0' до '9' посмотреть на позиции
          ее вхождения в secret и guess
        > для нахождения числа общих позиций может быть полезно
          воспользоваться структурой данных "множество" (set)
    """
    return [bull, cow]


def validate(n: int, guess: str) -> bool:
    if len(guess) == n:
        answer = 1
    else:
        answer = 0
    """
    Функция принимает параметр игры - длину загаданной строки, и догадку игрока
    и возвращает, правда ли игрок ввел корректную догадку (строку длины n из цифр)
    """
    return answer


def computer_player(n: int) -> Callable:
    """
    Функция принимает параметр игры - длину загаданной строки,
    и возвращает ФУНКЦИЮ, генерирующую догадки
    """

    def guess():
        pass

    return guess


# def real_player(n: int) -> Callable:
#     """
#     Функция принимает параметр игры - длину загаданной строки,
#     и возвращает ФУНКЦИЮ, получающую догадку от реального игрока
#     """
#     print(f'The secret word has length {n}')
#     return input


# def play(n: int, player: Callable):
#     """
#     Функция реализует процесс игры с заданной длиной слова и игроком
#     """
#     secret = create_secret(n)
#     attempts = 0
#     while True:
#         guess = player()
#         attempts += 1
#         if not validate(n, guess):
#             print(f'Your guess should be a string of {n} digits')
#             continue
#         bulls, cows = score(secret, guess)
#         if bulls == n:
#             print(f'Correct! You\'ve won in {attempts} guesses')
#             break
#         else:
#             print(f'Your guess has {bulls=} and {cows=}')


# if __name__ == '__main__':
#     n = 4
#     play(n, real_player(n))

#a = int(intput())
# b = input()
# print(validate(len(b), b))
# print(validate(4, b))




