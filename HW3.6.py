# Реализовать функцию int_func(), принимающую слово из маленьких латинских букв и возвращающую его же,
# но с прописной первой буквой. Например, print(int_func(‘text’)) -> Text.

def int_func(a):
    return str.title(a)
print(int_func(a = input('Insert lowercase text -> ')))