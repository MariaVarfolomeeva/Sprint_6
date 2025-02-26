import pytest
from selenium import webdriver


@pytest.fixture(scope="function")
def driver():
    """Фикстура для инициализации браузера перед тестом и закрытия после теста"""
    options = webdriver.FirefoxOptions()
    driver = webdriver.Firefox(options=options)
    driver.maximize_window()
    yield driver
    driver.quit()
