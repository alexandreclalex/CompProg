from io import StringIO
import sys
import time
import unittest
from unittest.mock import patch
import merch_madness as mm

# Testing stdin and stdout from https://ryip.me/posts/python/unittest-stdout-stderr/

class TestMerchMadness(unittest.TestCase):
    @patch('sys.stdin', open("inputs/singleInputSuccess.txt"))
    @patch('sys.stdout', new_callable = StringIO)
    def test_single_success(self, stdout):
        mm.execute()

        expected_output = f"100"

        actual_output = stdout.getvalue().strip("\n")

        self.assertEqual(expected_output, actual_output)

        sys.stdin.close()

    @patch('sys.stdin', open("inputs/squareInputNoStock.txt"))
    @patch('sys.stdout', new_callable = StringIO)
    def test_square_no_stock(self, stdout):
        mm.execute()

        expected_output = f"out of stock"

        actual_output = stdout.getvalue().strip("\n")

        self.assertEqual(expected_output, actual_output)

        sys.stdin.close()

    @patch('sys.stdin', open("inputs/squareInputOutOfStock.txt"))
    @patch('sys.stdout', new_callable = StringIO)
    def test_square_out_of_stock(self, stdout):
        mm.execute()

        expected_output = f"out of stock"

        actual_output = stdout.getvalue().strip("\n")

        self.assertEqual(expected_output, actual_output)

        sys.stdin.close()

    @patch('sys.stdin', open("inputs/squareInputSuccess.txt"))
    @patch('sys.stdout', new_callable = StringIO)
    def test_square_success(self, stdout):
        mm.execute()

        expected_output = f"50"

        actual_output = stdout.getvalue().strip("\n")

        self.assertEqual(expected_output, actual_output)

        sys.stdin.close()

    @patch('sys.stdin', open("inputs/squareInputRedirect.txt"))
    @patch('sys.stdout', new_callable = StringIO)
    def test_square_redirect_success(self, stdout):
        mm.execute()

        expected_output = f"250"

        actual_output = stdout.getvalue().strip("\n")

        self.assertEqual(expected_output, actual_output)

        sys.stdin.close()

    @patch('sys.stdin', open("inputs/squareInputRedirectCorners.txt"))
    @patch('sys.stdout', new_callable = StringIO)
    def test_square_redirect_corners_success(self, stdout):
        mm.execute()

        expected_output = f"350"

        actual_output = stdout.getvalue().strip("\n")

        self.assertEqual(expected_output, actual_output)

        sys.stdin.close()

    @patch('sys.stdin', open("inputs/generalInputSuccess.txt"))
    @patch('sys.stdout', new_callable = StringIO)
    def test_general_input(self, stdout):
        mm.execute()

        expected_output = f"out of stock"

        actual_output = stdout.getvalue().strip("\n")

        self.assertEqual(expected_output, actual_output)

        sys.stdin.close()

    @patch('sys.stdin', open("inputs/maxInput.txt"))
    @patch('sys.stdout', new_callable = StringIO)
    def test_single_success(self, stdout):

        start = time.time()

        mm.execute()

        end = time.time()

        self.assertLess(end - start, 1)

        sys.stdin.close()
