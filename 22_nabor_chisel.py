# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями).
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n — кол-во элементов первого множества.
# m — кол-во элементов второго множества. Затем пользователь вводит сами элементы множеств.
from random import randint

numberN = int(input("Введите количество элементов первого множества: "))
numberM = int(input("Введите количество элементов второго множества: "))

list_1 = [randint(0,9) for _ in range(numberN)]
list_2 = [randint(0,9) for _ in range(numberM)]

print(list_1)
print(list_2)

##list_3=[]
##
##for i in range(len(list_1)):
##    for j in range(len(list_2)):
##        if list_1[i] == list_2[j]:
##            list_3.append(list_1[i])

list_3 = [elem for elem in list_1 if elem not in list_2]

print(list_3)

##print(sorted(set(list_1)&set(list_2)))
