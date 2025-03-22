## Reflection

### 1. Identify any challenges or issues you encountered while writing your functions.

- Handling exceptions in user input: One challenge was ensuring that functions like get_account_number() and get_amount() properly handled invalid user inputs (e.g., non-numeric values). Initially, I struggled with distinguishing between TypeError and ValueError for different scenarios, but I learned to use try-except blocks effectively to catch and handle these exceptions.
- Code duplication in validation: I noticed that get_balance() and make_deposit() had duplicated validation logic for the account number. This made the code harder to maintain, so I created a helper function validate_account_number() to centralize the logic, which was a good learning experience in refactoring.
- Formatting output messages: Formatting the balance and deposit amounts as currency e.g., $1,500.01 was tricky at first. I had to learn how to use the f"${amount:,.2f}" format string to ensure the output was consistent and met the requirements.

### 2. Discuss the benefits and challenges of developing and using unit tests.

- Benefit: Catching bugs early: Writing unit tests for functions like get_amount() and make_deposit() helped me catch bugs early, such as incorrect exception handling for negative amounts. This saved time during user acceptance testing because I could fix issues before running the full application.
- Benefit: Confidence in refactoring: Unit tests gave me confidence to refactor my code (e.g., creating validate_account_number()). I knew that if I broke something, the tests would fail, which made the refactoring process less stressful and more systematic.
- Challenge: Writing comprehensive tests: A challenge was ensuring that my unit tests covered all possible scenarios, such as edge cases (e.g., zero or negative amounts). It took time to think through all the cases and write tests for them, but it was worth it for the improved reliability of the code.
- Challenge: Mocking user input with patch: A challenge was learning how to use the patch function from unittest.mock to mock user input for functions like get_task() and get_account_number(). I initially struggled with understanding how to set up the mock correctly and access the mocked input in my tests, which led to failing tests. I had to research the patch documentation and experiment with different setups to get it working, which was time-consuming but helped me to understand much better.