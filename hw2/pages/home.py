import os
import time

from selenium.webdriver.support import expected_conditions

from locators.locators_ui import HomeLocators
from pages.base import BasePage


class HomePage(BasePage):
    locators = HomeLocators()
    link_to_traffic_url = 'https://github.com/AlexLoner'
    form_title = 'SouthPark'
    form_text = 'Kenny the best'
    company_name = 'sp_kenny'


    def begin_creation(self):
        try:
            self.wait().until(expected_conditions.visibility_of_all_elements_located(self.locators.CREATE_NEW_CAMPAIGN))
            self.find(self.locators.CREATE_NEW_CAMPAIGN, 7).click()
        except:
            self.wait().until(expected_conditions.visibility_of_all_elements_located(self.locators.CREATE_NEW_CAMPAIGN2))
            self.find(self.locators.CREATE_NEW_CAMPAIGN2, 7).click()

    def count_campaigns(self):
        self.wait().until(expected_conditions.visibility_of_all_elements_located(self.locators.CAMPAIGNS_NUMBER))
        num = len(self.driver.find_elements(*self.locators.CAMPAIGNS_NUMBER))
        return num

    def go_to_traffic(self):
        # choose traffic campaign
        self.find(self.locators.BUTTON_TRAFFIC, 10).click()
        self.fill_field_by_css(selector=self.locators.LINK_TO_TRAFFIC[1], data=self.link_to_traffic_url,
                                    confirm=True)

    def choose_tizer(self):
        tizer = self.find(self.locators.TIZER)
        tizer.is_displayed()
        tizer.click()


    def upload_image(self):
        field_upload = self.find(self.locators.FORM_PICTURE)
        abs_path = os.path.abspath("hw2/help_data/Kenny-sp.jpg")
        field_upload.send_keys(abs_path)

    def fill_form(self):
        # go to form
        el_to_scroll = self.find(self.locators.FORM_TEXT)
        self.scroll_to_element(el_to_scroll)

        # fill text fields
        self.fill_field_by_css(selector=self.locators.FORM_TITLE[1], data=self.form_title)
        self.fill_field_by_css(selector=self.locators.FORM_TEXT[1], data=self.form_text)

        # upload image
        self.upload_image()

        # confirm form and create campaign
        self.find(self.locators.FORM_PICTURE_UPLOAD).click()
        self.find(self.locators.FORM_ADD_AD).click()
        self.find(self.locators.CAMPAIGN_CREATE_BUTTON).click()
