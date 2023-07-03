##Задача 28: Напишите рекурсивную функцию sum(a, b),
##возвращающую сумму двух целых неотрицательных чисел.
##Из всех арифметических операций допускаются только +1 и -1.
##Также нельзя использовать циклы.

def summa(num1: int, num2: int) -> int:
    if num2 == 0:
        return num1
    else:
        return summa(num1+1, num2-1)

number1 = int(input("Введите первое число: "))
number2 = int(input("Введите второе число: "))
print(summa(number1, number2))