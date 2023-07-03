##Хантер Василий получил доступ к классному журналуи хочет заменить все свои минимальные оценки на максимальные.
##Напишите программу, которая заменяет оценки Василия, но наоборот: все максимальные - на минимальные.

from random import randint

books = [randint(1,5) for _ in range(8)]

print(books)

max_=max(books)
min_=min(books)

##for i in range(len(book)):
##    if book[i] == max_:
##        book[i] = min_
##print(book)

print([book if book != max_ else min_ for book in books])

