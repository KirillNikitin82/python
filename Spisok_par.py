# Дан список чисел. Посчитайте, сколько в нем пар элементов, 
# равных друг другу. Считается, что любые два элемента, 
# равные друг другу образуют одну пару, которую необходимо посчитать. 
# Вводится список чисел. Все числа списка находятся на разных строках.

from random import randint
print(sorted(list_1 := [randint(0, 7) for _ in range(int(input("Введите количество элементов 1: ")))]))

list_2 = []
for i in range(len(list_1)-1):    
    if list_1[i] == list_1[i+1]:
        list_2.append(list_1[i])

print(len(set(list_2)))
