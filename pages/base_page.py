import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:

    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    @allure.step("Открытие страниыцы по url")
    def open(self, url):
        self.driver.get(url)

    @allure.step("Поиск элемента по локатору")
    def find(self, locator):
        return self.wait.until(
            EC.presence_of_element_located(locator)
        )

    @allure.step("Клик по элементу")
    def click(self, locator):
        self.find(locator).click()

    @allure.step("Внесение данных в поле с определенным локатором")
    def type(self, locator, text):
        element = self.find(locator)
        element.clear()
        element.send_keys(text)
    
    @allure.step("Проверка видимости элемента на экране")    
    def is_element_visible(self, locator):
        try:
            self.wait.until(EC.visibility_of_element_located(locator))
            return True
        except:
            return False

    @allure.step("Получение текущего url")        
    def get_current_url(self):
        return self.driver.current_url
    
    @allure.step("Переключение фокуса на новое окно")
    def focus_on_window(self):
        all_handles = self.driver.window_handles
        if len(all_handles) > 1:
            self.driver.switch_to.window(all_handles[1])
            print(f"Переключились на окно: {all_handles[1]}")
        else:
            print("Второе окно не открыто, остаёмся в текущем")

    @allure.step("Пролистать страницу до определенного элемента")    
    def scroll_to_element(self, locator):
        element = self.driver.find_element(*locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)