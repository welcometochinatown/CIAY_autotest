import time

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from base.base_class import Base
from utilities.logger import Logger


class MainPage(Base):
    url = 'https://shop.ciay.ru/'

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators

    personal_button = "(//*[contains(@class, 'personal-link')])[2]"
    email_login_field = "//input[@id='USER_LOGIN_POPUP']"
    password_field = "//input[@id='USER_PASSWORD_POPUP']"
    login_button = "//button[@name='Login1']"

    login_popup_checkword = "//*[contains(@class, 'form_head')]"
    topic_page_title_checkword = "//*[contains(@id, 'pagetitle')]"
    topic_heading_checkword = "//*[contains(@class, 'topic__heading')]"

    select_clothes_catalog = "(//*[contains(@class, 'dropdown-toggle')])[3]"

    # Getters

    def get_personal_button(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.personal_button)))

    def get_email_login_field(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.email_login_field)))

    def get_password_field(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.password_field)))

    def get_login_button(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.login_button)))

    def get_login_popup_checkword(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.login_popup_checkword)))

    def get_topic_page_title_checkword(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.topic_page_title_checkword)))

    def get_topic_heading_checkword(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.topic_heading_checkword)))

    def get_select_clothes_catalog(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.select_clothes_catalog)))

    # Actions

    def click_personal_button(self):
        self.get_personal_button().click()
        print("Нажимаем на кнопку входа в личный кабинет")

    def input_email_login_field(self, user_name_or_login):
        self.get_email_login_field().send_keys(user_name_or_login)
        print(f"Заполняем поле 'E-mail/Логин' : {user_name_or_login}")

    def input_password_field(self, password):
        self.get_password_field().send_keys(password)
        print(f"Заполняем поле 'E-mail/Логин' : {password}")

    def click_login_button(self):
        self.get_login_button().click()
        print("Нажимаем на кнопку ВОЙТИ")

    def click_select_clothes_catalog(self):
        self.get_select_clothes_catalog().click()
        print("Нажимаем на кнопку каталога - Одежда\n")

    # Methods

    def login_and_verify(self):

        Logger.add_start_step(method="login_and_verify")

        # Нажимаем на pop-up с авторизацией
        self.click_personal_button()

        # Проверяем, что открылся pop-up с авторизацией
        self.assert_word(self.get_login_popup_checkword(), "Личный кабинет")

        # Вводим тестовые данные для авторизации и нажимаем на кнопку Login
        self.input_email_login_field("petrotesterrino@proton.me")
        self.input_password_field("petpetVvi7pgtfdc")
        self.click_login_button()
        time.sleep(1)

        # Нажимаем на кнопку перехода в личный кабинет и проверяем, что перешли
        self.click_personal_button()
        self.assert_word(self.get_topic_heading_checkword(), "Личный кабинет")

        Logger.add_end_step(url=self.driver.current_url, method="login_and_verify")

    def enter_main_page(self):

        Logger.add_start_step(method="enter_main_page")

        self.driver.get(self.url)
        self.driver.maximize_window()

        # Получаем текущий URL
        self.get_current_url()

        # Авторизуемся и проверяем, что зашли в систему
        self.login_and_verify()

        # Нажимаем на кнопку перехода в каталог одежды
        self.click_select_clothes_catalog()

        # Проверяем, что перешли в каталог
        self.assert_word(self.get_topic_page_title_checkword(), "Одежда")

        Logger.add_end_step(url=self.driver.current_url, method="enter_main_page")
