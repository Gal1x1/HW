# Программа запрашивает у пользователя строку чисел, разделенных пробелом.
# При нажатии Enter должна выводиться сумма чисел.
# Пользователь может продолжить ввод чисел, разделенных пробелом и снова нажать Enter.
# Сумма вновь введенных чисел будет добавляться к уже подсчитанной сумме.
# Но если вместо числа вводится специальный символ, выполнение программы завершается.
# Если специальный символ введен после нескольких чисел,
# то вначале нужно добавить сумму этих чисел к полученной ранее сумме и после этого завершить программу.


def funct():
    a = 0
    while True:
        list_a = input("Insert arguments: ").split( )
        for num in list_a:
            if num == str():
                return a
            else:
                try:
                    a += int(num)
                except ValueError:
                    print('Exit with a letter')

        print(f'Sum is {a}')
funct()