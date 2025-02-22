"""
1.	Написать программу, которая будет складывать, вычитать, умножать или делить
два числа. Числа и знак операции вводятся пользователем. После выполнения
вычисления программа не должна завершаться, а должна запрашивать новые данные
для вычислений. Завершение программы должно выполняться при вводе символа '0'
в качестве знака операции. Если пользователь вводит неверный знак
(не '0', '+', '-', '*', '/'), то программа должна сообщать ему об ошибке и
снова запрашивать знак операции.

Также сообщать пользователю о невозможности деления на ноль,
если он ввел 0 в качестве делителя.

Подсказка:
Вариант исполнения:
- условие рекурсивного вызова - введена операция +, -, *, / - ШАГ РЕКУРСИИ
- условие завершения рекурсии - введена операция 0 - БАЗОВЫЙ СЛУЧАЙ

Пример:
Введите операцию (+, -, *, / или 0 для выхода): +
Введите первое число: 214
Введите второе число: 234
Ваш результат 448
Введите операцию (+, -, *, / или 0 для выхода): -
Введите первое число: вп
Вы вместо трехзначного числа ввели строку (((. Исправьтесь
Введите операцию (+, -, *, / или 0 для выхода):

Решите через рекурсию. Решение через цикл не принимается.
Для оценки Отлично в этом блоке необходимо выполнить 5 заданий из 7
"""


def get_value(msg):

    while True:
        input_value = input(msg)
        try:
            check_value = float(input_value)
        except ValueError:
            print('Введено некорректное значение операнда!')
        else:
            break

    return input_value


def task01(call_count):

    while True:
        oper_type = input('Введите знак операции (+, -, /, *), либо 0 для завершения: ')
        if oper_type not in ['+', '-', '/', '*', '0']:
            print('Введен некорректный символ операции')
        else:
            break
    if oper_type == '0':
        print(f'Завершение! В стеке {call_count} вызов (а, ов)')
        return

    operand1 = get_value('Введите значение первого операнда: ')
    operand2 = get_value('Введите значение второго операнда: ')

    try:
        print(f'Значение выражения {operand1} {oper_type} {operand2} = {eval(operand1 + oper_type + operand2)}')
    except ZeroDivisionError:
        print('Недопустимая операция деления на ноль!')

    call_count += 1

    task01(call_count)


task01(1)
