import time

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from base.base_class import Base
from utilities.logger import Logger


class CatalogClothesPage(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators

    topic_page_title_checkword = "//*[contains(@id, 'pagetitle')]"
    price_dropdown = "//*[contains(@class, 'prices')]"
    min_price_field = "//input[@id='MAX_SMART_FILTER_P1_MIN']"
    max_price_field = "//input[@id='MAX_SMART_FILTER_P1_MAX']"

    product = "(//*[contains(@class, 'item-title')])[5]"

    # Getters

    def get_topic_page_title_checkword(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.topic_page_title_checkword)))

    def get_price_dropdown(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.price_dropdown)))

    def get_min_price_field(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.min_price_field)))

    def get_max_price_field(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.max_price_field)))

    def get_product(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.product)))

    # Actions

    def click_price_dropdown(self):
        self.get_price_dropdown().click()
        print("Нажимаем на выпадающее меню - Цена")

    def input_min_price_field(self, min_price_field):
        self.get_min_price_field().clear()
        self.get_min_price_field().send_keys(min_price_field)
        print(f"Заполняем поле с минимальной ценой товара : {min_price_field}")

    def input_max_price_field(self, max_price_field):
        self.get_max_price_field().clear()
        self.get_max_price_field().send_keys(max_price_field)
        print(f"Заполняем поле с максимальной ценой товара : {max_price_field}")

    def click_product_link(self):
        self.get_product().click()
        print("Нажимаем на продукт - 'Футболка Good Luck grn'\n")

    # Methods

    def select_product(self):

        Logger.add_start_step(method="select_product")

        # Получаем текущий URL
        self.get_current_url()

        # Проверяем, что мы находимся на странице каталога - Одежда
        self.assert_url("https://shop.ciay.ru/catalog/odezhda/")

        # Выбираем фильтры
        self.click_price_dropdown()
        time.sleep(1)
        self.input_min_price_field("2000")
        time.sleep(1)
        self.input_max_price_field("7000")
        time.sleep(3)

        # Переходим в карточку продукта и проверяем, что выбрали нужную
        self.click_product_link()
        self.assert_word(self.get_topic_page_title_checkword(), "Футболка Good Luck grn")

        Logger.add_end_step(url=self.driver.current_url, method="select_product")
