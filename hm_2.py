# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой,
# а некоторые – гербом. Определите минимальное число монеток, 
# которые нужно перевернуть, чтобы все монетки были повернуты вверх одной 
# и той же стороной. 
# Выведите минимальное количество монет, которые нужно перевернуть

n = int(input("Введите количество монет: "))
count = 0
for i in range(n):
    x = int(input('Введите сторону монетки "решка - 0" или "герб - 1"'))
    if x == 0:
        count = count + 1
if count < n - count:
    print(count)
else:
     print(n - count)       

# Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница.
# Петя помогает Кате по математике. 
# Он задумывает два натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать. 
# Для этого Петя делает две подсказки. Он называет сумму этих чисел S и их произведение P. 
# Помогите Кате отгадать задуманные Петей числа.
   
    
S = int(input('Введите первое натуральное число: '))
P = int(input('Введите второе натуральное число: '))        
x = (S - int((S ** 2 - 4 * P) ** 0.5)) // 2
y = (S + int((S ** 2 - 4 * P) ** 0.5)) // 2
print('Сумма чисел равна {}, произведение чисел равна {}'.format(x, y))


# Задача 14: Требуется вывести все целые степени двойки 
# (т.е. числа вида 2k), не превосходящие числа N.

x = 0
y = 1
N = int(input("Введите число N: "))
while y <= N:
    y = 2 ** x
    if y <= N:
        x += 1
        print (y, end = " ")
    




