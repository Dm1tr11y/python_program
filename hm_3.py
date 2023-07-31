# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями). 
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n — кол-во элементов первого множества.
# m — кол-во элементов второго множества. Затем пользователь вводит сами элементы множеств.

n = (int(input("Введите число n элементов: ")))
list_1=[]
for i in range(n):
    number = int(input("Введите число: "))
    list_1.append(number)
print(list_1)


m = (int(input("Введите число n элементов: ")))
list_2 = []
for i in range(m):
    number = int(input("Введите число: "))
    list_2.append(number)
print(list_2)


list3 = list_1 + list_2

checked_list = []
for i in list3:
    if list3.count(i) > 1 and i not in checked_list:
        checked_list.append(i)
        print(i, end = ' ')


# Задача 24: В фермерском хозяйстве в Карелии выращивают чернику. Она растёт на круглой грядке,
# причём кусты высажены только по окружности. Таким образом, у каждого куста есть ровно два соседних. 
# Всего на грядке растёт N кустов. Эти кусты обладают разной урожайностью, 
# поэтому ко времени сбора на них выросло различное число ягод — на i-ом кусте выросло ai ягод.
# В этом фермерском хозяйстве внедрена система автоматического сбора черники. Эта система состоит 
# из управляющего модуля и нескольких собирающих модулей. Собирающий модуль за один заход,
# находясь непосредственно перед некоторым кустом, собирает ягоды с этого куста и с двух соседних с ним.
# Напишите программу для нахождения максимального числа ягод, которое может собрать за один заход 
# собирающий модуль, находясь перед некоторым кустом заданной во входном файле грядки.

n = int(input("Введите кол-во кустов: "))
list = []
for i in range(n):
    x = int(input("Введите кол-во ягод на кустах: "))
    list.append(x)

list_count = []
for i in range(len(list) - 1):
    list_count.append(list[i - 1] + list[i] + list[i + 1])
list_count.append(list[-2] + list[-1] + list[0])
print(max(list_count))