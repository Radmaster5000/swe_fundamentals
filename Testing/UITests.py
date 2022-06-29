import unittest


class UITests(unittest.TestCase):
    def test_invalid_input(self):
        self.assertEqual(True, False)  # add assertion here


if __name__ == '__main__':
    unittest.main()
