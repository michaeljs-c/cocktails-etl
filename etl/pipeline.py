import logging
from ingest import ingest_drinks_api_full, ingest_transactions_csv, ingest_bar_csv
from load import load_csv_to_table

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
logging.basicConfig(format='%(asctime)s : %(name)s : %(levelname)s : %(message)s')

data_sources = {
    'transactions': ingest_transactions_csv,
    'bar': ingest_bar_csv,
    'drinks': ingest_drinks_api_full
}

def record_metrics(df, df_name, logger):
    logger.info(f"Loading data from {df_name}. Rows: {len(df)}")

    missing_values = df.isnull().sum().sum()
    if missing_values > 0:
        logger.warning(f"Data quality issue in {df_name}: {missing_values} missing values found.")
    

def run_pipeline(config: dict, data_sources: dict) -> None:
    for data_source, ingest_func in data_sources.items():
        df = ingest_func(config)
        record_metrics(df, data_source, logger)
        df.to_csv(f"{config['STAGING_BUCKET']}/{data_source}.csv", index=False)

        load_csv_to_table(f"{config['STAGING_BUCKET']}/{data_source}.csv", data_source)
        logger.info(f"Data loaded from {data_source} to database successfully.")
