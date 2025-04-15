import time
import allure

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from base.base_class import Base
from utilities.logger import Logger


class ProductPage(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators

    topic_page_title_checkword = "//*[contains(@id, 'pagetitle')]"
    size_m = "(//li[contains(@class, 'item')])[2]"
    product_quant_plus_button = "(//*[contains(@class, 'plus')])[6]"
    add_to_cart_button = "//div[@id='bx_117848907_39125_basket_actions']"

    # Getters

    def get_topic_page_title_checkword(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.topic_page_title_checkword)))

    def get_size_m(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.size_m)))

    def get_product_quant_plus_button(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.product_quant_plus_button)))

    def get_add_to_cart_button(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.add_to_cart_button)))

    # Actions

    def click_size_m(self):
        self.get_size_m().click()
        print("Нажимаем на размер - М")

    def click_product_quant_plus_button(self):
        self.get_product_quant_plus_button().click()
        print("Добавляем +1 товар")

    def click_add_to_cart_button(self):
        self.get_add_to_cart_button().click()
        print("Нажимаем на кнопку добавления товара в корзину")

    def click_move_to_cart_button(self):
        self.get_add_to_cart_button().click()
        print("Нажимаем на переход в корзину\n")

    # Methods

    def buy_product(self):

        with allure.step("Buy product"):
            Logger.add_start_step(method="buy_product")

            # Получаем текущий URL
            self.get_current_url()

            # Проверяем, что мы находимся на странице каталога - Одежда
            self.assert_url("https://shop.ciay.ru/catalog/odezhda/futbolki/futbolka-good-luck-grn/")

            # Выбираем размер и количество
            self.click_size_m()
            time.sleep(1)
            self.click_product_quant_plus_button()
            time.sleep(1)

            # Добавляем товар в корзину и нажимаем еще раз, для перехода в корзину
            self.click_add_to_cart_button()
            time.sleep(1)
            self.click_move_to_cart_button()
            time.sleep(1)

            # Проверяем, что перешли в корзину
            self.assert_word(self.get_topic_page_title_checkword(), "Корзина")

            Logger.add_end_step(url=self.driver.current_url, method="buy_product")
