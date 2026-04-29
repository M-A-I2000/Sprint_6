import allure
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from pages.base_page import BasePage
from locators.base_locators import BaseLocators
from locators.order_form_locators import OrderLocators
from locators.about_rent_locators import RentLocators
from curl import *

class OrderPage(BasePage):

    @allure.step("Открыть начальную страницу")
    def open_order_page(self):
        self.open(BASE_URL)

    @allure.step("Нажать на верхнюю кнопку заказа")
    def click_top_order_button(self):
        self.click(BaseLocators.TOP_ORDER_BUTTON)

    @allure.step("Нажать на нижнюю кнопку заказа")
    def click_bottom_order_button(self):
        self.scroll_to_element(BaseLocators.BOTTOM_ORDER_BUTTON)
        button = self.find(BaseLocators.BOTTOM_ORDER_BUTTON)
        self.driver.execute_script("arguments[0].click();", button)

    @allure.step("Заполняем поле ввода станции метро")
    def fill_the_metro_station_input(self, station):
        wait = WebDriverWait(self.driver, 15)
        self.type(OrderLocators.METRO_STATION_INPUT, station)
        locator = (By.XPATH, f"//div[text() = '{station}']")
        metro_station = wait.until(EC.element_to_be_clickable(locator))
        metro_station.click() 

    @allure.step("Заполняем полную форму оформления заказа")
    def fill_out_the_order_form(self, name, surname, address, station, number):
        self.type(OrderLocators.NAME_INPUT, name)
        self.type(OrderLocators.SURNAME_INPUT, surname)
        self.type(OrderLocators.ADDRESS_INPUT, address)
        self.fill_the_metro_station_input(station)
        self.type(OrderLocators.TELEPHONE_INPUT, number)

    @allure.step("Надимаем на кнопку далее")
    def click_further_button(self):
        wait = WebDriverWait(self.driver, 15)
        button = wait.until(EC.element_to_be_clickable(OrderLocators.FURTHER_BUTTON))
        button.click()
        wait.until(EC.presence_of_element_located(RentLocators.DELIVERY_DATE_INPUT))

    @allure.step("Возвращение на начальную (домашнюю) страницу через лого самоката")
    def go_to_main_page(self):
        wait = WebDriverWait(self.driver, 15)
        button = wait.until(EC.element_to_be_clickable(BaseLocators.LOGO_BUTTON))
        button.click()

    @allure.step("Переход на страницу Дзена по клику на лого Яндекса")
    def go_to_dzen_page(self):
        wait = WebDriverWait(self.driver, 15)
        button = wait.until(EC.element_to_be_clickable(BaseLocators.YANDEX_BUTTON))
        button.click()

    @allure.step("Ожидание загрузки Дзена")
    def wait_when_dzen_loads(self):
        wait = WebDriverWait(self.driver, 40)
        page = wait.until(EC.url_contains("dzen.ru"))
        return page
  
    @allure.step("Проверяем, что мы находимся на начальной (домашней) странице")  
    def is_on_main_page(self):
        return self.is_element_visible(BaseLocators.HOME_HEADER)