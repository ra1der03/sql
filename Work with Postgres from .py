import psycopg2

conn=psycopg2.connect(database='lesson', user='postgres', password='q1w2e3r4t5y')

# создание таблицы

# with conn.cursor() as cur:
#     cur.execute('drop table client')
#     def createtable(cursor, query):
#         cursor.execute(query)
#     createtable(cur, ('''CREATE TABLE IF NOT EXISTS client(
#         id serial primary key,
#         first_name VARCHAR(30),
#         last_name VARCHAR(30),
#         email VARCHAR(30),
#         phone_number TEXT);'''))


# добавление нового клиента
#
# with conn.cursor() as cur:
#     def createclient(cursor, first_name, last_name, email, phone):
#         cursor.execute('''INSERT INTO client(first_name, last_name, email, phone_number) VALUES(%s,%s,%s,%s);
#         ''',(first_name, last_name, email, phone, ))
#         conn.commit()
#         cursor.execute('''SELECT * FROM client;
#         ''')
#         print(cursor.fetchall())
#     createclient(cur, 'Mark', 'Mope', 'sshdha@gmail.com', '823874')

# смена номера у клиента

# with conn.cursor() as cur:
#     def addnumberclient(cursor, phone, id):
#         cursor.execute('''UPDATE client SET phone_number=%s WHERE id=%s;
#         ''',(phone, id,))
#         cursor.execute('''SELECT * FROM client;
#         ''')
#         print(cursor.fetchall())
#     addnumberclient(cur, '83232323244444', 2)

# изменение данных о клиенте

# with conn.cursor() as cur:
#     def changeclient(cursor, name1, name2, email, phone, id):
#         cursor.execute('''UPDATE client SET first_name=%s, last_name=%s, email=%s, phone_number=%s WHERE id=%s;
#         ''',(name1, name2, email, phone, id,))
#         cursor.execute('''SELECT * FROM client;
#         ''')
#         print(cursor.fetchall())
#     changeclient(cur, 'HIJBj', 'JDKdek', 'jbrdk4bk@gmail.com', '83232323244444', 2)

#удаление номера клиента

# with conn.cursor() as cur:
#     def deletenumberclient(cursor,phone, id):
#         cursor.execute('''UPDATE client SET phone_number=%s WHERE id=%s;
#         ''',( phone, id,))
#         cursor.execute('''SELECT * FROM client;
#         ''')
#         print(cursor.fetchall())
#     deletenumberclient(cur, ' ', 2)

# удаление клиента

# with conn.cursor() as cur:
#     def deleteclient(cursor, id):
#         cursor.execute('''DELETE from client WHERE id=%s;
#         ''',(id,))
#         cursor.execute('''SELECT * FROM client;
#         ''')
#         print(cursor.fetchall())
#     deleteclient(cur, 2)

# найти клиента по номеру

with conn.cursor() as cur:
    def findclient(cursor, phone):
        cursor.execute('''SELECT * FROM client WHERE phone_number=%s;
        ''', (phone,))
        print(cursor.fetchall())
    findclient(cur, '86398347743')
