# Задача 32: Определить индексы элементов массива (списка), 
# значения которых принадлежат заданному диапазону 
# (т.е. не меньше заданного и не больше заданного максимума)

from random import randint

list_1 = [randint(1,10) for i in range(10)]
print(list_1)

minn = int(input("Введите минимум: "))
maxx = int(input("и максимум: "))
# list_2=[]
# for i in range(len(list_1)):
#     if maxx > list_1[i] > minn:
#         list_2.append(i)

list_2 = [i for i in range(len(list_1)) if maxx > list_1[i] > minn]
print(f"Элементы входящие в диапазон имеют следующие значения индексов: {list_2}")        