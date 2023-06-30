# Иван Васильевич пришел на рынок и решил купить два арбуза:
# один для себя, а другой для тещи. Понятно,
# что для себя нужно выбрать арбуз потяжелей,
# а для тещи полегче. Но вот незадача: арбузов
# слишком много и он не знает как же выбрать самый
# легкий и самый тяжелый арбуз? Помогите ему!
from random import randint

n = int(input("введите число: "))
weight = 0
# max_ = 0
# min_ = 20
max_ = float("-inf")
min_ = float("inf")
for _ in range(n):
    weight = randint(1, 80)
    if weight > max_:
        max_ = weight
    if weight < min_:
        min_ = weight
    print(weight, end=" ")
# print(f"min={min_},max={max_}")
print(f"\n{max_=} {min_=}")
