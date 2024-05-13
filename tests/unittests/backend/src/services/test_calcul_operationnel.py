import unittest

def calcul_ebe(revenue, operating_costs):
    """Calculates the Earnings Before Interest."""
    if revenue is None:
        raise ValueError("Revenue is missing")
    if operating_costs is None:
        raise ValueError("Operating costs are missing")
    if revenue < 0 or operating_costs < 0:
        raise ValueError("Values must be positive")

    return revenue - operating_costs

class TestCalculEBE(unittest.TestCase):

    def test_valid_values(self):
        """Tests valid input values."""
        self.assertEqual(calcul_ebe(1000, 500), 500)
        self.assertEqual(calcul_ebe(2000, 1000), 1000)
        self.assertEqual(calcul_ebe(0, 0), 0)

    def test_zero_revenue(self):
        """Tests zero revenue scenario."""
        self.assertEqual(calcul_ebe(0, 100), -100)

    def test_zero_operating_costs(self):
        """Tests zero operating costs scenario."""
        self.assertEqual(calcul_ebe(1000, 0), 1000)

    def test_negative_revenue(self):
        """Tests negative revenue scenario."""
        with self.assertRaises(ValueError):
            calcul_ebe(-1000, 500)

    def test_negative_operating_costs(self):
        """Tests negative operating costs scenario."""
        with self.assertRaises(ValueError):
            calcul_ebe(1000, -500)

    def test_missing_revenue(self):
        """Tests missing revenue input."""
        with self.assertRaises(ValueError):
            calcul_ebe(None, 500)

    def test_missing_operating_costs(self):
        """Tests missing operating costs input."""
        with self.assertRaises(ValueError):
            calcul_ebe(1000, None)

# Running the tests
if __name__ == "__main__":
    unittest.main()
