from selenium.webdriver.common.by import By

class BaseLocators():
    LOGO_BUTTON = (By.XPATH, "//img[@alt='Scooter']")
    HOME_HEADER = (By.XPATH, "//div[@class = 'Home_Header__iJKdX' and contains(text(), 'Самокат ')]")
    YANDEX_BUTTON = (By.CSS_SELECTOR, "a[href*='yandex']")
    TOP_ORDER_BUTTON = (By.XPATH, "//div[@class = 'Header_Nav__AGCXC']/button[contains(text(), 'Заказать')]")
    BOTTOM_ORDER_BUTTON = (By.XPATH,"//div[@class = 'Home_FinishButton__1_cWm']/button[contains(text(), 'Заказать')]")