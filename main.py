import psycopg2

conn=psycopg2.connect(database='lesson', user='postgres', password='q1w2e3r4t5y')

# создание таблицы

def createtable(cursor, query):
        cursor.execute(query)

# добавление нового клиента\номера

def create_numbers(cursor, phone, owner_id):
    cursor.execute('''INSERT INTO phone_numbers(number, owner_id) VALUES(%s, %s);
        ''',(phone, owner_id, ))
    cursor.execute('''SELECT * FROM phone_numbers;
        ''')
    print(cursor.fetchall())
def createclient(cursor, first_name, last_name, email, phone=None):
    cursor.execute('''INSERT INTO client(first_name, last_name, email) VALUES(%s,%s,%s);
        ''',(first_name, last_name, email, ))
    cursor.execute('''UPDATE client SET phone_number = number FROM phone_numbers 
                      WHERE id(client) = owner_id(phone_numbers)  ''')
    cursor.execute('''SELECT * FROM client;
        ''')
    print(cursor.fetchall())

# добавить номер клиента

def addnumberclient(cursor, id, phone=None):
    cursor.execute("""SELECT * FROM phone_numbers WHERE owner_id=%s;""", (id,))
    f = cursor.fetchall()
    phones = []
    for word in f:
        if phone == word[1]:
            break
        elif phone == None:
            phones.append(word[1])
        elif phone!=None and phone not in phones:
            phones.append(word[1])
            phones.append(phone)
        elif phone!=None:
            phones.append(word[1])
        else:
            pass
    cursor.execute("""INSERT INTO phone_numbers(number, owner_id) VALUES(%s, %s);""",(phone, id, ))
    # cursor.execute('''UPDATE client SET phone_number=%s WHERE id=%s;''',(phones,id, ))
    cursor.execute('''UPDATE client SET phone_number = number FROM phone_numbers  
                      WHERE id(client) = owner_id(phone_numbers)  ''')
    cursor.execute('''SELECT * FROM client;''')
    print(cursor.fetchall())


# изменение данных о клиенте

def changeclient(cursor,id, name1=None, name2=None, email=None, phone=None):
    cursor.execute('''SELECT * FROM client where id=%s;
                ''',(id,))
    f=(cursor.fetchall())
    mass=[name1,name2, email, phone]
    for i, ob in enumerate(mass):
        if ob==None:
            mass[i]=f[0][i+1]
        else:
            pass
    cursor.execute('''UPDATE client SET first_name=%s, last_name=%s, email=%s, phone_number=%s WHERE id=%s;
        ''',(mass[0], mass[1], mass[2], mass[3],id))
    cursor.execute('''SELECT * FROM client;
            ''')
    print(cursor.fetchall())

# удаление номера клиента

def deletenumberclient(cursor, id, phone):
    cursor.execute('''DELETE from phone_numbers WHERE number=%s and owner_id=%s;
        ''',(phone, id,))
    addnumberclient(cursor, id)
    cursor.execute('''SELECT * FROM client;
        ''')
    print(cursor.fetchall())

# удаление клиента
def deleteclient(cursor, id):
    cursor.execute('''DELETE from client WHERE id=%s;
        ''',(id,))
    cursor.execute('''SELECT * FROM client;
        ''')
    print(cursor.fetchall())


# найти клиента по номеру

def findclient(cursor, first_name=None, last_name=None, email=None, phone_number=None):
    names=['first_name','last_name','email','phone_number']
    counter, list=0,[]
    mass=[first_name,last_name, email, phone_number]
    for i, ob in enumerate(mass, 0):
        if ob!=None:
            list.append(names[i])
            list.append(ob)
        else:
            pass
    sql=''
    print(list) 
    for i, word in enumerate(list, 0):
        if i%2==0 and i<1:
            sql+=word
        elif i%2==0 and i>1:
            sql+='AND '+str(word)
        elif i%2!=0 and len(list)>2:
            sql+="='"+str(word)+"' "
        else:
            sql+='='+"'"+str(word)+"'"

    cursor.execute('''SELECT * FROM client where ''' + sql)
    print(cursor.fetchall())

# вызовы функций

if __name__ == "__main__":
    with conn.cursor() as cur:
        cur.execute('drop table client cascade')
        createtable(cur, ('''CREATE TABLE IF NOT EXISTS client(
                id serial PRIMARY KEY,
                first_name VARCHAR(30),
                last_name VARCHAR(30),
                email VARCHAR(30),
                phone_number TEXT);'''))
        createtable(cur, ('''CREATE TABLE IF NOT EXISTS phone_numbers(id serial, number TEXT ,
                 owner_id INTEGER UNIQUE primary key, FOREIGN KEY(owner_id) REFERENCES client(id));'''))
        cur.execute('''ALTER TABLE phone_numbers DROP CONSTRAINT phone_numbers_owner_id_fkey; 
        ALTER TABLE phone_numbers DROP CONSTRAINT phone_numbers_pkey;''')

        create_numbers(cur,  '47625348', 1)
        create_numbers(cur, '34243438', 1)
        create_numbers(cur, '78137892', 2)
        create_numbers(cur, '19236819', 3)

        createclient(cur, 'Mark', 'Mope', 'sshdha@gmail.com')
        createclient(cur, 'David', 'Rod', 'sknesafa@gmail.com')
        createclient(cur, 'Mikkey', 'Rurk', 'bwhjdsda@gmail.com' )

        addnumberclient(cur, 1)
        addnumberclient(cur, 2)
        addnumberclient(cur, 3, 727723747)
        addnumberclient(cur, 3, 276363)

        # changeclient(cur,  3,'Mikkey', phone='2039823473,28172834')

        # deletenumberclient(cur, 1, '47625348')

        # deleteclient(cur, 1)

        findclient(cur, email='sshdha@gmail.com', phone_number=34243438)

