from BasePage import BasePage


class LoginPage(BasePage):
    url = 'http://fix-inside.tensor.ru'

    def setLogin(self, login):
        self.fill_form_by_css("input.controls-TextBox__field.js-controls-TextBox__field[type=text]", login)

    def setPassword(self, password):
        self.fill_form_by_css("input.js-controls-TextBox__field.controls-TextBox__field[type=password]", password)
