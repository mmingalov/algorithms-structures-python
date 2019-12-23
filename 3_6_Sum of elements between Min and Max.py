# 6. В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами.
# Сами минимальный и максимальный элементы в сумму не включать.
import random
# list1 = [1, 30, 15, 6, 4, 2]
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

sum=0
print('Source list: ', list1)
print(f'Min:{min}[{min_idx}]', f'Max:{max}[{max_idx}]')
if abs(max_idx-min_idx)<2:
    print('No elements between MIN and MAX. Sum=',sum)
else:
    n1 = min_idx+1 if min_idx <max_idx else max_idx + 1
    n2 = min_idx if min_idx > max_idx else max_idx
    # step = -1 if max_idx < min_idx else 1
    for i in range(n1,n2,1):
        # print(i)
        sum+=list1[i]

    print(f'Number of elements between MIN and MAX is {abs(max_idx-min_idx)-1}. Sum=',sum)