from datetime import datetime, timedelta

def get_birthdays_per_week(users):
    today = datetime.now().date()
    next_week = today + timedelta(days=7)
    weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    birthdays = {day: [] for day in weekdays}
    for user in users:
        birthday = user['birthday'].date()
        if birthday >= today and birthday < next_week:
            if birthday.weekday() == 5 or birthday.weekday() == 6:
                birthdays['Monday'].append(user['name'])
            else:
                day = weekdays[birthday.weekday()]
                birthdays[day].append(user['name'])
    for day in weekdays:
        if birthdays[day]:
            names = ', '.join(birthdays[day])
            print(f'{day}: {names}')