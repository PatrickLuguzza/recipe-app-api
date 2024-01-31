"""
Sample tests
"""
from django.test import SimpleTestCase

from papp import calc


class CalcTest(SimpleTestCase):
    """Test the calc module"""

    def test_add_number(self):
        """Test adding numbers"""
        res = calc.add(5, 6)

        self.assertEqual(res, 11)

    def test_subtract_number(self):
        """Test subtract numbers"""
        res = calc.subtract(10, 15)

        self.assertEqual(res, 5)
