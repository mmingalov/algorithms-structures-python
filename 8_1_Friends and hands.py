# 1. На улице встретились N друзей. Каждый пожал руку всем остальным друзьям (по одному разу). Сколько рукопожатий было?
# Примечание. Решите задачу при помощи построения графа.

def friends(num):

    g = set()#[]

    for i in range(num):
        for j in range (num):
            if i!=j:
                ss = set()
                ss.add(i)
                ss.add(j)
                g.add(tuple(ss))
    print(g)

    return len(g)

f = int(input("Введите кол-во друзей: "))
result = friends(f)
print('Количество рукопожатий: ', result)