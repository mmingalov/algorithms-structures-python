import cProfile
import sys

"""Написать программу, доказывающую или проверяющую, что для множества натуральных чисел выполняется равенство:
1+2+...+n = n(n+1)/2, где n — любое натуральное число."""

"""Программная реализация №2. Простая рекурсия."""
sys.setrecursionlimit(10000)


def sum_n(n):
    if n == 1:
        return n
    value = n + sum_n(n-1)
    return value


def compare(n):
    if sum_n(n) == n * (n + 1) / 2:
        return True


cProfile.run('compare(10)')
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#      10/1    0.000    0.000    0.000    0.000 Les_4_task_2.py:11(sum_n)
#         1    0.000    0.000    0.000    0.000 Les_4_task_2.py:18(compare)
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
cProfile.run('compare(100)')
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#     100/1    0.000    0.000    0.000    0.000 Les_4_task_2.py:11(sum_n)
#         1    0.000    0.000    0.000    0.000 Les_4_task_2.py:18(compare)
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
cProfile.run('compare(1000)')
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.001    0.001 <string>:1(<module>)
#    1000/1    0.001    0.000    0.001    0.001 Les_4_task_2.py:11(sum_n)
#         1    0.000    0.000    0.001    0.001 Les_4_task_2.py:18(compare)
#         1    0.000    0.000    0.001    0.001 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

# homework>python -m timeit -n 1000 -s "import Les_4_task_2" "Les_4_task_2.compare(10)"
# 1000 loops, best of 5: 1.45 usec per loop

# python -m timeit -n 1000 -s "import Les_4_task_2" "Les_4_task_2.compare(100)"
# 1000 loops, best of 5: 14.6 usec per loop

# python -m timeit -n 1000 -s "import Les_4_task_2" "Les_4_task_2.compare(1000)"
# 1000 loops, best of 5: 182 usec per loop
