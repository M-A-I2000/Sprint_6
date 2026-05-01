import allure
from pages.base_page import BasePage
from locators.order_window_locators import WindowLocators

class OrderWindowPage(BasePage):

    @allure.step("Нажимаем на кнопку Да")
    def click_accept_button(self):
        button = self.wait_presence_of_element(WindowLocators.YES_BUTTON)
        button.click()

    @allure.step("Нажимаем на кнопку Нет")
    def reject_the_order(self):
        self.click(WindowLocators.NO_BUTTON)

    @allure.step("Проверяем появление окна успешной регистрации заказа")    
    def is_order_success_message_visible(self):
        return self.is_element_visible(WindowLocators.ORDER_HEADER)

    
