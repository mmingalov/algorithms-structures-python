# 3. В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.
import random
list1 = [8, 3, 15, 6, 4, 2]
# list1 = [9, 29, 17, 4, 20, 3, 17, 2]
list1 = [random.randint(0,32) for _ in range(8)]
min_idx = 0
max_idx = 0
min = list1[min_idx]
max = list1[max_idx]

for idx, item in enumerate(list1):
    if item<min:
        min_idx = idx
        min = list1[min_idx]
    if item>max:
        max_idx = idx
        max = list1[max_idx]

print('Source list: ', list1)
print(f'Min:{min}', f'Max:{max}')
list1[max_idx] = min
list1[min_idx] = max
print('Result list:', list1)
