""" This module contains utility functions for processing data. """

import logging
from typing import List
import pandas as pd

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(pathname)s - %(funcName)s - %(message)s",
)


def handle_none_in_dataframe(
    dataframe: pd.DataFrame, columns_to_default: List[str]
) -> pd.DataFrame:
    """Handle None values and missing columns in the financial dataframe."""
    for col in columns_to_default:
        if col not in dataframe:
            dataframe[col] = 0

    # Fill any remaining None or NaN values in the dataframe with 0
    dataframe = dataframe.fillna(0)

    return dataframe


def format_financial_data(financial_dataframe):
    """Process the financial dataframe into the necessary format for the calculations"""
    if financial_dataframe.empty:
        return None
    if financial_dataframe.shape[0] > 1:
        logging.warning(
            "Multiple rows found for the given client number. Using the first row."
        )
        financial_dataframe = financial_dataframe.head(1)
    return financial_dataframe
