import allure
import pytest
from pages.main_page import MainPage
from pages.order_page import OrderPage
from data.order_data import order_data


class TestOrderScooter:

    @allure.step("Открытие главной страницы и клик на кнопку заказа с позицией {button_position}")
    def order_scooter(self, driver, button_position, first_name, last_name, address, phone):
        """Общий метод для заказа самоката через указанную кнопку"""
        main_page = MainPage(driver)
        main_page.open()

        main_page.click_order_button(button_position)

        order_page = OrderPage(driver)
        order_page.fill_order_form(first_name, last_name, address, phone)

        order_page.submit_order()

        return order_page

    @pytest.mark.parametrize("first_name, last_name, address, phone", order_data)
    @allure.feature("Заказ самокатов")
    @allure.story("Оформление заказа через кнопки")
    @allure.title("Тест: заказ самоката через верхнюю кнопку с разными данными")
    @allure.step("Открытие главной страницы и клик на верхнюю кнопку заказа")
    def test_order_scooter_top_button(self, driver, first_name, last_name, address, phone):
        """Тест: заказ самоката через верхнюю кнопку с разными данными"""
        order_page = self.order_scooter(driver, "top", first_name, last_name, address, phone)

        assert order_page.is_success_message_displayed(), "Сообщение об успешном заказе не появилось!"

    @pytest.mark.parametrize("first_name, last_name, address, phone", order_data)
    @allure.feature("Заказ самокатов")
    @allure.story("Оформление заказа через кнопки")
    @allure.title("Тест: заказ самоката через нижнюю кнопку с разными данными")
    @allure.step("Открытие главной страницы и клик на нижнюю кнопку заказа")
    def test_order_scooter_bottom_button(self, driver, first_name, last_name, address, phone):
        """Тест: заказ самоката через нижнюю кнопку с разными данными"""
        order_page = self.order_scooter(driver, "bottom", first_name, last_name, address, phone)

        assert order_page.is_success_message_displayed(), "Сообщение об успешном заказе не появилось!"
