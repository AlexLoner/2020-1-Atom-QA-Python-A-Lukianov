import string
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support import expected_conditions
from locators.locators_ui import AudLocators
from pages.base import BasePage
import random


class AudPage(BasePage):
    locators = AudLocators()

    def begin_creation(self):
        try:
            self.find(self.locators.SEGMENTS_NEW).click()
        except:
            self.find(self.locators.SEGMENTS_NEW2).click()

    def create_segment(self):
        self.find(self.locators.SEGMENTS_NAME_INPUT)
        name = ''.join(random.choices(string.ascii_letters, k=10))
        self.fill_field_by_xpath(self.locators.SEGMENTS_NAME_INPUT[1], data=name)
        self.find(self.locators.ADD_BUTTON).click()
        self.find(self.locators.GALOCHKA).click()
        self.find(self.locators.CONFIRM_SEGMENT_DATA).click()
        self.find(self.locators.CONFIRM_CREATION).click()
        return name

    def delete_segment(self, name):
        self.wait().until(expected_conditions.visibility_of_any_elements_located(self.locators.DEL_BUTTONS))
        delete_segment = self.locators.SEGMENTS_NAME_REMOVE[1].replace('___', name)
        loc = (self.locators.SEGMENTS_NAME_REMOVE[0], delete_segment)
        self.find(loc).click()
        self.wait().until(expected_conditions.visibility_of_element_located(self.locators.CONFIRM_ANNIHILATION))
        self.find(self.locators.CONFIRM_ANNIHILATION).click()
        self.driver.refresh()
        return self.check_exist(loc)

    def check_exist(self, loc):
        try:
            self.find(loc)
            return True
        except NoSuchElementException:
            return False
        except TimeoutException:
            return False
