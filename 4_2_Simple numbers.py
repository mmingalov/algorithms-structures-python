# 2. Написать два алгоритма нахождения i-го по счёту простого числа.
# Функция нахождения простого числа должна принимать на вход натуральное и возвращать соответствующее простое число.
# Проанализировать скорость и сложность алгоритмов.
# Первый — с помощью алгоритма «Решето Эратосфена».
# Примечание. Алгоритм «Решето Эратосфена» разбирался на одном из прошлых уроков. Используйте этот код и попробуйте его улучшить/оптимизировать под задачу.
# Второй — без использования «Решета Эратосфена».
import cProfile

def IsPrime(n):
   d = 2
   while d * d <= n and n % d != 0:
       d += 1
   return d * d > n

def method1(i): #i-е по счету простое число
    ii=1
    find = 0
    while find<i:
        ii += 1
        if IsPrime(ii):
            find+=1
            # print(ii)

    return(ii)

def method2(p): #решето Эратосфена
    n = 1000000
    count = 0
    sieve = [i for i in range(n)]
    sieve[1]=0
    for i in range(2,n):
        if sieve[i] != 0:
            j = i*2
            count += 1
            # print(count, i)
        while j<n:
            sieve[j]=0
            j+=i
        if count == p:
            # print('Достигнуто заданное i-е число', p)
            return(i)
            break
    result = [i for i in sieve if i!=0]
    return result

limit = 1000
print('Result method1:',method1(limit))
print('Result method2 - Eratosphen:',method2(limit))

print('limit:',limit)
cProfile.run('method1(limit)')
cProfile.run('method2(limit)')

# limit: 250
#          1586 function calls in 0.002 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.002    0.002 4_2_Simple numbers.py:15(method1)
#      1582    0.002    0.000    0.002    0.000 4_2_Simple numbers.py:9(IsPrime)
#         1    0.000    0.000    0.002    0.002 <string>:1(<module>)
#         1    0.000    0.000    0.002    0.002 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#
#
#          5 function calls in 0.587 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.517    0.517    0.579    0.579 4_2_Simple numbers.py:26(method2)
#         1    0.063    0.063    0.063    0.063 4_2_Simple numbers.py:29(<listcomp>)
#         1    0.008    0.008    0.587    0.587 <string>:1(<module>)
#         1    0.000    0.000    0.587    0.587 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

#ВЫВОД
#как показало сравнение, алгоритм решето Эратосфена в моем исполнении уступает альтернативному методу method1