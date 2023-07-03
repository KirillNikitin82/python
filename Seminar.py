##Последовательностью Фибоначи называется последовательность чисел
##а0, а1, ...,аn, ..., где а0=0, а1=1, ak = (ak-1) + (ak-2), где k>1
##Требуется найти N= число Фибоначи

def Fibo_index(n):
    if n in [1,2]:
        return 1
    return Fibo_index(n-1)+Fibo_index(n-2)
print (Fibo_index(8))

