""" Unit tests for the calcul ratio tresorerie module """

import unittest
from unittest.mock import patch
import pandas as pd
from backend.src.services.calcul_ratios_tresorerie import (
    calcul_fond_de_roulement,
    calcul_ratio_liquidite_generale,
    calcul_ratio_liquidite_rapide,
    calcul_ratio_liquidite_immediate,
    calcul_besoins_en_fonds_de_roulement,
    format_tresorerie_data,
    calcul_tresorerie_ratios,
)


class TestCalculFondRoulement(unittest.TestCase):
    """Unit tests for the calcul fond de roulement"""

    def setUp(self):
        # Mocking the logging to check log outputs
        self.patcher = patch("utils.fill_database.logging")
        self.mock_logging = self.patcher.start()

    def tearDown(self):
        self.patcher.stop()

    def test_basic_calculation(self):
        """Test the basic calculation of the working capital"""
        # Valid input with positive values
        actif_circulant = 1000
        dettes_courantes = 600
        result = calcul_fond_de_roulement(actif_circulant, dettes_courantes)
        self.assertEqual(result, 400)  # 1000 - 600

    def test_negative_working_capital(self):
        """Test the case where the working capital is negative"""
        # Valid input where liabilities exceed assets
        actif_circulant = 500
        dettes_courantes = 800
        result = calcul_fond_de_roulement(actif_circulant, dettes_courantes)
        self.assertEqual(result, -300)  # 500 - 800

    def test_zero_working_capital(self):
        """Test the case where the working capital is zero"""
        # Valid input where assets equal liabilities
        actif_circulant = 700
        dettes_courantes = 700
        result = calcul_fond_de_roulement(actif_circulant, dettes_courantes)
        self.assertEqual(result, 0)

    def test_missing_assets(self):
        """Test the case where the assets are missing"""
        # No "Current Assets" column
        dettes_courantes = 500

        with self.assertRaises(KeyError):
            calcul_fond_de_roulement(dettes_courantes, None)

    def test_missing_liabilities(self):
        """Test the case where the liabilities are missing"""
        # No "Current Liabilities" column
        actif_circulant = 700

        with self.assertRaises(KeyError):
            calcul_fond_de_roulement(actif_circulant, None)

    def test_empty_data(self):
        """Test the case where the data is empty"""

        with self.assertRaises(KeyError):
            calcul_fond_de_roulement(None, None)


class TestCalculRatioLiquiditeGenerale(unittest.TestCase):
    """Unit tests for the calcul ratio liquidite generale"""

    def setUp(self):
        # Mocking the logging to check log outputs
        self.patcher = patch("backend.src.services.calcul_ratios_tresorerie.logging")
        self.mock_logging = self.patcher.start()

    def tearDown(self):
        self.patcher.stop()

    def test_basic_calculation(self):
        """Test the basic calculation of the current ratio"""
        # Valid input with positive values
        actif_circulant = 1000
        dettes_courantes = 500
        result = calcul_ratio_liquidite_generale(actif_circulant, dettes_courantes)
        self.assertEqual(result, 2.0)  # 1000 / 500

    def test_zero_liabilities(self):
        """Test the case where the liabilities are zero"""
        # Valid input with zero liabilities
        actif_circulant = 1000
        dettes_courantes = 0

        with self.assertRaises(ZeroDivisionError):
            calcul_ratio_liquidite_generale(actif_circulant, dettes_courantes)

    def test_negative_liabilities(self):
        """Test the case where the liabilities are negative"""
        # Valid input with negative liabilities
        actif_circulant = 1000
        dettes_courantes = -200
        result = calcul_ratio_liquidite_generale(actif_circulant, dettes_courantes)
        self.assertEqual(result, -5.0)  # 1000 / (-200)

    def test_missing_assets(self):
        """Test the case where the assets are missing"""
        # No "Current Assets" column
        dettes_courantes = 500

        with self.assertRaises(KeyError):
            calcul_ratio_liquidite_generale(None, dettes_courantes)

    def test_missing_liabilities(self):
        """Test the case where the liabilities are missing"""
        # No "Current Liabilities" column
        actif_circulant = 700

        with self.assertRaises(KeyError):
            calcul_ratio_liquidite_generale(actif_circulant, None)

    def test_empty_dataframe(self):
        """Test the case where the dataframe is empty"""
        with self.assertRaises(KeyError):
            calcul_ratio_liquidite_generale(None, None)


