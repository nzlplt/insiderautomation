import logging
import traceback

from selenium import webdriver
from pages.home_page import HomePage
from pages.careers_page import CareersPage
from pages.qa_jobs_page import QAJobsPage
from pages.lever_application_page import LeverApplicationPage


class InsiderTest:
    def __init__(self):
        self.driver = webdriver.Chrome()  
        self.driver.maximize_window()
        logging.basicConfig(level=logging.INFO)

    def run_test(self):
        home_page = HomePage(self.driver)
        careers_page = CareersPage(self.driver)
        qa_jobs_page = QAJobsPage(self.driver)
        lever_application_page = LeverApplicationPage(self.driver)

        try:
            home_page.open()
            assert home_page.is_home_page_opened(), "Home page is not opened"
            logging.info("Home page opened successfully")

            home_page.click_company_menu()
            logging.info("Clicked on Company menu")

            home_page.click_careers()
            logging.info("Clicked on Careers")

            assert careers_page.is_careers_page_opened(), "Careers page is not opened"
            logging.info("Careers page opened successfully")

            logging.info("Checking if Locations block is visible")
            assert careers_page.is_locations_block_visible(), "Locations block is not visible"
            logging.info("Locations block is visible")

            logging.info("Checking if Teams block is visible")
            assert careers_page.is_teams_block_visible(), "Teams block is not visible"
            logging.info("Teams block is visible")
            logging.info("Checking if Life at Insider block is visible")
            assert careers_page.is_life_at_insider_block_visible(), "Life at Insider block is not visible"
            logging.info("Life at Insider block is visible")
            qa_jobs_page.open()
            qa_jobs_page.click_see_all_qa_jobs()
            qa_jobs_page.accept_cookies()
            qa_jobs_page.filter_by_location_and_department("Istanbul, Turkey", "Quality Assurance")
            #qa_jobs_page.filter_jobs("Istanbul, Turkey", "Quality Assurance")
            qa_jobs_page.verify_department_contains("Quality Assurance", "Istanbul,Turkey")
            assert qa_jobs_page.is_job_list_present(), "Job list is not present"
            assert qa_jobs_page.check_job_details(), "Job details are incorrect"
            logging.info("Job list is present and details are correct")
            qa_jobs_page.accept_cookies()
            qa_jobs_page.click_view_role()
            assert lever_application_page.is_lever_application_form_opened(), "Lever Application form is not opened"
            logging.info("Lever Application form opened successfully")


        except AssertionError as e:

            logging.error(f"Test failed: {str(e)}")

            logging.error(f"Traceback: {traceback.format_exc()}")

            self.driver.save_screenshot("error_screenshot.png")

        except Exception as e:

            logging.error(f"An unexpected error occurred: {str(e)}")

            logging.error(f"Traceback: {traceback.format_exc()}")

            self.driver.save_screenshot("error_screenshot.png")
        finally:
            self.driver.quit()


if __name__ == "__main__":
    test = InsiderTest()
    test.run_test()
