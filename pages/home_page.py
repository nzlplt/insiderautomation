from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from .base_page import BasePage


class HomePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.url = "https://useinsider.com/"

    def open(self):
        self.driver.get(self.url)

    def is_home_page_opened(self):
        try:
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "body"))
            )
            return self.driver.current_url.startswith(self.url)
        except:
            return False

    def click_company_menu(self):
        company_menu_locator = (By.XPATH, "//a[contains(text(), 'Company')]")
        self.click_element(company_menu_locator)

    def click_careers(self):
        careers_locator = (By.XPATH, "//a[contains(text(), 'Careers')]")
        self.click_element(careers_locator)
