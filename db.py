from pathlib import Path
import pandas as pd
from sqlalchemy import create_engine

ROOT = Path(__file__).resolve().parent
DB_PATH = ROOT / 'database' / 'mercado_ti.db'
CSV_PATH = ROOT / 'dados' / 'simulacao_mercado_ti_brasil.csv'


def get_engine():
    DB_PATH.parent.mkdir(parents=True, exist_ok=True)
    return create_engine(f'sqlite:///{DB_PATH}', future=True)


def initialize_database():
    engine = get_engine()
    if not DB_PATH.exists():
        df = pd.read_csv(CSV_PATH, parse_dates=['data'])
        df.to_sql('mercado_ti', engine, if_exists='replace', index=False)
    return engine


def load_data():
    engine = initialize_database()
    return pd.read_sql('SELECT * FROM mercado_ti', engine, parse_dates=['data'])
