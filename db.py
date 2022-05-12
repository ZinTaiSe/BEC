from style import db_ex as d
import sqlite3
import os

db = sqlite3.connect("energy.db")
sql = db.cursor()


def create_some_data():
    sql.execute("CREATE TABLE IF NOT EXISTS energy ("
                "id INT,"
                "time DATE,"
                "address TEXT,"
                "photo TEXT,"
                "person TEXT)")
    sql.execute("DELETE FROM energy")
    for val in d:
        sql.execute(f"INSERT INTO energy VALUES (?, ?, ?, ?, ?)", (val[0], val[1], val[2], val[3], val[4]))
    db.commit()


def show_data():
    list_of_contents = list()
    for value in sql.execute("SELECT * FROM energy"):
        list_of_contents.append(value)
    return list_of_contents


def sort_by_date():
    data = show_data()
    list_of_contents = list()
    temp_list = list()

    for value in data:
        temp = value[1].split()[0].split(".")
        temp_list.append(int(temp[2]+temp[1]+temp[0]))

    for i in range(len(temp_list)):
        index = temp_list.index(max(temp_list))
        list_of_contents.append(index)
        temp_list.pop(index)
        temp_list.insert(index, 0)
    temp_list.clear()

    for i in list_of_contents:
        temp_list.append(show_data()[i])

    return temp_list


def sort_by_person():
    data = show_data()
    temp_list = list()

    for item in data:
        person = item[4]
        for it in data:
            if person in it[4]:
                temp_list.append(it)
                data.remove(it)

    temp_list.append(data[0])
    return temp_list


def data_for_person(name):
    data = show_data()
    list_of_contents = list()
    for element in data:
        if name.text() == element[4]:
            list_of_contents.append(element)

    return list_of_contents


def check_new_data():
    values = list()
    for value in os.listdir("img"):
        values.append(value)
    for value in show_data():
        if value[3] in values:
            values.pop(values.index(value[3]))
    if len(values) != 0:
        create_some_data()
