# Продолжить работу над заданием.
# В программу должна попадать строка из слов, разделенных пробелом.
# Каждое слово состоит из латинских букв в нижнем регистре.
# Сделать вывод исходной строки, но каждое слово должно начинаться с заглавной буквы.
# Необходимо использовать написанную ранее функцию int_func().

def int_func(a):
    return str.title(a)
print(int_func(a = input('Insert lowercase text -> ')))

b = input('Insert another lowercase text -> ').split()
print(str.title(' '.join(b)))
from dill.source import getsource
print(getsource(int_func(a)))

