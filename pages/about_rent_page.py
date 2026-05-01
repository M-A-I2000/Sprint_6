import allure
import random
from pages.base_page import BasePage
from locators.about_rent_locators import RentLocators

class RentPage(BasePage):

    @allure.step("Заполняем поле даты")
    def fill_the_date_field(self, date):
        self.type(RentLocators.DELIVERY_DATE_INPUT, date)

    @allure.step("Случайным образом выбираем срок аренды")
    def get_random_rent_button(self):
        rent_buttons = [
            RentLocators.DAY_RENT_BUTTON,
            RentLocators.TWO_DAYS_RENT_BUTTON,
            RentLocators.THREE_DAYS_RENT_BUTTON,
            RentLocators.FOUR_DAYS_RENT_BUTTON,
            RentLocators.FIVE_DAYS_RENT_BUTTON,
            RentLocators.SIX_DAYS_RENT_BUTTON,
            RentLocators.SEVEN_DAYS_RENT_BUTTON
        ]
        return random.choice(rent_buttons)
    
    @allure.step("Заполняем поле в выбором срока аренды")
    def fill_the_rent_days_input(self):
        self.click(RentLocators.DROPDOWN_ARROW)
        random_button = self.get_random_rent_button()
        self.click(random_button)

    @allure.step("Выбираем черный цвет")
    def choose_black(self):
        checkbox = self.wait_element_to_be_clickable(RentLocators.BLACK_COLOUR_INPUT)
        checkbox.click()

    @allure.step("Выбираем серый цвет")
    def choose_gray(self):
        checkbox = self.wait_element_to_be_clickable(RentLocators.GRAY_COLOUR_INPUT)
        checkbox.click()

    @allure.step("Нажимаем на кнопку заказать")
    def click_order_button(self):
        button = self.wait_element_to_be_clickable(RentLocators.ORDER_BUTTON)
        button.click()

    @allure.step("Нажимаем на кнопку назад")
    def click_the_back_button(self):
        self.click(RentLocators.BACK_BUTTON)


    
