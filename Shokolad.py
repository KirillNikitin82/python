#  Требуется определить,
# можно ли от шоколадки размером n × m долек отломить k долек,
# если разрешается сделать один разлом по прямой между дольками
# (то есть разломить шоколадку на два прямоугольника).

# *Пример:*

# 3 2 4 -> yes
# 3 2 1 -> no
print("введите размеры шоколадки M*N долек ")
n = int(input("N: "))
m = int(input("M: "))
k = int(input("сколько долек отломить за один раз? "))
if (k % m == 0 and n * m > k) or (k % n == 0 and n * m > k):
    print(f"{n} {m} {k} -> YES")
else:
    print(f"{n} {m} {k} -> NO")
