import random

def task1():
    numbers = input('Введите список из чисел, разделенных пробелом: ').split()
    num_list = [int(i) for i in numbers]
    print("Список чисел: ", num_list)

def task2():
    print(set(random.randrange(1, 99) for i in range(20)))

def task3():
    numbers = [random.randint(1, 99) for i in range(random.randint(1,10))]
    randomNumber = random.randint(0,len(numbers))
    randomNumber1 = random.randint(0, len(numbers))
    print('Случайный список цифр',numbers)
    print('Корень из числа под индексом',random.randint(0,len(numbers)),'равен',(numbers[randomNumber]**0.5))
    print('Среднее арифметическое двух случайных чисел под индексами',randomNumber,'и',randomNumber1,' равно',(numbers[randomNumber]+numbers[randomNumber1])/2)

def task4(n):
    numbers = [random.randint(1, 99) for i in range(random.randint(1,10))]
    numbers2 = []
    numbers3 = []
    numbers4 = []
    print('Сгенерированный список',numbers)
    for number in numbers:
        numbers2.append(number*2)
        numbers3.append(number-n)
        numbers4.append(round(number/numbers[0],2))
    print('Увеличенные значения в списке в 2 раза',numbers2)
    print('Уменьшенные значения в списке на {}'.format(n), numbers3)
    print('Уменьшенные значения в списке на первый элемент {}'.format(numbers[0]), numbers4)

def task5():
    numbers = [random.randint(-50, 200) for i in range(random.randint(1,10))]
    numbers1 = []
    numbers2 = []
    print('Сгенерированный список',numbers)
    for number in numbers:
        if number > 0:
            numbers1.append(number)
        if number < 100:
            numbers2.append(number)
    print('Положительный список', numbers1)
    print('Cписок из чисел, не больше 100', numbers2)

def task6():
    numbers = [random.randint(-50, 200) for i in range(random.randint(3,10))]
    MAX = 0
    MIN = 200
    maxIndex = 0
    minIndex = 0
    print('Сгенерированный список',numbers)
    for number in numbers:
        for num in range(len(numbers)):
            if number > MAX:
                MAX = number
            if number < MIN:
                MIN=number
            if numbers[num]== MAX:
                maxIndex = num
            if numbers[num] == MIN:
                minIndex = num
    print('Макимальный элемент', MAX)
    print('Минимальный элемент', MIN)
    print('Максимальный элемент больше минимального на', MAX-MIN)
    print('Индекс максимального элемент', maxIndex)
    print('Индекс минимального элемент', minIndex)

def task7():
    numbers = [random.randint(-50, 200) for i in range(random.randint(8,10))]
    MAX = numbers[3]
    numbers1 = []
    print('Сгенерированный список', numbers)
    for i in range(len(numbers)):
        numbers1.append(numbers[i])
    numbers1.remove(numbers[2])
    numbers1.remove(numbers[5])
    numbers1.insert(2, numbers[5])
    numbers1.insert(5,numbers[2])
    print('Измененный список', numbers1)
    numbers2 = numbers
    for number in numbers:
        if number > MAX:
            MAX = number
            break
    for num in range(len(numbers)):
        if numbers[num] == MAX:
            maxIndex = numbers[num]
    numbers2.remove(numbers2[3])
    numbers2.insert(3,maxIndex)
    print('Споск, где поеменены 3 и макисмальный элемент массива', numbers2)
task7()