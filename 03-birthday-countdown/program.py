import datetime

def print_header():

    print('--------------------------------------------------')
    print('               BIRTHDAY COUNTDOWN')
    print('--------------------------------------------------')


def get_birthday():

    print('When were you born?')
    year = int(input('Year [YYYY]: '))
    month = int(input('Month [MM]: '))
    day = int(input('Day [DD]: '))

    birthday = datetime.date(year, month, day)

    return birthday


def compute_days_between_dates(original_date, target_date):

    current_year = datetime.date(target_date.year, original_date.month, original_date.day)
    dt = current_year - target_date

    return dt.days


def print_birthday_info(days):

    if days < 0:
        print('You had your birthday {} days ago'.format(-days))
    elif days > 0:
        print('Your birthday is in {} days!'.format(days))
    else:
        print('Happy birthday!!!')


def main():

    print_header()
    bday = get_birthday()
    print(bday)
    today = datetime.date.today()
    num_days = compute_days_between_dates(bday, today)
    print_birthday_info(num_days)


main()