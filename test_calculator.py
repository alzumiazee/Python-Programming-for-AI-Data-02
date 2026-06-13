import unittest

# Import the functions we want to test
from calculator import add_percentages, calculate_vat


class TestCalculatorFunctions(unittest.TestCase):
    def test_add_percentages_positive(self):
        """Test adding standard positive numbers."""
        self.assertEqual(add_percentages(10, 20), 30)

    def test_add_percentages_negative(self):
        """Test that negative percentage inputs resolve mathematically."""
        self.assertEqual(add_percentages(-5, 5), 0)

    def test_calculate_vat_valid(self):
        """Test standard VAT multiplication and decimal rounding."""
        self.assertEqual(calculate_vat(100, 0.15), 15.0)
        self.assertEqual(calculate_vat(10.55, 0.20), 2.11)

    def test_calculate_vat_negative_rate_error(self):
        """Test that a negative rate successfully triggers a ValueError."""
        with self.assertRaises(ValueError):
            calculate_vat(100, -0.05)


if __name__ == "__main__":
    unittest.main()
