# Задача 12: 
# Петя и Катя – брат и сестра. Петя – студент,
# а Катя – школьница. Петя помогает Кате по математике. 
# Он задумывает два натуральных числа X и Y (X,Y≤1000), 
# а Катя должна их отгадать. Для этого Петя делает две подсказки. 
# Он называет сумму этих чисел S и их произведение P.                                                                                                                                                        Помогите Кате отгадать задуманные Петей числа.

s = int(input("Введите сумму чисел X и Y: "))
p = int(input("Введите произведение чисел X и Y: "))

for x in range(1, 1001):
    y = s - x
    if x * y == p:
        print("Число X =", x)
        print("Число Y =", y)
        break
else:
    print("Такие числа X и Y не существуют.")