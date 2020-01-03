# 1. Проанализировать скорость и сложность одного любого алгоритма из разработанных в рамках домашнего задания первых трех уроков.
# Примечание. Идеальным решением будет:
# a. выбрать хорошую задачу, которую имеет смысл оценивать,
# b. написать 3 варианта кода (один у вас уже есть),
# c. проанализировать 3 варианта и выбрать оптимальный,
# d. результаты анализа вставить в виде комментариев в файл с кодом (не забудьте указать, для каких N вы проводили замеры),
# e. написать общий вывод: какой из трёх вариантов лучше и почему.

# Выбрала часть реализации, которая вычисляет 1+2+...+n, из задачи проверки, равно ли это выражение n(n+1)/2, где n — любое натуральное число.

import cProfile


def equation_proof1(n):
    return iterated1(n) == combined(n)


def equation_proof2(n):
    return iterated2(n) == combined(n)


def equation_proof3(n):
    return iterated3(n) == combined(n)


def combined(n):
    return n * (n + 1) / 2


# через рекурсию, при больших n (более 995) происходит переполнение
def iterated1(n):
    if n == 1:
        return n
    return n + iterated1(n - 1)


# python -m timeit -n 1000 -s "import les_4_task_1" "les_4_task_1.iterated1(5)"
# 1000 loops, best of 5: 700 nsec per loop

# cProfile.run('iterated1(5)')
#
# 5/1  les_4_task_1.py:31(iterated1)

# python -m timeit -n 1000 -s "import les_4_task_1" "les_4_task_1.iterated1(500)"
# 1000 loops, best of 5: 103 usec per loop

# cProfile.run('iterated1(500)')
#
# 500/1  les_4_task_1.py:31(iterated1)

# python -m timeit -n 1000 -s "import les_4_task_1" "les_4_task_1.iterated1(990)"
# 1000 loops, best of 5: 180 usec per loop

# cProfile.run('iterated1(990)')
#
# 990/1    0.001    0.000    0.001    0.001 les_4_task_1.py:31(iterated1)


def iterated2(n):
    n_sum = 0
    while n >= 1:
        n_sum += n
        n -= 1
    return n_sum


# python -m timeit -n 1000 -s "import les_4_task_1" "les_4_task_1.iterated2(5)"
# 1000 loops, best of 5: 948 nsec per loop

# cProfile.run('iterated2(5)')
#
# 1  les_4_task_1.py:59(iterated2)

# python -m timeit -n 1000 -s "import les_4_task_1" "les_4_task_1.iterated2(500)"
# 1000 loops, best of 5: 49.2 usec per loop

# cProfile.run('iterated2(500)')
#
# 1 les_4_task_1.py:59(iterated2)

# python -m timeit -n 1000 -s "import les_4_task_1" "les_4_task_1.iterated2(1000)"
# 1000 loops, best of 5: 103 usec per loop

# cProfile.run('iterated2(1000)')
#
# 1 les_4_task_1.py:59(iterated2)

# python -m timeit -n 1000 -s "import les_4_task_1" "les_4_task_1.iterated2(5000)"
# 1000 loops, best of 5: 526 usec per loop

# cProfile.run('iterated2(5000)')
#
# 1 les_4_task_1.py:59(iterated2)

def iterated3(n):
    n_sum = 0
    for i in range(n+1):
        n_sum += i
    return n_sum

# python -m timeit -n 1000 -s "import les_4_task_1" "les_4_task_1.iterated3(5)"
# 1000 loops, best of 5: 579 nsec per loop

# cProfile.run('iterated3(5)')
#
# 1 les_4_task_1.py:95(iterated3)

# python -m timeit -n 1000 -s "import les_4_task_1" "les_4_task_1.iterated3(500)"
# 1000 loops, best of 5: 27 usec per loop

# cProfile.run('iterated3(500)')
#
# 1 les_4_task_1.py: 95(iterated3)

# python -m timeit -n 1000 -s "import les_4_task_1" "les_4_task_1.iterated3(1000)"
# 1000 loops, best of 5: 58.7 usec per loop

# cProfile.run('iterated3(1000)')
#
# 1 les_4_task_1.py:95(iterated3)

# python -m timeit -n 1000 -s "import les_4_task_1" "les_4_task_1.iterated3(5000)"
# 1000 loops, best of 5: 330 usec per loop

# cProfile.run('iterated3(5000)')
#
# 1 les_4_task_1.py:95(iterated3)

# Сложность алгоритмов - O(n)
# Последний вариант оказался самым оптимальным, в том числе по ограничению стека вызова функции

# print(equation_proof1(5))
# print(equation_proof2(5))
# print(equation_proof3(5))
