from selenium.webdriver.common.by import By

class OrderLocators():
    NAME_INPUT = (By.XPATH, "//input[@placeholder = '* Имя']")
    SURNAME_INPUT = (By.XPATH, "//input[@placeholder = '* Фамилия']")
    ADDRESS_INPUT = (By.XPATH,"//input[@placeholder = '* Адрес: куда привезти заказ']")
    METRO_STATION_INPUT = (By.XPATH, "//input[@placeholder = '* Станция метро']")
    TELEPHONE_INPUT = (By.XPATH, "//input[@placeholder = '* Телефон: на него позвонит курьер']")
    FURTHER_BUTTON = (By.XPATH,"//button[contains(text(), 'Далее')]")
