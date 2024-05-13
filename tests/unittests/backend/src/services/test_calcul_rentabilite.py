""" Tests for the calcul_ratios_rentabilite module. """

import unittest
from unittest.mock import patch
import pandas as pd
from backend.src.services.calcul_ratios_rentabilite import (
    calcul_ratio_marge_operationnelle,
    calcul_marge_nette,
    calcul_roe,
    calcul_roa,
    calcul_rentabilite_ratios,
)


class TestCalculRatioMargeOperationnelle(unittest.TestCase):
    """Tests the calcul_ratio_marge_operationnelle function."""

    def test_valid_ratio(self):
        """Tests a valid operating margin ratio calculation."""
        self.assertAlmostEqual(calcul_ratio_marge_operationnelle(50, 100), 0.5)
        self.assertAlmostEqual(calcul_ratio_marge_operationnelle(200, 400), 0.5)

    def test_zero_revenue(self):
        """Tests ratio calculation with zero revenue."""
        with self.assertRaises(ZeroDivisionError) as context:
            calcul_ratio_marge_operationnelle(50, 0)
        self.assertEqual(
            str(context.exception),
            "Revenue cannot be zero",
        )

    def test_large_values(self):
        """Tests ratio calculation with large values."""
        self.assertAlmostEqual(
            calcul_ratio_marge_operationnelle(1_000_000, 2_000_000), 0.5
        )

    def test_negative_values(self):
        """Tests ratio calculation with negative inputs."""
        self.assertAlmostEqual(calcul_ratio_marge_operationnelle(-50, 100), -0.5)
        self.assertAlmostEqual(calcul_ratio_marge_operationnelle(50, -100), -0.5)

    def test_zero_profit(self):
        """Tests ratio calculation with zero operating profit."""
        self.assertAlmostEqual(calcul_ratio_marge_operationnelle(0, 100), 0.0)


class TestCalculMargeNette(unittest.TestCase):
    """Tests the calcul_marge_nette function."""

    def test_valid_ratio(self):
        """Tests a valid net margin calculation."""
        self.assertAlmostEqual(calcul_marge_nette(50, 100), 0.5)
        self.assertAlmostEqual(calcul_marge_nette(200, 400), 0.5)

    def test_zero_revenue(self):
        """Tests ratio calculation with zero revenue."""
        with self.assertRaises(ZeroDivisionError) as context:
            calcul_marge_nette(50, 0)
        self.assertEqual(str(context.exception), "Revenue cannot be zero")

    def test_large_values(self):
        """Tests ratio calculation with large values."""
        self.assertAlmostEqual(calcul_marge_nette(1_000_000, 2_000_000), 0.5)

    def test_negative_values(self):
        """Tests ratio calculation with negative inputs."""
        self.assertAlmostEqual(calcul_marge_nette(-50, 100), -0.5)
        self.assertAlmostEqual(calcul_marge_nette(50, -100), -0.5)

    def test_zero_profit(self):
        """Tests ratio calculation with zero profit."""
        self.assertAlmostEqual(calcul_marge_nette(0, 100), 0.0)


class TestCalculROE(unittest.TestCase):
    """Tests the calcul_roe function."""

    def test_valid_ratio(self):
        """Tests a valid ROE calculation."""
        self.assertAlmostEqual(calcul_roe(50, 100), 0.5)
        self.assertAlmostEqual(calcul_roe(200, 400), 0.5)

    def test_zero_equity(self):
        """Tests ROE calculation with zero equity."""
        with self.assertRaises(ZeroDivisionError) as context:
            calcul_roe(50, 0)
        self.assertEqual(str(context.exception), "Equity cannot be zero")

    def test_large_values(self):
        """Tests ROE calculation with large values."""
        self.assertAlmostEqual(calcul_roe(1_000_000, 2_000_000), 0.5)

    def test_negative_values(self):
        """Tests ROE calculation with negative inputs."""
        self.assertAlmostEqual(calcul_roe(-50, 100), -0.5)
        self.assertAlmostEqual(calcul_roe(50, -100), -0.5)

    def test_zero_profit(self):
        """Tests ROE calculation with zero profit."""
        self.assertAlmostEqual(calcul_roe(0, 100), 0.0)


class TestCalculROA(unittest.TestCase):
    """Tests the calcul_roa function."""

    def test_valid_ratio(self):
        """Tests a valid ROA calculation."""
        self.assertAlmostEqual(calcul_roa(50, 100), 0.5)
        self.assertAlmostEqual(calcul_roa(200, 400), 0.5)

    def test_zero_assets(self):
        """Tests ROA calculation with zero assets."""
        with self.assertRaises(ZeroDivisionError) as context:
            calcul_roa(50, 0)
        self.assertEqual(str(context.exception), "Total Assets cannot be zero")

    def test_large_values(self):
        """Tests ROA calculation with large values."""
        self.assertAlmostEqual(calcul_roa(1_000_000, 2_000_000), 0.5)

    def test_negative_values(self):
        """Tests ROA calculation with negative inputs."""
        self.assertAlmostEqual(calcul_roa(-50, 100), -0.5)
        self.assertAlmostEqual(calcul_roa(50, -100), -0.5)

    def test_zero_profit(self):
        """Tests ROA calculation with zero profit."""
        self.assertAlmostEqual(calcul_roa(0, 100), 0.0)


class TestCalculRentabiliteRatios(unittest.TestCase):
    """Tests the calcul_rentabilite_ratios function."""

    @patch("backend.src.utils.interactions_database.get_necessary_data")
    @patch(
        "backend.src.services.calcul_ratios_rentabilite.calcul_ratio_marge_operationnelle"
    )
    @patch("backend.src.services.calcul_ratios_rentabilite.calcul_marge_nette")
    @patch("backend.src.services.calcul_ratios_rentabilite.calcul_roe")
    @patch("backend.src.services.calcul_ratios_rentabilite.calcul_roa")
    def test_valid_client_simplifie(
        self, mock_roa, mock_roe, mock_marge_nette, mock_marge_op, mock_data
    ):
        """Tests valid client with simplified financial structure."""
        mock_data.return_value = pd.DataFrame(
            {
                "profit": [50000],
                "equity": [100000],
                "total_assets": [200000],
                "resultat_exploitation": [40000],
                "revenue": [150000],
            }
        )

        mock_marge_op.return_value = 0.2667
        mock_marge_nette.return_value = 0.3333
        mock_roe.return_value = 0.5
        mock_roa.return_value = 0.25

        result = calcul_rentabilite_ratios(5)

        self.assertAlmostEqual(
            result["Ratio de marge operationnelle"]["value"], 0.2667, places=4
        )
        self.assertAlmostEqual(result["Marge nette"]["value"], 0.3333, places=4)

    def test_invalid_client_number(self):
        """Tests handling of an invalid client number."""
        with self.assertRaises(KeyError) as context:
            calcul_rentabilite_ratios(11)
        self.assertEqual(
            str(context.exception), "'Client number must be between 0 and 10'"
        )

    def test_missing_client_number(self):
        """Tests handling of a missing client number."""
        with self.assertRaises(KeyError) as context:
            calcul_rentabilite_ratios(None)
        self.assertEqual(str(context.exception), "'Client number is missing'")


if __name__ == "__main__":
    unittest.main()
