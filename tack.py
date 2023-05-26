#Поиск чисел
festNumber=int(input("Загадай первое натуральное- число >    "))
secondNumber=int(input("Загадай второе число больше 999->  "))
check=bool
while(check):
    if secondNumber<999 or festNumber<1:
        festNumber=int(input("Загадай повторно первое число больше нуля-> "))
        secondNumber=int(input("Загадай повторно второе число больше 999-> "))
    else:
        check=False
summTwoNumbers=festNumber+secondNumber
produktTwoNumbrs=festNumber*secondNumber
print(f"Подсказка, чтобы угадать два числа:")
print(f"Сумма этих чисел равна {summTwoNumbers }")
print(f"Произведение этих чисел равно {produktTwoNumbrs}")
print(f"Чтобы найти эти два числа , надо составить уравнение\n x+y={summTwoNumbers} и х*у={produktTwoNumbrs}")
print(f"Два урвнения можно представить как квадратное -> уу-{summTwoNumbers}у+{produktTwoNumbrs}=0 и решать через дисременант")
discriminant=summTwoNumbers**2-4*produktTwoNumbrs
import math
if discriminant>0:
    number1=int((summTwoNumbers- math.sqrt(discriminant))/2)
    number2=int((summTwoNumbers+ math.sqrt(discriminant))/2)
    print(f"Первое число равно {number1} , второе число равно {number2}")
elif discriminant==0:
    number=int((summTwoNumbers)/2)
    print(f"Первое число равно {number} , второе число равно {number}")
else:
    print(f"Не получаетя найти ответ")
# Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.
numberN=int(input("Введите число до которго посчтитаь степень двойки"))
i=0
while 2**i<=numberN:
    
    print(i)
    i+=1
