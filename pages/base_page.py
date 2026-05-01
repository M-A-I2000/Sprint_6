import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:

    def __init__(self, driver, timeout=15):
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
        self.driver.switch_to.window(self.driver.window_handles[1])

    @allure.step("Клик на элемент через JavaScript")
    def js_click(self, element):
        self.driver.execute_script("arguments[0].click();", element)

    @allure.step("Пролистать страницу до определенного элемента")    
    def scroll_to_element(self, locator):
        element = self.driver.find_element(*locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    @allure.step("Ожидаем, пока элемент станет кликабельным, и возвращаем его")
    def wait_element_to_be_clickable(self, locator):
        return self.wait.until(EC.element_to_be_clickable(locator))

    @allure.step("Ожидает видимости элемента и возвращает его")
    def wait_visibility_of_element(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))

    @allure.step("Ожидает присутствия элемента в DOM и возвращает его")        
    def wait_presence_of_element(self, locator):
        return self.wait.until(EC.presence_of_element_located(locator))
    
    @allure.step("Ожидает присутствие текста в URL и возвращает результат")
    def wait_when_page_contains_text(self, text):
        page = WebDriverWait(self.driver, 40).until(EC.url_contains(text))
        return page    