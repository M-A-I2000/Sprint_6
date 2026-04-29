import allure
import pytest
from pages.faq_page import FaqPage
from faq_data import *
from locators.faq_locators import FaqLocators

class TestFaqPage:

    @allure.title("Проверка видимости и содержания ответа на первый вопрос FAQ")
    @allure.description(
    "Открываем страницу FAQ, находим вопрос «Стоимость и оплата», "
    "раскрываем его и проверяем, что ответ отображается и содержит ожидаемый текст."
    )
    def test_faq_question_1(self, driver):
        expected_answer = answer_1
        page = FaqPage(driver)
        page.open_faq_page()
        page.open_question_by_text(FaqLocators.COST_AND_PAYMENT_QESTION)
        page.is_answer_visible_by_question(FaqLocators.COST_AND_PAYMENT_ANSWER)
        actual_answer = page.get_answer_text_by_question(FaqLocators.COST_AND_PAYMENT_ANSWER)
        assert expected_answer in actual_answer

    @allure.title("Проверка видимости и содержания ответа на второй вопрос FAQ")
    @allure.description(
    "Открываем страницу FAQ, находим вопрос о возможности заказа нескольких самокатов, "
    "раскрываем его и проверяем, что ответ отображается и содержит ожидаемый текст."
    )
    def test_faq_question_2(self, driver):
        expected_answer = answer_2
        page = FaqPage(driver)
        page.open_faq_page()
        page.open_question_by_text(FaqLocators.MULTIPLE_SCOOTERS_AVAILABLE_QESTION)
        page.is_answer_visible_by_question(FaqLocators.MULTIPLE_SCOOTERS_AVAILABLE_ANSWER)
        actual_answer = page.get_answer_text_by_question(FaqLocators.MULTIPLE_SCOOTERS_AVAILABLE_ANSWER)
        assert expected_answer in actual_answer

    @allure.title("Проверка видимости и содержания ответа на третий вопрос FAQ")
    @allure.description(
    "Открываем страницу FAQ, находим вопрос о рассчете аремени аренды, "
    "раскрываем его и проверяем, что ответ отображается и содержит ожидаемый текст."
    )
    def test_faq_question_3(self, driver):
        expected_answer = answer_3
        page = FaqPage(driver)
        page.open_faq_page()
        page.open_question_by_text(FaqLocators.RENT_TIME_CALCULATION_QESTION)
        page.is_answer_visible_by_question(FaqLocators.RENT_TIME_CALCULATION_ANSWER)
        actual_answer = page.get_answer_text_by_question(FaqLocators.RENT_TIME_CALCULATION_ANSWER)
        assert expected_answer in actual_answer

    @allure.title("Проверка видимости и содержания ответа на четвертый вопрос FAQ")
    @allure.description(
    "Открываем страницу FAQ, находим вопрос о возможности оформления заказа на дату заказа, "
    "раскрываем его и проверяем, что ответ отображается и содержит ожидаемый текст."
    )
    def test_faq_question_4(self, driver):
        expected_answer = answer_4
        page = FaqPage(driver)
        page.open_faq_page()
        page.open_question_by_text(FaqLocators.TODAY_BOOKING_POSSIBLE_QESTION)
        page.is_answer_visible_by_question(FaqLocators.TODAY_BOOKING_POSSIBLE_ANSWER)
        actual_answer = page.get_answer_text_by_question(FaqLocators.TODAY_BOOKING_POSSIBLE_ANSWER)
        assert expected_answer in actual_answer

    @allure.title("Проверка видимости и содержания ответа на пятый вопрос FAQ")
    @allure.description(
    "Открываем страницу FAQ, находим вопрос о продлении заказа, "
    "раскрываем его и проверяем, что ответ отображается и содержит ожидаемый текст."
    )
    def test_faq_question_5(self, driver):
        expected_answer = answer_5
        page = FaqPage(driver)
        page.open_faq_page()
        page.open_question_by_text(FaqLocators.RENT_EXTENSION_OR_EARLY_RETURN_QESTION)
        page.is_answer_visible_by_question(FaqLocators.RENT_EXTENSION_OR_EARLY_RETURN_ANSWER)
        actual_answer = page.get_answer_text_by_question(FaqLocators.RENT_EXTENSION_OR_EARLY_RETURN_ANSWER)
        assert expected_answer in actual_answer

    @allure.title("Проверка видимости и содержания ответа на шестой вопрос FAQ")
    @allure.description(
    "Открываем страницу FAQ, находим вопрос про доставку зарядки, "
    "раскрываем его и проверяем, что ответ отображается и содержит ожидаемый текст."
    )
    def test_faq_question_6(self, driver):
        expected_answer = answer_6
        page = FaqPage(driver)
        page.open_faq_page()
        page.open_question_by_text(FaqLocators.CHARGER_INCLUDED_QESTION)
        page.is_answer_visible_by_question(FaqLocators.CHARGER_INCLUDED_ANSWER)
        actual_answer = page.get_answer_text_by_question(FaqLocators.CHARGER_INCLUDED_ANSWER)
        assert expected_answer in actual_answer

    @allure.title("Проверка видимости и содержания ответа на седьмой вопрос FAQ")
    @allure.description(
    "Открываем страницу FAQ, находим вопрос об отмене заказа, "
    "раскрываем его и проверяем, что ответ отображается и содержит ожидаемый текст."
    )
    def test_faq_question_7(self, driver):
        expected_answer = answer_7
        page = FaqPage(driver)
        page.open_faq_page()
        page.open_question_by_text(FaqLocators.ORDER_CANCELLATION_POSSIBLE_QESTION)
        page.is_answer_visible_by_question(FaqLocators.ORDER_CANCELLATION_POSSIBLE_ANSWER)
        actual_answer = page.get_answer_text_by_question(FaqLocators.ORDER_CANCELLATION_POSSIBLE_ANSWER)
        assert expected_answer in actual_answer

    @allure.title("Проверка видимости и содержания ответа на восьмой вопрос FAQ")
    @allure.description(
    "Открываем страницу FAQ, находим вопрос о доставке за МКАД, "
    "раскрываем его и проверяем, что ответ отображается и содержит ожидаемый текст."
    )
    def test_faq_question_8(self, driver):
        expected_answer = answer_8
        page = FaqPage(driver)
        page.open_faq_page()
        page.open_question_by_text(FaqLocators.DELIVERY_BEYOND_MKAD_QESTION)
        page.is_answer_visible_by_question(FaqLocators.DELIVERY_BEYOND_MKAD_ANSWER)
        actual_answer = page.get_answer_text_by_question(FaqLocators.DELIVERY_BEYOND_MKAD_ANSWER)
        assert expected_answer in actual_answer
