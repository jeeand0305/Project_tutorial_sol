import datetime
from models import *
from peewee import *
from sqlite3 import *

print("sozdanie tables  v SQL")
#Core Functionality
# вписываем наши модели классов из models.ру
# оригинал
# with db:
#     db.create_tables([Expense, Payment])
#     print("done")

print("добавка по штучно tables  v SQL")

# # ________________________________________________
# # добавка по штучно
# with db:
#     kommunalka = Expense(name = "Коммуналка").save()
#     # execute  дает возможность вносить по несколько данных \
#     # блогодаря одному name
#     benzin = Expense.create(name = "Бензин")
#     inet = Expense.insert(name = "Интернет").execute()
# print("done")

print("добавка данных в таблицу списком словарей или картежей")

# ________________________________________________
# добавка данных в таблицу списком словарей или картежей
# with db:
#     expenses = Expense.select()
#     payments = [
#         {'amount':13, 'payment_date':datetime.date(2022,11,5)\
#             , 'expense_id': expenses[0].id},
#         {'amount': 14, 'payment_date': datetime.date(2022, 11, 6) \
#             , 'expense_id': expenses[1].id},
#         {'amount': 15, 'payment_date': datetime.date(2022, 11, 7) \
#             , 'expense_id': expenses[1].id},
#         {'amount': 16, 'payment_date': datetime.date(2022, 11, 8) \
#             , 'expense_id': expenses[2].id},
#         {'amount': 17, 'payment_date': datetime.date(2022, 11, 9) \
#             , 'expense_id': expenses[1].id}
#     ]
#     # _________________varianty_________________________
# {'amount': 13, 'payment_date': datetime.date(2022, 11, 5), 'expense_id': expenses[0]},
# {'amount': 14, 'payment_date': datetime.date(2022, 11, 6), 'expense_id': expenses[1]},
# {'amount': 15, 'payment_date': datetime.date(2022, 11, 7), 'expense_id': expenses[1]},
# {'amount': 16, 'payment_date': datetime.date(2022, 11, 8), 'expense_id': expenses[2]},
# {'amount': 17, 'payment_date': datetime.date(2022, 11, 9), 'expense_id': expenses[1]}
#     _________________________________________________________
# Payment('amount'= 13, 'payment_date'= datetime.date(2022, 11, 5), 'expense_id'= expenses[0]),
# Payment('amount'= 14, 'payment_date'= datetime.date(2022, 11, 6), 'expense_id'= expenses[1]),
# Payment('amount'= 15, 'payment_date'= datetime.date(2022, 11, 7), 'expense_id'= expenses[1]),
# Payment('amount'= 16, 'payment_date'= datetime.date(2022, 11, 8), 'expense_id'= expenses[2]),
# Payment('amount'= 17, 'payment_date'= datetime.date(2022, 11, 9), 'expense_id'= expenses[1])

    # Payment.insert_many(payments).execute()
    # print("done")

print("выборка из таблице SQL ")

with db:
    # __________________________________________
    # expenses = Expense.select().where(Expense.id)# == 2)
    # print(expenses)# otvet nizu
    # #SELECT "t1"."id", "t1"."name" FROM "expenses" \
    # # AS "t1" WHERE "t1"."id"

    # # __________________________________________
    # expenses = Expense.select().where(Expense.id)
    # print(expenses[0].id, expenses[0].name, len(expenses))# otvet nizu
    # # 1 Коммуналка 3

    # # __________________________________________
    # expenses = Expense.select().where(Expense.id == 2)
    # print(expenses[0].id, expenses[0].name, len(expenses))  # otvet nizu
    # 2 Бензин 1

    # ____________________________________________________
    # expenses = Expense.select().where(Expense.id )
    # print(expenses)#[0].id, expenses[0].name, len(expenses))  # otvet nizu
    # for i in expenses:
    #     print(i)# otvet 1 2 3
    # #получается селект делит на количество строк если\
    # # не присвоен строгий номер типа (Expense.id == 2)\
    # # если это будет id ключь не повторяющися то будет\
    # # одно значение если не ключь несколько значений\
    # #  /expenses[индекс].имя_столбца/ получаем значение \
    # # строки из таблице под нужным индексом

    # # _____________________________________________________________
    # payments = Payment.select().where(Payment.expense_id ==2 )
    # print(payments[0].id, payments[0].payment_date, len(payments))  # otvet nizu
    # # 2 2022 - 11 - 06  3
    # for i in payments:
    #     print(payments)
    # # SELECT "t1"."id", "t1"."amount", "t1"."payment_date",\
    # # "t1"."expense_id" FROM "payments" AS "t1" WHERE \
    # # ("t1"."expense_id" = 2) и т.д.
    # #  type(payments) = <class 'peewee.ModelSelect'>
    # # как я понял разбивает на типизацию  "t1"."id" итд
    # # где "t1" это значение строки относится к типизаци с индексом
    # # а ."id" это имя столбца

    # # __________________________________________________________
    # expenses = Expense.get(Expense.id ==2)
    # print(expenses.id, expenses.name)# pint vnizu
    # # 2 Бензин

    #________________________________________________________________
    # получение данных с двух таблиц
    # variant1
    # allpayments = Payment.select().join(Expense)\
    #     .where(Expense.id == 2)
    # #variant2
    # allpayments = Payment.select().where(Payment.expense_id == 2)
    # for i in allpayments:
    #     print(i.amount, i.payment_date, i.expense_id.name)



    print("done")
