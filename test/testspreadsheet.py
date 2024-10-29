from unittest import TestCase
from spreadsheet import SpreadSheet


class TestSpreadSheet(TestCase):

    def test_evaluate_valid_integer(self):
        spreadsheet = SpreadSheet()
        spreadsheet.set("A1","1")
        self.assertEqual(1,spreadsheet.evaluate("A1"))


    def test_evaluate_invalid_integer(self):
        spreadsheet = SpreadSheet()
        spreadsheet.set("A1","1.5")
        self.assertEqual("#ERROR",spreadsheet.evaluate("A1"))


    def test_evaluate_valid_string(self):
        spreadsheet = SpreadSheet()
        spreadsheet.set("A1", "'Apple'")
        self.assertEqual("Apple", spreadsheet.evaluate("A1"))


    def test_evaluate_invalid_string(self):
        spreadsheet = SpreadSheet()
        spreadsheet.set("A1", "'Apple")
        self.assertEqual("#ERROR", spreadsheet.evaluate("A1"))


    def test_evaluate_valid_simple_formula_string(self):
        spreadsheet = SpreadSheet()
        spreadsheet.set("A1", "='Apple'")
        self.assertEqual("Apple", spreadsheet.evaluate("A1"))


    def test_evaluate_valid_simple_formula_integer(self):
        spreadsheet = SpreadSheet()
        spreadsheet.set("A1", "=1")
        self.assertEqual(1, spreadsheet.evaluate("A1"))


    def test_evaluate_invalid_simple_formula_string(self):
        spreadsheet = SpreadSheet()
        spreadsheet.set("A1", "='Apple")
        self.assertEqual("#ERROR", spreadsheet.evaluate("A1"))

    def test_evaluate_valid_simple_formula_ref(self):
        spreadsheet = SpreadSheet()
        spreadsheet.set("A1", "=B1")
        spreadsheet.set("B1", "42")

        self.assertEqual(42, spreadsheet.evaluate("A1"))

    def test_evaluate_valid_simple_formula_ref_string(self):
        spreadsheet = SpreadSheet()
        spreadsheet.set("A1", "=B1")
        spreadsheet.set("B1", "'Apple'")

        self.assertEqual("Apple", spreadsheet.evaluate("A1"))


    def test_evaluate_invalid_simple_formula_ref_sting(self):
        spreadsheet = SpreadSheet()
        spreadsheet.set("A1", "=B1")
        spreadsheet.set("B1", "'Apple")

        self.assertEqual("#ERROR", spreadsheet.evaluate("A1"))

    def test_evaluate_invalid_simple_formula_ref_circle(self):
        spreadsheet = SpreadSheet()
        spreadsheet.set("A1", "=A1")
        spreadsheet.set("B1", "42")

        self.assertEqual("#CIRCULAR", spreadsheet.evaluate("A1"))

    def test_evaluate_valid_formula_sum(self):
        spreadsheet = SpreadSheet()
        spreadsheet.set("A1", "=3+1")

        self.assertEqual(4, spreadsheet.evaluate("A1"))

    def test_evaluate_invalid_formula_sum(self):
        spreadsheet = SpreadSheet()
        spreadsheet.set("A1", "=3+1.5")

        self.assertEqual("#ERROR", spreadsheet.evaluate("A1"))


    def test_evaluate_valid_formula_div(self):
        spreadsheet = SpreadSheet()
        spreadsheet.set("A1", "=4/2")

        self.assertEqual(2, spreadsheet.evaluate("A1"))


    def test_evaluate_invalid_formula_div_by_zero(self):
        spreadsheet = SpreadSheet()
        spreadsheet.set("A1", "=1/0")

        self.assertEqual("#ERROR", spreadsheet.evaluate("A1"))

    def test_evaluate_valid_formula_times(self):
        spreadsheet = SpreadSheet()
        spreadsheet.set("A1", "=3*2")

        self.assertEqual(6, spreadsheet.evaluate("A1"))

    def test_evaluate_valid_formula_multiple_operations(self):
        spreadsheet = SpreadSheet()
        spreadsheet.set("A1", "=1+3*2")

        self.assertEqual(7, spreadsheet.evaluate("A1"))