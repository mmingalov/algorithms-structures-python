import cProfile


"""Написать программу, доказывающую или проверяющую, что для множества натуральных чисел выполняется равенство:
1+2+...+n = n(n+1)/2, где n — любое натуральное число."""

"""Программная реализация №1. Простой цикл."""


def sum_n(n):
    summa = 0
    for x in range(1, n + 1):
        summa += x
    return summa


def compare(n):
    if sum_n(n) == n * (n + 1) / 2:
        return True


cProfile.run('compare(10)')
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#         1    0.000    0.000    0.000    0.000 Les_4_task_1.py:10(sum_n)
#         1    0.000    0.000    0.000    0.000 Les_4_task_1.py:17(compare)
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
cProfile.run('compare(100)')
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#         1    0.000    0.000    0.000    0.000 Les_4_task_1.py:10(sum_n)
#         1    0.000    0.000    0.000    0.000 Les_4_task_1.py:17(compare)
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
cProfile.run('compare(10000)')
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.001    0.001 <string>:1(<module>)
#         1    0.001    0.001    0.001    0.001 Les_4_task_1.py:10(sum_n)
#         1    0.000    0.000    0.001    0.001 Les_4_task_1.py:17(compare)
#         1    0.000    0.000    0.001    0.001 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
cProfile.run('compare(1000000)')
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.055    0.055 <string>:1(<module>)
#         1    0.055    0.055    0.055    0.055 Les_4_task_1.py:10(sum_n)
#         1    0.000    0.000    0.055    0.055 Les_4_task_1.py:17(compare)
#         1    0.000    0.000    0.055    0.055 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


# python -m timeit -n 1000 -s "import Les_4_task_1" "Les_4_task_1.compare(10)"
# 1000 loops, best of 5: 807 nsec per loop

# python -m timeit -n 1000 -s "import Les_4_task_1" "Les_4_task_1.compare(100)"
# 1000 loops, best of 5: 5.05 usec per loop

# python -m timeit -n 1000 -s "import Les_4_task_1" "Les_4_task_1.compare(1000)"
# 1000 loops, best of 5: 47.1 usec per loop

# python -m timeit -n 1000 -s "import Les_4_task_1" "Les_4_task_1.compare(10000)"
# 1000 loops, best of 5: 520 usec per loop
