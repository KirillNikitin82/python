# Дан массив, состоящий из целых чисел. Напишите программу, 
# которая в данном массиве определит количество элементов, 
# у которых два соседних и, при этом, оба соседних элемента меньше данного. 
# Сначала вводится число N — количество элементов в массиве 
# Далее записаны N чисел — элементы массива. Массив состоит из целых чисел.
from random import randint
print(list_1 := [randint(0, 20) for _ in range(int(input("Введите количество элементов 1: ")))])
print(len([i for i in range(1, len(list_1)-1) if list_1[i-1] < list_1[i] > list_1[i+1]]))