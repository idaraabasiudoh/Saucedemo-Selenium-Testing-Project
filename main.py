from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

def init_driver():
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")
    service = Service(executable_path="/Users/idara-abasiudoh/Documents/Code_Files/Python/Selenuim/saucedemo_test/chromedriver_mac64/chromedriver")
    driver = webdriver.Chrome(service=service, options=chrome_options)
    return driver