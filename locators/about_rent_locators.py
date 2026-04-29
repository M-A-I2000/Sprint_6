from selenium.webdriver.common.by import By

class RentLocators():
    DELIVERY_DATE_INPUT = (By.XPATH, "//input[@placeholder = '* Когда привезти самокат']")
    CALENDAR = (By.XPATH, "//div[@class = 'react-datepicker__month-container']")
    DROPDOWN_ARROW = (By.XPATH, "//span[@class = 'Dropdown-arrow']")
    DAY_RENT_BUTTON = (By.XPATH,"//div[@class = 'Dropdown-option' and contains(text(), 'сутки')]")
    TWO_DAYS_RENT_BUTTON = (By.XPATH, "//div[@class = 'Dropdown-option' and contains(text(), 'двое суток')]")
    THREE_DAYS_RENT_BUTTON = (By.XPATH, "//div[@class = 'Dropdown-option' and contains(text(), 'трое суток')]")
    FOUR_DAYS_RENT_BUTTON = (By.XPATH, "//div[@class = 'Dropdown-option' and contains(text(), 'четверо суток')]")
    FIVE_DAYS_RENT_BUTTON = (By.XPATH, "//div[@class = 'Dropdown-option' and contains(text(), 'пятеро суток')]")
    SIX_DAYS_RENT_BUTTON = (By.XPATH, "//div[@class = 'Dropdown-option' and contains(text(), 'шестеро суток')]")
    SEVEN_DAYS_RENT_BUTTON = (By.XPATH, "//div[@class = 'Dropdown-option' and contains(text(), 'семеро суток')]")
    BLACK_COLOUR_INPUT = (By.XPATH, "//input[@id = 'black']")
    GRAY_COLOUR_INPUT = (By.XPATH, "//input[@id = 'grey']")
    COMMENT_INPUT = (By.XPATH, "//input[@placeholder = 'Комментарий для курьера']")
    BACK_BUTTON = (By.XPATH, "//button[contains(text(), 'Назад')]")
    ORDER_BUTTON = (By.XPATH, "//div[@class = 'Order_Buttons__1xGrp']/button[contains(text(), 'Заказать')]")