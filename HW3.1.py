# Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
# Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.


def divide(a, b):
    if b == 0:
        print("Can't divide by zero")
    return a / b
print(divide(int(input("Insert 1.arg: ")), int(input("Insert 2.arg: "))))

