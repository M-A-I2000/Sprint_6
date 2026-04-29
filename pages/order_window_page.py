import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
from locators.order_window_locators import WindowLocators
from locators.successful_order_window_locators import OrderedLocators

class OrderWindowPage(BasePage):

    @allure.step("Нажимаем на кнопку Да")
    def click_accept_button(self):
        wait = WebDriverWait(self.driver, 15)
        button = wait.until(EC.presence_of_element_located(WindowLocators.YES_BUTTON))
        button.click()
        wait.until(EC.visibility_of_element_located(OrderedLocators.SUCCESSFUL_ORDER_WINDOW))

    @allure.step("Нажимаем на кнопку Нет")
    def reject_the_order(self):
        self.click(WindowLocators.NO_BUTTON)
    
    @allure.step("Нажимаем на кнопку просмотра статуса заказа")    
    def click_status_button(self):
        wait = WebDriverWait(self.driver, 15)
        button = wait.until(EC.element_to_be_clickable(OrderedLocators.STATUS_BUTTON))
        button.click()

    @allure.step("Проверяем выдна ли кнопка отмены заказа")
    def is_order_cancellation_button_visible(self):
        return self.is_element_visible(OrderedLocators.CANCEL_THE_ORDER_BUTTON)

    @allure.step("Проверяем появление окна успешной регистрации заказа")    
    def wait_order_success_message(self):
        wait = WebDriverWait(self.driver, 15)
        message = wait.until(EC.visibility_of_element_located(OrderedLocators.ORDER_HEADER))
        return message.text

    
