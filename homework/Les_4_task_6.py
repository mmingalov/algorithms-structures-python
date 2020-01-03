"""Второй — без использования «Решета Эратосфена».
Примечание. Вспомните классический способ проверки числа на простоту.
применяю метод перебора делителей от 2 до корень из n"""

import cProfile
import math


def prime(n):
    # в 100000 тысячах чисел содержится примерно 10000 простых (на самом деле меньше, но тенденция примерно такова)
    numbers = n * 10
    prime_list = [0, 1, 2, 3]
    # i - это число, проверяемое на простоту
    for i in range(4, numbers):
        # узнаем, было ли хоть одно входжение
        inputs = False
        # j- это набор его всевозможных делителей
        for j in range(2, round(i / 2) + 1):
            if i % j == 0:
                inputs = True
                break

        if not inputs:
            prime_list.append(i)

    return prime_list[n]


cProfile.run('prime(10)')
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#         1    0.000    0.000    0.000    0.000 Les_4_task_6.py:9(prime)
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#        96    0.000    0.000    0.000    0.000 {built-in method builtins.round}
#        23    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

cProfile.run('prime(100)')
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.002    0.002 <string>:1(<module>)
#         1    0.002    0.002    0.002    0.002 Les_4_task_6.py:9(prime)
#         1    0.000    0.000    0.003    0.003 {built-in method builtins.exec}
#       996    0.000    0.000    0.000    0.000 {built-in method builtins.round}
#       166    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
cProfile.run('prime(200)')
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.014    0.014 <string>:1(<module>)
#         1    0.013    0.013    0.014    0.014 Les_4_task_6.py:9(prime)
#         1    0.000    0.000    0.014    0.014 {built-in method builtins.exec}
#      1996    0.000    0.000    0.000    0.000 {built-in method builtins.round}
#       301    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

cProfile.run('prime(400)')
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.042    0.042 <string>:1(<module>)
#         1    0.041    0.041    0.042    0.042 Les_4_task_6.py:9(prime)
#         1    0.000    0.000    0.042    0.042 {built-in method builtins.exec}
#      3996    0.001    0.000    0.001    0.000 {built-in method builtins.round}
#       548    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


# python -m timeit -n 1000 -s "import Les_4_task_6" "Les_4_task_6.prime(10)"
# 1000 loops, best of 5: 78.5 usec per loop

# python -m timeit -n 1000 -s "import Les_4_task_6" "Les_4_task_6.prime(100)"
# 1000 loops, best of 5: 2.4 msec per loop

# python -m timeit -n 1000 -s "import Les_4_task_6" "Les_4_task_6.prime(200)"
# 1000 loops, best of 5: 9.84 msec per loop

# python -m timeit -n 1000 -s "import Les_4_task_6" "Les_4_task_6.prime(400)"
# 1000 loops, best of 5: 35.8 msec per loop


