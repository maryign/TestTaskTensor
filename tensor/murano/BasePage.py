from time import sleep

from selenium.webdriver import ActionChains


class BasePage(object):
    url = None

    def __init__(self, driver):
        self.driver = driver

    def fill_form_by_css(self, form_css, value):
        self.driver.find_element_by_css_selector(form_css).send_keys(value)

    def click_by_css(self, form_css):
        self.driver.find_element_by_css_selector(form_css).click()

    def double_click_by_css(self, form_css):
        st = self.driver.find_element_by_css_selector(form_css)
        ch = ActionChains(self)
        ch.click(st)
        sleep(5)
        ch.click(st)
        ch.perform()

    def navigate(self):
        self.driver.get(self.url)
