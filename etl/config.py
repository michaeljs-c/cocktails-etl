TRANSACTION_DROP_BUCKET = 'data/transaction_file_dropzone'
STAGING_BUCKET = 'data/staging'
TRANSACTION_FILES = {
    "london": f"{TRANSACTION_DROP_BUCKET}/london_transactions.csv",
    "budapest": f"{TRANSACTION_DROP_BUCKET}/budapest.csv",
    "ny": f"{TRANSACTION_DROP_BUCKET}/ny.csv",
}
BAR_FILE = "data/bar_data.csv"
RAW_TRANSACTION_COLUMNS = ["datetime", "drink", "amount"]
RAW_DRINKS_COLUMNS = ['drink_id', 'drink_name', 'glass_type']
TRANSACTION_FILE_READ_OPTIONS = {
    'london': dict(sep='\t', names=RAW_TRANSACTION_COLUMNS),
    'ny': dict(names=RAW_TRANSACTION_COLUMNS, skiprows=1),
    'budapest': dict(names=RAW_TRANSACTION_COLUMNS, skiprows=1),
    'default': dict(names=RAW_TRANSACTION_COLUMNS)
}
DRINKS_API_URL = "https://www.thecocktaildb.com/api/json/v1/1/search.php"
DRINKS_BATCH_MODE = 'FULL' # FULL -> queries all data from api, INCREMENTAL -> processes only new data (REQUIRES PREMIUM API ACCOUNT)
DATABASE_URI = 'sqlite:///data/database.db'