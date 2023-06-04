import sqlalchemy as sq
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()

class Publisher(Base):
    __tablename__ = 'publisher'
    id = sq.Column(sq.Integer, primary_key=True)
    name = sq.Column(sq.String, unique=True)
    books = relationship('Book', backref='publisher')


class Book(Base):
     __tablename__ = 'book'
     id = sq.Column(sq.Integer, primary_key=True)
     title = sq.Column(sq.String(length=40))
     id_publisher = sq.Column(sq.Integer, sq.ForeignKey('publisher.id'), nullable=False)
     book_stocks = relationship('Stock', backref="book_stock")


class Shop(Base):
    __tablename__ = 'shop'
    id = sq.Column(sq.Integer, primary_key=True)
    name = sq.Column(sq.String(length=40), unique=True)
    shop_stocks = relationship('Stock', backref="shop_stock")


class Stock(Base):
    __tablename__ = 'stock'
    id = sq.Column(sq.Integer, primary_key=True)
    id_book = sq.Column(sq.Integer, sq.ForeignKey('book.id'), nullable=False)
    id_shop = sq.Column(sq.Integer, sq.ForeignKey('shop.id'), nullable=False)
    count = sq.Column(sq.Integer, nullable=False)
    sales_stock = relationship('Sale', backref="stock")


class Sale(Base):
    __tablename__ = 'sale'
    id = sq.Column(sq.Integer, primary_key=True)
    price = sq.Column(sq.Numeric, nullable=False)
    date_sale = sq.Column(sq.Date, nullable=False)
    id_stock = sq.Column(sq.Integer, sq.ForeignKey('stock.id'), nullable=False)
    count = sq.Column(sq.Integer, nullable=False)


def create_tables(engine):
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)