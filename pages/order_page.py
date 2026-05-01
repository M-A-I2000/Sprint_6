import allure
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from locators.order_form_locators import OrderLocators
from curl import *

class OrderPage(BasePage):

    @allure.step("Открыть начальную страницу")
    def open_order_page(self):
        self.open(BASE_URL)

    @allure.step("Заполняем поле ввода станции метро")
    def fill_the_metro_station_input(self, station):
        self.type(OrderLocators.METRO_STATION_INPUT, station)
        locator = (By.XPATH, f"//div[text() = '{station}']")
        metro_station = self.wait_element_to_be_clickable(locator)
        metro_station.click() 

    @allure.step("Заполняем полную форму оформления заказа")
    def fill_out_the_order_form(self, name, surname, address, station, number):
        self.type(OrderLocators.NAME_INPUT, name)
        self.type(OrderLocators.SURNAME_INPUT, surname)
        self.type(OrderLocators.ADDRESS_INPUT, address)
        self.fill_the_metro_station_input(station)
        self.type(OrderLocators.TELEPHONE_INPUT, number)

    @allure.step("Нажимаем на кнопку далее")
    def click_further_button(self):
        button = self.wait_element_to_be_clickable(OrderLocators.FURTHER_BUTTON)
        button.click()

