"""
Задание 1.

Для каждой из трех задач выполнить следующее:

1) для каждого выражения вместо !!! укажите сложность этого выражения.
2) определите сложность задачи в целом.

Примечание:
Прошу вас внимательно читать ТЗ и не забыть выполнить все пункты.
"""

import random


#############################################################################################
def check_1(lst_obj):
    """Функция должна создать множество из списка.

    Алгоритм 3:
    Создать множество из списка

    Сложность: O(N) - линейная сложность.
    """
    lst_to_set = set(lst_obj)  # O(len(lst_obj)), в общем случае O(N) - линейная сложность
    return lst_to_set  # O(1)


#############################################################################################
def check_2(lst_obj):
    """Функция должная вернуть True, если все элементы списка различаются.

    Алгоритм 1:
    Проходимся по списку и для каждого элемента проверяем,
    что такой элемент отстутствует
    в оставшихся справа элементах

    Сложность:
        Если принять k = len(lst_obj) * (len(lst_obj) + 1) / 2,
                     N = len(lst_obj), то
        O(k * N) - линейная сложность (или O(N^2) квадратичная??).
        Т.е. условие if внутри цикла выполняется количество, равное сумме порядковых номеров элементов списка
    """
    for j in range(len(lst_obj)):          # O(len(lst_obj)), в общем случае O(N) - линейная сложность
        if lst_obj[j] in lst_obj[j+1:]:    # O(len(lst_obj) - j), в общем случае O(N) - линейная сложность
            return False                   # O(1)
    return True                            # O(1)


#############################################################################################
def check_3(lst_obj):
    """Функция должная вернуть True, если все элементы списка различаются.

    Алгоритм 2:
    Вначале выполним для списка сортировку, далее, сравниваем элементы попарно
    Если присутствуют дубли, они будут находиться рядом.

    Сложность: O(N log N) - линейно-логарифмическая
    """
    lst_copy = list(lst_obj)                 # O(N)
    lst_copy.sort()                          # O(N log N)
    for i in range(len(lst_obj) - 1):        # O(N)
        if lst_copy[i] == lst_copy[i+1]:     # O(1)
            return False                     # O(1)
    return True                              # O(1)

#############################################################################################


for j in (50, 500, 1000, 5000, 10000):
    # Из 100000 чисел возьмем 'j' случайно выбранных
    # Всего 10 тыс. чисел
    lst = random.sample(range(-100000, 100000), j)

print(check_1(lst))
print(check_2(lst))
print(check_3(lst))
