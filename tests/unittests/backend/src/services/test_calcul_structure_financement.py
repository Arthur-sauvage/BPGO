""" Tests for the calcul_ratios_structure_financement module. """

import unittest
from unittest.mock import patch
import pandas as pd
from backend.src.services.calcul_ratios_structure_financement import (
    calcul_ratio_endettement,
    calcul_ratio_solvabilite,
    calcul_ratio_dettes_long_terme_fonds_propres,
    calcul_ratio_couverture_interets,
    format_financement_structure_data,
    calcul_financement_structure_ratios,
)


class TestCalculRatioEndettement(unittest.TestCase):
    """Tests the calcul_ratio_endettement function."""

    def test_valid_ratio(self):
        """Tests a valid endettement ratio calculation."""
        self.assertAlmostEqual(calcul_ratio_endettement(100, 50), 0.5)
        self.assertAlmostEqual(calcul_ratio_endettement(200, 100), 0.5)

    def test_zero_capital(self):
        """Tests ratio calculation with zero capital."""
        with self.assertRaises(ZeroDivisionError) as context:
            calcul_ratio_endettement(0, 50)
        self.assertEqual(
            str(context.exception),
            "Share Capital cannot be zero",
        )

    def test_large_values(self):
        """Tests ratio calculation with large values."""
        self.assertAlmostEqual(calcul_ratio_endettement(1_000_000, 500_000), 0.5)

    def test_negative_values(self):
        """Tests ratio calculation with negative inputs."""
        self.assertAlmostEqual(calcul_ratio_endettement(100, -50), -0.5)
        self.assertAlmostEqual(calcul_ratio_endettement(-100, 50), -0.5)

    def test_zero_debt(self):
        """Tests ratio calculation with zero debt."""
        self.assertAlmostEqual(calcul_ratio_endettement(100, 0), 0.0)


class TestCalculRatioSolvabilite(unittest.TestCase):
    """Tests the calcul_ratio_solvabilite function."""

    def test_valid_ratio(self):
        """Tests a valid solvability ratio calculation."""
        self.assertAlmostEqual(calcul_ratio_solvabilite(50, 100), 0.5)
        self.assertAlmostEqual(calcul_ratio_solvabilite(100, 200), 0.5)

    def test_zero_total_actif(self):
        """Tests ratio calculation with zero total_actif."""
        with self.assertRaises(ZeroDivisionError) as context:
            calcul_ratio_solvabilite(50, 0)
        self.assertEqual(
            str(context.exception),
            "Total Actif cannot be zero",
        )

    def test_large_values(self):
        """Tests ratio calculation with large values."""
        self.assertAlmostEqual(calcul_ratio_solvabilite(500_000, 1_000_000), 0.5)

    def test_negative_values(self):
        """Tests ratio calculation with negative inputs."""
        self.assertAlmostEqual(calcul_ratio_solvabilite(-50, 100), -0.5)
        self.assertAlmostEqual(calcul_ratio_solvabilite(50, -100), -0.5)

    def test_zero_capital(self):
        """Tests ratio calculation with zero capital_social."""
        self.assertAlmostEqual(calcul_ratio_solvabilite(0, 100), 0.0)


class TestCalculRatioDettesLongTermeFondsPropres(unittest.TestCase):
    """Tests the calcul_ratio_dettes_long_terme_fonds_propres function."""

    def test_valid_ratio(self):
        """Tests a valid long-term debt to equity ratio calculation."""
        self.assertAlmostEqual(
            calcul_ratio_dettes_long_terme_fonds_propres(100, 50), 0.5
        )
        self.assertAlmostEqual(
            calcul_ratio_dettes_long_terme_fonds_propres(200, 100), 0.5
        )

    def test_zero_capital(self):
        """Tests ratio calculation with zero capital."""
        with self.assertRaises(ZeroDivisionError) as context:
            calcul_ratio_dettes_long_terme_fonds_propres(0, 50)
        self.assertEqual(
            str(context.exception),
            "Share Capital cannot be zero",
        )

    def test_large_values(self):
        """Tests ratio calculation with large values."""
        self.assertAlmostEqual(
            calcul_ratio_dettes_long_terme_fonds_propres(1_000_000, 500_000), 0.5
        )

    def test_negative_values(self):
        """Tests ratio calculation with negative inputs."""
        self.assertAlmostEqual(
            calcul_ratio_dettes_long_terme_fonds_propres(100, -50), -0.5
        )
        self.assertAlmostEqual(
            calcul_ratio_dettes_long_terme_fonds_propres(-100, 50), -0.5
        )

    def test_zero_debt(self):
        """Tests ratio calculation with zero long-term debt."""
        self.assertAlmostEqual(
            calcul_ratio_dettes_long_terme_fonds_propres(100, 0), 0.0
        )