class TestCalculRatioLiquiditeRapide(unittest.TestCase):
    """Unit tests for the calcul ratio liquidite rapide function"""

    def test_basic_calculation(self):
        """Test the basic calculation of the quick ratio"""
        cash = 1000
        receivables = 500
        liabilities = 800
        result = calcul_ratio_liquidite_rapide(cash, receivables, liabilities)
        self.assertEqual(result, 1.875)  # (1000 + 500) / 800

    def test_zero_liabilities(self):
        """Test the case where the liabilities are zero"""
        cash = 1000
        receivables = 500
        liabilities = 0

        with self.assertRaises(ZeroDivisionError):
            calcul_ratio_liquidite_rapide(cash, receivables, liabilities)

    def test_negative_liabilities(self):
        """Test the case where the liabilities are negative"""
        cash = 1000
        receivables = 500
        liabilities = -200
        result = calcul_ratio_liquidite_rapide(cash, receivables, liabilities)
        self.assertEqual(result, -7.5)  # (1000 + 500) / (-200)

    def test_missing_cash(self):
        """Test the case where the cash is missing"""
        receivables = 500
        liabilities = 800

        result = calcul_ratio_liquidite_rapide(None, receivables, liabilities)
        self.assertEqual(result, 500 / 800)  # 500 / 800

    def test_missing_accounts_receivable(self):
        """Test the case where the accounts receivable are missing"""
        cash = 700
        liabilities = 600

        result = calcul_ratio_liquidite_rapide(cash, None, liabilities)
        self.assertEqual(result, 700 / 600)  # 700 / 600

    def test_empty_dataframe(self):
        """Test the case where the dataframe is empty"""
        with self.assertRaises(KeyError):
            calcul_ratio_liquidite_rapide(None, None, None)


class TestCalculRatioLiquiditeImmediate(unittest.TestCase):
    """Unit tests for the calcul ratio liquidite immediate function"""

    def test_basic_calculation(self):
        """Test the basic calculation of the cash ratio"""
        cash = 1000
        liabilities = 500
        result = calcul_ratio_liquidite_immediate(cash, liabilities)
        self.assertEqual(result, 2.0)  # 1000 / 500

    def test_zero_liabilities(self):
        """Test the case where the liabilities are zero"""
        cash = 1000
        liabilities = 0

        with self.assertRaises(ZeroDivisionError):
            calcul_ratio_liquidite_immediate(cash, liabilities)

    def test_negative_liabilities(self):
        """Test the case where the liabilities are negative"""
        cash = 1000
        liabilities = -200
        result = calcul_ratio_liquidite_immediate(cash, liabilities)
        self.assertEqual(result, -5.0)  # 1000 / (-200)

    def test_missing_cash(self):
        """Test the case where the cash is missing"""
        liabilities = 500

        with self.assertRaises(KeyError):
            calcul_ratio_liquidite_immediate(None, liabilities)

    def test_missing_liabilities(self):
        """Test the case where the liabilities are missing"""
        cash = 1000

        with self.assertRaises(KeyError):
            calcul_ratio_liquidite_immediate(cash, None)

    def test_empty_data(self):
        """Test the case where the data is empty"""
        with self.assertRaises(KeyError):
            calcul_ratio_liquidite_immediate(None, None)


class TestCalculBesoinsEnFondsDeRoulement(unittest.TestCase):
    """Unit tests for the calcul besoins en fonds de roulement function"""

    def test_basic_calculation(self):
        """Test the basic calculation of the working capital needs"""
        stock = 1000
        receivables = 500
        payables = 600
        result = calcul_besoins_en_fonds_de_roulement(stock, receivables, payables)
        self.assertEqual(result, 900)  # (1000 + 500) - 600

    def test_negative_working_capital_needs(self):
        """Test the case where the working capital needs are negative"""
        stock = 300
        receivables = 200
        payables = 600
        result = calcul_besoins_en_fonds_de_roulement(stock, receivables, payables)
        self.assertEqual(result, -100)  # (300 + 200) - 600

    def test_zero_working_capital_needs(self):
        """Test the case where the working capital needs are zero"""
        stock = 400
        receivables = 200
        payables = 600
        result = calcul_besoins_en_fonds_de_roulement(stock, receivables, payables)
        self.assertEqual(result, 0)  # (400 + 200) - 600

    def test_missing_inventory(self):
        """Test the case where the inventory is missing"""
        receivables = 500
        payables = 600

        result = calcul_besoins_en_fonds_de_roulement(None, receivables, payables)
        self.assertEqual(result, -100)  # 500 - 600

    def test_missing_receivables(self):
        """Test the case where the accounts receivable are missing"""
        stock = 400
        payables = 300

        result = calcul_besoins_en_fonds_de_roulement(stock, None, payables)
        self.assertEqual(result, 100)  # 400 - 300

    def test_missing_payables(self):
        """Test the case where the accounts payable are missing"""
        stock = 700
        receivables = 200

        result = calcul_besoins_en_fonds_de_roulement(stock, receivables, None)
        self.assertEqual(result, 900)  # 700 + 200

    def test_empty_data(self):
        """Test the case where the data is empty"""

        with self.assertRaises(KeyError):
            calcul_besoins_en_fonds_de_roulement(None, None, None)


