""" Unit tests for the calcul ratio interaction with the database module """

import unittest
from unittest.mock import patch, MagicMock, ANY
import pandas as pd
from backend.src.utils.interactions_database import get_necessary_data
from backend.src.utils.queries import (
    QUERY_TRESORERIE_SIMPLIFIE,
    QUERY_TRESORERIE_COMPLET
)


class TestGetNecessaryData(unittest.TestCase):
    """Unit tests for the get_necessary_data function"""

    @patch("backend.src.utils.interactions_database.connect_to_db")
    @patch("pandas.read_sql_query")
    def test_get_necessary_data_success(self, mock_read_sql_query, mock_connect_to_db):
        """Test the successful retrieval of the necessary data"""
        mock_connection = MagicMock()
        mock_connect_to_db.return_value = mock_connection
        mock_read_sql_query.return_value = pd.DataFrame(
            {
                "actif_circulant": [10000],
                "dettes_courantes": [5000],
                "cash": [2000],
                "receivables_1": [1000],
                "receivables_2": [500],
                "payables_1": [500],
                "stock_1": [1000],
                "stock_2": [500],
                "stock_3": [200],
                "stock_4": [300],
                "stock_5": [400],
            }
        )

        # Running the test
        result = get_necessary_data(
            1, QUERY_TRESORERIE_SIMPLIFIE, QUERY_TRESORERIE_COMPLET
        )
        mock_read_sql_query.assert_called_once_with(
            ANY,  # You can use the actual SQL string or unittest.mock.ANY if you do not want to assert the query text
            mock_connection,
            params={"numero_client": 1},
        )
        self.assertIsInstance(result, pd.DataFrame)
        self.assertFalse(result.empty)

    @patch("backend.src.utils.interactions_database.connect_to_db")
    @patch("pandas.read_sql_query", side_effect=Exception("Database error"))
    def test_get_necessary_data_failure(self, mock_read_sql_query, mock_connect_to_db):
        """Test the failure to retrieve the necessary data"""
        # Setting up mocks
        mock_connection = MagicMock()
        mock_connect_to_db.return_value = mock_connection

        # Running the test
        result = get_necessary_data(
            10, QUERY_TRESORERIE_SIMPLIFIE, QUERY_TRESORERIE_COMPLET
        )
        self.assertIsInstance(result, pd.DataFrame)
        self.assertTrue(result.empty)


if __name__ == "__main__":
    unittest.main()
