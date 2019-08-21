import unittest
from src.utils.counter import Counter


class TestCount(unittest.TestCase):

    def test_count_positive(self):
        self.assertEqual(Counter.count_zeros('ADas@#RSSDCV000000SDAA0AD000ADS'), 6)
        self.assertEqual(Counter.count_zeros('ASDNOVDfasaVSMAPSPXKSMSPD'), 0)
        self.assertEqual(Counter.count_zeros('ghddhgbgesafhisufdhsahdlhsdflsahdfjsdfsdfds0sdfsdfsfsd'), 1)

    def test_count_exception(self):
        self.assertRaises(TypeError, Counter.count_zeros(11521532))
        self.assertFalse(Counter.count_zeros(1252436345))

