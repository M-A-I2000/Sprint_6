import allure
import pytest
from pages.order_page import OrderPage
from pages.order_window_page import OrderWindowPage
from pages.about_rent_page import RentPage
from pages.main_page import MainPage

class TestOrderScooter:

    @allure.title("Заказ самоката через верхнюю кнопку")
    @allure.description(
    "1. Открываем страницу заказа.\n"
    "2. Нажимаем верхнюю кнопку заказа.\n"
    "3. Заполняем форму: имя, фамилия, адрес, станция метро, номер телефона.\n"
    "4. Нажимаем «Далее».\n"
    "5. Заполняем дату и срок аренды, выбираем цвет «Чёрный».\n"
    "6. Переходим далее для подтверждения заказа.\n"
    "7. Принимаем условия.\n"
    "8. Проверяем статус."
    )
    @pytest.mark.parametrize(
            "name, surname, address, station, number, date",
            [
                ['Иван', 'Иванов', 'Москва', 'Коньково', '89161234567', '12.06.2027'],
                ['Ваня', 'Тестов', 'Проспект мира', 'Войковская', '89993215476', '13.06.2027']
            ]
    )
    def test_order_scooter_by_top_button(self, driver, name, surname, address, station, number, date):
        main_page = MainPage(driver)
        main_page.open_main_page()
        main_page.click_top_order_button()
        order_page = OrderPage(driver)
        order_page.fill_out_the_order_form(name, surname, address, station, number)
        order_page.click_further_button()
        about_rent_page = RentPage(driver)
        about_rent_page.fill_the_date_field(date)
        about_rent_page.fill_the_rent_days_input()
        about_rent_page.choose_black()
        about_rent_page.click_order_button()
        order_window_page = OrderWindowPage(driver)
        order_window_page.click_accept_button()
        
        assert order_window_page.is_order_success_message_visible()


    @allure.title("Заказ самоката через нижнюю кнопку")
    @allure.description(
    "1. Открываем страницу заказа.\n"
    "2. Нажимаем нижнюю кнопку заказа.\n"
    "3. Заполняем форму: имя, фамилия, адрес, станция метро, номер телефона.\n"
    "4. Нажимаем «Далее».\n"
    "5. Заполняем дату и срок аренды, выбираем цвет «Серый».\n"
    "6. Переходим далее для подтверждения заказа.\n"
    "7. Принимаем условия.\n"
    "8. Проверяем статус."
    )
    @pytest.mark.parametrize(
            "name, surname, address, station, number, date",
            [
                ['Иван', 'Иванов', 'Москва', 'Коньково', '89161234567', '12.06.2027'],
                ['Ваня', 'Тестов', 'Проспект мира', 'Войковская', '89993215476', '13.06.2027']
            ]
    )
    def test_order_scooter_by_bottom_button(self, driver, name, surname, address, station, number, date):
        main_page = MainPage(driver)
        main_page.open_main_page()
        main_page.click_bottom_order_button()
        order_page = OrderPage(driver)
        order_page.fill_out_the_order_form(name, surname, address, station, number)
        order_page.click_further_button()
        about_rent_page = RentPage(driver)
        about_rent_page.fill_the_date_field(date)
        about_rent_page.fill_the_rent_days_input()
        about_rent_page.choose_gray()
        about_rent_page.click_order_button()
        order_window_page = OrderWindowPage(driver)
        order_window_page.click_accept_button()
        
        assert order_window_page.is_order_success_message_visible()