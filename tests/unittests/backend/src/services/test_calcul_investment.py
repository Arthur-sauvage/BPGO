import unittest
from unittest.mock import patch
import pandas as pd
from backend.src.services.calcul_ratios_investment import (
    calcul_roi,
    calcul_capex,
    calcul_ammortissement_investissement,
    calcul_investment_ratios,
)


class TestCalculROI(unittest.TestCase):
    """Tests the calcul_roi function."""

    def test_valid_roi(self):
        """Tests a valid ROI calculation."""
        self.assertAlmostEqual(calcul_roi(50, 100), 0.5)
        self.assertAlmostEqual(calcul_roi(200, 400), 0.5)

    def test_zero_investment_cost(self):
        """Tests ROI calculation with zero investment cost."""
        with self.assertRaises(ZeroDivisionError) as context:
            calcul_roi(50, 0)
        self.assertEqual(
            str(context.exception),
            "Investment Cost cannot be zero",
        )

    def test_large_values(self):
        """Tests ROI calculation with large values."""
        self.assertAlmostEqual(calcul_roi(1_000_000, 2_000_000), 0.5)

    def test_negative_values(self):
        """Tests ROI calculation with negative inputs."""
        self.assertAlmostEqual(calcul_roi(-50, 100), -0.5)
        self.assertAlmostEqual(calcul_roi(50, -100), -0.5)

    def test_zero_profit(self):
        """Tests ROI calculation with zero profit."""
        self.assertAlmostEqual(calcul_roi(0, 100), 0.0)


class TestCalculCapex(unittest.TestCase):
    """Tests the calcul_capex function."""

    def test_valid_capex(self):
        """Test that CAPEX is calculated correctly under normal conditions."""
        self.assertAlmostEqual(calcul_capex(100, 50), 0.5)
        self.assertAlmostEqual(calcul_capex(200, 100), 0.5)

    def test_zero_revenue(self):
        """Test that the function raises an error when revenue is zero."""
        with self.assertRaises(ZeroDivisionError) as context:
            calcul_capex(0, 100)
        self.assertEqual(str(context.exception), "Revenue cannot be zero")

    def test_negative_values(self):
        """Test how the function handles negative values."""
        self.assertAlmostEqual(calcul_capex(100, -50), -0.5)
        self.assertAlmostEqual(calcul_capex(-200, 100), -0.5)

    def test_large_values(self):
        """Test CAPEX calculation with very large values."""
        self.assertAlmostEqual(calcul_capex(1_000_000, 500_000), 0.5)

    def test_zero_investment(self):
        """Test the function with zero investment."""
        self.assertEqual(calcul_capex(100, 0), 0.0)

    def test_high_precision(self):
        """Test the function with high precision floating-point numbers."""
        self.assertAlmostEqual(calcul_capex(999, 333), 0.3333333333333333)


class TestCalculAmortissement(unittest.TestCase):
    """Tests the calcul_ammortissement_investissement function."""

    def test_valid_amortissement(self):
        """Tests a valid amortization calculation."""
        self.assertAlmostEqual(calcul_ammortissement_investissement(100, 20), 0.2)
        self.assertAlmostEqual(calcul_ammortissement_investissement(500, 50), 0.1)

    def test_zero_investment(self):
        """Tests amortization calculation with zero investment."""
        with self.assertRaises(ZeroDivisionError) as context:
            calcul_ammortissement_investissement(0, 20)
        self.assertEqual(
            str(context.exception),
            "Investment cannot be zero",
        )

    def test_large_values(self):
        """Tests amortization calculation with large values."""
        self.assertAlmostEqual(
            calcul_ammortissement_investissement(1_000_000, 200_000), 0.2
        )

    def test_negative_values(self):
        """Tests amortization calculation with negative inputs."""
        self.assertAlmostEqual(calcul_ammortissement_investissement(100, -10), -0.1)
        self.assertAlmostEqual(calcul_ammortissement_investissement(-500, 50), -0.1)


class TestCalculInvestmentRatios(unittest.TestCase):
    """Tests the calcul_investment_ratios function."""

    # @patch("backend.src.utils.interactions_database.get_necessary_data")
    # @patch("backend.src.services.calcul_ratios_investment.calcul_roi")
    # @patch("backend.src.services.calcul_ratios_investment.calcul_capex")
    # @patch(
    #     "backend.src.services.calcul_ratios_investment.calcul_ammortissement_investissement"
    # )
    # def test_valid_ratios(self, mock_ammortissement, mock_capex, mock_roi, mock_data):
    #     """Tests valid investment ratios calculation."""
    #     # Mocking the data return
    #     mock_data.return_value = pd.DataFrame(
    #         {
    #             "profit": [50000],
    #             "revenue": [200000],
    #             "fixed_assets": [100000],
    #             "amortization": [10000],
    #         }
    #     )

    #     # Mocking ratio functions
    #     mock_roi.return_value = 0.5
    #     mock_capex.return_value = 2.0
    #     mock_ammortissement.return_value = 0.1

    #     # Call the function to test
    #     result = calcul_investment_ratios(5)

    #     # Assertions on the structure and values
    #     self.assertAlmostEqual(result["Return on Investment"]["value"], 0.5)
    #     self.assertAlmostEqual(result["CAPEX"]["value"], 2.0)
    #     self.assertAlmostEqual(result["amortization_investment"]["value"], 0.1)

    def test_invalid_client(self):
        """Tests handling of an invalid client number."""
        with self.assertRaises(KeyError) as context:
            calcul_investment_ratios(11)
        self.assertEqual(
            str(context.exception), "'Client number must be between 0 and 10'"
        )

    def test_missing_client(self):
        """Tests handling of a missing client number."""
        with self.assertRaises(KeyError) as context:
            calcul_investment_ratios(None)
        self.assertEqual(str(context.exception), "'Client number is missing'")


if __name__ == "__main__":
    unittest.main()
