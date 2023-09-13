import pandas as pd
import requests
import string

def base_preprocess(df: pd.DataFrame):
    if "Unnamed: 0" in df.columns:
        df = df.drop(["Unnamed: 0"], axis=1)
    if "datetime" in df.columns:
        df["datetime"] = pd.to_datetime(df["datetime"])
    return df


def ingest_transactions_csv(config: dict) -> pd.DataFrame:
    df_union = pd.DataFrame()

    for location, transaction_file_path in config['TRANSACTION_FILES'].items():
        df = base_preprocess(
            pd.read_csv(
                transaction_file_path, 
                **config['TRANSACTION_FILE_READ_OPTIONS'].get(
                    location, 
                    config['TRANSACTION_FILE_READ_OPTIONS']['default']
                )
            )
        )
        df['location'] = location
        df_union = pd.concat([df_union, df])

    return df_union

def ingest_bar_csv(config: dict) -> pd.DataFrame:
    df = pd.read_csv(config['BAR_FILE'])
    return df

def ingest_drinks_api_full(config: dict) -> pd.DataFrame:
    letters = string.ascii_lowercase
    rows = []

    # there could a better way to get all drinks
    for char in letters:
        data = requests.get(f"{config['DRINKS_API_URL']}?f={char}").json()
        if data['drinks'] is not None:
            for drink in data['drinks']:
                rows.append(
                    (
                        drink['idDrink'],
                        drink['strDrink'],
                        drink['strGlass']
                    )
                )
    df = pd.DataFrame(rows, columns=config['RAW_DRINKS_COLUMNS'])
    return df

def ingest_drinks_api_incremental(config: dict) -> pd.DataFrame:
    """
    PLACEHOLDER
    
    Queries the 'latest' drinks from the API to only add new items
    """
    ...

def ingest_api_transactions(config: dict) -> pd.DataFrame:
    """
    PLACEHOLDER

    API Ingestion function to be developed upon API availability
    """
    ...
