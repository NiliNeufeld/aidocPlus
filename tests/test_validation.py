import unittest
from BL.validations import Validations


class TestSearchValidation(unittest.TestCase):

    def setUp(self) -> None:
        self.val = Validations()

    def test_valid_input(self):
        # Arrange
        str0 = "abc"

        # Act
        output = self.val.search_validation(str0)

        # Assert
        self.assertTrue(output)

    def test_invalid_input_too_short(self):
        # Arrange
        str1 = "ab"

        # Act
        output = self.val.search_validation(str1)

        # Assert
        self.assertFalse(output)

    def test_invalid_input_contains_digit(self):
        # Arrange
        str2 = "abc1"

        # Act
        output = self.val.search_validation(str2)

        # Assert
        self.assertFalse(output)

