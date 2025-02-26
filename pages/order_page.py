from selenium.webdriver.common.by import By


class OrderPage:
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

    def __init__(self, driver):
        self.driver = driver

    def fill_order_form(self, first_name, last_name, address, phone):
        """Заполняет форму заказа."""
        self.driver.find_element(*self.FIRST_NAME_INPUT).send_keys(first_name)
        self.driver.find_element(*self.LAST_NAME_INPUT).send_keys(last_name)
        self.driver.find_element(*self.ADDRESS_INPUT).send_keys(address)
        self.driver.find_element(*self.PHONE_INPUT).send_keys(phone)

        self.driver.find_element(*self.DELIVERY_DATE_INPUT).send_keys("2025-02-26")
        self.driver.find_element(*self.RENTAL_PERIOD_SELECT).click()
        self.driver.find_element(*self.COLOR_SELECT).click()

    def submit_order(self):
        """Отправляет форму."""
        self.driver.find_element(*self.NEXT_BUTTON).click()

    def is_success_message_displayed(self):
        """Проверяет, что сообщение об успешном заказе отображается."""
        try:
            success_message = self.driver.find_element(*self.SUCCESS_MESSAGE)
            return success_message.is_displayed()
        except:
            return False

    def click_scooter_logo(self):
        """Кликает на логотип Самоката для возврата на главную страницу."""
        scooter_logo = self.driver.find_element(*self.SCOOTER_LOGO)
        scooter_logo.click()

    def is_open(self):
        """Проверяет, что страница Самоката открыта."""
        return "scooter" in self.driver.current_url