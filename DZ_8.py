import datetime
# список словників
# datetime.datetime(1997, 8, 11) - створює об'єкт з конкретною датою 1997рік 08місяць 11день
USERS = [
    {
        'name': 'VOLDEMAR',
        'datetime': datetime.datetime(1990, 8, 3)
    },
    {
        'name': 'BILL',
        'datetime': datetime.datetime(1990, 8, 4)
    },
    {
        'name': 'KAIL',
        'datetime': datetime.datetime(1990, 8, 4)
    },
    {
        'name': 'PAUL',
        'datetime': datetime.datetime(1991, 8, 5)
    },
    {
        'name': 'MICKLE',
        'datetime': datetime.datetime(1992, 8, 6)
    },
    {
        'name': 'MARRY',
        'datetime': datetime.datetime(2002, 8, 6)
    },
    {
        'name': 'ZOI',
        'datetime': datetime.datetime(1993, 8, 7)
    },
    {
        'name': 'MARGARET',
        'datetime': datetime.datetime(1994, 8, 8)
    },
    {
        'name': 'JIM',
        'datetime': datetime.datetime(1995, 8, 9)
    },
    {
        'name': 'KIM',
        'datetime': datetime.datetime(1996, 8, 10)
    },
    {
        'name': 'TOM',
        'datetime': datetime.datetime(1997, 8, 11)
    },
    {
        'name': 'JAMES',
        'datetime': datetime.datetime(1997, 8, 11)
    },
]


def get_birthdays_per_week(users):
    # назви днів тижня по порядку
    days_of_week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    # поточна дата
    day = datetime.date.today()
    # дата кінці тижня
    end_day = day + datetime.timedelta(days=7)
    # пустий список імен що день народження на вихідних
    weekend_list = []
    # пустий список дня народжнення в будні дні
    day_list = []
    # цикл : поки поточний день менше ріне останньому дню
    while day <= end_day:
        # випадок : якщо день тижня - субота, неділя
        if day.weekday() in [5,6]:
            # цикл : обходимо список
            for user in users:
                # випадок : день і місяць співпадають
                if user['datetime'].month == day.month and user['datetime'].day == day.day:
                    # додаємо в список вихідного дня
                    weekend_list.append(user['name'])   
        # випадок : день тижня не вихідний
        else:
            # цикл : обходимо список
            for user in users:
                # випадок : день і місяць співпадають
                if user['datetime'].month == day.month and user['datetime'].day == day.day:
                    # додаємо в список звичайного дня
                    day_list.append(user['name'])
            # випадок : понеділок
            if  day.weekday() == 0:
                # приєднуємо список тих у кого в вихідний день
                day_list = weekend_list + day_list
                weekend_list = []
            # випадок : якщо у списку є імена
            if day_list:
                # виводимо день : імена
                print(f'{days_of_week[day.weekday()]}:',*day_list)
            # очищаємо список
            day_list = []
        # + 1 день до поточного
        day = day + datetime.timedelta(days=1)


if __name__ == "__main__":
    get_birthdays_per_week(USERS)
