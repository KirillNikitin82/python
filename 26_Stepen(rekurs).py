##Напищите программу, которая на вход принимает два числа A и В,
##и возводит число А в целую степень В с помощью рекурсии.

number1= int(input("Введите число: "))
number2= int(input("Введите степень числа: "))

def multinumber(num1: int, num2: int) -> int:
    if num2 == 0:
        return 1
    else:
        res = num1*multinumber(num1, num2-1)
        return res

print(multinumber(number1, number2))