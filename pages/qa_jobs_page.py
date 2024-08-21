import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC, wait

from .base_page import BasePage


class QAJobsPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.department_drop_down = None
        self.location_drop_down = None
        self.view_role_button = None
        self.wait = None
        self.department_dropdown = None
        self.location_dropdown = None
        self.url = "https://useinsider.com/careers/quality-assurance/"

    def open(self):
        self.driver.get(self.url)

    def click_see_all_qa_jobs(self):
        see_all_qa_jobs_locator = (By.XPATH, "//a[contains(text(), 'See all QA jobs')]")
        self.click_element(see_all_qa_jobs_locator)

    def filter_jobs(self, location, department):

        location_dropdown = (By.XPATH, "//select[@name='filter-by-location']")
        department_dropdown = (By.XPATH, "//select[@name='filter-by-department']")

        self.click_element(location_dropdown)
        self.click_element((By.XPATH, f"//li[contains(text(), '{location}')]"))

        self.click_element(department_dropdown)
        self.click_element((By.XPATH, f"//li[contains(text(), '{department}')]"))

    def filter_by_location_and_department(self, location, department):

        try:

            if self.location_dropdown is None or self.department_dropdown is None:
                raise ValueError("Dropdown elements are not found on the page.")

            location_select = Select(self.location_dropdown)
            department_select = Select(self.department_dropdown)

            # Seçim yap
            location_select.select_by_visible_text(location)
            department_select.select_by_visible_text(department)


        except Exception as e:
            print(f"An error occurred: {e}")

    def verify_department_contains(driver, expected_department, expected_location):

        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#career-position-list")))


        position_list = driver.find_element(By.CSS_SELECTOR, "#career-position-list")
        driver.execute_script("arguments[0].scrollIntoView();", position_list)


        job_elements = driver.find_elements(By.XPATH, "//div[contains(@class,'position-list-item col')]")

        for i in range(1, len(job_elements) + 1):
            time.sleep(2)  # Java'daki Thread.sleep()'e karşılık gelir

            # Department ve Location verilerini al
            actual_department = driver.find_element(By.XPATH,
                                                    f"(//span[contains(@class,'position-department')])[{i}]").text
            actual_location = driver.find_element(By.XPATH, f"(//div[contains(@class,'position-location')])[{i}]").text

            print(f"actualDepartment = {actual_department}")
            print(f"actualLocation = {actual_location}")

            # Assert işlemleri
            assert expected_department in actual_department, f"Expected department '{expected_department}' not found in '{actual_department}'"
            assert expected_location in actual_location, f"Expected location '{expected_location}' not found in '{actual_location}'"

    def is_job_list_present(self):
        job_list = (By.CSS_SELECTOR, ".jobs-list")
        return self.is_element_visible(job_list)

    def check_job_details(self):
        job_items = self.driver.find_elements(By.CSS_SELECTOR, ".job-item")
        for job in job_items:
            position = job.find_element(By.CSS_SELECTOR, ".position").text
            department = job.find_element(By.CSS_SELECTOR, ".department").text
            location = job.find_element(By.CSS_SELECTOR, ".location").text

            if "Quality Assurance" not in position or \
                    "Quality Assurance" not in department or \
                    "Istanbul, Turkey" not in location:
                return False
        return True

    def click_view_role(self):

        view_role_button = (By.XPATH, "(//a[text()='View Role'])")
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(view_role_button)).click()
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "form#lever-form"))
        )
        assert "Lever" in self.driver.current_url

    def find_elements(self, XPATH, param):
        pass

    def find_element(self, CSS_SELECTOR, param):
        pass

    def execute_script(self, param, position_list):
        pass
