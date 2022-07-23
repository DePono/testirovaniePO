import math
from random import randint
#Task 1
def print_n_times(n):
    for i in range(10):
        print(n)

#Task 2
def print_with_point(n):
    for i in range(15):
        print(n,n+0.4)

#Task 3
def print_multiplication_table(n):
    for i in range(7):
        print(i,'x',n,'=',i*n)

#Task 4.1
def sum_of_numbers(a,b):
    while a<=b:
        total = 0
        for i in range(a,b+1):
            total += i
            a += i
            if a == b:
                break
        print(total)

#Task 5
def average_of_numbers(a,n):
        total = 0
        for i in range(abs(a),abs(n+1)):
            total += i
        average = total/(n)
        print(average)

#Task 6.1
def fibbonaci_k_chlen(n):
    if n <2:
        return n
    return fibbonaci_k_chlen(n-2) + fibbonaci_k_chlen(n-1)

#Task 6.2
def fibbonaci_first_n_chlenov(n):
    row = [1,1]
    fibrow=[]
    if n <2:
        return row
    for i in range(n):
        fibrow.append(fibbonaci_k_chlen(i+1))
    return fibrow

#Task 6.3
def fibbonaci_sum_first_n_chlenov(n):
    row = [1,1]
    fibrow=[]
    total = 0
    if n <=2:
        return print(row)
    for i in range(n):
        fibrow.append(fibbonaci_k_chlen(i+1))
    for i in fibrow:
        total+=i
    if total%2 == 0:
        return print('сумма ряда',fibrow,'есть',total,'и это четная сумма')
    else:
        return print('сумма ряда',fibrow,'есть',total,'и это нечетная сумма')

#Task 7.1/2
def row_of_numbers(n):
    summa = 0
    count = 0
    numbers=[]
    for i in range(n):
        i=randint(1,100)
        numbers.append(i)
    numbers.append(0)
    for i in numbers:
        summa+=i
        count+=1
    return print('Сумма последовательности чисел',numbers,'равна',summa,'число элементов равно',count)

#Task 8.1/2(10.1/2)
def number(n):
    count_of_3 = 0
    count_of_last_number = 0
    count_of_even = 0
    count_more_than_five = 0
    count_more_than_seven = 0
    count_zero_and_five = 0
    numb = []
    number=randint(n,100000)
    MAX = 0
    MIN = 9
    for i in str(number):
        if i == '3':
            count_of_3+=1
        if i == str(number)[-1]:
            count_of_last_number+=1
        if int(i) % 2 == 0:
            count_of_even+=1
        if i > '5':
            count_more_than_five += 1
        if i > '7':
            count_more_than_seven += 1
        if i=='0' or i=='7':
            count_zero_and_five += 1
        numb.append(int(i))
    for i in numb:
        if i > MAX:
            MAX = i
        if i < MIN:
            MIN = i
    return print('Дано число',number,'в нем количество 3 равно',count_of_3,
                 ' Количество послeдней цифры',str(number)[-1],'равно',count_of_last_number,
                 ' Количество цифр, которые четные', count_of_even,
                 ' Количество цифр, больше 5, равно', count_more_than_five,
                 ' Количество цифр, больше 7, равно', count_more_than_seven,
                 ' Количество цифр 0 и 7 , равно', count_zero_and_five,
                 ' Максимальная цифра', MAX, ' Мнимальная цифра', MIN,
                 )

#Task 12
def bank_accounts(n):
    INCREASE = 0.02
    MOUNTH = []
    for i in range(12):
        MOUNTH.append(n)
    for i in range(len(MOUNTH)):
        MOUNTH[i] = MOUNTH[i-1]*INCREASE+MOUNTH[i-1]
    for i in range(len(MOUNTH)):
        if MOUNTH[i]-n>30:
            print('На',i+1,'месяце величина ежемесячного увеличения превысит 30 рублей и будет равна',round(MOUNTH[i]-n,2))
            break
    for i in range(len(MOUNTH)):
        if MOUNTH[i]>1200:
            print('На',i,'месяце размер вклада превысит 1200 и будет',round(MOUNTH[i],2))
            break

#Task Самостоятельная работа
def kg_in_ib(n):
    LB=453
    for i in range(1,n):
        print(i,'х',LB,'=',i*LB,'кг')

def harmonic_series(n):
    count = 0
    for i in range(1,n):
        count+=1/n
    return print('Сумма ряда из 1/n',n,'чисел равна',count)

harmonic_series(3)