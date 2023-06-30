# На столе лежат n монеток. Некоторые из них лежат вверх решкой, 
# а некоторые – гербом. Определите минимальное число монеток, 
# которые нужно перевернуть, чтобы все монетки были повернуты вверх одной и той же стороной. 
# Выведите минимальное количество монет, которые нужно перевернуть

from random import randint
n = int(input("Введите количество монет: "))
list_1=[randint(0,1) for i in range(n)]
print(list_1)
list_1.sort()
reshka=0
orel=0
for i in range (len(list_1)):
    if list_1[i]==0:
        reshka+=1
    else:
        orel+=1
print(list_1)
print()
print(f'{reshka= } {orel= }')
if reshka>orel:
    print(f"Нужно перевернуть минимум {orel} монет")
else:
    print(f"Нужно перевернуть минимум {reshka} монет")


