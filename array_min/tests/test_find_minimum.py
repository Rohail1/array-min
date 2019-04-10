from unittest import TestCase
from array_min.minimum import find_minimum


class FindMinimumTest(TestCase):

    def testMinimum(self):

        # Duplicate Numbers in series
        self.assertEqual(find_minimum([9, 7, 6, 2, 3, 3, 4, 5, 7]), 2)

        self.assertEqual(find_minimum([100, 99, 98, 97, 16, 17, 18, 19, 22]), 16)
        self.assertEqual(find_minimum([55, 54, 53, 53, 51, 60, 62, 63]), 51)
        self.assertEqual(find_minimum([19, 18, 15, 14, 16, 17, 18, 20]), 14)

        # Only Decreasing Series
        self.assertEqual(find_minimum([19, 18, 15, 14, 13]), 13)

        # Only Increasing Series
        self.assertEqual(find_minimum([20, 21, 35, 66, 77]), 20)

