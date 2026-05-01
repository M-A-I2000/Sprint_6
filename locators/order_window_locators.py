from selenium.webdriver.common.by import By

class WindowLocators():
    ORDER_CONFIRMATION_WINDOW = (By.XPATH, "//div[@class = 'Order_Modal__YZ-d3']")
    YES_BUTTON = (By.XPATH, "//button[contains(text(), 'Да')]")
    NO_BUTTON = (By.XPATH, "//button[contains(text(), 'Нет')]")
    ORDER_HEADER = (By.XPATH, "//div[contains(text(), 'Заказ оформлен')]")