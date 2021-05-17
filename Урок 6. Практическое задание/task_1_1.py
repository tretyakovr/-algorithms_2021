"""
Задание 1.

Выполните профилирование памяти в скриптах
Проанализировать результат и определить программы с
наиболее эффективным использованием памяти.

Примечание: Для анализа возьмите любые 3-5 ваших РАЗНЫХ скриптов!
(хотя бы 3 разных для получения оценки отл).
На каждый скрипт вы должны сделать как минимум по две реализации.

Можно взять задачи с курса Основ
или с текущего курса Алгоритмов

Результаты профилирования добавьте в виде комментариев к коду.
Обязательно сделайте аналитику (что с памятью в ваших скриптах, в чем ваша оптимизация и т.д.)

ВНИМАНИЕ: ЗАДАНИЯ, В КОТОРЫХ БУДУТ ГОЛЫЕ ЦИФРЫ ЗАМЕРОВ (БЕЗ АНАЛИТИКИ)
БУДУТ ПРИНИМАТЬСЯ С ОЦЕНКОЙ УДОВЛЕТВОРИТЕЛЬНО

Попытайтесь дополнительно свой декоратор используя ф-цию memory_usage из memory_profiler
С одновременным замером времени (timeit.default_timer())!
"""

# Здесь код из 1 примера домашнего задания к 4 уроку. Необходимо сформировать массив с индексами
# четных элементов исходного массива


from random import randint
import memory_profiler


def decor(func):
    def wrapper(*args):
        m1 = memory_profiler.memory_usage()
        ret_val = func(args[0])
        m2 = memory_profiler.memory_usage()

        return ret_val, m2[0] - m1[0]
    return wrapper


@decor
def func_1(nums):
    new_list = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_list.append(i)

    return new_list


@decor
def func_2(nums):
    return tuple(i for i in range(len(nums)) if nums[i] % 2 == 0)


lst_to_func = [randint(0, i) for i in (range(1000))]

# Исходный вариант скрипта
res, mem_diff = func_1(lst_to_func)
print(f'Исходный вариант скрипта. Использовано {mem_diff} Mib памяти')

# Вариант с использованием кортежа. Так как в теле функции фактически никаких операций не выполняется,
# то использование памяти = 0?
res, mem_diff = func_2(lst_to_func)
print(f'Измененный вариант скрипта. Использовано {mem_diff} Mib памяти')

# Исходный вариант скрипта. Использовано 0.0703125 Mib памяти
# Измененный вариант скрипта. Использовано 0.0 Mib памяти
