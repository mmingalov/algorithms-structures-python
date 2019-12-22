# 9. Среди натуральных чисел, которые были введены, найти наибольшее по сумме цифр.
# Вывести на экран это число и сумму его цифр.

# сумма цифр в числе
def sumNumber(num):
    summa=0
    for i in num:
        summa+=int(i)
    return summa


numbers = input('Введите натуральные числа, разделенные пробелом: ').split(sep=' ')
max_number_index = 0
nn=-1
for n in numbers:
    nn+=1
    sn = sumNumber(n)
    si = sumNumber(numbers[max_number_index])
    if sn>si:
        max_number_index = nn
print(f'Искомое число={numbers[max_number_index]}, сумма его цифр={sumNumber(numbers[max_number_index])}')