# Определить, является ли год, который ввел пользователь, високосным или не високосным.
import datetime
year  = int(input('Введите год: '))
date1 = datetime.date(year, 3, 1)
date2 = date1 - datetime.timedelta(days=1)
if date2.day == 29:
    print(f"Високосный ({date2})")
else:
    print("Обычный")