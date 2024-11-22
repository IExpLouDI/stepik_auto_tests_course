import unittest


class TestAbs(unittest.TestCase):

	def test_1(self):
		assert abs(-42) == 42, "Should be absolute value of a number"

	def test_2(self):
		assert abs(-42) == - 42, "Should be absolute value of a number"


if __name__ == "__main__":
	unittest.main()
