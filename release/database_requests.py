import sqlite3

"""
        Данный модуль реализует функции для генерации запросов к базе данных
"""


def add_data_to_db(db: str, table: str, columns: (list, tuple), values: (list, tuple)) -> None:
    """
    :param db: Используемая база данных
    :param table: Таблица, в которую вставлять новые значения
    :param columns: Список колонок, в которые надо вставлять значения
    :param values: Список вставляемых значений
    :return: None
    """

    con = sqlite3.connect(db)
    cur = con.cursor()

    request = f"""INSERT INTO {table}({', '.join(columns)}) VALUES ({", ".join(values)})"""
    print(request)
    cur.execute(request)

    con.commit()
    con.close()
    print('added')


def update_data_in_db(db: str, table: str, update_data: dict, conditions: dict) -> None:
    """
    :param db: Используемая база данных
    :param table: Таблица, в которой обновляются значения
    :param update_data: Словарь обновляемых значений вида: <Ключ> = <Значение>
    :param conditions: Словарь условий обновления строк вида: <Ключ> = <Значение>
    :return: None
    """

    con = sqlite3.connect(db)
    cur = con.cursor()

    # Создание запроса, основываясь на параметрах функции
    request = f"""UPDATE {table} SET """
    for column, value in update_data.items():
        request += f"{column} = {value}, "
    request = request[:-2] + (" WHERE " if conditions else "")

    for column, value in conditions.items():
        request += f"{column} = '{value}' AND "
    request = request[:-5]
    #

    print(request)
    cur.execute(request)

    con.commit()
    con.close()
    print('updated')


def delete_data_from_db(db: str, table: str, conditions: dict, not_fl=False) -> None:
    """
    :param db: Используемая база данных
    :param table: Таблица, в которой удаляются значения
    :param conditions: Словарь условий удаления строк вида: <Ключ> IN <Значение>
    :param not_fl: Флажок, обозначающий нужно ли добавлять NOT перед условиями сравнения
    :return: None
    """

    con = sqlite3.connect(db)
    cur = con.cursor()

    request = f"""DELETE FROM {table}{' WHERE ' if conditions else ''}"""

    # Создание запроса, основываясь на параметрах функции
    for column, value in conditions.items():
        request += f"""{column}{' NOT' if not_fl else ''} IN ('{"', '".join(value)}') AND """
    if conditions:
        request = request[:-5]
    #

    print(request)
    cur.execute(request)

    con.commit()
    con.close()
    print('deleted')


def get_data_from_db(db: str, table: str, columns: str,
                     conditions_equal=None, conditions_like=None, ordering=None,
                     is_distinct=False) -> list:
    """
    :param db: Используемая база данных
    :param table: Таблица, из которой достются данные
    :param columns: Строка колонок, которые необходимо возвращать
    :param conditions_equal: Словарь условий сравнения вида. Сравнение: <Ключ> IN <Значение>
    :param conditions_like: Словарь условий сравнения вида. Сравнение: <Ключ> LIKE <Значение>
    :param ordering: Словарь условий сортировки. Сортировка <Ключ> <Значение>,
                     в качестве значения выступает тип сортировки: 0 (ASC) или 1 (DESC)
    :param is_distinct: Необходимость выбора только неповторяющихся колонок
    :return: Возвращает список кортежей с выбранной информацией
    """

    con = sqlite3.connect(db)
    cur = con.cursor()

    # Создание запроса, основываясь на параметрах функции
    request = f"""SELECT {'DISTINCT ' if is_distinct else ''}{columns} FROM {table}"""

    if conditions_equal:
        request += " WHERE "
        for column, value in conditions_equal.items():
            request += f"""{column} IN ('{"', '".join(value)}') AND """
        request = request[:-5]

    if conditions_like:
        request += f" {'AND' if conditions_equal else 'WHERE'} "
        for column, value in conditions_like.items():
            request += f"{column} LIKE '{value}' OR "
        request = request[:-4]

    if ordering:
        request += ' ORDER BY '
        for column, order_type in ordering.items():
            request += f"{column} {'ASC' if order_type == 0 else 'DESC'}, "
        request = request[:-2]
    #

    print(request)
    res = cur.execute(request).fetchall()

    con.close()

    return res


if __name__ == '__main__':
    ####
    # !!! Внимание, данный код моежт изменить состояние базы данных, запускать только осознанно !!!
    print(*get_data_from_db('clients.db', 'clients', '*', conditions_like={'name': '%уко%'},
                            ordering={'name': 0}), sep='\n')
    dates = get_data_from_db('clients.db', 'payments_table', 'id, date')

    for cl_id, cl_date in dates:
        d_info = '.'.join(map(lambda x: x.rjust(2, '0'), cl_date.split('.')[::-1]))
        update_data_in_db('clients.db', 'payments_table', {'date': f"'{d_info}'"}, {'id': cl_id})
    ####
