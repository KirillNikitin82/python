##Напишите функцию, которая принимает одно число и проверяет является ли оно простым.



##def Proverka (a):
##    for i in range(2, a):
##        if a % i == 0:
##            return "Число составное"
##        return "Число простое"



def Is_simple(num: int) -> bool:
    if num in (1,2):
        return True
    if num % 2 == 0:
        return False
    for div in range(3, int(num**0.5)+1,2):
        if num % div == 0:
            return False
    return True

n = int(input("Введите число: "))
print(Is_simple(n))