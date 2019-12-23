# 5. В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве.
# Примечание к задаче: пожалуйста не путайте «минимальный» и «максимальный отрицательный». Это два абсолютно разных значения.

import random
# list1 = [8, 3, 15, 6, 4, 2]
# list1 = [9, 29, 17, 4, 20, 3, 17, 2]
list1 = [random.randint(-100,100) for _ in range(8)]

max_neg_idx = -1
for idx, item in enumerate(list1):
    if item<0:
        if max_neg_idx<0:
            max_neg_idx=idx
            max = item
        if item>max:
            max_neg_idx = idx
            max = item

print('Source list:',list1)
if max_neg_idx<0:
    print('Source list did not include negative numbers!')
else:
    print(f'Position is: {max_neg_idx}, value is:{max}')