import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from pages.base_page import BasePage
from curl import *

class FaqPage(BasePage):

    @allure.step("Открыть страницу с FAQ")
    def open_faq_page(self):
        self.open(BASE_URL)

    @allure.step("Нажать на вопрос")
    def open_question_by_text(self, question_locator):
        self.scroll_to_element(question_locator)
        wait = WebDriverWait(self.driver, 10)
        question = wait.until(EC.element_to_be_clickable(question_locator))
        question.click()

    @allure.step("Получить текст ответа на вопрос")
    def get_answer_text_by_question(self, answer_locator):
        wait = WebDriverWait(self.driver, 10)
        answer = wait.until(EC.visibility_of_element_located(answer_locator))
        return answer.text

    @allure.step("Проверка видимости элемента ответа (локатор: {answer_locator})")
    def is_answer_visible_by_question(self, answer_locator):
        try:
            wait = WebDriverWait(self.driver, 10)
            answer = wait.until(EC.visibility_of_element_located(answer_locator))
            if answer.is_displayed():
                return True, "Ответ успешно отобразился на экране"
            else:
                return False, "Элемент ответа найден, но скрыт (не отображается на экране)"
        except TimeoutException:
            return False, "Таймаут ожидания: элемент ответа не найден в течение 10 секунд"
        except Exception as e:
            return False, f"Неожиданная ошибка при проверке видимости: {str(e)}"