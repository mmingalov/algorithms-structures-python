# 1. Подсчитать, сколько было выделено памяти под переменные в ранее разработанных программах в рамках первых трех уроков.
# Проанализировать результат и определить программы с наиболее эффективным использованием памяти.
# Примечание: По аналогии с эмпирической оценкой алгоритмов идеальным решением будет:
# a. выбрать хорошую задачу, которую имеет смысл оценивать по памяти;
# b. написать 3 варианта кода (один у вас уже есть);
# проанализировать 3 варианта и выбрать оптимальный;
# c. результаты анализа (количество занятой памяти в вашей среде разработки) вставить в виде комментариев в файл с кодом.
# Не забудьте указать версию и разрядность вашей ОС и интерпретатора Python;
# d. написать общий вывод: какой из трёх вариантов лучше и почему.

 #объявили переменную для подсчета сколько было выделено памяти под переменные
total_memory = 0

def show_size(x, level=0):
    print('\t'* level, f'type= {x.__class__}, size= {sys.getsizeof(x)}, object= {x}')
    global total_memory
    total_memory += sys.getsizeof(x)
    if hasattr(x,'__iter__'):
        if hasattr(x,'items'):
            for xx in x.items():
                show_size(xx,level + 1)
        elif not isinstance(x,str):
            for xx in x:
                show_size(xx, level +1)
    # return sys.getsizeof(x)
    return total_memory

#ЗАДАЧА
# 9. Найти максимальный элемент среди минимальных элементов столбцов матрицы.
import random
import sys
print(sys.version, sys.platform)
# 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 19:29:22) [MSC v.1916 32 bit (Intel)] win32


matrix = [[random.randint(0,50) for _ in range(8)] for _ in range(8)]
show_size(matrix)
# type= <class 'list'>, size= 68 №--строка/список
# type= <class 'int'>, size= 14 #--элемент в строке/списке
print('Всего выделено памяти под переменные total_memory=',total_memory)
for line in matrix: #печатаем матрицу
    # show_size(line)
    # type = <class 'list'>, size= 68
    for item in line:
        # show_size(item)
        # type = <class 'int'>, size= 12, object= 0
        # type = <class 'int'>, size= 14, object= 29
        print(f'{item:>4}',end='')
    print()

min_element_column = None
show_size(min_element_column)
# type= <class 'NoneType'>, size= 8, object= None
print('Всего выделено памяти под переменные total_memory=',total_memory)
list=[]
show_size(list)
# type = <class 'list'>, size= 36, object=[]
print('Всего выделено памяти под переменные total_memory=',total_memory)
for col in range(0,len(matrix)):
    min_element_column = matrix[0][col]
    for row in matrix:
        if row[col]<min_element_column:
            min_element_column = row[col]
        # show_size(row)
        # type = <class 'list'>, size= 68
        #     type = <class 'int'>, size= 14
    list.append(min_element_column)

print()
#печатаем минимальные элементы
max = list[0]
show_size(max)
# type= <class 'int'>, size= 14, object= 14
for item in list:
    print(f'{item:>4}', end='')
    if item>max:
        max=item
    # show_size(item)
    # type = <class 'int'>, size= 14
print()
print(f'MAX element among MIN elements of columns in matrix is: {max}')
print('Всего выделено памяти под переменные total_memory=',total_memory)