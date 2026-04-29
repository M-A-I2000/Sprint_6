from selenium.webdriver.common.by import By

class OrderedLocators():
    SUCCESSFUL_ORDER_WINDOW = (By.XPATH, "//div[@class = 'Order_Modal__YZ-d3']")
    ORDER_HEADER = (By.XPATH, "//div[contains(text(), 'Заказ оформлен')]")
    STATUS_BUTTON = (By.XPATH, "//button[contains(text(), 'Посмотреть статус')]")
    CANCEL_THE_ORDER_BUTTON = (By.XPATH, "//button[contains(text(), 'Отменить заказ')]")