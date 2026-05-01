import allure
import pytest
from pages.main_page import MainPage
from pages.base_page import BasePage
from faq_data import *
from locators.main_page_locators import MainLocators

class TestMainPage:

    @allure.title("Проверка видимости и содержания ответа на вопрос FAQ")
    @allure.description(
    "Открываем страницу FAQ, находим вопрос, "
    "раскрываем его и проверяем, что ответ отображается и содержит ожидаемый текст."
    )
    @pytest.mark.parametrize(
        "question_locator, answer_locator, expected_answer",
        [
            [MainLocators.COST_AND_PAYMENT_QESTION, MainLocators.COST_AND_PAYMENT_ANSWER, answer_1],
            [MainLocators.MULTIPLE_SCOOTERS_AVAILABLE_QESTION, MainLocators.MULTIPLE_SCOOTERS_AVAILABLE_ANSWER, answer_2],
            [MainLocators.RENT_TIME_CALCULATION_QESTION, MainLocators.RENT_TIME_CALCULATION_ANSWER, answer_3],
            [MainLocators.TODAY_BOOKING_POSSIBLE_QESTION, MainLocators.TODAY_BOOKING_POSSIBLE_ANSWER, answer_4],
            [MainLocators.RENT_EXTENSION_OR_EARLY_RETURN_QESTION, MainLocators.RENT_EXTENSION_OR_EARLY_RETURN_ANSWER, answer_5],
            [MainLocators.CHARGER_INCLUDED_QESTION, MainLocators.CHARGER_INCLUDED_ANSWER, answer_6],
            [MainLocators.ORDER_CANCELLATION_POSSIBLE_QESTION, MainLocators.ORDER_CANCELLATION_POSSIBLE_ANSWER, answer_7],
            [MainLocators.DELIVERY_BEYOND_MKAD_QESTION, MainLocators.DELIVERY_BEYOND_MKAD_ANSWER, answer_8]
        ]
    )
    def test_faq_question(self, driver, question_locator, answer_locator, expected_answer):
        page = MainPage(driver)
        page.open_main_page()
        page.open_question_by_text(question_locator)
        page.is_answer_visible_by_question(answer_locator)
        actual_answer = page.get_answer_text_by_question(answer_locator)
        assert expected_answer in actual_answer

    @allure.title("Переход на главную страницу при клике по логотипу")
    @allure.description(
    "1. Открываем страницу заказа.\n"
    "2. Нажимаем верхнюю кнопку заказа (для активации логотипа).\n"
    "3. Кликаем по логотипу.\n"
    "4. Проверяем, что пользователь оказался на главной странице."
    )
    def test_clicking_the_logo_button_redirects_to_the_home_page(self, driver):
        main_page = MainPage(driver)
        main_page.open_main_page()
        main_page.click_top_order_button()
        main_page.go_to_main_page()

        assert main_page.is_on_main_page()

    @allure.title("Переход на страницу Дзен при клике по логотипу Дзен")
    @allure.description(
    "1. Открываем страницу заказа.\n"
    "2. Кликаем по логотипу Дзен.\n"
    "3. Проверяем, что пользователь перешёл на страницу dzen.ru."
    )
    def test_clicking_the_dzen_logo_redirects_to_the_dzen_page(self, driver):
        page = MainPage(driver)
        window = BasePage(driver)
        page.open_main_page()
        page.go_to_dzen_page()
        window.focus_on_window()
        page.wait_when_dzen_loads()

        assert "dzen.ru" in window.get_current_url()
