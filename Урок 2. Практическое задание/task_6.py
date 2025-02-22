"""
6.	В программе генерируется случайное целое число от 0 до 100.
Пользователь должен его отгадать не более чем за 10 попыток. После каждой
неудачной попытки должно сообщаться больше или меньше введенное пользователем
число, чем то, что загадано. Если за 10 попыток число не отгадано,
то вывести загаданное число.

Подсказка:
Базовый случай здесь - угадали число или закончились попытки

Решите через рекурсию. Решение через цикл не принимается.
Для оценки Отлично в этом блоке необходимо выполнить 5 заданий из 7
"""

import random


def task06(riddle_num, try_count):
    if try_count == 0:
        print(f'За заданное число попыток угадать число не удалось! Загаданное число {riddle_num}')
        return

    while True:
        try:
            guess_num = int(input(f'Отгадайте загаданное число из диапазона от 0 до 100. Осталось {try_count} попыток: '))
        except ValueError:
            print('Введено некорректное значение, попробуйте еще раз!')
        else:
            if guess_num < 0 or guess_num > 100:
                print('Загадано число в диапазоне от 0 до 100! Попробуйте еще раз!')
            else:
                break

    if guess_num == riddle_num:
        print(f'Вы угадали! Это действительно число {riddle_num}')
        return
    else:
        if guess_num < riddle_num:
            print('Недолет!')
        elif guess_num > riddle_num:
            print('Перелет!')

    try_count -= 1

    task06(riddle_num, try_count)


task06(random.randint(0, 100), 10)
