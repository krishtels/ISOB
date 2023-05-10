import unittest
from caesar_code import CaesarCode
from vegener_code import VigenereCode


class TestCaesar(unittest.TestCase):
    def setUp(self):
        self.code = CaesarCode.code
        self.decode = CaesarCode.decode

    def test_case_1(self):
        self.assertEqual(self.code('abc', 3), 'def')

    def test_case_2(self):
        self.assertEqual(self.code('awfdsfdnsjnfzfrer', 12), 'mirperpzevzrlrdqd')

    def test_case_3(self):
        self.assertEqual(self.decode('mirperp zevzrl rdqd', 12), 'awfdsfd nsjnfz frer')

    def test_case_4(self):
        self.assertEqual(self.code(self.decode('mirperpzevzrlrdqd', 12), 12), 'mirperpzevzrlrdqd')


class TestVigenereCipher(unittest.TestCase):
    def setUp(self):
        self.code = VigenereCode.code
        self.decode = VigenereCode.decode

    def test_case_1(self):
        self.assertEqual(self.code('aaaaaaaa aaaaaa aaaaaaaaaa', 'ab'), 'abababab bababa ababababab')

    def test_case_2(self):
        self.assertEqual(self.code('qewrtryyuv', 'a'), 'qewrtryyuv')

    def test_case_3(self):
        self.assertEqual(self.code(self.decode('erkfljigojeroiergikfkjg', 'lemon'), 'lemon'), 'erkfljigojeroiergikfkjg')


if __name__ == "__main__":
    unittest.main()
