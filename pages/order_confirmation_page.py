from selenium.webdriver.common.by import By


class OrderConfirmationPage:
    SUCCESS_POPUP = (By.XPATH, "//div[contains(@id893731730 (@class), 'Order_ModalHeader')]")
    CLOSE_BUTTON = (By.XPATH, "//button[text()='Закрыть']")

    def __init__(self, driver):
        self.driver = driver

    def is_order_success_popup_visible(self):
        """Проверка, что всплывающее окно с подтверждением заказа появилось"""
        return self.driver.find_element(*self.SUCCESS_POPUP).is_displayed()

    def close_popup(self):
        """Закрытие всплывающего окна"""
        self.driver.find_element(*self.CLOSE_BUTTON).click()
