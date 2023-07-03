# Даны два массива чисел. Требуется вывести те элементы первого массива 
# (в том порядке, в каком они идут в первом массиве), которых нет во втором массиве. 
# Пользователь вводит число N - количество элементов в первом массиве, 
# затем N чисел - элементы массива. Затем число M - количество элементов во 
# втором массиве. Затем элементы второго массива

from random import randint
my_list_1 = [randint(0, 20) for _ in range(int(input("Введите количество элементов 1: ")))]
my_list_2 = [randint(0, 20) for _ in range(int(input("Введите количество элементов 2: ")))]

print(list_3 := [item for item in my_list_1 if item not in my_list_2])