# Найти сумму n элементов следующего ряда чисел: 1, -0.5, 0.25, -0.125,…
# Количество элементов (n) вводится с клавиатуры.

kol = int(input('Введите кол-во элементов в ряду: '))
result = 0
def sum1(n,m):
    if n<=m:
        result = 1/((-2)**(n-1))
        # print(result)
        return (result+sum1(n+1,m))
    else:
        return 0

print(sum1(1,kol))