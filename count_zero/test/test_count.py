import unittest
from src.utils.counter import Counter


class TestCount(unittest.TestCase):

    def test_count_positive_1(self):
        self.assertEqual(Counter.count_zeroes('ADas@#RSSDCV000000SDAA0AD000ADS'), 6)

    def test_count_positive_2(self):
        self.assertEqual(Counter.count_zeroes('ASDNOVDfasaVSMAPSPXKSMSPD'), 0)

    def test_count_positive_3(self):
        self.assertEqual(Counter.count_zeroes('ghddhgbgesafhisufdhsahdlhsdflsahdfjsdfsdfds0sdfsdfsfsd'), 1)

    def test_count_negative(self):
        self.assertEqual(Counter.count_zeroes(11521532), '\tNot a string')
