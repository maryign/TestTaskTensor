from tensor1.BasePage import BasePage


class SignInPage(BasePage):
    # url = 'http://fix-inside.tensor.ru'
    # url = 'https://appulatebeta.com'
    def setLogin(self, login):
        self.fill_form_by_css("input.controls-TextBox__field.js-controls-TextBox__field[type=text]", login)

    def setPassword(self, password):
        self.fill_form_by_css("input.js-controls-TextBox__field.controls-TextBox__field[type=password]", password)
