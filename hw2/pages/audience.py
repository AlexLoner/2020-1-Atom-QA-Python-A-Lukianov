import time

from selenium.webdriver.support import expected_conditions
from locators.locators_ui import AudLocators
from pages.base import BasePage


class AudPage(BasePage):
    locators = AudLocators()

    def count_segments(self, update=False):
        if update:  # Need some time to update number on the page
            time.sleep(2)
        try:
            self.wait().until(expected_conditions.visibility_of_all_elements_located(self.locators.SEGMENTS_NUMBER))
            tmp = self.find(self.locators.SEGMENTS_NUMBER)
        except:
            self.wait().until(expected_conditions.visibility_of_all_elements_located(self.locators.SEGMENTS_NUMBER2))
            tmp = self.find(self.locators.SEGMENTS_NUMBER2)
        return int(tmp.text)

    def begin_creation(self):
        try:
            self.find(self.locators.SEGMENTS_NEW).click()
        except:
            self.find(self.locators.SEGMENTS_NEW2).click()

    def create_segment(self):
        self.find(self.locators.ADD_BUTTON).click()
        self.find(self.locators.GALOCHKA).click()
        self.find(self.locators.CONFIRM_SEGMENT_DATA).click()
        self.find(self.locators.CONFIRM_CREATION).click()

    def delete_segment(self):
        self.wait().until(expected_conditions.visibility_of_any_elements_located(self.locators.DEL_BUTTONS))
        self.driver.find_elements_by_css_selector(self.locators.DEL_BUTTONS[1])[-1].click()
        self.wait().until(expected_conditions.visibility_of_element_located(self.locators.CONFIRM_ANNIHILATION))
        self.find(self.locators.CONFIRM_ANNIHILATION).click()


