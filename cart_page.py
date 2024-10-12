from selenium.webdriver.common.by import By

class CartPage:
    def __init__(self, driver):
        self.driver = driver
        self.cart_items = (By.CLASS_NAME, "cart_item")

    def verify_cart_items(self):
        items = self.driver.find_elements(*self.cart_items)
        assert len(items) > 0, "Cart is empty"