'''Unit tests for Ants Vs. SomeBees (ants.py).'''

import unittest
import doctest
import os
import sys
from ucb import main
import ants

class TestProblemA6(AntTest):

    def test_wall(self):
        error_msg = 'WallAnt isn\'t parameterized quite right'
        self.assertEqual(4, ants.WallAnt().armor, error_msg)
        self.assertEqual(4, ants.WallAnt.food_cost, error_msg)



@main
def main(*args):
    import argparse
    parser = argparse.ArgumentParser(description="Run Ants Tests")
    parser.add_argument('--verbose', '-v', action='store_true')
    args = parser.parse_args()
    doctest.testmod(ants, verbose=args.verbose)
    stdout = sys.stdout
    with open(os.devnull, 'w') as sys.stdout:
        verbosity = 2 if args.verbose else 1
        tests = unittest.main(exit=False, verbosity=verbosity)
    sys.stdout = stdout
