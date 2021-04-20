# Реализовать функцию my_func(), которая принимает три позиционных аргумента,
# и возвращает сумму наибольших двух аргументов.

def my_func(a, b, c):
    funclist = [a, b, c]
    try:
        funclist.remove(min(funclist))
        return sum(funclist)
    except TypeError:
        return "Insert numbers"
print(my_func(1, 2, 3))
