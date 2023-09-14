import logging
from ingest import ingest_drinks_api_full, ingest_transactions_csv, ingest_bar_csv
from load import load_drinks, load_glasses, load_transactions
from dataclasses import dataclass
from typing import Callable
import pandas as pd

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
logging.basicConfig(format='%(asctime)s : %(name)s : %(levelname)s : %(message)s')

@dataclass
class Datasource:
    name: str
    ingest_func: Callable[[dict], pd.DataFrame]
    load_func: Callable

data_sources = [
    Datasource('glass', ingest_bar_csv, load_glasses),
    Datasource('drink', ingest_drinks_api_full, load_drinks),
    Datasource('transactions', ingest_transactions_csv, load_transactions)
]

def record_metrics(df, df_name, logger):
    logger.info(f"Loading data from {df_name}. Rows: {len(df)}")

    missing_values = df.isnull().sum().sum()
    if missing_values > 0:
        logger.warning(f"Data quality issue in {df_name}: {missing_values} missing values found.")
    

def run_pipeline(session, config: dict, data_sources: list[Datasource]) -> None:
    for source in data_sources:
        df = source.ingest_func(config)
        record_metrics(df, source.name, logger)
        staging_path = f"{config['STAGING_BUCKET']}/{source.name}.csv" 
        df.to_csv(staging_path, index=False)

        source.load_func(session, staging_path, logger)
        logger.info(f"Data loaded from {source.name} to database successfully.")
    session.commit()
    session.close()
