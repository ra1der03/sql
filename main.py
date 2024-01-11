import sqlalchemy
from sqlalchemy.orm import sessionmaker

from models import Create_tables, Publisher, Book, Stock, Shop, Sale

DSN = 'postgresql://postgres:q1w2e3r4t5y@localhost:5432/orm_testing'
engine = sqlalchemy.create_engine(DSN)

Create_tables(engine)

Session = sessionmaker(bind=engine)
session = Session()

publisher1 = Publisher(name='Александр Пушкин')
publisher2 = Publisher(name='Джек Лондон')
publisher3 = Publisher(name='Айн Ренд')
session.add_all([publisher1, publisher2, publisher3])


book1 = Book(name='Капитанская дочка', publisher=publisher1)
book2 = Book(name='Руслан и Людмила', publisher=publisher1)
book3 = Book(name='Евгений Онегин', publisher=publisher1)
book4 = Book(name='Мартин Иден', publisher=publisher2)
book5 = Book(name='Морской волк', publisher=publisher2)
book6 = Book(name='Зов предков', publisher=publisher2)
book7 = Book(name='Источник', publisher=publisher3)
book8 = Book(name='Атлант расправил плечи', publisher=publisher3)
book9 = Book(name='Мы, живые', publisher=publisher3)


shop1 = Shop(name='Буквоед')
shop2 = Shop(name='Подписные издания')
shop3 = Shop(name='АльпинаКнига')
session.add_all([book1, book2, book3, book4, book5, book6, book7, book8, book9, shop1, shop2, shop3])


stock1 = Stock(book=book1, shop=shop1, count=11)
stock2 = Stock(book=book2, shop=shop1, count=10)
stock3 = Stock(book=book3, shop=shop1, count=9)
stock4 = Stock(book=book4, shop=shop2, count=21)
stock5 = Stock(book=book5, shop=shop2, count=12)
stock6 = Stock(book=book6, shop=shop2, count=13)
stock7 = Stock(book=book7, shop=shop3, count=9)
stock8 = Stock(book=book8, shop=shop3, count=8)
stock9 = Stock(book=book9, shop=shop3, count=14)
session.add_all([stock1, stock2, stock3, stock4, stock5, stock6, stock7, stock8, stock9])


sale1 = Sale(price=300, date_sale='2024-01-02', stock=stock1, count=1)
sale2 = Sale(price=400, date_sale='2024-01-02', stock=stock2, count=1)
sale3 = Sale(price=250, date_sale='2024-01-08', stock=stock3, count=1)
sale4 = Sale(price=500, date_sale='2024-01-03', stock=stock4, count=1)
sale5 = Sale(price=600, date_sale='2024-01-04', stock=stock5, count=1)
sale6 = Sale(price=700, date_sale='2024-01-05', stock=stock6, count=1)
sale7 = Sale(price=800, date_sale='2024-01-10', stock=stock7, count=1)
sale8 = Sale(price=900, date_sale='2024-01-06', stock=stock8, count=1)
sale9 = Sale(price=750, date_sale='2024-01-11', stock=stock9, count=1)


session.add_all([sale1, sale2, sale3, sale4, sale5, sale6, sale7, sale8, sale9])

session.commit()

name = input("Введите имя автора: ")
result1 = session.query(Publisher, Book.name).filter(Publisher.name.like('%'+name+'%'))
session.query(Book, Stock).join(Book, Book.id == Stock.book_id)
session.query(Shop, Stock).join(Shop, Shop.id == Stock.shop_id)
session.query(Sale, Stock).join(Sale, Stock.id == Sale.stock_id)
# .join(Address, User.id == Address.user_id)\
for c in result1.join(Book, Publisher.id == Book.publisher_id).all():
    for i in session.query(Book.name, Shop.name, Sale.price, Sale.date_sale).filter(Book.name == c[1]).all():
        print(i)

session.close()