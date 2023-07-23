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
    


# Задача 1.  сложная необязательная. 
# Посчитать сумму цифр любого целого или вещественного числа. 
# Через строку решать нельзя.

N = int(input("Введите число: "))
sum = 0 
while N > 0: 
    x = N % 10 
    sum += x 
    N //= 10
print("Сумма цифр равна:", sum)



# Задача 2. Де моргана необязательная 
# Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = 
# ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.
# теперь надо проверить ее практически
# в цикле 100 раз прогоняем
# каждый раз генерируем случайное количество предикат от 3 до 15
# и конечно со случайным булевым значением
# и засекаем общее время выполнения программы
# юзаем библиотеки random и time
# предикаты НЕ ЗАДАЕМ как целое число!

""" Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.  """



# Задача.  3 необязательная
# Валентина прогуляла лекцию по математике. 
# Преподаватель решил подшутить над нерадивой студенткой и 
# попросил ее на практическом занятии перечислить все положительные делители 
# некоторых целых чисел. 
# Для несложных примеров студентка быстро нашла решения 
# (для числа 6 это: 1, 2, 3, 6; а для числа 16 это: 1, 2, 4, 8, 16),
# но этим все не закончилось. 
# На домашнее задание ей дали варианты 
# посложнее: 23436, 190187200, 380457890232.
# Решить такое вручную, как вы понимаете, практически нереально. 
# Вот Валентина и обратилась к вам за помощью. 
# Помогите ей (при помощи функции all_divisors(number), которую напишете сами). 
# Постарайтесь найти самое оптимальное решение. 
# Результат представьте в виде списка (не забудьте отсортировать по возрастанию).

