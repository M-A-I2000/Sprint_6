import allure
from selenium.common.exceptions import TimeoutException
from pages.base_page import BasePage
from locators.main_page_locators import MainLocators
from curl import *

class MainPage(BasePage):

    @allure.step("Открыть страницу с FAQ")
    def open_main_page(self):
        self.open(BASE_URL)

    @allure.step("Нажать на верхнюю кнопку заказа")
    def click_top_order_button(self):
        self.click(MainLocators.TOP_ORDER_BUTTON)

    @allure.step("Нажать на нижнюю кнопку заказа")
    def click_bottom_order_button(self):
        self.scroll_to_element(MainLocators.BOTTOM_ORDER_BUTTON)
        button = self.find(MainLocators.BOTTOM_ORDER_BUTTON)
        self.js_click(button)

    @allure.step("Нажать на вопрос")
    def open_question_by_text(self, question_locator):
        self.scroll_to_element(question_locator)
        question = self.wait_element_to_be_clickable(question_locator)
        question.click()

    @allure.step("Получить текст ответа на вопрос")
    def get_answer_text_by_question(self, answer_locator):
        answer = self.wait_visibility_of_element(answer_locator)
        return answer.text

    @allure.step("Проверка видимости элемента ответа (локатор: {answer_locator})")
    def is_answer_visible_by_question(self, answer_locator):
        try:
            answer = self.wait_visibility_of_element(answer_locator)
            if answer.is_displayed():
                return True, "Ответ успешно отобразился на экране"
            else:
                return False, "Элемент ответа найден, но скрыт (не отображается на экране)"
        except TimeoutException:
            return False, "Таймаут ожидания: элемент ответа не найден в течение 10 секунд"
        except Exception as e:
            return False, f"Неожиданная ошибка при проверке видимости: {str(e)}"
        
    @allure.step("Возвращение на начальную (домашнюю) страницу через лого самоката")
    def go_to_main_page(self):
        button = self.wait_element_to_be_clickable(MainLocators.LOGO_BUTTON)
        button.click()

    @allure.step("Переход на страницу Дзена по клику на лого Яндекса")
    def go_to_dzen_page(self):
        button = self.wait_element_to_be_clickable(MainLocators.YANDEX_BUTTON)
        button.click()

    @allure.step("Ожидание загрузки Дзена")
    def wait_when_dzen_loads(self):
        text = "dzen.ru"
        page = self.wait_when_page_contains_text(text)
        return page
  
    @allure.step("Проверяем, что мы находимся на начальной (домашней) странице")  
    def is_on_main_page(self):
        return self.is_element_visible(MainLocators.HOME_HEADER)