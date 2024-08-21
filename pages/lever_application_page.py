from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from .base_page import BasePage


class LeverApplicationPage(BasePage):
    def is_lever_application_form_opened(self):
        try:
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, ".application-form"))
            )
            return "lever.co" in self.driver.current_url.lower()
        except:
            return False
