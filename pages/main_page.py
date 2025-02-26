from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class MainPage:
    URL = "https://qa-scooter.praktikum-services.ru/"

    ORDER_BUTTON_TOP = (By.XPATH, "//button[@class='Button_Button__ra12g']")
    ORDER_BUTTON_BOTTOM = (By.XPATH, "//button[contains(@id893731730 (@class), 'Button_Middle__1CSJM')]")
    SCOOTER_LOGO = (By.XPATH, "//a[@class='Header_LogoScooter__3lsAR']")
    YANDEX_LOGO = (By.XPATH, "//a[@class='Header_LogoYandex__3TSOI']")
    FAQ_QUESTIONS = (By.XPATH, "//div[@class='accordion__item']")
    FAQ_ANSWERS = (By.XPATH, "//div[@class='accordion__panel']")

    def __init__(self, driver):
        self.driver = driver

    def open(self):
        self.driver.get(self.URL)

    def click_order_button(self, position):
        """Клик по кнопке 'Заказать' (верхняя или нижняя)"""
        if position == "top":
            self.driver.find_element(*self.ORDER_BUTTON_TOP).click()
        elif position == "bottom":
            self.driver.find_element(*self.ORDER_BUTTON_BOTTOM).click()

    def click_question(self, index):
        """Клик по вопросу в разделе 'Вопросы о важном'"""
        questions = self.driver.find_elements(*self.FAQ_QUESTIONS)
        questions[index].click()

    def is_answer_visible(self, index):
        """Проверка, что ответ на вопрос видим"""
        answers = self.driver.find_elements(*self.FAQ_ANSWERS)
        return answers[index].is_displayed()

    def click_scooter_logo(self):
        """Клик по логотипу 'Самокат'"""
        self.driver.find_element(*self.SCOOTER_LOGO).click()

    def click_yandex_logo(self):
        """Клик по логотипу 'Яндекса' и возврат URL новой вкладки"""
        self.driver.find_element(*self.YANDEX_LOGO).click()
        WebDriverWait(self.driver, 5).until(EC.number_of_windows_to_be(2))
        self.driver.switch_to.window(self.driver.window_handles[1])
        return self.driver.current_url
