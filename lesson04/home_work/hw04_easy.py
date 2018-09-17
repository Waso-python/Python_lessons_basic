# Все задачи текущего блока решите с помощью генераторов списков!
import random
# Задание-1:
# Дан список, заполненный произвольными целыми числами. 
# Получить новый список, элементы которого будут
# квадратами элементов исходного списка
# [1, 2, 4, 0] --> [1, 4, 16, 0]


def rand_int(count, fr, to):
    lst_g = [random.randint(fr, to) for _ in range(count)]
    return lst_g


def stepen(lst):
    new_lst = [el*el for el in lst]
    return new_lst


a = rand_int(8,-20,20)
b = stepen(a)
print(a)
print(b)


# Задание-2:
# Даны два списка фруктов.
# Получить список фруктов, присутствующих в обоих исходных списках.
a = ["apple", "grapefruit", "strawberry", "orange"]
b = ["Banana", "Guava", "Kiwi", "orange", "apple"]

def compare_lst(lst1,lst2):
    lst3 = list()
    for el in lst1:
        if el in lst2:
            lst3.append(el)
        else: pass
    return lst3
print(compare_lst(a,b))




# Задание-3:
# Дан список, заполненный произвольными числами.
# Получить список из элементов исходного, удовлетворяющих следующим условиям:
# + Элемент кратен 3
# + Элемент положительный
# + Элемент не кратен 4

a1 = list()
a2 = list()
a3 = list()

lst = rand_int(10, -15, 15)

a1 = [el for el in lst if not el % 3]
a2 = [el for el in lst if el >= 0]
a3 = [el for el in lst if el % 4]

print(lst)
print(a1)
print(a2)
print(a3)