class TestCalculRatioCouvertureInterets(unittest.TestCase):
    """Tests the calcul_ratio_couverture_interets function."""

    def test_valid_ratio(self):
        """Tests a valid interest coverage ratio calculation."""
        self.assertAlmostEqual(calcul_ratio_couverture_interets(100, 50), 2.0)
        self.assertAlmostEqual(calcul_ratio_couverture_interets(200, 100), 2.0)

    def test_zero_interets(self):
        """Tests ratio calculation with zero interets."""
        with self.assertRaises(ZeroDivisionError) as context:
            calcul_ratio_couverture_interets(50, 0)
        self.assertEqual(
            str(context.exception),
            "Interests cannot be zero",
        )

    def test_large_values(self):
        """Tests ratio calculation with large values."""
        self.assertAlmostEqual(
            calcul_ratio_couverture_interets(1_000_000, 500_000), 2.0
        )

    def test_negative_values(self):
        """Tests ratio calculation with negative inputs."""
        self.assertAlmostEqual(calcul_ratio_couverture_interets(100, -50), -2.0)
        self.assertAlmostEqual(calcul_ratio_couverture_interets(-100, 50), -2.0)

    def test_zero_resultat(self):
        """Tests ratio calculation with zero resultat_exercice."""
        self.assertAlmostEqual(calcul_ratio_couverture_interets(0, 100), 0.0)


class TestFormatFinancementStructureData(unittest.TestCase):

    def test_empty_dataframe(self):
        """Tests the function with an empty dataframe."""
        df = pd.DataFrame()
        self.assertIsNone(format_financement_structure_data(df))

    def test_multiple_rows(self):
        """Tests the function with multiple rows."""
        df = pd.DataFrame(
            {
                "lt_dettes_financieres_1": [100, 200],
                "lt_dettes_financieres_2": [50, 150],
            }
        )
        formatted_df = format_financement_structure_data(df)

        # Check it only retains the first row
        self.assertEqual(formatted_df.shape[0], 1)

    def test_missing_columns(self):
        """Tests the function with missing columns."""
        df = pd.DataFrame(
            {
                "lt_dettes_financieres_1": [100],
            }
        )

        formatted_df = format_financement_structure_data(df)

        # Check that lt_dettes_financieres is calculated correctly
        self.assertEqual(formatted_df["lt_dettes_financieres"].iloc[0], 100)

    def test_complete_dataframe(self):
        """Tests the function with a complete dataframe."""
        df = pd.DataFrame(
            {
                "lt_dettes_financieres_1": [100],
                "lt_dettes_financieres_2": [50],
            }
        )

        formatted_df = format_financement_structure_data(df)

        # Check that lt_dettes_financieres is calculated correctly
        self.assertEqual(formatted_df["lt_dettes_financieres"].iloc[0], 150)


class TestCalculFinancementStructureRatios(unittest.TestCase):
    """Tests the calcul_financement_structure_ratios function."""

    @patch("backend.src.utils.interactions_database.get_necessary_data")
    @patch(
        "backend.src.services.calcul_ratios_structure_financement.calcul_ratio_endettement"
    )
    @patch(
        "backend.src.services.calcul_ratios_structure_financement.calcul_ratio_solvabilite"
    )
    @patch(
        "backend.src.services.calcul_ratios_structure_financement.calcul_ratio_dettes_long_terme_fonds_propres"
    )
    @patch(
        "backend.src.services.calcul_ratios_structure_financement.calcul_ratio_couverture_interets"
    )
    def test_valid_client_simplifie(
        self,
        mock_couverture,
        mock_long_term,
        mock_solvabilite,
        mock_endettement,
        mock_data,
    ):
        """Tests valid client with simplified financial structure."""
        mock_data.return_value = pd.DataFrame(
            {
                "fonds_propres": [100000],
                "dettes_courantes": [50000],
                "lt_dettes_financieres_1": [15000],
                "lt_dettes_financieres_2": [10000],
                "resultat_exploitation": [20000],
                "interets": [5000],
                "total_actif": [150000],
            }
        )

        mock_endettement.return_value = 0.5
        mock_solvabilite.return_value = 0.6667
        mock_long_term.return_value = 0.25
        mock_couverture.return_value = 4.0

        result = calcul_financement_structure_ratios(5)

        self.assertAlmostEqual(result["Ratio d'endettement"]["value"], 0.5)
        self.assertAlmostEqual(
            result["Ratio de solvabilité"]["value"], 0.6667, places=4
        )

    def test_invalid_client_number(self):
        """Tests handling of an invalid client number."""
        with self.assertRaises(KeyError) as context:
            calcul_financement_structure_ratios(11)
        self.assertEqual(
            str(context.exception), "'Client number must be between 0 and 10'"
        )

    def test_missing_client_number(self):
        """Tests handling of a missing client number."""
        with self.assertRaises(KeyError) as context:
            calcul_financement_structure_ratios(None)
        self.assertEqual(str(context.exception), "'Client number is missing'")


if __name__ == "__main__":
    unittest.main()
