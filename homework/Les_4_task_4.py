import cProfile
import sys

"""Написать программу, доказывающую или проверяющую, что для множества натуральных чисел выполняется равенство:
1+2+...+n = n(n+1)/2, где n — любое натуральное число."""

"""Программная реализация №4. Рекурсия с сохранением значений в словарь."""
sys.setrecursionlimit(10000)


def sum_n(n):
    sum_dict = {i: None for i in range(1, n+1)}
    sum_dict[1] = 1

    def sum_d(n):
        if n == 1:
            return sum_dict[1]
        sum_dict[n] = n + sum_d(n-1)
        return sum_dict[n]

    return sum_d(n)


def compare(n):
    if sum_n(n) == n * (n + 1) / 2:
        return True


cProfile.run('compare(10)')
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#         1    0.000    0.000    0.000    0.000 Les_4_task_4.py:11(sum_n)
#         1    0.000    0.000    0.000    0.000 Les_4_task_4.py:12(<dictcomp>)
#      10/1    0.000    0.000    0.000    0.000 Les_4_task_4.py:15(sum_d)
#         1    0.000    0.000    0.000    0.000 Les_4_task_4.py:24(compare)
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
cProfile.run('compare(100)')
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#         1    0.000    0.000    0.000    0.000 Les_4_task_4.py:11(sum_n)
#         1    0.000    0.000    0.000    0.000 Les_4_task_4.py:12(<dictcomp>)
#     100/1    0.000    0.000    0.000    0.000 Les_4_task_4.py:15(sum_d)
#         1    0.000    0.000    0.000    0.000 Les_4_task_4.py:24(compare)
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
cProfile.run('compare(1000)')
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.001    0.001 <string>:1(<module>)
#         1    0.000    0.000    0.001    0.001 Les_4_task_4.py:11(sum_n)
#         1    0.000    0.000    0.000    0.000 Les_4_task_4.py:12(<dictcomp>)
#    1000/1    0.001    0.000    0.001    0.001 Les_4_task_4.py:15(sum_d)
#         1    0.000    0.000    0.001    0.001 Les_4_task_4.py:24(compare)
#         1    0.000    0.000    0.001    0.001 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

# python -m timeit -n 1000 -s "import Les_4_task_4" "Les_4_task_4.compare(10)"
# 1000 loops, best of 5: 3.6 usec per loop

# python -m timeit -n 1000 -s "import Les_4_task_4" "Les_4_task_4.compare(100)"
# 1000 loops, best of 5: 29.2 usec per loop

# python -m timeit -n 1000 -s "import Les_4_task_4" "Les_4_task_4.compare(1000)"
# 1000 loops, best of 5: 344 usec per loop
