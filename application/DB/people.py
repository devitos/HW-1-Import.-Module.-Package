if __name__ == '__main__':
    print('ТУТ ВЫВОДИМ СПИСОК СОТРУДНИКОВ')


employees = {'ПЕТР': 'Директор', 'ИВАН': '1ый уровень', 'КСЕНИЯ': '2ой уровень', 'АЛЕКСАНДР': '2ой уровень',
                   'СЕРГЕЙ': '3ий уровень'}


def get_employees():
    NAME_list = list()
    for NAME in employees:
        NAME_list.append(NAME)
    return NAME_list

