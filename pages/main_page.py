from selenium.webdriver.common.by import By
from .base_page import BasePage


class MainPage(BasePage):
    ORDER_BUTTON_TOP = (By.XPATH, "//button[contains(@class, 'Button_Button__ra12g') and text()='Заказать']")
    ORDER_BUTTON_BOTTOM = (By.XPATH, "//button[contains(@class, 'Button_Button__ra12g') and text()='Заказать']")
    YANDEX_LOGO = (By.XPATH, "//a[@href='https://dzen.ru']")
    SCOOTER_LOGO = (By.XPATH, "//a[@href='/']")

    def open(self):
        self.driver.get("https://qa-scooter.praktikum-services.ru/")

    def click_order_button(self, position):
        if position == "top":
            self.click(*self.ORDER_BUTTON_TOP)
        elif position == "bottom":
            self.click(*self.ORDER_BUTTON_BOTTOM)

    def click_yandex_logo(self):
        self.click(*self.YANDEX_LOGO)
        return self.driver.window_handles[1]

    def click_scooter_logo(self):
        self.click(*self.SCOOTER_LOGO)

    def is_open(self):
        return "qa-scooter" in self.get_url()
