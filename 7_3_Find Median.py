# 3. Массив размером 2m + 1, где m — натуральное число, заполнен случайным образом.
# Найдите в массиве медиану. Медианой называется элемент ряда, делящий его на две равные части:
# в одной находятся элементы, которые не меньше медианы, в другой — не больше медианы.
# Примечание: задачу можно решить без сортировки исходного массива.
# Но если это слишком сложно, используйте метод сортировки, который не рассматривался на уроках
# (сортировка слиянием также недопустима).

import random
import numpy as np

def sorting_bubble(array):
    n=1
    while n<len(array):
        swapped = False #вводим переменную флаг для фиксирования наличия перестановок в данной итерации
        for i in range(len(array)-n):

            if array[i] > array[i+1]:
                array[i], array[i+1] = array[i+1], array[i]
                swapped = True
        if swapped == False:
            return array    #выходим, если перестановок в итерации не было

        # print('Итерация',n,': ',array)
        n+=1
    return array

m = 15
array = [random.randint(-100,100) for _ in range(2*m+1)]
random.shuffle(array)
print('Исходный массив:')
print(array)

array2 = sorting_bubble(array)

median_np = np.median(array)
print(f'Медиана через numpy = {median_np}')

i = len(array2)-1
idx = int(i/2)
median_sort = array2[idx]
print(f'Медиана через sorting = {median_sort}')
