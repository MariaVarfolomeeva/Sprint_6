import allure
from pages.main_page import MainPage
from pages.order_page import OrderPage


class TestLogos:

    @allure.feature("Логотипы")
    @allure.story("Переходы по логотипам")
    @allure.title("Тест: переход на главную страницу 'Самоката' при нажатии на логотип")
    @allure.step("Открытие главной страницы и клик на кнопку заказа сверху")
    def test_logo_scooter_redirects_to_home(self, driver):
        """Тест: переход на главную страницу 'Самоката' при нажатии на логотип"""
        main_page = MainPage(driver)
        main_page.open()
        main_page.click_order_button("top")
        order_page = OrderPage(driver)
        order_page.click_scooter_logo()

        assert main_page.is_open(), "После клика на логотип 'Самоката' не произошло возвращения на главную!"

    @allure.feature("Логотипы")
    @allure.story("Переходы по логотипам")
    @allure.title("Тест: проверка перехода в 'Яндекс.Дзен' через логотип")
    @allure.step("Открытие главной страницы и клик на логотип Яндекса")
    def test_logo_yandex_redirects_to_dzen(self, driver):
        """Тест: проверка перехода в 'Яндекс.Дзен' через логотип"""
        main_page = MainPage(driver)
        main_page.open()
        new_tab_url = main_page.click_yandex_logo()

        assert "dzen.ru" in new_tab_url, "После клика на логотип 'Яндекса' не открылся 'Дзен'!"
