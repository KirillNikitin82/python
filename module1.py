##def sum_numbers(n):
##    sum_=0
##    for i in range (1, n+1):
##        sum_+=i
##    return sum_
##
##n=int(input("Введите число "))
##print(sum_numbers(n))

##def sum_str(*args):
##    res = 0
##    for i in args:
##        res += i
##    return res
####print(sum_str("|","r","d","d"))
##print(int(sum_str(3, 4, 5)))

##import module_max as mm
##
##print(mm.max1(5, 9))

##def fib(n):
##    if n in [1,2]:
##        return 1
##    return fib(n-1)+fib(n-2)
##
##list_1=[]
##for i in range(1, 10):
##    list_1.append(fib(i))
##print(list_1)

##def quick_sort(array):
##    if len(array)<=1:
##        return array
##    else:
##        pivor = array[0]
##        less=[i for i in array[1:] if i <= pivor]
##        greater = [i for i in array[1:] if i > pivor]
##    return quick_sort(less) + [pivor] + quick_sort(greater)
##
##arr=[23,43,2,345,5,67,9,0,3,32]
##print(quick_sort(arr))

def merge_sort(nums):
    if len(nums)>1:
        mid = len(nums)//2
        left = nums[ : mid]
        right = nums[mid : ]
        merge_sort(left)
        merge_sort(right)
        i=j=k=0
        while i< len(left) and j<len(right):
            if left[i] < right[j]:
                nums[k] = left[i]
                i+=1
            else:
                nums[k] = right[j]
                j+=1
            k += 1
        while i < len(left):
            nums[k] = left[i]
            i+=1
            k+=1
        while j < len(right):
            nums[k] = right[j]
            j += 1
            k += 1

numbers = [22,34,56,788,5,4,3,21,3,4,67]
merge_sort(numbers)
print (numbers)







