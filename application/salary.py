if __name__ == '__main__':
    print('ТУТ СЧИТАЕМ ЗАРПЛАТУ')

SALARY_BY_POST = {'Директор': 1500, '1ый уровень': 800, '2ой уровень': 1100, '3ий уровень': 1300}

def calculate_salary():
    SALARY = dict()
    for POST in SALARY_BY_POST:
        SALARY[POST] = SALARY_BY_POST[POST] * 12
    return SALARY