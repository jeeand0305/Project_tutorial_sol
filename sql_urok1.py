import sqlite3
import datetime
# db=""
#
# db = sqlite3.connect("db/database.db")
# cursor = db.cursor()
# query = """ CREATE TABLE IF NOT EXISTS \
# expenses(id INTEGER, name TEXT)"""
# cursor.execute(query)
# db.close()

# ______________________________________________
# #sozdal name stolbov v tablice
# with sqlite3.connect("db/database_zapas.db") as db:
#     curs = db.cursor()
#     query = """ CREATE TABLE IF NOT EXISTS \
#     expenses(id INTEGER, name TEXT)"""
#     curs.execute(query)
#

# ____________________________________________________
# # zapolnenie tablice
# with sqlite3.connect("db/database_zapas.db") as db:
#     curs = db.cursor()
#     # варианты записи в таблицу
#     query1 = """ INSERT INTO expenses \
#     (id, name) VALUES(1, "Коммуналка") """
#     query2 = """ INSERT INTO expenses \
#     (name, id) VALUES("Соляра", 1)"""
#     query3 = """ INSERT INTO expenses \
#     VALUES(3, "Интернет") """
#     curs.execute(query1)
#     curs.execute(query2)
#     curs.execute(query3)
#     # db.commit()

#  # создание новой таблицы
# with sqlite3.connect("db/database_zapas.db") as db:
#     curs = db.cursor()
#     query = """ CREATE TABLE IF NOT EXISTS payments(
#         id INTEGER,
#         amount REAL,
#         payment_date INTEGER,
#         expense_id INTEGER
#     )"""
#
#     curs.execute(query)
#     db.commit()

 # добовление столбца в существующую таблицу

# c.execute("alter table linksauthor add column '%s' 'float'" % author)
# alter - изменить
# table - таблицу
# linksauthor - название таблицы, которую менять
# add - добавить
# column - колонку
# '%s' - сюда будет подставлено название добавляемой колонки
# 'float' - тип добавляемой колонки - число с плавающей точкой
# % author - подставить название колонки из переменной author

# with sqlite3.connect("db/database.db") as db:
#     curs = db.cursor()
#     query = """ ALTER TABLE payments \
#     ADD Dop_stol_pro INTEGER;"""
#
#     curs.execute(query)
# #     db.commit()

# # заполнение таблице Dop_stol_pro
# #
# insert_payments = [
#     (1, 1),
#     (2, 2),
#     (3, 2),
#     (4, 4),
#     (5, 3),
#     (6, 2),
#     (7, 1)
# ]

# with sqlite3.connect("db/database.db") as db:
#     curs = db.cursor()
#  # переменая содается в ней есть столбцы
#     query = \
#         """DELETE FROM payments WHERE id = 2 """
#     curs.execute(query)
#     db.commit()


#  # upravlenie timengem
def taim_cod(y,m, d):
    return datetime.datetime.timestamp(datetime.datetime(y,m,d))

def get_date(tmsstamp):
    return datetime.datetime.fromtimestamp(tmsstamp).date()

# ________________________________________________
# #  variant1
# #  работа с таблицей пересчет
# with sqlite3.connect("db/database_zapas.db") as db:
#     curs = db.cursor()
#     query = """SELECT * FROM payments"""
#
#     curs.execute(query)
#     sum = 0
#     for res in curs:
# #  index slujit nomerom v stolbce
#         sum += res[1]
#         print(res)
#     print("TOTAL", sum)

# _________________________________________________
# #  variant2
# #  работа с таблицей пересчет данных с payments
# with sqlite3.connect("db/database_zapas.db") as db:
#     curs = db.cursor()
    #  берем данные из
    #  SELECT столбца  amount, payment_date
    #  перберает FROM payments
    #  ищем строки с номером 2
    # записываем WHERE expense_id = 2
#   # раз amount, payment_date то индекса всего 2
#     query = """
#     SELECT amount, payment_date
#     FROM payments
#     WHERE expense_id = 2"""
#
#     curs.execute(query)
#     sum = 0
#     for res in curs:
# #  index slujit nomerom v stolbce
#         sum += res[0]
#  # с индексом пурга но как я понял они сдвигаются
#         print(res[0], get_date(res[1]))
#     print("TOTAL", sum)

# ______________________________________________
# #работа с двумя таблицами получения данных с двух таблиц\
# #  #    payments и expenses
# with sqlite3.connect("db/database_zapas.db") as db:
#     curs = db.cursor()
#     #  берем данные из
#     #  SELECT столбца  amount, payment_date, name\
#     # JOIN expenses ON expenses.id работа код таблицей\
#     #  expenses там есть столбец name
#     #  перберает FROM payments
#     #  ищем строки с номером 2
#     # записываем WHERE expense_id = 2
#     # раз amount, payment_date то индекса всего 2
#     query = """
#     SELECT amount, payment_date, name FROM payments\
#     JOIN expenses ON expenses.id = payments.expense_id\
#     WHERE expense_id = 2"""
#
#     curs.execute(query)
#     sum = 0
#     for res in curs:
# #  index slujit nomerom v stolbce
#         sum += res[0]
#  # с индексом пурга но как я понял они сдвигаются
#         print(res[0], get_date(res[1]), res[2])
#     print("TOTAL", sum)

# __________________________________________________________
# #  # внесение данных в таблицу списком состоящим из картежей
# insert_payments = [
#     (1, 120, taim_cod(2023, 1, 2), 1),
#     (2, 100, taim_cod(2023, 1, 4), 2),
#     (3, 122, taim_cod(2023, 1, 5), 2),
#     (4, 20, taim_cod(2023, 1, 7), 3),
#     (5, 180, taim_cod(2023, 1, 8), 2),
#     (6, 130, taim_cod(2023, 1, 9), 1),
#     (7, 10, taim_cod(2023, 1, 15), 2)
# ]
#
# with sqlite3.connect("db/database_zapas.db") as db:
#     curs = db.cursor()
#  # переменая содается в ней есть столбцы
#     query = """ INSERT INTO payments\
#     (id, amount, payment_date, expense_id)
#     VALUES(?,?,?,?); """
#  # вносит списоком(list) с картежами(typle) insert_payments
#     curs.executemany(query,insert_payments)
#     db.commit()
#   # пересчитывает количество в переменой внесений curs.rowcount
#     print(curs.rowcount, "stronng dobavleno table")

# _______________________________________________________________________
# # work is data udobni sposob super cod
# dtr = datetime.datetime(2023,2,1)
# print(dtr, "dtr")
# dts = datetime.datetime.timestamp(dtr)
# print(dts, "dts")
# # преобразует ежесекудный с начала 1970 года, формат в дату
# print("good read", datetime.datetime.\
#       fromtimestamp(dts).date())

# ________________________________________________
# # work is data strong no udobni sposob
# mozhet prigaditsa
# day_str = "01-02-2022"
# day_obj = datetime.datetime.strptime\
#     (day_str, "%d-%m-%Y").date()
# print(day_obj, "day_obj")
# new_day_str = str(day_obj.day)+"-"\
#     +str(day_obj.month)+"-"+str(day_obj.year)
# print(new_day_str, "new_day_str")