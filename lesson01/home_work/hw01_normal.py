import random
import math
__author__ = 'Колмачевский Василий'

# Задача-1: Дано произвольное целое число, вывести самую большую цифру этого числа.
# Например, дается x = 58375.
# Нужно вывести максимальную цифру в данном числе, т.е. 8.
# Подразумевается, что мы не знаем это число заранее.
# Число приходит в виде целого беззнакового.
# Подсказки:
# * постарайтесь решить задачу с применением арифметики и цикла while;
# * при желании и понимании решите задачу с применением цикла for.

rand_chislo = random.randint(0, 876567789)
print("Произвольное целое число: ", rand_chislo)
chislo = rand_chislo
maxx = 0

while chislo != 0:
    digit = chislo % 10 #остаток от деления на 10 будет крайним числом
    if digit > maxx:
        maxx = digit

    chislo = chislo // 10 #уменьшаем разряд

print("в числе - ",rand_chislo," максимальная цифра  - ",maxx)



# Задача-2: Исходные значения двух переменных запросить у пользователя.
# Поменять значения переменных местами. Вывести новые значения на экран.
# Решите задачу, используя только две переменные.
# Подсказки:
# * постарайтесь сделать решение через действия над числами;
# * при желании и понимании воспользуйтесь синтаксисом кортежей Python.
x = input("Введите значение переменной X ")
y = input("Введите значение переменной Y")

(x,y) = (y,x)

print("Новое значение X - ",x)
print("Новое значение Y - ",y)

# Задача-3: Напишите программу, вычисляющую корни квадратного уравнения вида
# ax² + bx + c = 0.
# Коэффициенты уравнения вводятся пользователем.
# Для вычисления квадратного корня воспользуйтесь функцией sqrt() модуля math:
# import math
# math.sqrt(4) - вычисляет корень числа 4
print("Решаем квадратное уравнение ax² + bx + c = 0")
a = int(input("Введите значение коэффициента А "))
b = int(input("Введите значение коэффициента В "))
c = int(input("Введите значение коэффициента С "))
print("Получаем уравнение - ",a,"x^2+",b,"x+",c,"=0")
d = b*b - 4*a*c
print("Дискриминант равен = ",str(d))

if d > 0:
    x1 = (-b + math.sqrt(b * b - 4 * a * c)) / (2 * a)
    x2 = (-b - math.sqrt(b * b - 4 * a * c)) / (2 * a)
    print("корней два - ",x1," and ",x2)
elif d == 0:
    x1 = -b / 2 * a
    print("корень один - ", x1)
else:
    print("корней на множестве действительных чисел нет")