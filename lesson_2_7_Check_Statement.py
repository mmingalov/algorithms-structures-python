# 7. Написать программу, доказывающую или проверяющую, что для множества натуральных чисел выполняется равенство:
# 1+2+...+n = n(n+1)/2, где n — любое натуральное число.

def r1(n):
    sum=0
    for i in range (1,n+1):
        sum += i
    return sum

def r2(n):
    sum=0
    return n*(n+1)/2

N = int(input('Введите натуральное число: '))
print('Способ 1:',r1(N),' Способ 2:',r2(N), r1(N)==r2(N))
