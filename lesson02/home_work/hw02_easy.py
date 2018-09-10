import random

# Задача-1:
# Дан список фруктов.
# Напишите программу, выводящую фрукты в виде нумерованного списка,
# выровненного по правой стороне.

# Пример:
# Дано: ["яблоко", "банан", "киви", "арбуз"]
# Вывод:
# 1. яблоко
# 2.  банан
# 3.   киви
# 4.  арбуз
a = ["яблоко", "банан", "киви", "арбуз"]
for s in a:
    print("{:>}".format(s))
# Подсказка: воспользоваться методом .format()


# Задача-2:
# Даны два произвольные списка.
# Удалите из первого списка элементы, присутствующие во втором списке.
s1 = [1,2,3,4,5,6,7,8]
s2 = [3,4,5]
for st in s2:
    i = s1.count(st)
    while i > 0:
        s1.remove(st)
        i-=1
print(s1)

# Задача-3:
# Дан произвольный список из целых чисел.
# Получите НОВЫЙ список из элементов исходного, выполнив следующие условия:
# если элемент кратен двум, то разделить его на 4, если не кратен, то умножить на два.
aa = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
bb = list()

for a1 in aa:
    if a1%2 == 0:
        bb.append(a1 / 4)
    else:
        bb.append(a1 * 2)

print(bb)
