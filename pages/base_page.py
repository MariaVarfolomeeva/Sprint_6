import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    @allure.step("Открытие страницы {url}")
    def open_url(self, url):
        """Открывает страницу по указанному URL."""
        self.driver.get(url)

    @allure.step("Поиск элемента {by}, {value}")
    def find_element(self, by, value, timeout=10, handle_exceptions=False):
        """Поиск одного элемента с возможностью подавления ошибок."""
        try:
            return self.wait.until(EC.presence_of_element_located((by, value)))
        except:
            if handle_exceptions:
                return None
            raise

    @allure.step("Поиск списка элементов {by}, {value}")
    def find_elements(self, by, value, timeout=10, handle_exceptions=False):
        """Поиск нескольких элементов с возможностью подавления ошибок."""
        try:
            return self.wait.until(EC.presence_of_all_elements_located((by, value)))
        except:
            if handle_exceptions:
                return []
            raise

    @allure.step("Клик по элементу {by}, {value}")
    def click(self, by, value):
        """Кликает по элементу."""
        element = self.find_element(by, value)
        element.click()

    @allure.step("Ввод текста '{text}' в элемент {by}, {value}")
    def send_keys(self, by, value, text):
        """Вводит текст в элемент."""
        element = self.find_element(by, value)
        element.clear()
        element.send_keys(text)

    @allure.step("Проверка видимости элемента {by}, {value}")
    def is_element_visible(self, by, value, timeout=10):
        """Проверяет видимость элемента на странице."""
        try:
            return self.wait.until(EC.visibility_of_element_located((by, value))) is not None
        except:
            return False

    @allure.step("Проверка присутствия элемента {by}, {value}")
    def is_element_present(self, by, value, timeout=10):
        """Проверяет присутствие элемента на странице."""
        try:
            self.find_element(by, value, timeout)
            return True
        except:
            return False

    @allure.step("Получение текущего URL")
    def get_url(self):
        """Возвращает текущий URL страницы."""
        return self.driver.current_url

    @allure.step("Получение списка открытых окон")
    def get_window_handles(self):
        """Возвращает список всех открытых окон/вкладок."""
        return self.driver.window_handles

    @allure.step("Ожидание открытия нового окна")
    def wait_for_new_window(self, timeout=10):
        """Ожидает открытия нового окна/вкладки."""
        self.wait.until(lambda d: len(d.window_handles) > 1)

    @allure.step("Переключение на новое окно")
    def switch_to_new_window(self):
        """Переключает фокус на новое окно."""
        window_handles = self.driver.window_handles
        self.driver.switch_to.window(window_handles[-1])

    @allure.step("Закрытие текущего окна")
    def close_current_window(self):
        """Закрывает текущее окно/вкладку."""
        self.driver.close()

    @allure.step("Переключение на родительское окно")
    def switch_to_parent_window(self):
        """Возвращает фокус на родительское окно."""
        window_handles = self.driver.window_handles
        self.driver.switch_to.window(window_handles[0])

    @allure.step("Ожидание элемента {by}, {value}")
    def wait_for_element(self, by, value, timeout=10):
        """Ожидание видимости элемента на странице с заданным тайм-аутом."""
        return self.wait.until(EC.visibility_of_element_located((by, value)))

    @allure.step("Ожидание исчезновения элемента {by}, {value}")
    def wait_for_element_to_disappear(self, by, value, timeout=10):
        """Ожидание исчезновения элемента на странице."""
        return self.wait.until(EC.invisibility_of_element_located((by, value)))

    @allure.step("Ожидание кликабельности элемента {by}, {value}")
    def wait_for_element_to_be_clickable(self, by, value, timeout=10):
        """Ожидание, пока элемент не станет кликабельным."""
        return self.wait.until(EC.element_to_be_clickable((by, value)))
