# Для списка реализовать обмен значений соседних элементов, т.е.
# Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
# При нечетном количестве элементов последний сохранить на своем месте.
# Для заполнения списка элементов необходимо использовать функцию input().

el = input('Insert elements - ').split()
for x in range(1, len(el), 2):
    el.insert(x - 1, el.pop(x))
print(el)
# EV
# a = input('Insert elements - ').split()
# i = 0
# print(f'original list {a}')
# while i + 1 < len(a):
# if i % 2 == 0:
# a.insert(i, a.pop(i+1))
# i += 1
# print(f'changed list {a}')
#
# listx = list(input('Insert elements - '))
# for i in range(1, len(listx, 2):
#     listx[i - 1], listx[i] = listx[i], list[i - 1]
#     print(listx)