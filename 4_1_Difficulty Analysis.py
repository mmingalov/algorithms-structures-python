# 1. Проанализировать скорость и сложность одного любого алгоритма из разработанных в рамках домашнего задания первых трех уроков.
# Примечание. Идеальным решением будет:
# a. выбрать хорошую задачу, которую имеет смысл оценивать,
# b. написать 3 варианта кода (один у вас уже есть),
# c. проанализировать 3 варианта и выбрать оптимальный,
# d. результаты анализа вставить в виде комментариев в файл с кодом (не забудьте указать, для каких N вы проводили замеры),
# e. написать общий вывод: какой из трёх вариантов лучше и почему.


#ВЫБИРАЕМ ЗАДАЧУ
# Найти сумму n элементов следующего ряда чисел: 1, -0.5, 0.25, -0.125,…
# Количество элементов (n) вводится с клавиатуры.
import cProfile
import math
kol =  899 #int(input('Введите кол-во элементов в ряду: '))
result = 0

def sum2(n,m):
    result = 1
    # print(result)
    while n<m:
        s=2**n
        # print(result)
        value = 1/(s*(-1)**(n))
        # print(value)
        result += value
        n+=1

    return result

def sum1(n,m):
    result = 0
    if n<=m:
        result = 1/((-2)**(n-1))
        # print(result)
        return (result+sum1(n+1,m))
    else:
        return 0


# res = sum1(1,kol)
# print(f'Result sum1: {res}')
# res = sum2(1,kol)
# print(f'Result sum2: {res}')

print('kol:',kol)
cProfile.run('sum1(1,kol)')
cProfile.run('sum2(1,kol)')

# под выбранную задачу осилил только два решения
# их и проанализируем ниже


# kol: 899
#          903 function calls (4 primitive calls) in 0.003 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#     900/1    0.003    0.000    0.003    0.003 4_1_Difficulty Analysis.py:31(sum1)
#         1    0.000    0.000    0.003    0.003 <string>:1(<module>)
#         1    0.000    0.000    0.003    0.003 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#
#
#          4 function calls in 0.002 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.002    0.002    0.002    0.002 4_1_Difficulty Analysis.py:18(sum2)
#         1    0.000    0.000    0.002    0.002 <string>:1(<module>)
#         1    0.000    0.000    0.002    0.002 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

#ВЫВОД
#Вариант sum1 с использованием рекурсии как правило работает медленнее