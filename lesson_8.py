from datetime import datetime, timedelta, date
from collections import defaultdict
from pprint import pprint


def get_next_week_start(d: datetime):
    diff_days = 7 - d.weekday()
    return d + timedelta(days=diff_days)


def prepare_birthday(text: str):
    bd = datetime.strptime(text, '%d , %m , %Y')
    return bd.replace(year=datetime.now().year).date()


def get_birthdays_per_week(users):
    birthdays = defaultdict(list)

    today = datetime.now().date()

    next_week_start = get_next_week_start(today)
    start_period = next_week_start - timedelta(2)
    end_period = next_week_start + timedelta(4)

    happy_users = [user for user in users if start_period <= prepare_birthday(user['birthday']) <= end_period]

    for user in happy_users:
        current_bd = prepare_birthday(user['birthday'])
        if current_bd.weekday() in (5, 6):
            birthdays['Monday'].append(users['name'])
        else:
            birthdays[current_bd.strftime('%A')].append(user['name'])
    return birthdays


if __name__ == "__main__":
    users = [{"name": "Koky", "birthday": "15 , 4 , 1997"},
             {"name": "Rok", "birthday": "25 , 12 , 1999"},
             {"name": "Filok", "birthday": "5 , 4 , 1991"},
             {"name": "Reka", "birthday": "8 , 10 , 1990"},
             {"name": "Koka", "birthday": "30 , 4 , 2003"},
             {"name": "Slok", "birthday": "21 , 5 , 1985"},
             {"name": "Hoker", "birthday": "22 , 3 , 1988"},
             {"name": "Skok", "birthday": "22 , 3 , 2002"}]

    result = get_birthdays_per_week(users)

    pprint(result)
