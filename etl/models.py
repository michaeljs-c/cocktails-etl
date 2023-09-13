from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker, relationship
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Float

Base = declarative_base()

class GlassType(Base):
    __tablename__ = 'glass_type'

    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True, nullable=False)
    
    def __init__(self, name):
        self.name = name


class Drink(Base):
    __tablename__ = 'drink'

    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True, nullable=False)
    glass_type_id = Column(Integer, nullable=False)

    def __init__(self, name, glass_type_id):
        self.name = name
        self.glass_type_id = glass_type_id

class Transaction(Base):
    __tablename__ = 'transaction'

    id = Column(Integer, primary_key=True)
    datetime = Column(DateTime, nullable=False)
    drink_id = Column(Integer, ForeignKey('drink.id'), nullable=False)
    sale_amount = Column(Float, nullable=False)
    location = Column(String, nullable=False)

    drink = relationship("Drink", back_populates="transactions")

    def __init__(self, datetime, drink_id, sale_amount, location):
        self.datetime = datetime
        self.drink_id = drink_id
        self.sale_amount = sale_amount
        self.location = location

TYPES = {
    'bar': GlassType,
    'drinks': Drink,
    'transactions': Transaction
}
