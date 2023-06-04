import sqlalchemy
import psycopg2
from sqlalchemy.orm import sessionmaker
from models import create_tables, Publisher, Book, Shop, Stock, Sale


DSN = 'postgresql://postgres:0509@localhost:5432/book'
engine = sqlalchemy.create_engine(DSN)

create_tables(engine)

Session = sessionmaker(bind=engine)
session = Session()


publisher1 = Publisher(name='Pushkin')
publisher2 = Publisher(name='Dostaevsky')
publisher3 = Publisher(name='Adam Douglas')
session.add_all([publisher1, publisher2, publisher3])
session.commit()
book1_1 = Book(title='Captains daughter', id_publisher=1)
book1_2 = Book(title='Eugene Onegin', id_publisher=1)
book1_3 = Book(title='Snowstorm', id_publisher=1)
session.add_all([book1_1, book1_2, book1_3])
session.commit()
book2_1 = Book(title='Crime and punishment', id_publisher=2)
book2_2 = Book(title='Idiot', id_publisher=2)
book2_3 = Book(title='Demons', id_publisher=2)
session.add_all([book2_1, book2_2, book2_3])
session.commit()
book3_1 = Book(title='The Hitch-Hiker’s Guide To The Galaxy', id_publisher=3)
book3_2 = Book(title='Mostly Harmless', id_publisher=3)
book3_3 = Book(title='So Long And Thanks For All The Fish', id_publisher=3)
session.add_all([book3_1, book3_2, book3_3])
session.commit()
shop1 = Shop(name='Book & Shop')
shop2 = Shop(name='BookFord')
session.add_all([shop1, shop2])
session.commit()
stock1 = Stock(id_book=1, id_shop=1, count=12)
stock2 = Stock(id_book=2, id_shop=1, count=10)
stock3 = Stock(id_book=3, id_shop=1, count=17)
stock4 = Stock(id_book=4, id_shop=1, count=2)
stock5 = Stock(id_book=5, id_shop=1, count=10)
stock6 = Stock(id_book=6, id_shop=1, count=7)
stock7 = Stock(id_book=7, id_shop=2, count=7)
stock8 = Stock(id_book=8, id_shop=2, count=13)
stock9 = Stock(id_book=9, id_shop=2, count=1)
session.add_all([stock1, stock2, stock3, stock4, stock5, stock6, stock7, stock8, stock9])
session.commit()
sale1 = Sale(price=700, date_sale='22-06-2023', id_stock=1, count=1)
sale2 = Sale(price=1200, date_sale='25-06-2023', id_stock=1, count=1)
sale3 = Sale(price=1400, date_sale='25-06-2023', id_stock=1, count=1)
sale4 = Sale(price=300, date_sale='27-06-2023', id_stock=1, count=1)
sale5 = Sale(price=2100, date_sale='01-07-2023', id_stock=1, count=2)
session.add_all([sale1, sale2, sale3, sale4, sale5])
session.commit()

input_publisher = 'Pushkin'
sale_info = session.query(Book.title, Shop.name, Sale.price, Sale.date_sale)\
    .join(Stock, Sale.id_stock == Stock.id)\
    .join(Shop, Stock.id_shop == Shop.id) \
    .join(Book, Stock.id_book == Book.id)\
    .join(Publisher, Book.id_publisher == Publisher.id) \
    .filter(Publisher.name == input_publisher) \
    .order_by(Sale.date_sale.desc())
for row in sale_info.all():
    print(f'{row[0]} | {row[1]} | {row[2]} | {row[3].strftime("%d-%m-%Y")}')
session.close()