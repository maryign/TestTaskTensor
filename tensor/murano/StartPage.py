from tensor1.BasePage import BasePage


class MainPage(BasePage):
    def click_signin_button(self):
        self.click_by_css("a.sign-in-button.transparent-button.transparent-button--white")

