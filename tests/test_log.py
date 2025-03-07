import allure
from pages.main_page import MainPage
from pages.order_page import OrderPage


class TestLogos:

    @allure.feature("Логотипы")
    @allure.story("Переходы по логотипам")
    @allure.title("Тест: переход на главную страницу 'Самоката' при нажатии на логотип")
    def test_logo_scooter_redirects_to_home(self, driver):
        """Тест: переход на главную страницу 'Самоката' при нажатии на логотип"""
        main_page = MainPage(driver)

        with allure.step("Открытие главной страницы и клик на кнопку заказа сверху"):
            main_page.open()
            main_page.click_order_button("top")

        order_page = OrderPage(driver)
        with allure.step("Клик на логотип Самоката для возврата на главную страницу"):
            order_page.click_scooter_logo()

        with allure.step("Проверка, что главная страница открыта"):
            assert main_page.is_open(), "После клика на логотип 'Самоката' не произошло возвращения на главную!"

    @allure.feature("Логотипы")
    @allure.story("Переходы по логотипам")
    @allure.title("Тест: проверка перехода в 'Яндекс.Дзен' через логотип")
    def test_logo_yandex_redirects_to_dzen(self, driver):
        """Тест: проверка перехода в 'Яндекс.Дзен' через логотип"""
        main_page = MainPage(driver)

        with allure.step("Открытие главной страницы и клик на логотип Яндекса"):
            main_page.open()
            new_tab_url = main_page.click_yandex_logo()

        with allure.step("Проверка, что открылся сайт 'Дзен'"):
            assert "dzen.ru" in new_tab_url, "После клика на логотип 'Яндекса' не открылся 'Дзен'!"
