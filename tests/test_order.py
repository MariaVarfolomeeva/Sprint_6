import allure
import pytest
from pages.main_page import MainPage
from pages.order_page import OrderPage
from data.order_data import order_data


class TestOrderScooter:

    @pytest.mark.parametrize("first_name, last_name, address, phone", order_data)
    @allure.feature("Заказ самокатов")
    @allure.story("Оформление заказа через кнопки")
    @allure.title("Тест: заказ самоката через верхнюю кнопку с разными данными")
    def test_order_scooter_top_button(self, driver, first_name, last_name, address, phone):
        """Тест: заказ самоката через верхнюю кнопку с разными данными"""
        main_page = MainPage(driver)
        main_page.open()
        main_page.click_order_button("top")

        order_page = OrderPage(driver)
        order_page.fill_order_form(first_name, last_name, address, phone)
        order_page.submit_order()

        assert order_page.is_success_message_displayed(), "Сообщение об успешном заказе не появилось!"

    @pytest.mark.parametrize("first_name, last_name, address, phone", order_data)
    @allure.feature("Заказ самокатов")
    @allure.story("Оформление заказа через кнопки")
    @allure.title("Тест: заказ самоката через нижнюю кнопку с разными данными")
    def test_order_scooter_bottom_button(self, driver, first_name, last_name, address, phone):
        """Тест: заказ самоката через нижнюю кнопку с разными данными"""
        main_page = MainPage(driver)
        main_page.open()
        main_page.click_order_button("bottom")

        order_page = OrderPage(driver)
        order_page.fill_order_form(first_name, last_name, address, phone)
        order_page.submit_order()

        assert order_page.is_success_message_displayed(), "Сообщение об успешном заказе не появилось!"
