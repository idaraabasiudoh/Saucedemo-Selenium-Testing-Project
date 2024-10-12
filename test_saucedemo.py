import unittest
from main import init_driver
from login_page import LoginPage
from inventory_page import InventoryPage
from cart_page import CartPage
from checkout_page import CheckoutPage

class SaucedemoTest(unittest.TestCase):
    def setUp(self):
        self.driver = init_driver()
        self.driver.get("https://www.saucedemo.com/")

    def test_saucedemo_flow(self):
        login_page = LoginPage(self.driver)
        login_page.login("standard_user", "secret_sauce")

        inventory_page = InventoryPage(self.driver)
        inventory_page.verify_inventory_page()
        inventory_page.add_first_product_to_cart()

        cart_page = CartPage(self.driver)
        cart_page.verify_cart_items()

        checkout_page = CheckoutPage(self.driver)
        checkout_page.proceed_to_checkout()

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()