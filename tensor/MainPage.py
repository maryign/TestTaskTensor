from time import sleep
from selenium.webdriver import ActionChains

from BasePage import BasePage


class MainPage(BasePage):
    def staff_submit(self):
        st = self.driver.find_element_by_css_selector(
            "span[class = 'navigation-LeftNavigation__icon staff navigation-LeftNavigation__hoverActive']")
        ch = ActionChains(self.driver)
        ch.click(st)
        sleep(2)
        ch.click(st)
        sleep(2)
        ch.click(st)
        ch.perform()
