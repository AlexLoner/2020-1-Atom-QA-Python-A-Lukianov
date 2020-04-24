from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators.locators_ui import BaseLocators


class BasePage:

    locators = BaseLocators()

    def __init__(self, driver):
        self.driver = driver

    def find(self, locator, timeout=None):
        return self.wait(timeout).until(expected_conditions.presence_of_element_located(locator))

    def wait(self, timeout=None):
        if timeout is None:
            timeout = 8
        return WebDriverWait(self.driver, timeout=timeout)

    def fill_field_by_xpath(self, selector, data, confirm=False):
        field = self.driver.find_element_by_xpath(selector)
        field.clear()
        field.send_keys(data)
        if confirm:
            field.send_keys(Keys.RETURN)

    def fill_field_by_css(self, selector, data, confirm=False):
        field = self.driver.find_element_by_css_selector(selector)
        field.clear()
        field.send_keys(data)
        if confirm:
            field.send_keys(Keys.RETURN)

    def scroll_to_element(self, element):
        self.driver.execute_script('arguments[0].scrollIntoView(true);', element)

    def _log_in(self, email, password):
        log_button = self.find(self.locators.LOGIN_BUTTON)
        log_button.click()

        self.fill_field_by_css(selector=self.locators.FORM_EMAIL[1], data=email)
        self.fill_field_by_css(selector=self.locators.FORM_PASSWORD[1], data=password, confirm=True)
