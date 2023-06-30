#Дан список чисел. Определите, сколько в нем
#встречается различных чисел.
from random import randint
# list_1=[randint(0,10) for i in range(8)]
# print(list_1, end=" ")
# count=1
# list_1.sort()
# print()
# print(list_1, end=" ")
# for i in range(len(list_1)-1):
#     if list_1[i]!=list_1[i+1]:
#         count+=1
# print(count)     
print(my_list := [randint(0,5) for _ in range(10)])
print(len(set(my_list)))