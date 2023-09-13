import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import GlassType, Drink, Transaction, TYPES
from config import DATABASE_URI

engine = create_engine(DATABASE_URI)
Session = sessionmaker(bind=engine)
session = Session()

def load_csv_to_table(csv_file: str, table: str) -> None:
    df = pd.read_csv(csv_file)
    df.to_sql(TYPES[table].__tablename__, engine, if_exists='append', index=False)

    session.commit()
    session.close()
