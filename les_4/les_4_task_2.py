# 2. Написать два алгоритма нахождения i-го по счёту простого числа. Функция нахождения простого числа
# должна принимать на вход натуральное и возвращать соответствующее простое число.
# Проанализировать скорость и сложность алгоритмов.
# Первый — с помощью алгоритма «Решето Эратосфена».
# Примечание. Алгоритм «Решето Эратосфена» разбирался на одном из прошлых уроков. Используйте этот код
# и попробуйте его улучшить/оптимизировать под задачу.
# Второй — без использования «Решета Эратосфена».
# Примечание. Вспомните классический способ проверки числа на простоту.
# Пример работы программ:
# >>> sieve(2)
# 3
# >>> prime(4)
# 7
# >>> sieve(5)
# 11
# >>> prime(1)
# 2

import cProfile


def sieve(i):
    # if i < 1:
    #     return "no prime"
    count = 0
    num = 2
    while True:
        if is_sieve_prime(num):
            count += 1
        if count == i:
            break
        num += 1
    return num


def is_sieve_prime(n):
    lst_init = [i for i in range(n + 1)]
    lst_init[1] = 0
    for i in range(2, n + 1):
        if lst_init[i] != 0:
            j = i * 2
            while j < (n + 1):
                lst_init[j] = 0
                j += i
    result = [i for i in lst_init if i != 0]
    if n in result:
        return True
    return False


# print(sieve(12))

# python -m timeit -n 1000 -s "import les_4_task_2" "les_4_task_2.sieve(12)"
# 1000 loops, best of 5: 214 usec per loop

# python -m timeit -n 100 -s "import les_4_task_2" "les_4_task_2.sieve(12)"
# 100 loops, best of 5: 213 usec per loop

# cProfile.run('sieve(12)')
#
# 1    les_4_task_2.py:22(sieve)
# 36   les_4_task_2.py:36(is_sieve_prime)

# python -m timeit -n 100 -s "import les_4_task_2" "les_4_task_2.sieve(100)"
# 100 loops, best of 5: 46.8 msec per loop

# cProfile.run('sieve(100)')
#
# 1    les_4_task_2.py:22(sieve)
# 540  les_4_task_2.py:36(is_sieve_prime)

# python -m timeit -n 10 -s "import les_4_task_2" "les_4_task_2.sieve(255)"
# 10 loops, best of 5: 468 msec per loop

# cProfile.run('sieve(255)')
#
# 1       0.003    0.003    0.470    0.470 les_4_task_2.py:22(sieve)
# 1612    0.395    0.000    0.466    0.000 les_4_task_2.py:36(is_sieve_prime)

# cProfile.run('sieve(1000)')
#
# 1       0.068    0.068   12.400   12.400 les_4_task_2.py:22(sieve)
# 7918   10.651    0.001   12.333    0.002 les_4_task_2.py:36(is_sieve_prime)

# Сложность O(n**2) - квадратичная сложность


def is_prime(i):
    if i == 2:
        return True
    for ind in range(2, i):
        if (i % ind) == 0:
            return False
    return True


def prime(n):
    # if n < 1:
    #     return "no prime"
    count = 0
    i = 1
    while count < n:
        i += 1
        if is_prime(i):
            count += 1
    return i


# print(prime(1))
# print(prime(2))
# print(prime(3))
# print(prime(4))
# print(prime(5))

# python -m timeit -n 1000 -s "import les_4_task_2" "les_4_task_2.prime(12)"
# 1000 loops, best of 5: 24.6 usec per loop

# python -m timeit -n 100 -s "import les_4_task_2" "les_4_task_2.prime(12)"
# 100 loops, best of 5: 24.9 usec per loop

# cProfile.run('prime(12)')
#
# 36   les_4_task_2.py:88(is_prime)
# 1    les_4_task_2.py:97(prime)

# python -m timeit -n 100 -s "import les_4_task_2" "les_4_task_2.prime(100)"
# 100 loops, best of 5: 1.46 msec per loop

# cProfile.run('prime(100)')
#
# 540    0.001    0.000    0.001    0.000 les_4_task_2.py:88(is_prime)
# 1      0.000    0.000    0.002    0.002 les_4_task_2.py:97(prime)

# python -m timeit -n 100 -s "import les_4_task_2" "les_4_task_2.prime(255)"
# 100 loops, best of 5: 11.8 msec per loop

# cProfile.run('prime(255)')
#
# 1612    0.012    0.000    0.012    0.000 les_4_task_2.py:88(is_prime)
# 1       0.000    0.000    0.012    0.012 les_4_task_2.py:97(prime)

# python -m timeit -n 100 -s "import les_4_task_2" "les_4_task_2.prime(1000)"
# 100 loops, best of 5: 269 msec per loop

# cProfile.run('prime(1000)')
#
# 7918    0.256    0.000    0.256    0.000 les_4_task_2.py:88(is_prime)
# 1       0.002    0.002    0.258    0.258 les_4_task_2.py:97(prime)

# Сложность O(n**2) - квадратичная сложность
# Алгоритм по классическому поиску простых чисел оказался быстрее (в данной реализации).
# В алгоритме с решетом Эратосфена на каждое последующее число из предполагаемых простых создаётся новое решето,
# можно попробовать реализовать с запоминанием предыдущих расчётов
