from selenium.webdriver.common.by import By
from pages.base_page import BasePage
import allure


class OrderConfirmationPage(BasePage):
    SUCCESS_POPUP = (By.XPATH, "//div[contains(@id, 'Order_ModalHeader')]")
    CLOSE_BUTTON = (By.XPATH, "//button[text()='Закрыть']")

    def __init__(self, driver):
        super().__init__(driver)

    @allure.step("Проверка, что всплывающее окно с подтверждением заказа отображается")
    def is_order_success_popup_visible(self):
        """Проверка, что всплывающее окно с подтверждением заказа появилось"""
        return self.is_element_visible(self.SUCCESS_POPUP)

    @allure.step("Закрытие всплывающего окна с подтверждением")
    def close_popup(self):
        """Закрытие всплывающего окна"""
        self.click(self.CLOSE_BUTTON)
