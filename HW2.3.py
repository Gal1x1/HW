# Пользователь вводит месяц в виде целого числа от 1 до 12.
# Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
# Напишите решения через list и через dict.

# month = int(input("Insert month - "))
# if month.isdigit() and 0 <= month <= 12:
# seasons = {'зима': 12, 1, 2, 'весна': 3, 4, 5, 'лето': 6, 7, 8, 'осень': 9, 10, 11}
# if month == i from seasons.values(1)
# print(seasons.keys(1))
# # print(seasons.keys())
# # seasons.values()
# хотела вызвать из множества лист и с каждым списком сравнить, но не получалось

while True:
    user_month = int(input("Insert month - "))
    if month.isdigit() and 0 <= month <= 12:
        season_1 = ['зима', 'весна', 'лето', 'осень', 'зима']
        season_2 = {0: 'зима', 1: 'весна', 2: 'лето', 3: 'осень', 4: 'зима'}
        print(f'Season list - {season_1[user_month]) // 3]}\nSeason list -  {season_2[user_month]} // 3]}')
        break
    else:
        print('Error')
# почему когда run, тогда пишет f-string: unmatched?