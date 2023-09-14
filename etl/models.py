from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker, relationship
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Float
import config

Base = declarative_base()
engine = create_engine(config.DATABASE_URI)
Session = sessionmaker(bind=engine, autoflush=False)

class GlassStock(Base):
    __tablename__ = 'glass_type'

    id = Column(Integer, primary_key=True)
    stock = Column(Integer, nullable=False)
    location_id = Column(String,  ForeignKey('location.id'), nullable=True)
    
    def __init__(self, id, stock, location_id):
        self.id = id
        self.stock = stock
        self.location_id = location_id

class Glass(Base):
    __tablename__ = 'glass'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    
    def __init__(self, name):
        self.name = name

class Location(Base):
    __tablename__ = 'location'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, unique=True, nullable=False)
    
    def __init__(self, name):
        self.name = name

class Drink(Base):
    __tablename__ = 'drink'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, unique=True, nullable=False)
    glass_id = Column(Integer, ForeignKey('glass.id'), nullable=True)

    def __init__(self, name, glass_id):
        self.name = name
        self.glass_id = glass_id


class Transaction(Base):
    __tablename__ = 'transactions'

    id = Column(Integer, primary_key=True, autoincrement=True)
    datetime = Column(DateTime, nullable=False)
    drink_id = Column(Integer, ForeignKey('drink.id'), nullable=False)
    location_id = Column(String,  ForeignKey('location.id'), nullable=False)
    sale_amount = Column(Float, nullable=False)

    # drink = relationship("Drink", back_populates="transactions")

    def __init__(self, datetime, drink_id, location_id, sale_amount):
        self.datetime = datetime
        self.drink_id = drink_id
        self.sale_amount = sale_amount
        self.location_id = location_id

Base.metadata.create_all(engine)
