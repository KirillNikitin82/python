##Дано натуральное число N и последовательность из N элементов.
##Требуется вывести эту последовательность в обратном порядкею
##В программе запрещается объявлять массивы и использовать циклы даже для ввода и вывода.

number = int(input("Введите число:"))

##def revers(num):
##    print(num)
##    if num == 0:
##        return
##    else:
##        revers(num-1)
##
##print(revers(number))

stroka =""

def razvorot(num: int):
    if num==0:
        return ""
    char = input("Введите что-то: ")
    return razvorot(num-1) + char

print(razvorot(number))