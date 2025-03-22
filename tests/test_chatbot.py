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
from src.chatbot import ACCOUNTS, VALID_TASKS, get_amount, get_balance, make_deposit

#Unit tests for the chatbot module.
class TestChatbot(TestCase):

    # Test that get_amount raises TypeError for non-numeric input.
    def test_get_amount_non_numeric(self):
        '''Test that get_amount raises TypeError for non-numeric input'''
        with patch('builtins.input', return_value="abc"):
            with self.assertRaises(TypeError) as cm:
                get_amount()
            
            # (Assert)Assuring that amount must be a numeric type.
            self.assertEqual(str(cm.exception), "Amount must be a numeric type.")
 
    #Test that get_amount raises ValueError for zero input.
    def test_get_amount_zero(self):
        '''Test that get_amount raises ValueError for zero input.'''
        with patch('builtins.input', return_value="0"):
            with self.assertRaises(ValueError) as cm:
                get_amount()
            # (Assert)Amount must be a value greater than zero.
            self.assertEqual(str(cm.exception), "Amount must be a value greater than zero")

    # Test that get_amount raises ValueError for negative input.
    def test_get_amount_negative(self):
        '''Test that get_amount raises ValueError for negative input.'''
        with patch('builtins.input', return_value="-5"):
            with self.assertRaises(ValueError) as cm:
                get_amount()
            # (Assert)Amount must be a value greater than zero.
            self.assertEqual(str(cm.exception),"Amount must be a value greater than zero")

    # Test that get_amount returns a float for valid positive input
    def test_get_amount_valid(self):
        '''Test that get_amount returns a float for valid positive input.'''
        with patch('builtins.input', return_value="10.5"):
            result = get_amount()
            # Assert
            self.assertEqual(result, 10.5)
            self.assertIsInstance(result, float)

    # Test that get_balance raises TypeError for non-integer account number.
    def test_get_balance_non_integer(self):
        """Test that get_balance raises TypeError for non-integer account number."""
        invalid_account_number = "123456"
        # Act & Assert
        with self.assertRaises(TypeError) as cm:
            get_balance(invalid_account_number)
        self.assertEqual(str(cm.exception), "Account number must be an int type.")

    # Test that get_balance raises ValueError for non-existent account number.
    def test_get_balance_non_existent_account(self):
        """Test that get_balance raises ValueError for non-existent account number."""
        non_existent_account = 999999
        # Act & Assert
        with self.assertRaises(ValueError) as cm:
            get_balance(non_existent_account)
        self.assertEqual(str(cm.exception), "Account number does not exist.")

    #Test that get_balance returns the correct balance message for a valid account.
    def test_get_balance_valid(self):
        """Test that get_balance returns the correct balance message for a valid account."""
        valid_account_number = 123456
        expected_message = "Your current balance for account 123456 is $1,000.00."
        # Act
        result = get_balance(valid_account_number)
        # Assert
        self.assertEqual(result, expected_message)
    
    def setUp(self):
    # Reset ACCOUNTS to initial state before each test
        ACCOUNTS.clear()
        ACCOUNTS.update({
        123456: {"balance": 1000.0},
        789012: {"balance": 2000.0}
    })
    
    def test_make_deposit_success(self):
        """Test that make_deposit updates the balance and returns the correct message."""
        account_number = 123456
        amount = 500.01
        initial_balance = ACCOUNTS[account_number]["balance"]  # Capture initial balance
        expected_message = f"You have made a deposit of ${amount:,.2f} to account {account_number}."
        
        result = make_deposit(account_number, amount)
        
        self.assertEqual(result, expected_message)  # Check the returned message
        self.assertEqual(ACCOUNTS[account_number]["balance"], initial_balance + amount)
                         
    def test_make_deposit_non_integer_account(self):
        """Test that make_deposit raises TypeError for non-integer account number."""
        with self.assertRaises(TypeError) as cm:
            make_deposit("123456", 100.0)
        self.assertEqual(str(cm.exception), "Account number must be an int type.")

    def test_make_deposit_non_existent_account(self):
        """Test that make_deposit raises ValueError for non-existent account number."""
        with self.assertRaises(ValueError) as cm:
            make_deposit(999999, 100.0)
        self.assertEqual(str(cm.exception), "Account number does not exist.")

    def test_make_deposit_non_numeric_amount(self):
        """Test that make_deposit raises ValueError for non-numeric amount."""
        with self.assertRaises(ValueError) as cm:
            make_deposit(123456, "abc")
        self.assertEqual(str(cm.exception), "Amount must be a numeric type.")

    def test_make_deposit_zero_amount(self):
        """Test that make_deposit raises ValueError for zero amount."""
        with self.assertRaises(ValueError) as cm:
            make_deposit(123456, 0)
        self.assertEqual(str(cm.exception), "Amount must be a value greater than zero.")

    def test_make_deposit_negative_amount(self):
        """Test that make_deposit raises ValueError for negative amount."""
        with self.assertRaises(ValueError) as cm:
             make_deposit(123456, -100.0)
        self.assertEqual(str(cm.exception), "Amount must be a value greater than zero.")
    
    @patch('builtins.input', return_value="withdraw")
    def test_get_task_invalid(self, mock_input):
        """Test that get_task raises ValueError for invalid task."""
        with self.assertRaises(ValueError) as cm:
            get_task()
        self.assertEqual(str(cm.exception), '"withdraw" is an unknown task.')

    @patch('builtins.input', return_value="EXIT")
    def test_get_task_valid(self, mock_input):
        """Test that get_task returns valid task in lowercase."""
        result = get_task()
        self.assertEqual(result, "exit")

if __name__ == '__main__':
    main()