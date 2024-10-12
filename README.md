# Saucedemo Selenium Testing Project

This project automates testing for the Saucedemo website using Python and Selenium. The tests include login functionality, adding items to the cart, and proceeding to checkout.

## Project Structure

```bash
saucedemo_test/
├── main.py
├── login_page.py
├── inventory_page.py
├── cart_page.py
├── checkout_page.py
└── test_saucedemo.py
```

## Setup

1. Clone the repository.
2. Install dependencies:
   ```bash
   pip install selenium
   ```

3.	Download ChromeDriver and update main.py with the correct path.

## Running the Tests

Run the test script using:

```bash 
python test_saucedemo.py
```

Features Tested

1. Login: Tests the login functionality with valid credentials.
2. Inventory Page: Verifies the presence of products and adds items to the cart.
3. Cart and Checkout: Confirms the cart has items and proceeds to checkout.


Requirements

	•	Python 3.x
	•	Selenium
	•	ChromeDriver

License

This project is licensed under the MIT License.
