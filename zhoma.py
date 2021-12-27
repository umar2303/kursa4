import sqlite3

db = sqlite3.connect('server.db')
sql = db.cursor()

sql.execute(""" CREATE TABLE IF NOT EXISTS ttovar (delivery TEXT)""")
sql.execute(""" CREATE TABLE IF NOT EXISTS ttovar2 (delivered TEXT)""")
db.commit()


def create():
    smth = input("Write tovar: ")
    sql.execute(f"SELECT delivery FROM ttovar WHERE delivery = '{smth}'")
    if sql.fetchone() is None:
        sql.execute(f"INSERT INTO ttovar VALUES (?,)", (smth))
        db.commit()
        print("Tovar was inserted")
    else:
        print('Tovar still inserted')


def find_tovar():
    smth = input("Write ttovar for searching: ")
    sql.execute(f"SELECT delivery FROM ttovar WHERE delivery = '{smth}'")
    if sql.fetchone() is not None:
        value = sql.execute(f"SELECT delivery FROM ttovar WHERE delivery = '{smth}'")
        print(f"Your tovar is in. Asnd it is {value}.")
    else:
        print("There isn't any tovar")


def take_delivery_tovar():
    for value in sql.execute(f"SELECT * FROM ttovar"):
        print(value[0])


def take_delivered_tovar():
    for value in sql.execute(f"SELECT * FROM ttovar2"):
        print(value[0])


def dostavka():
    smth = input("write: ")
    sql.execute(f"SELECT delivery FROM ttovar WHERE delivery = '{smth}'")
    if sql.fetchone() is None:
        print(f"There isn't any {smth}")
    else:
        sql.execute(f"DELETE delivery FROM ttovar WHERE delivery = '{smth}'")
        sql.execute(f"INSERT INTO ttovar2 VALUES (?, ?)", (smth))
        print("delivered")


def count4():
    k = 0
    for value in sql.execute(f"SELECT * FROM ttovar2"):
        k += 1
    print(k)


def count5():
    k = 0
    for value in sql.execute(f"SELECT * FROM ttovar"):
        k += 1
    print(k)


def menu():
    while True:
        try:
            global k
            k = int(input(
                "Приветствую дорогой, Ремонтник!\nПожалуйста наберите номер меню для работы с программой, если закончили, то наберите 7:\n"
                "1. Сделать ремонт.\n"
                "2. Сделать замену\n"
                "3.Сделать обслуживаниe.\n"
                "4. Выполнить заказ запчастей.\n"
                "5.Посмотреть список заказанного оборудование. \n"
                "6.Удалить запчасть "
                "7.Выход.\n"
                "==> "))
            if k == 1:
                take_delivery_tovar()
            elif k == 2:
                take_delivered_tovar()
            elif k == 3:
                dostavka()
            elif k == 4:
                count4()
            elif k == 5:
                count5()
            else:
                print("i dont now it")

        except Exception as e:
            print(repr(e))