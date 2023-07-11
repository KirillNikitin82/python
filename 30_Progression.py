# Задача 30:  Заполните массив элементами арифметической прогрессии. 
# Её первый элемент, разность и количество элементов нужно ввести с клавиатуры. 
# Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.

elems = int(input("Введите первый элемент: "))
steps = int(input("Введите шаг: "))
lenns = int(input("Введите количество элементов: "))


print(res := [elems + i * steps for i in range(lenns)])

# res=[]
# res.append(elems)
# for _ in range(lenns-1):
#     elems+=steps
#     res.append(elems)
# print(res)


