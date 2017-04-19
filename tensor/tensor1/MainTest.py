import unittest

import LoginPage
from selenium import webdriver


class SignupTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

    # def logg(self, logger):
    #     logger.setLevel(logging.INFO)
    #     formatter = logging.Formatter('%(asctime)s %(name)-12s %(levelname)-8s %(message)s')
    #     console = logging.StreamHandler()
    #     console.setLevel(logging.WARNING)
    #     console.setFormatter(formatter)
    #
    #     filehandler = logging.FileHandler('logger.log')
    #     filehandler.setLevel(logging.INFO)
    #     filehandler.setFormatter(formatter)
    #
    #     logger.addHandler(console)
    #     logger.addHandler(filehandler)

    def testSteps(self):
        # logger = logging.getLogger(__name__)
        # self.logg(logger)
        # wait = WebDriverWait(self.driver, 120)
        homepage = LoginPage.LoginPage(self.driver)
        homepage.navigate()
        # logger.warning('Login page open')
        # wait.until(EC.presence_of_all_elements_located(
        #     (By.CSS_SELECTOR, "div[class = 'loginForm__main ws-component ws-enabled ws-has-focus'")))
        #
        # homepage.setLogin('check_rigth_user')
        # homepage.setPassword('qwerty123' + Keys.ENTER)
        #
        # # print(self.driver.title)
        # assert "СБИС" in self.driver.title
        #
        # wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "div[class='ws-window-overlay']")))
        # logger.info('Login done')
        # logger.warning('Main page open')
        #
        # mainpage = MainPage(self.driver)
        # mainpage.staff_submit()
        #
        # staffpage = StaffPage(self.driver)
        # wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "span[sbisname='OurCompany']")))
        # # print(self.driver.title)
        # assert "Сотрудники" in self.driver.title
        # logger.warning('Staff page open')
        # wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'span[sbisname="OurCompany"]')))
        # staffpage.set_company()
        # wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,
        #                                              "div[class = 'ws-window-titlebar-custom ws-sticky-header__block ws-float-area__close-button-wrapper ws-window-titlebar ws-sticky-header__fixed ws-sticky-header__registered'][title='Выберите организацию']")))
        #
        # # проверка: открылась форма с подразделениями
        # assert "Выберите организацию" in self.driver.page_source
        # logger.info('Window with units open')
        #
        # staffpage.find_company()
        # # проверка: текст ссылки изменился, стала Наша компания
        # wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,"span[data-component='SBIS3.CONTROLS.SelectorButton']")))
        # assert 'Наша компания' in self.driver.find_element_by_css_selector("span[data-component='SBIS3.CONTROLS.SelectorButton']").text
        # staffpage.find_person('Белова Олеся Александровна')
        # wait.until(EC.visibility_of_element_located(
        #     (By.CSS_SELECTOR, 'div[class="marginForHint listEmpl-first-line ws-ellipsis"]')))
        # # проверка: такая запись в таблице найдена
        # assert "Белова Олеся" in self.driver.page_source
        # logger.info('Person was found')
        # staffpage.open_card()
        # wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[name="CardButtons"]')))
        # # проверка: карточка открылась
        # assert 'Заходил'  in self.driver.page_source
        # logger.info('Card open')
        # # print(self.driver.page_source)
        # staffpage.close_card()
        # sleep(5)
        # # проверка: карточка закрылась
        # assert 'Заходил'  not in self.driver.page_source
        # logger.info('Card close')
        # sleep(15)
        # # self.driver.find_element_by_css_selector('span.controls-Link__field').click()
        # staffpage.open_menu()
        #
        # wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,             'div[class="asLink ws-hover-target buttons-list-item js-controls-ListView__item controls-ListView__item"][data-id="99"]')))
        # # проверка: открылось меню
        # assert 'Личный аккаунт'  in self.driver.page_source
        # logger.info('Menu open')
        # staffpage.exit()
        # wait.until(EC.title_contains('Вход в систему'))
        # # проверка: вышли с сайта
        # assert 'Вход в систему' in self.driver.title
        # logger.info('Exit done')
        # logger.warning('Exit done')
        # logger.warning('Test done')


    def tearDown(self):
        self.driver.close()
