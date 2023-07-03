##Последовательностью Фибоначи называется последовательность чисел
##а0, а1, ...,аn, ..., где а0=0, а1=1, ak = (ak-1) + (ak-2), где k>1
##Требуется найти N= число Фибоначи

def Fibo_number(n):
    if n in [1,2]:
        return 1
    return Fibo_number(n-1)+Fibo_number(n-2)

n = int(input("Введите номер числа фибоначи"))
print (Fibo_number(n))

