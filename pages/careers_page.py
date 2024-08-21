from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from .base_page import BasePage


class CareersPage(BasePage):
    def is_careers_page_opened(self):
        try:
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "body"))
            )
            return "careers" in self.driver.current_url.lower()
        except:
            return False

    def is_locations_block_visible(self):
        locations_locator = (By.CSS_SELECTOR, "#career-our-location")
        return self.is_element_visible(locations_locator)

    def is_teams_block_visible(self):
        teams_locator = (By.CSS_SELECTOR, "#career-find-our-calling")
        return self.is_element_visible(teams_locator)

    def is_life_at_insider_block_visible(self):
        life_at_insider_locator = (By.XPATH, "//h2[text()='Life at Insider']")
        return self.is_element_visible(life_at_insider_locator)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def scroll_to_element(self, element):
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def absences_of_teams_block(self):
        teams_block = self.driver.find_element(By.ID, "teamsBlock")
        self.scroll_to_element(teams_block)
        return teams_block.is_displayed()

    def absences_of_location_block(self):
        location_block = self.driver.find_element(By.ID, "locationBlock")
        self.scroll_to_element(location_block)
        return location_block.is_displayed()

    def absences_of_life_block(self):
        life_at_insider_block = self.driver.find_element(By.ID, "lifeAtInsiderBlock")
        self.scroll_to_element(life_at_insider_block)
        return life_at_insider_block.is_displayed()