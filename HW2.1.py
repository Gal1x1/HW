# Создать список и заполнить его элементами различных типов данных.
# Реализовать скрипт проверки типа данных каждого элемента
# Использовать функцию type() для проверки типа.
# Элементы списка можно не запрашивать у пользователя, а указать явно, в программе.

text = input("Insert text - ")
integer = int(input("Insert integer - "))
decimal = float(input("Insert decimal - "))
ls = [text, integer, decimal]
print (ls)
for x in ls:
    print(f"{x} - {type(x)}")