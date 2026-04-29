import allure
import pytest
from pages.base_page import BasePage
from pages.order_page import OrderPage
from pages.order_window_page import OrderWindowPage
from pages.about_rent_page import RentPage

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
    "8. Проверяем статус и убеждаемся, что кнопка отмены заказа видна."
    )
    @pytest.mark.parametrize(
            "name, surname, address, station, number, date",
            [
                ['Иван', 'Иванов', 'Москва', 'Калужская', '89161234567', '12.06.2027'],
                ['Ваня', 'Тестов', 'Проспект мира', 'Войковская', '89993215476', '13.06.2027']
            ]
    )
    def test_order_scooter_by_top_bytton(self, driver, name, surname, address, station, number, date):
        order_page = OrderPage(driver)
        order_page.open_order_page()
        order_page.click_top_order_button()
        order_page.fill_out_the_order_form(name, surname, address, station, number)
        order_page.click_further_button()
        about_rent_page = RentPage(driver)
        about_rent_page.fill_the_date_field(date)
        about_rent_page.fill_the_rent_days_input()
        about_rent_page.choose_black()
        about_rent_page.click_order_button()
        order_window_page = OrderWindowPage(driver)
        order_window_page.click_accept_button()
        order_window_page.click_status_button()
        
        assert order_window_page.is_order_cancellation_button_visible()


    @allure.title("Заказ самоката через нижнюю кнопку")
    @allure.description(
    "1. Открываем страницу заказа.\n"
    "2. Нажимаем нижнюю кнопку заказа.\n"
    "3. Заполняем форму: имя, фамилия, адрес, станция метро, номер телефона.\n"
    "4. Нажимаем «Далее».\n"
    "5. Заполняем дату и срок аренды, выбираем цвет «Серый».\n"
    "6. Переходим далее для подтверждения заказа.\n"
    "7. Принимаем условия.\n"
    "8. Проверяем статус и убеждаемся, что кнопка отмены заказа видна."
    )
    @pytest.mark.parametrize(
            "name, surname, address, station, number, date",
            [
                ['Иван', 'Иванов', 'Москва', 'Калужская', '89161234567', '12.06.2027'],
                ['Ваня', 'Тестов', 'Проспект мира', 'Войковская', '89993215476', '13.06.2027']
            ]
    )
    def test_order_scooter_by_bottom_bytton(self, driver, name, surname, address, station, number, date):
        order_page = OrderPage(driver)
        order_page.open_order_page()
        order_page.click_bottom_order_button()
        order_page.fill_out_the_order_form(name, surname, address, station, number)
        order_page.click_further_button()
        about_rent_page = RentPage(driver)
        about_rent_page.fill_the_date_field(date)
        about_rent_page.fill_the_rent_days_input()
        about_rent_page.choose_gray()
        about_rent_page.click_order_button()
        order_window_page = OrderWindowPage(driver)
        order_window_page.click_accept_button()
        order_window_page.click_status_button()
        
        assert order_window_page.is_order_cancellation_button_visible()

    @allure.title("Переход на главную страницу при клике по логотипу")
    @allure.description(
    "1. Открываем страницу заказа.\n"
    "2. Нажимаем верхнюю кнопку заказа (для активации логотипа).\n"
    "3. Кликаем по логотипу.\n"
    "4. Проверяем, что пользователь оказался на главной странице."
    )
    def test_clicking_the_logo_button_redirects_to_the_home_page(self, driver):
        page = OrderPage(driver)
        page.open_order_page()
        page.click_top_order_button()
        page.go_to_main_page()

        assert page.is_on_main_page()

    @allure.title("Переход на страницу Дзен при клике по логотипу Дзен")
    @allure.description(
    "1. Открываем страницу заказа.\n"
    "2. Кликаем по логотипу Дзен.\n"
    "3. Проверяем, что пользователь перешёл на страницу dzen.ru."
    )
    def test_clicking_the_dzen_logo_redirects_to_the_dzen_page(self, driver):
        page = OrderPage(driver)
        window = BasePage(driver)
        page.open_order_page()
        page.go_to_dzen_page()
        window.focus_on_window()
        page.wait_when_dzen_loads()

        assert "dzen.ru" in window.get_current_url()