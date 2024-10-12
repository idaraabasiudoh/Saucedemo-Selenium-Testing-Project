from selenium.webdriver.common.by import By

class InventoryPage:
    def __init__(self, driver):
        self.driver = driver
        self.product_list = (By.CLASS_NAME, "inventory_item")
        self.add_to_cart_button = (By.CLASS_NAME, "btn_inventory")

    def verify_inventory_page(self):
        assert "inventory" in self.driver.current_url, "Not on inventory page"
    
    def add_first_product_to_cart(self):
        self.driver.find_element(*self.add_to_cart_button).click()