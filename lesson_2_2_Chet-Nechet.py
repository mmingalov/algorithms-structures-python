# 2. Посчитать четные и нечетные цифры введенного натурального числа.
# Например, если введено число 34560, в нем 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).
number = input('Введите число: ')
chet = 0
# zero = 0
nechet = 0
for i in number:
    if int(i) != 0:
        nechet+= int(i)%2
    chet = len(number) - nechet
print (f'Нечетных: {nechet}, четных: {chet}')