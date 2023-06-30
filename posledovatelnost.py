# Дана последовательность из N целых чисел
# и число К. Необходимо сдвинуть всю
# последовательность (сдвиг циклический)
# на К элементов вправо (К-положительное число)
from random import randint
print(my_list := [randint(0, 20) for _ in range(10)])
k = int(input("Введите на сколько сдвинуть"))
# my_list_2 = []
# for i in range(len(my_list) - k):
#     a = my_list.pop(0)
#     my_list_2.append(a)
# for j in range(len(my_list)):
#     my_list_2.insert(j, my_list[j])
# print(my_list_2)

for i in range(len(my_list)):
    print(my_list[(i-k)%len(my_list)], end=" ")
print()

print(str(my_list[-k:] + my_list[:-k]))

for _ in range(k):
    my_list.insert(0, my_list.pop())
print(my_list)
