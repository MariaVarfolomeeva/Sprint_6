import allure
from selenium.webdriver.common.by import By
from .base_page import BasePage


class MainPage(BasePage):
    ORDER_BUTTON_TOP = (By.XPATH, "//button[contains(@class, 'Button_Button__ra12g') and text()='Заказать']")
    ORDER_BUTTON_BOTTOM = (By.XPATH, "//button[contains(@class, 'Button_Button__ra12g') and text()='Заказать']")
    YANDEX_LOGO = (By.XPATH, "//a[@href='https://dzen.ru']")
    SCOOTER_LOGO = (By.XPATH, "//a[@href='/']")

    @allure.step("Открытие главной страницы")
    def open(self):
        """Открывает главную страницу сайта."""
        self.open_url("https://qa-scooter.praktikum-services.ru/")

    @allure.step("Клик на кнопку заказа {position}")
    def click_order_button(self, position):
        """Кликает на кнопку заказа в зависимости от указанной позиции."""
        if position == "top":
            self.click(*self.ORDER_BUTTON_TOP)
        elif position == "bottom":
            self.click(*self.ORDER_BUTTON_BOTTOM)

    @allure.step("Клик на логотип Яндекса")
    def click_yandex_logo(self):
        """Кликает на логотип Яндекса и возвращает URL нового окна."""
        self.click(*self.YANDEX_LOGO)
        self.wait_for_new_window()
        self.switch_to_new_window()
        return self.get_url()

    @allure.step("Клик на логотип Самоката")
    def click_scooter_logo(self):
        """Кликает на логотип Самоката для возвращения на главную страницу."""
        self.click(*self.SCOOTER_LOGO)
        self.switch_to_parent_window()

    @allure.step("Проверка, что открыта главная страница")
    def is_open(self):
        """Проверяет, что страница открыта, проверяя URL."""
        return "qa-scooter" in self.get_url()
