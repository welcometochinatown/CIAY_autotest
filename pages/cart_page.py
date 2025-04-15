import time
import allure

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from base.base_class import Base
from utilities.logger import Logger


class CartPage(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators

    topic_page_title_checkword = "//*[contains(@id, 'pagetitle')]"
    product_size_check = "//*[contains(@class, 'basket-item-property-value')]"
    product_summary_check = "//*[contains(@class, 'basket-coupon-block-total-price-current')]"
    checkout_button = "//*[contains(@class, 'basket-checkout-btn')]"

    clear_cart_button = "//*[contains(@class, 'remove_all_basket')]"
    clear_cart_check = "//*[contains(@class, 'bx-sbb-empty-cart-text')]"

    # Getters

    def get_topic_page_title_checkword(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.topic_page_title_checkword)))

    def get_product_size_check(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.product_size_check)))

    def get_product_summary_check(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.product_summary_check)))

    def get_checkout_button(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.checkout_button)))

    def get_clear_cart_button(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.clear_cart_button)))

    def get_clear_cart_check(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.clear_cart_check)))

    # Actions

    def click_checkout_button(self):
        self.get_checkout_button().click()
        print("Нажимаем на кнопку - Перейти к оформлению")

    def click_clear_cart_button(self):
        self.get_clear_cart_button().click()
        print("Нажимаем на кнопку - очистить\n")

    # Methods

    def check_product_in_cart(self):

        with allure.step("Сheck product in cart"):
            Logger.add_start_step(method="check_product_in_cart")

            # Получаем текущий URL
            self.get_current_url()

            # Проверяем, что мы находимся в корзине
            self.assert_url("https://shop.ciay.ru/basket/")

            # Проверки товара в корзине и делаем скриншот
            self.assert_word(self.get_product_size_check(), "M")
            self.assert_word(self.get_product_summary_check(), "7 000 руб.")
            self.get_screenshot()

            # Переходим к оформлению заказа
            self.click_checkout_button()

            # Проверяем, что перешли к оформлению заказа
            self.assert_word(self.get_topic_page_title_checkword(), "Оформление заказа")
            self.get_screenshot()

            # Возвращаемся в корзину и очищаем список товаров
            self.driver.back()
            time.sleep(1)
            self.click_clear_cart_button()
            time.sleep(1)
            self.assert_word(self.get_clear_cart_check(), "Ваша корзина пуста")

            Logger.add_end_step(url=self.driver.current_url, method="check_product_in_cart")

