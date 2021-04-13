import unittest
from main import bubbleSort

class TestStringMethods(unittest.TestCase):

    def test_empty(self):
        self.assertEqual(bubbleSort([]), [])

    def test_one_element_array(self):
        self.assertEqual(bubbleSort(["1"]), ["1"])

    def test_simple_strings(self):
        self.assertEqual(bubbleSort(["b", "a", "c"]), ["a", "b", "c"])

    def test_numbers(self):
        self.assertEqual(bubbleSort([3, 1, 2]), [1, 2, 3])

    def test_number_long(self):
        self.assertEqual(bubbleSort([5, 7, 4, 1, 8, 10]), ([1, 4, 5, 7, 8, 10]))

    def test_simple_strings_different_register(self):
        self.assertEqual(bubbleSort(["a", "A", "B", "b"]), ["A", "B", "a", "b"])

    def test_simple_strings_special_symbol(self):
        self.assertEqual(bubbleSort(["a", "A", "!", "B"]), ["!", "A", "B", "a"])

    def test_simple_strings_special_symbol_and_numbers_and_register(self):
        self.assertEqual(bubbleSort(["a", "5", "!", "B"]), ["!", "5", "B", "a"])

    def test_long_strings(self):
        self.assertEqual(bubbleSort(["aaa", "aba", "aab", "bba"]), ["aaa", "aab", "aba", "bba"])

    def test_long_strings_different_cases_1(self):
        self.assertEqual(bubbleSort(["Aaa", "aba", "Bab", "bba"]), ["Aaa", "Bab", "aba", "bba"])

    def test_long_strings_different_cases_2(self):
        self.assertEqual(bubbleSort(["bbF", "Aaa", "ABA", "Cba", "Bab", "bba"]), ["ABA", "Aaa", "Bab", "Cba", "bbF", "bba"])

    def test_long_strings_special_symbol(self):
        self.assertEqual(bubbleSort(["!", "a!", "@a!"]), ["!", "@a!", "a!"])

    def test_long_strings_special_symbol_different_cases(self):
        self.assertEqual(bubbleSort(["A!", "a!", "@a!"]), ["@a!", "A!", "a!"])

    def test_equal_elements(self):
        self.assertEqual(bubbleSort(["a", "a", "a"]), ["a", "a", "a"])

if __name__ == '__main__':
    unittest.main()