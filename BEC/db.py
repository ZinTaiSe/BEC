import sqlite3

db = sqlite3.connect("energy.db")
sql = db.cursor()


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
