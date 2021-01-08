from datetime import datetime
from application.DB.people import get_employees
from application.salary import calculate_salary



def main_salary():
    a = get_employees()
    b = calculate_salary()
    return a, b


def main_menu():
    d = datetime.now()
    dn = d.strftime('%x %X')
    print(f'На {dn} можно узнать:')
    print('Список сотрудников нажмите С \nСписок годовых зарплат нажмите S \n'
          'Общий список нажмите O \nДля выхода нажмите Q')
    while True:
        user_input = input('Введите команду:')
        if user_input == 'c':
            print(get_employees())
        elif user_input == 's':
            print(calculate_salary())
        elif user_input == 'o':
            print(main_salary())
        elif user_input == 'q':
            print('Bye, bye!')
            break


main_menu()