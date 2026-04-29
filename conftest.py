import pytest
import allure
from selenium import webdriver

@allure.description("Открытие и закрытие браузера")
@pytest.fixture(scope="function")
def driver():
    driver = webdriver.Firefox()
    driver.maximize_window()

    driver.delete_all_cookies()

    yield driver

    driver.delete_all_cookies()
    driver.quit()