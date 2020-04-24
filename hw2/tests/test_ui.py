import pytest

from tests.base_ui import BaseCase


class Test(BaseCase):

    @pytest.mark.UI
    def test_login_pos(self, auto_log):
        home_page = auto_log
        home_page.find(home_page.locators.CAMPAIGNS_LINE).is_displayed()

    @pytest.mark.UI
    def test_login_negative(self):
        self.base_page._log_in(self.config['kenny'], 'sdfajksdhfkj786')
        self.driver.find_element_by_css_selector('button[class="mcBtn"]').is_displayed()

    @pytest.mark.UI
    def test_create_campaign(self, auto_log):
        home_page = auto_log

        try:
            campaigns_before = home_page.count_campaigns()
            home_page.begin_creation()
        except:
            home_page.begin_creation()
            campaigns_before = 1  # Including hat of the table

        home_page.go_to_traffic()
        home_page.choose_tizer()
        home_page.fill_form()

        # check existence of new campaign
        campaigns_after = home_page.count_campaigns()
        assert campaigns_before + 1 == campaigns_after

    @pytest.mark.UI
    def test_create_segment(self, auto_log):
        home_page = auto_log
        home_page.find(home_page.locators.SEGMENTS_LINE).click()
        self.aud_page.begin_creation()
        name = self.aud_page.create_segment()

        # search new segment
        new_segment = self.aud_page.locators.SEGMENTS_NAME_REMOVE[1].replace('___', name)
        loc = (self.aud_page.locators.SEGMENTS_NAME_REMOVE[0], new_segment)
        res = self.aud_page.check_exist(loc)
        assert res

    @pytest.mark.UI
    def test_wheel_segment(self, auto_log):
        home_page = auto_log
        home_page.find(home_page.locators.SEGMENTS_LINE).click()
        self.aud_page.begin_creation()
        name = self.aud_page.create_segment()
        print(name)
        res = self.aud_page.delete_segment(name=name)
        assert not res
