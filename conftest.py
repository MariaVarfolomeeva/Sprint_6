import pytest
import allure
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from webdriver_manager.firefox import GeckoDriverManager


@pytest.fixture(scope="function")
def driver():
    """Фикстура для инициализации WebDriver для Firefox"""
    options = Options()
    options.headless = True

    driver = webdriver.Firefox(executable_path=GeckoDriverManager().install(), options=options)

    yield driver

    driver.quit()


@pytest.fixture(scope="function", autouse=True)
def add_allure_environment():
    """Фикстура для добавления данных в Allure отчет"""
    allure.dynamic.label("browser", "Firefox")
    allure.dynamic.label("version", "Latest")
    allure.dynamic.label("test_framework", "pytest")
