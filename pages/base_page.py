from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def find_element(self, by, value):
        return WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((by, value)))

    def click(self, by, value):
        element = self.find_element(by, value)
        element.click()

    def send_keys(self, by, value, text):
        element = self.find_element(by, value)
        element.clear()
        element.send_keys(text)

    def is_element_present(self, by, value):
        try:
            self.find_element(by, value)
            return True
        except:
            return False

    def wait_for_element(self, by, value, timeout=10):
        WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located((by, value)))

    def get_url(self):
        return self.driver.current_url
