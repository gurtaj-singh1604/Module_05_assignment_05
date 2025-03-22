"""This module defines the Chatbot application.

Allows the user to perform balance inquiries and make 
deposits to their accounts.

Example:
    $ python src/chatbot.py
"""

__author__ = "COMP-1327 Faculty, Gurtaj Singh"
__version__ = "20.03.2025"

ACCOUNTS = {
    123456: {
        "balance": 1000.0
    },
    789012: {
        "balance": 2000.0
    }
} 

VALID_TASKS = [
    "balance", 
    "deposit", 
    "exit"
]

def get_account_number():
    try:
        # Prompt the user to enter an account number and convert the input string to an integer
        account_number = int(input("Please enter your account number: "))
    except ValueError:
        # Raise a TypeError if the input is not a valid integer (e.g., "abc" or "12.5")
        raise TypeError("Account number must be an int type.")
    
    # Check if the entered account number exists in the ACCOUNTS dictionary
    if account_number not in ACCOUNTS:
        raise ValueError("Account number entered does not exist.")
    
    # Return the validated account number if it passes all checks
    return account_number

def get_amount():
    try:
        # Prompt user for input and convert it to a float
        amount = float(input("Enter an amount: "))
    except ValueError:
        # Raise TypeError if the input cannot be converted to a float
        raise TypeError("Amount must be a numeric type.")
    
    # Check if the amount is zero or negative
    if amount <= 0:
        raise ValueError("Amount must be a value greater than zero.")
    
    # Return the validated amount as a float
    return amount

def get_balance(account_number):
    # Validate that account_number is an integer
    if not isinstance(account_number, int):
        raise TypeError("Account number must be an int type.")
    
    # Validate that account_number exists in ACCOUNTS
    if account_number not in ACCOUNTS:
        raise ValueError("Account number does not exist.")
    
    # Get the balance from ACCOUNTS and format it as currency
    balance = ACCOUNTS[account_number]["balance"]
    formatted_balance = f"${balance:,.2f}"
    
    # Return the formatted string
    return f"Your current balance for account {account_number} is {formatted_balance}."

def make_deposit(account_number, amount):
    # Validate that account_number is an integer
    if not isinstance(account_number, int):
        raise TypeError("Account number must be an int type.")

    # Validate that account_number exists in ACCOUNTS
    if account_number not in ACCOUNTS:
        raise ValueError("Account number does not exist.")

    # Validate that amount is numeric (int or float)
    if not isinstance(amount, (int, float)):
        raise ValueError("Amount must be a numeric type.")

    # Validate that amount is greater than zero
    if amount <= 0:
        raise ValueError("Amount must be a value greater than zero.")

    # Update the balance in ACCOUNTS by adding the amount
    ACCOUNTS[account_number]["balance"] += float(amount)

    # Format the amount as currency (e.g., $1,500.01)
    formatted_amount = f"${amount:,.2f}"

    # Return the confirmation message
    return f"You have made a deposit of {formatted_amount} to account {account_number}."

def get_task():
    task = input("What would you like to do (balance/deposit/exit)?: ").lower()
    if task not in VALID_TASKS:
        raise ValueError(f'"{task}" is an unknown task.')
    return task
    
def chatbot():
    """Performs the Chatbot functionality."""
    COMPANY_NAME = "PiXELL River Financial"
    
    # Print welcome message
    print(f"Welcome! I'm the {COMPANY_NAME} Chatbot! Let's get chatting!")

    # For getting the account number once at the start
    try:
        account_number = get_account_number()
    except (ValueError, TypeError) as e:
        # Print exception message
        print(e)
        # Print thank you message
        print(f"Thank you for banking with {COMPANY_NAME}.")
        # Exiting the function if account number is invalid
        return
    
    # Main loop to process tasks
    while True:
        # Get the task
        try:
            task = get_task()
        except ValueError as e:
            print(e)  
            continue  
        
        # Check if the task is "exit"
        if task == "exit":
            break
        
        # Handle "deposit" task
        if task == "deposit":
            try:
                amount = get_amount()
                deposit_message = make_deposit(account_number, amount)
                print(deposit_message)
            except (ValueError, TypeError) as e:
                print(e)  
        
        # Handle "balance" task
        elif task == "balance":
            try:
                balance_message = get_balance(account_number)
                print(balance_message)
            except (ValueError, TypeError) as e:
                print(e)  
    
    # Print thank-you message before exiting
    print(f"Thank you for banking with {COMPANY_NAME}.")

if __name__ == "__main__":
    chatbot()
