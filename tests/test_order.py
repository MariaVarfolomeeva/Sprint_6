import allure
import pytest
from pages.main_page import MainPage
from pages.order_page import OrderPage

order_data = [
    ("Иван", "Иванов", "Москва, ул. Ленина, 10", "89995553322"),
    ("Анна", "Петрова", "Санкт-Петербург, ул. Пушкина, 5", "81234567890")
]


@pytest.mark.parametrize("first_name, last_name, address, phone", order_data)
@allure.feature("Заказ самокатов")
@allure.story("Оформление заказа через кнопки")
@allure.title("Тест: заказ самоката через верхнюю кнопку с разными данными")
@allure.description(
    "Тест проверяет функциональность заказа самоката через верхнюю кнопку на главной странице с различными пользовательскими данными")
def test_order_scooter_top_button(driver, first_name, last_name, address, phone):
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
@allure.description(
    "Тест проверяет функциональность заказа самоката через нижнюю кнопку на главной странице с различными пользовательскими данными")
def test_order_scooter_bottom_button(driver, first_name, last_name, address, phone):
    """Тест: заказ самоката через нижнюю кнопку с разными данными"""
    main_page = MainPage(driver)
    main_page.open()
    main_page.click_order_button("bottom")

    order_page = OrderPage(driver)
    order_page.fill_order_form(first_name, last_name, address, phone)
    order_page.submit_order()

    assert order_page.is_success_message_displayed(), "Сообщение об успешном заказе не появилось!"


@allure.feature("Проверка логотипов")
@allure.story("Переход на главную страницу при клике на логотип Самоката")
@allure.title("Тест: переход на главную страницу 'Самоката' при нажатии на логотип")
@allure.description("Этот тест проверяет, что при клике на логотип 'Самоката' происходит переход на главную страницу")
def test_logo_scooter_redirects_to_home(driver):
    """Тест: переход на главную страницу 'Самоката' при нажатии на логотип"""
    main_page = MainPage(driver)
    main_page.open()
    main_page.click_order_button("top")

    order_page = OrderPage(driver)
    order_page.click_scooter_logo()

    assert main_page.is_open(), "После клика на логотип 'Самоката' не произошло возвращения на главную!"


@allure.feature("Проверка логотипов")
@allure.story("Переход в Яндекс.Дзен при клике на логотип Яндекса")
@allure.title("Тест: проверка перехода в 'Яндекс.Дзен' через логотип")
@allure.description("Этот тест проверяет, что при клике на логотип 'Яндекса' открывается страница 'Дзен'")
def test_logo_yandex_redirects_to_dzen(driver):
    """Тест: проверка перехода в 'Яндекс.Дзен' через логотип"""

    main_page = MainPage(driver)
    main_page.open()

    new_tab_url = main_page.click_yandex_logo()

    assert "dzen.ru" in new_tab_url, "После клика на логотип 'Яндекса' не открылся 'Дзен'!"
