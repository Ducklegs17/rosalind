import os

import unittest
import decoder

class TestStringMethods(unittest.TestCase):
    def test_split_into_codons(self):
        self.assertEqual(decoder.split_into_codons("AAABBBCCC"), ["AAA","BBB","CCC"])

    def test_remove_stop(self):
        self.assertEqual(decoder.remove_stop("ABCStop"), "ABC")

if __name__ == "__main__":
    unittest.main()
