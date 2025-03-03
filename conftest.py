import pytest
import allure
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from webdriver_manager.firefox import GeckoDriverManager


@pytest.fixture(scope="function")
def driver():
    """Фикстура для инициализации WebDriver для Firefox"""
    options = Options()
    options.headless = True

    service = Service(GeckoDriverManager().install())

    driver = webdriver.Firefox(service=service, options=options)
    driver.set_page_load_timeout(30)
    driver.set_script_timeout(30)

    yield driver

    driver.quit()


@pytest.fixture(scope="function", autouse=True)
def add_allure_environment():
    """Фикстура для добавления данных в Allure отчет"""
    allure.dynamic.label("browser", "Firefox")
    allure.dynamic.label("version", "Latest")
    allure.dynamic.label("test_framework", "pytest")
