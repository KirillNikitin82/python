# Найдите сумму цифр трехзначного числа.
# *Пример:*
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0) |

num= input('введите число :')
# if num.__len__!=2:
#     print("введите трехзначное число")
#     raise SystemExit

a=int (num[0])
b=int (num[1])
c=int (num[2])
sum=a+b+c

print (num," -> ",sum,"(",num[0],"+",num[1],"+",num[2],")") 

