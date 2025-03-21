"""This module defines the TestChatbot class.

The TestChatbot class contains unit test methods to test the 
src.chatbot.Chatbot class.

You must execute this module in command-line where your present
working directory is the root directory of the project.

Example:
    python -m unittest tests/test_chatbot.py
"""

__author__ = "COMP-1327 Faculty"
__version__ = "1.0.2025"

from unittest import TestCase, main
from unittest.mock import patch
from src.chatbot import ACCOUNTS, VALID_TASKS, get_amount

#Unit tests for the chatbot module.
class TestChatbot(TestCase):

    # Test that get_amount raises TypeError for non-numeric input.
    def test_get_amount_non_numeric(self):
        with patch('builtins.input', return_value="abc"):
            with self.assertRaises(TypeError) as cm:
                get_amount()
            
            # Assuring that amount must be a numeric type.
            self.assertEqual(str(cm.exception), "Amount must be a numeric type.")
 
    #Test that get_amount raises ValueError for zero input.
    def test_get_amount_zero(self):
        with patch('builtins.input', return_value="0"):
            with self.assertRaises(ValueError) as cm:
                get_amount()
            # Amount must be a value greater than zero.
            self.assertEqual(str(cm.exception), "Amount must be a value greater than zero")

    # Test that get_amount raises ValueError for negative input.
    def test_get_amount_negative(self):
        with patch('builtins.input', return_value="-5"):
            with self.assertRaises(ValueError) as cm:
                get_amount()
            # Amount must be a value greater than zero.
            self.assertEqual(str(cm.exception),"Amount must be a value greater than zero")

    # Test that get_amount returns a float for valid positive input.
    def test_get_amount_valid(self):
        with patch('builtins.input', return_value="10.5"):
            result = get_amount()
            self.assertEqual(result, 10.5)
            self.assertIsInstance(result, float)

if __name__ == '__main__':
    main()