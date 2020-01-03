"""Написать два алгоритма нахождения i-го по счёту простого числа. Функция нахождения простого числа должна принимать
на вход натуральное и возвращать соответствующее простое число. Проанализировать скорость и сложность алгоритмов.
Первый — с помощью алгоритма «Решето Эратосфена»."""

import cProfile


def primes(n):

    sieve = [i for i in range(n*10)]
    sieve[1] = 0

    for i in range(2, n*10):
        if sieve[i] != 0:
            j = i * 2
            while j < n*10:
                sieve[j] = 0
                j += i
    result = [i for i in sieve if i != 0]
    return result[n]


cProfile.run('primes(10)')
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#         1    0.000    0.000    0.000    0.000 Les_4_task_5.py:10(<listcomp>)
#         1    0.000    0.000    0.000    0.000 Les_4_task_5.py:19(<listcomp>)
#         1    0.000    0.000    0.000    0.000 Les_4_task_5.py:8(primes)
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
cProfile.run('primes(100)')
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#         1    0.000    0.000    0.000    0.000 Les_4_task_5.py:10(<listcomp>)
#         1    0.000    0.000    0.000    0.000 Les_4_task_5.py:19(<listcomp>)
#         1    0.000    0.000    0.000    0.000 Les_4_task_5.py:8(primes)
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
cProfile.run('primes(1000)')
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.004    0.004 <string>:1(<module>)
#         1    0.000    0.000    0.000    0.000 Les_4_task_5.py:10(<listcomp>)
#         1    0.000    0.000    0.000    0.000 Les_4_task_5.py:19(<listcomp>)
#         1    0.003    0.003    0.004    0.004 Les_4_task_5.py:8(primes)
#         1    0.000    0.000    0.004    0.004 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
cProfile.run('primes(2000)')
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.008    0.008 <string>:1(<module>)
#         1    0.001    0.001    0.001    0.001 Les_4_task_5.py:10(<listcomp>)
#         1    0.001    0.001    0.001    0.001 Les_4_task_5.py:19(<listcomp>)
#         1    0.007    0.007    0.008    0.008 Les_4_task_5.py:8(primes)
#         1    0.000    0.000    0.008    0.008 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
cProfile.run('primes(5000)')
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.021    0.021 <string>:1(<module>)
#         1    0.002    0.002    0.002    0.002 Les_4_task_5.py:10(<listcomp>)
#         1    0.001    0.001    0.001    0.001 Les_4_task_5.py:19(<listcomp>)
#         1    0.018    0.018    0.021    0.021 Les_4_task_5.py:8(primes)
#         1    0.000    0.000    0.021    0.021 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

# python -m timeit -n 1000 -s "import Les_4_task_5" "Les_4_task_5.primes(10)"
# 1000 loops, best of 5: 25 usec per loop

# python -m timeit -n 1000 -s "import Les_4_task_5" "Les_4_task_5.primes(100)"
# 1000 loops, best of 5: 353 usec per loop

# python -m timeit -n 1000 -s "import Les_4_task_5" "Les_4_task_5.primes(1000)"
# 1000 loops, best of 5: 4.1 msec per loop

# python -m timeit -n 1000 -s "import Les_4_task_5" "Les_4_task_5.primes(2000)"
# 1000 loops, best of 5: 8.47 msec per loop

# python -m timeit -n 1000 -s "import Les_4_task_5" "Les_4_task_5.primes(5000)"
# 1000 loops, best of 5: 22.4 msec per loop




