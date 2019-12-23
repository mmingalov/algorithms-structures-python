# 9. Найти максимальный элемент среди минимальных элементов столбцов матрицы.
import random
matrix = [[random.randint(0,50) for _ in range(5)] for _ in range(5)]

#печатаем матрицу
for line in matrix:
    for item in line:
        print(f'{item:>4}',end='')
    print()
min_element_column = []
list=[]
for col in range(0,len(matrix)):
    min_element_column = matrix[0][col]
    for row in matrix:
        if row[col]<min_element_column:
            min_element_column = row[col]
    list.append(min_element_column)

print()
#печатаем минимальные элементы
max = list[0]
for item in list:
    print(f'{item:>4}', end='')
    if item>max:
        max=item
print()
print(f'MAX element among MIN elements of columns in matrix is: {max}')
