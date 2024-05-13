""" Utils module for the backend. """

import os
from sqlalchemy import create_engine
from sqlalchemy.exc import SQLAlchemyError, DatabaseError
import logging
from dotenv import load_dotenv
import pandas as pd

load_dotenv()

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(pathname)s - %(funcName)s - %(message)s",
)


def connect_to_db():
    """Connect to the database."""
    """
    Establishes a connection to the PostgreSQL database.

    Returns:
        sqlalchemy.engine.base.Engine: Engine object for interacting with the database.
    """
    db_user = os.getenv("POSTGRES_USER")
    db_password = os.getenv("POSTGRES_PASSWORD")
    db_host = os.getenv("POSTGRES_HOST")
    db_port = os.getenv("POSTGRES_PORT")
    db_name = os.getenv("POSTGRES_DB")

    if not all([db_user, db_password, db_host, db_port, db_name]):
        raise ValueError("One or more database environment variables are not set")

    db_url = (
        f"postgresql+psycopg2://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}"
    )

    try:
        engine = create_engine(db_url)
        engine.connect()
        logging.info("Connected to postgres engine !")
        return engine.raw_connection()
    except DatabaseError as db_err:
        # Handle database connection errors specifically
        logging.error(f"Database connection error: {db_err}", exc_info=True)
        raise db_err
    except SQLAlchemyError as sa_err:
        # Handle other SQLAlchemy errors
        logging.error(f"SQLAlchemy error: {sa_err}", exc_info=True)
        raise sa_err
    except Exception as e:
        # Catch-all for any other exceptions, which is a fallback mechanism
        logging.error(f"Unexpected error occurred: {e}", exc_info=True)
        raise e


def get_necessary_data(
    numero_client: int, query_bilan_simplifie: str, query_bilan_complet: str
) -> pd.DataFrame:
    """Fetch financial data for a given client number from the database."""
    connection = connect_to_db()
    if 0 < numero_client < 8:
        query: str = query_bilan_simplifie
    elif 7 < numero_client < 11:
        query: str = query_bilan_complet
    else:
        raise KeyError("Client number must be between 0 and 10")
    params = {"numero_client": numero_client}
    try:
        financial_data = pd.read_sql_query(query, connection, params=params)
        return financial_data
    except Exception as error:  # pylint: disable=broad-except
        print(f"An error occurred: {error}")
        return pd.DataFrame()
    
def get_specific_metric(numero_client: int, metric: str, query_bilan_simplifie: str, query_bilan_complet: str):
    connection = connect_to_db()
    if 0 < numero_client < 8:
        query: str = query_bilan_simplifie
    elif 7 < numero_client < 11:
        query: str = query_bilan_complet
    else:
        raise KeyError("Client number must be between 0 and 10")
    query = query.format(metric=metric)
    params = {"numero_client": numero_client}
    try:
        financial_data = pd.read_sql_query(query, connection, params=params)
        logging.info("Data fetched successfully %s", financial_data)
        return financial_data
    except Exception as error:  # pylint: disable=broad-except
        print(f"An error occurred: {error}")
        return pd.DataFrame()
