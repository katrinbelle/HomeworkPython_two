# Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.
numberN=int(input("Введите число до которго посчтитаь степень двойки"))
i=0
while 2**i<=numberN:
    
    print(i)
    i+=1