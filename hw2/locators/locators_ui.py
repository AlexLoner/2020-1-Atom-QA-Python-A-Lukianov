from selenium.webdriver.common.by import By


class BaseLocators:

    LOGIN_BUTTON = (By.CLASS_NAME, 'responseHead-module-button-1BMAy4')
    FORM_EMAIL = (By.NAME, 'input[name="email"]')
    FORM_PASSWORD = (By.NAME, 'input[name="password"]')
    PUSH_BUTTON = (By.CLASS_NAME, 'authForm-module-button-2G6lZu authForm-module-disabled-2n9q65')


class HomeLocators:

    CAMPAIGNS_LINE = (By.CSS_SELECTOR, 'a[href="/campaigns"]')
    SEGMENTS_LINE = (By.CSS_SELECTOR, 'a[href="/segments"]')
    CAMPAIGNS_NUMBER = (By.XPATH, '//td[@data-id="campaignName"]')
    CREATE_NEW_CAMPAIGN = (By.CSS_SELECTOR,
                           'a[class ="campaigns-tbl-settings__button campaigns-tbl-settings__button_new"]')
    # CREATE_NEW_CAMPAIGN2 = (By.XPATH, '//span/a[@href="/campaign/new"]')


    CREATE_NEW_CAMPAIGN2 = (By.XPATH, '//span[@class ="empty-table-data-message__text"]//a[@href="/campaign/new"]')
    BUTTON_TRAFFIC = (By.CSS_SELECTOR, 'div[class="column-list-item _traffic"]')
    LINK_TO_TRAFFIC = (By.CSS_SELECTOR, 'input[class="input__inp js-form-element"][data-gtm-id="ad_url_text"]')


    TIZER = (By.ID, '149')
    FORM_TITLE = (By.CSS_SELECTOR, 'input[data-gtm-id="banner_form_title"]')
    FORM_TEXT = (By.CSS_SELECTOR, 'textarea[data-gtm-id="banner_form_text"]')
    FORM_PICTURE = (By.XPATH, '//input[@data-gtm-id="load_image_btn_90_75"]')
    FORM_PICTURE_UPLOAD = (By.CSS_SELECTOR, 'input[type="submit"]')
    FORM_ADD_AD = (By.XPATH, '//span/button[@data-class-name="Submit"]')
    CAMPAIGN_CREATE_BUTTON = (By.XPATH, '//div[@class="button__text" and contains(text(), "Создать кампанию")]')


class AudLocators:

    SEGMENTS_LINE = (By.CSS_SELECTOR, 'a[href="/segments"]')

    SEGMENTS_NEW = (By.XPATH, '//div[@class="segments-list__btn-wrap js-create-button-wrap"]/button')
    SEGMENTS_NEW2 = (By.CSS_SELECTOR, 'a[href="/segments/segments_list/new"]')

    SEGMENTS_NUMBER = (By.CSS_SELECTOR, 'span[class ="js-total-count"]')
    SEGMENTS_NUMBER2 = (By.XPATH, '//div[@class="left-nav__item _active"]//span[@class="left-nav__count js-nav-item-count"]')

    ADD_BUTTON = (By.CSS_SELECTOR, 'span[data-translated="Add audience segments..."]')
    SEGMENTS_NAME_INPUT = (By.XPATH, '//div[@class="js-segment-name"]//input[@class="input__inp js-form-element"]')
    SEGMENTS_NAME_REMOVE = (By.XPATH, '//a[contains(text(), "___")]//..//../td[@data-id="remove"]//span')
    GALOCHKA = (By.CSS_SELECTOR, 'input[class="adding-segments-source__checkbox js-main-source-checkbox"]')
    CONFIRM_SEGMENT_DATA = (By.XPATH, '//div[@class="adding-segments-modal__footer"]//button[@data-class-name="Submit"]')
    CONFIRM_CREATION = (By.CSS_SELECTOR, 'button[data-class-name="Submit"]')

    DEL_BUTTONS = (By.CSS_SELECTOR, 'span[class="icon-cross"]')
    CONFIRM_ANNIHILATION = (By.CSS_SELECTOR, 'button[class="button button_confirm-remove button_general"]')