class TestFormatTresorerieData(unittest.TestCase):
    """Unit tests for the format_tresorerie_data function"""

    def test_basic_transformation(self):
        """Test the basic transformation of the financial data"""
        df_financial = pd.DataFrame(
            {
                "receivables_1": [200],
                "receivables_2": [300],
                "stock_1": [100],
                "stock_2": [50],
                "stock_3": [75],
                "stock_4": [25],
                "stock_5": [150],
                "payables_1": [500],
            }
        )

        result = format_tresorerie_data(df_financial)

        self.assertEqual(result["receivables"].iloc[0], 500)  # 200 + 300
        self.assertEqual(result["stock"].iloc[0], 400)  # 100 + 50 + 75 + 25 + 150
        self.assertEqual(result["payables"].iloc[0], 500)

    def test_empty_dataframe(self):
        """Test the case where the dataframe is empty"""
        df_financial = pd.DataFrame()

        result = format_tresorerie_data(df_financial)
        self.assertIsNone(result)

    def test_missing_columns(self):
        """Test the case where some columns are missing"""
        df_financial = pd.DataFrame({"receivables_1": [200], "payables_1": [300]})

        result = format_tresorerie_data(df_financial)

        # Only remaining columns should be transformed
        self.assertEqual(result["receivables"].iloc[0], 200)
        self.assertEqual(result["stock"].iloc[0], 0)


class TestCalculTresorerieRatios(unittest.TestCase):
    """Unit tests for the calcul_tresorerie_ratios function"""

    @patch("backend.src.services.calcul_ratios_tresorerie.get_necessary_data")
    @patch("backend.src.services.calcul_ratios_tresorerie.format_tresorerie_data")
    @patch("backend.src.services.calcul_ratios_tresorerie.calcul_fond_de_roulement")
    @patch(
        "backend.src.services.calcul_ratios_tresorerie.calcul_ratio_liquidite_generale"
    )
    @patch(
        "backend.src.services.calcul_ratios_tresorerie.calcul_ratio_liquidite_rapide"
    )
    @patch(
        "backend.src.services.calcul_ratios_tresorerie.calcul_ratio_liquidite_immediate"
    )
    @patch(
        "backend.src.services.calcul_ratios_tresorerie.calcul_besoins_en_fonds_de_roulement"
    )
    def test_valid_data(
        self,
        mock_besoins,
        mock_imm,
        mock_rapide,
        mock_generale,
        mock_fond,
        mock_format,
        mock_data,
    ):
        """Test the calculation of the treasury ratios with valid data"""
        financial_data = pd.DataFrame(
            {
                "actif_circulant": [10000],
                "dettes_courantes": [6000],
                "cash": [3000],
                "receivables": [2000],
                "stock": [500],
                "payables": [1000],
            }
        )

        mock_data.return_value = financial_data
        mock_format.return_value = financial_data

        mock_fond.return_value = 4000
        mock_generale.return_value = 1.67
        mock_rapide.return_value = 0.83
        mock_imm.return_value = 0.5
        mock_besoins.return_value = 1500

        # Run function
        result = calcul_tresorerie_ratios(numero_client=1)

        # Assertions for each ratio
        self.assertEqual(result["fond de roulement"]["value"], 4000)
        self.assertEqual(result["ratio de liquidité générale"]["value"], 1.67)
        self.assertEqual(result["ratio de liquidité rapide"]["value"], 0.83)
        self.assertEqual(result["ratio de liquidité immédiate"]["value"], 0.5)
        self.assertEqual(result["besoins en fonds de roulement"]["value"], 1500)

    def test_client_not_found(self):
        """Test the case where the client is not found"""
        with self.assertRaises(KeyError):
            calcul_tresorerie_ratios(numero_client=12345)

    @patch("backend.src.services.calcul_ratios_tresorerie.get_necessary_data")
    @patch(
        "backend.src.services.calcul_ratios_tresorerie.format_tresorerie_data",
        side_effect=KeyError,
    )
    def test_missing_columns(self, mock_format, mock_data):
        """Test the case where the financial data is missing columns"""
        with self.assertRaises(KeyError):
            calcul_tresorerie_ratios(numero_client=1)


if __name__ == "__main__":
    unittest.main()
