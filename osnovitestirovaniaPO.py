import math
#Объявляем константы большими буквами
CELCIUS = 36.6
FAHRENHEIT = 1.8
KELVIN = -273.15
#Очки за игру
WINSCORE = 3
LOSESCORE = 0
NOTHINGSCORE = 1

#Функция для перевода в Фаренгейты
def celcuis_to_fahrenheit(temp):
    fahr = 32
    convert = temp*FAHRENHEIT+fahr
#округялем до двух цифр после запятой, используя round
    return print(CELCIUS, 'градусов Цельсия будет',round(convert,2),'градусов по Фаренгейту')

#Функция для перевода в Кельвины
def celcuis_to_kelvin(temp):
    convert = temp+KELVIN
# округялем до двух цифр после запятой, используя round
    return print(CELCIUS, 'градусов Цельсия будет',round(convert,2),'градусов по Кельвину')

#Функция для проверки вместимости круга в квадрат
def circle_and_square(r,a):
    # Ищем диагональ квадрата
    d = math.sqrt(a**2+a**2)
    if d/2 <= r:
        print('Круг с радусом',r,'мм вмещает в себя квадрат со стороной', a,'мм','так как диагональ квадрата',round(d,2),',а диаметр круга',round(2*r,2))
    else:
        print('Квадрат со стороной',a,'мм поместит в себя kруг с радусом', r,'и диаметром',2*r,'мм',',так как диагональ квадрата',round(d,2),',а диаметр круга',round(2*r,2))

#Функция для определения результата игры
def team_play(score):
    if score > LOSESCORE:
        if score > NOTHINGSCORE:
            print('Был выигрыш')
        else:
            print('Была ничья')
    else:
        print('Проиграла')

#Функция для определения площади круга и квадрата
def square_of_figures(r,a):
    s_of_square = a**2
    s_of_circle = math.pi*(r**2)
    if s_of_circle > s_of_square and s_of_square < s_of_circle:
        print('Площадь круга',s_of_circle,'больше площади квадрата',s_of_square)
    if s_of_circle < s_of_square and s_of_square > s_of_circle:
        print('Площадь круга', s_of_circle, 'меньше площади квадрата', s_of_square)
    if s_of_circle == s_of_square and s_of_square == s_of_circle:
        print('Площадь круга', s_of_circle, 'равна площади квадрата', s_of_square)

#Функция сравнения трех чисел
def compare_of_number(a,b,c):
    d = a+b+c
    if d//100>0:
        print('Сумма чисел',a,b,c,' равна', d,'и это не двузначное число')
    if d//100==0:
        print('Сумма чисел',a,b,c,' равна', d,'и это двузначное число')
    if a<d:
        print('Cуммa цифр a,b,c',a,b,c,'равное',d,'больше числа a =',a)
    if a > d:
        print('Cуммa цифр a,b,c', a, b, c, 'равное', d, 'меньше число a =', a)
#Вызваем функции с передачей исходной температуры (задача 2)
celcuis_to_fahrenheit(CELCIUS)
celcuis_to_kelvin(CELCIUS)
#Вызваем функции с передачей радиуса и стороной квадрата (задача 4)
circle_and_square(8,6)
circle_and_square(6,20)
#Вызваем функции с передачей значения очков (самостоятельная работа)
team_play(3)
team_play(1)
team_play(0)
#Вызваем функции с передачей значения ралиуса и квадрата (самостоятельная работа)
square_of_figures(2,2)
square_of_figures(1,2)
square_of_figures(1,3)
square_of_figures(0,0)
#Вызваем функции с передачей значения трех чисел (самостоятельная работа)
compare_of_number(20,1,9)
