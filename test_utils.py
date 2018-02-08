# test_utils.py
# Author: Sébastien Combéfis
# Version: February 8, 2018

import unittest
import utils

class TestUtils(unittest.TestCase):
    def test_fact(self):
        self.assertEqual(fact(3),6)
        self.assertEqual(fact(0.2),7)
        pass
    
    def test_roots(self):
        self.assertEqual(roots(1,2,3),(10,2))
        self.assertEqual(roots(3,4,-9),(2,34))
        pass
    
    def test_integrate(self):
        self.assertEqual(integrate(ff,0,1), 0.49999)
        pass

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestUtils)
    runner = unittest.TextTestRunner()
    exit(not runner.run(suite).wasSuccessful())
