from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def click_element(self, locator):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(locator)).click()

    def is_element_visible(self, locator):
        return WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator))

    def accept_cookies(self):

        accept_button_xpath = "//a[@id='wt-cli-accept-all-btn']"
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, accept_button_xpath))).click()
