import allure
from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class OrderPage(BasePage):
    FIRST_NAME_INPUT = (By.XPATH, '//input[@placeholder="* Имя"]')
    LAST_NAME_INPUT = (By.XPATH, '//input[@placeholder="* Фамилия"]')
    ADDRESS_INPUT = (By.XPATH, '//input[@placeholder="* Адрес: куда привезти заказ"]')
    PHONE_INPUT = (By.XPATH, '//input[@placeholder="* Телефон: на него позвонит курьер"]')
    NEXT_BUTTON = (By.XPATH, '//button[text()="Далее"]')

    DELIVERY_DATE_INPUT = (By.XPATH, '//input[@placeholder="* Когда привезти самокат"]')
    RENTAL_PERIOD_SELECT = (By.XPATH, '//div[@class="Dropdown-placeholder"]')
    COLOR_SELECT = (By.XPATH, '//div[@class="Checkbox_Checkbox__input__L4S2g"]')

    SUCCESS_MESSAGE = (By.XPATH, '//div[contains(text(), "Спасибо за заказ!")]')

    SCOOTER_LOGO = (By.XPATH, '//a[@href="/"]')

    @allure.step("Заполнение формы заказа: {first_name} {last_name}, {address}, {phone}")
    def fill_order_form(self, first_name, last_name, address, phone, delivery_date="2025-02-26"):
        """Заполняет форму заказа."""
        self.send_keys(*self.FIRST_NAME_INPUT, first_name)
        self.send_keys(*self.LAST_NAME_INPUT, last_name)
        self.send_keys(*self.ADDRESS_INPUT, address)
        self.send_keys(*self.PHONE_INPUT, phone)
        self.send_keys(*self.DELIVERY_DATE_INPUT, delivery_date)
        self.click(*self.RENTAL_PERIOD_SELECT)
        self.click(*self.COLOR_SELECT)

    @allure.step("Отправка формы заказа")
    def submit_order(self):
        """Отправляет форму заказа."""
        self.click(*self.NEXT_BUTTON)

    @allure.step("Проверка успешного сообщения о заказе")
    def is_success_message_displayed(self):
        """Проверяет, что сообщение об успешном заказе отображается."""
        return self.is_element_visible(self.SUCCESS_MESSAGE)

    @allure.step("Клик на логотип для возврата на главную")
    def click_scooter_logo(self):
        """Кликает на логотип Самоката для возврата на главную страницу."""
        self.click(*self.SCOOTER_LOGO)

    @allure.step("Проверка, что страница заказа открыта")
    def is_open(self):
        """Проверяет, что страница Самоката открыта."""
        return "scooter" in self.get_url()

