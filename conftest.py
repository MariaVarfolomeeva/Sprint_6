import pytest
import allure
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service
from webdriver.firefox import GeckoDriverManager


@pytest.fixture(scope="function")
def driver():
    """Фикстура для инициализации WebDriver для Firefox"""

    options = Options()
    options.headless = True

    driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()), options=options)

    yield driver

    driver.quit()


@pytest.fixture(scope="function", autouse=True)
def add_allure_environment():
    """Фикстура для добавления данных в Allure отчет"""
    allure.environment(
        **{
            "Browser": "Firefox",
            "Version": "Latest",
            "Test Framework": "pytest",
        }
    )