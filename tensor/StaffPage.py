from time import sleep

from selenium.webdriver import ActionChains

from BasePage import BasePage


class StaffPage(BasePage):
    def set_company(self):
        self.click_by_css("span[sbisname='OurCompany']")

    def find_company(self):
        self.click_by_css('td.controls-DataGridView__td.controls-DataGridView__firstContentCell')

    def find_person(self, name):
        self.fill_form_by_css('input[placeholder="Укажите ФИО, подразделение, телефон..."]', name)

    def open_card(self):
        self.click_by_css('div[id = "userName"]')

    def close_card(self):
        self.click_by_css('div[sbisname="floatAreaCloseButton"]')

    def open_menu(self):
        self.click_by_css('span.controls-Link__field')
        # self.click_by_css('i[class="controls-Link__icon  icon-16 icon-Profile icon-disabled"][title="Вне работы"]')
        # self.click_by_css('i[class="controls-Link__icon  icon-16 icon-Profile icon-disabled"]')

    def exit(self):

        st = self.driver.find_element_by_css_selector(
            'div[class="asLink ws-hover-target buttons-list-item js-controls-ListView__item controls-ListView__item"][data-id="99"]')
        ch = ActionChains(self.driver)
        ch.click(st)
        sleep(2)
        ch.click(st)
        sleep(2)
        ch.click(st)
        ch.perform()
        # self.click_by_css(
        #     'div[class="asLink ws-hover-target buttons-list-item js-controls-ListView__item controls-ListView__item"][data-id="99"]')
