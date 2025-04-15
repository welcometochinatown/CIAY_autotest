import time

import allure
from selenium import webdriver

from pages.main_page import MainPage
from pages.catalog_clothes_page import CatalogClothesPage
from pages.product_page import ProductPage
from pages.cart_page import CartPage


@allure.description("Test buy product")
def test_buy_product(set_group, set_up):
    """

    Test path:

    1. Переходим на сайт по url
    2. Нажимаем на кнопку авторизации
    3. Проверяем, что открылся поп-ап с авторизацией по ключевому слову
    4. Авторизуемся с заданными email и password и нажимаем кнопку ВОЙТИ
    5. Нажимаем на кнопку авторизации
    6. Проверяем, что перешли в личный кабинет по ключевому слову/url
    7. Нажимаем на кнопку одежда
    8. Меняем фильтр ЦЕНА - 2000 - 7000
    9. Нажимаем на товар "Футболка Good Luck grn"
    10. Проверяем, что перешли на страницу товара по ключевому слову/url
    11. Выбираем размер М и 2 штуки, добавляем в корзину
    12. Переходим в корзину
    13. Проверяем, что добавился нужный товар, количество, сумму, делаем скриншот
    14. Нажимаем на кнопку Перейти к оформлению
    15. Проверяем, что перешли на страницу оформления, делаем скриншот
    16. Возвращаемся на страницу с корзиной
    17. Нажимаем на кнопку очистить
    18. Завершаем тест
    _______________________

    Ожидаемый результат:
    Положительное прохождение всего бизнес-пути с заданными параметрами,
    2 скриншота (страница товара в корзине и страница оформления заказа)

    :param set_up:
    :param set_group:
    :return:
    """

    options = webdriver.FirefoxOptions()
    driver = webdriver.Firefox(options=options)

    mp = MainPage(driver)
    mp.enter_main_page()

    ccp = CatalogClothesPage(driver)
    ccp.select_product()

    pp = ProductPage(driver)
    pp.buy_product()

    cp = CartPage(driver)
    cp.check_product_in_cart()

    time.sleep(3)
    driver.quit()
