# Дан массив, состоящий из целых чисел.
# Напишите программу, которая подсчитает
# количество элементов массива, больших
# предыдущего (элемента с предыдущим номером)

from random import randint

print(my_list := [randint(0, 20) for _ in range(10)])
# count = 0
# for i in range(len(my_list) - 1):
#     if (my_list[i] > my_list[i + 1]):
#         count += 1
# print(f"Кол-во элементов больше предыдущего = {count}")

print(len([i for i in range(1, len(my_list)) if my_list[i-1]<my_list[i]]))