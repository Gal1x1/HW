# Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя:
# имя, фамилия, год рождения, город проживания, email, телефон.
# Функция должна принимать параметры как именованные аргументы.
# Реализовать вывод данных о пользователе одной строкой.

def userdata(q, w, e, r, t, z):
    return q+w+e+r+t+z
print(input("Insert full name: "), input("Insert surname: "), input("Insert date of birth: "),
                 input("Insert residence: "), input("Insert email: "), input("Insert phone num: "))
print("ok,thnx")