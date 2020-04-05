import pytest

from pages.audience import AudPage
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
        aud_page = AudPage(home_page.driver)
        aud_page.begin_creation()
        segments_before = aud_page.count_segments()
        aud_page.create_segment()
        segments_after = aud_page.count_segments()
        assert segments_before + 1 == segments_after


    @pytest.mark.UI
    def test_wheel_segment(self, auto_log):
        home_page = auto_log
        home_page.find(home_page.locators.SEGMENTS_LINE).click()
        self.aud_page.begin_creation()

        segments_before = self.aud_page.count_segments()
        self.aud_page.create_segment()
        self.aud_page.delete_segment()
        segments_after = self.aud_page.count_segments(True)
        assert segments_before == segments_after
