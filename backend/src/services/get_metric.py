""" This module contains the function that returns the metric of a client. """

import logging
from src.utils.interactions_database import get_specific_metric
from src.utils.queries import QUERY_SIMPLIFIE, QUERY_COMPLET

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(pathname)s - %(funcName)s - %(message)s",
)


def get_metric(numero_client: int, metric: str):

    financial_dataframe = get_specific_metric(
        numero_client, metric, QUERY_SIMPLIFIE, QUERY_COMPLET
    )

    metric = financial_dataframe["metric"].values[0]
    logging.info("Metric for client %s : %s", numero_client, metric)

    return {"metric": metric}
