# 1. Пользователь вводит данные о количестве предприятий, их наименования и прибыль за четыре квартала для каждого предприятия.
# Программа должна определить среднюю прибыль (за год для всех предприятий)
# и отдельно вывести наименования предприятий, чья прибыль выше среднего и ниже среднего.

# вычислить прибыль за год каждой компании, а затем посчитать среднюю прибыль за год среди всех компаний

N = 3
Names = ['A','B','C']
Money1 = [100,200,300,400]
Money2 = [200,300,400,500]
Money3 = [300,400,500,600]

from collections import namedtuple, OrderedDict
import random
# prop = ['enterprise','Q1','Q2','Q3','Q4', 'Total',defaults = [0]]
New_Enterprise = namedtuple('New_Enterprise','enterprise Q1 Q2 Q3 Q4 Total',defaults = [0])

N = int(input('Введите кол-во предприятий для теста. Их значения поквартальной прибыли будут сгенерированы автоматически: '))
enterprises = []
total_sum=0
for i in range(N):
    ne = New_Enterprise('A'+str(i),random.randint(500,999),random.randint(500,999),random.randint(500,999),random.randint(500,999))
    ne2 = ne._replace(Total=ne.Q1+ne.Q2+ne.Q3+ne.Q4)
    enterprises.append(ne2)
    total_sum += ne2.Total

print('Были сгенерированы предприятия',enterprises, sep='\n')
print('Общая прибыль за год по всем предприятиям:', total_sum)
avg_sum = total_sum/N
print('Средняя прибыль за год по всем предприятиям:', avg_sum)

list_beyond = []
list_above = []
dict_beyond = {}
dict_above = {}
for e in enterprises:
    if e.Total<avg_sum:
        # list_beyond.append(e.enterprise)
        dict_beyond[e.enterprise]=e.Total
    else:
        # list_above.append(e.enterprise)
        dict_above[e.enterprise] = e.Total

print('Прибыль ниже среднего у:',OrderedDict(sorted(dict_beyond.items(),key=lambda x: x[1])))
print('Прибыль выше среднего у:',OrderedDict(sorted(dict_above.items(),key=lambda x: x[1])))