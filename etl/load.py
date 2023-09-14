import pandas as pd
from models import Drink, Glass, GlassStock, Transaction, Location
# def load_csv_to_table(engine, csv_file: str, table: str) -> None:
#     df = pd.read_csv(csv_file)
#     df.to_sql(TYPES[table].__tablename__, engine, if_exists='append', index=False)

def load_transactions(session, staging_path, logger):
    df = pd.read_csv(staging_path, parse_dates=['datetime'])
    for _, row in df.iterrows():
        try:
            drink_id = session.query(Drink.id).filter(Drink.name==row['drink']).scalar()
            if not drink_id:
                drink = Drink(row['drink'], None)
                session.add(drink)
                session.commit()
                drink_id = session.query(Drink.id).filter(Drink.name==row['drink']).scalar()
            location_id = session.query(Location.id).filter(Location.name==row['location']).scalar()
            if not location_id:
                session.add(Location(row['location']))
                session.commit()
                location_id = session.query(Location.id).filter(Location.name==row['location']).scalar()
            transaction = Transaction(row['datetime'], drink_id, location_id, row['amount'])
            session.add(transaction)

        except Exception as e:
            logger.error(e)
            raise e
    session.commit()

def load_glasses(session, staging_path, logger):
    df = pd.read_csv(staging_path)
    for _, row in df.iterrows():
        try:
            location_id = session.query(Location.id).filter(Location.name==row['bar']).scalar()
            if not location_id:
                session.add(Location(row['bar']))
                location_id = 1
                session.commit()
                
            glass_id = session.query(Glass.id).filter(Glass.name==row['glass_type']).scalar()
            if not glass_id:
                glass = Glass(row['glass_type'])
                session.add(glass)
                session.commit()
                glass_id = session.query(Glass.id).filter(Glass.name==row['glass_type']).scalar()

                glass_stock = GlassStock(glass_id, row['stock'], location_id)
                session.add(glass_stock)

        except Exception as e:
            logger.error(e)
            raise e
    session.commit()

def load_drinks(session, staging_path, logger):
    df = pd.read_csv(staging_path)
    for _, row in df.iterrows():
        try:
            glass_id = session.query(Glass.id).filter(Glass.name==row['glass_type']).scalar()
            if not glass_id:
                session.add(Glass(row['glass_type'], 0, None))
                glass_id = 1

            drink_id = session.query(Drink.id).filter(Drink.name==row['drink_name']).scalar()
            if not drink_id:
                drink = Drink(row['drink_name'], glass_id)
                session.add(drink)
            
        except Exception as e:
            logger.error(e)
            raise e
    session.commit()
