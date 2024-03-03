import time
import allure
from selenium.webdriver.common.by import By
import re

from tests.services.utils import (
    make_driver,
    make_screenshot,
    open_drop_down_list,
)
from tests.resources.enums import Browser
from tests.core.exceptions import AllureStepError


class AddJewelryToCart:
    SELECT_JEWELRY_TOPIC = 'select jewelry topic'
    SELECT_FIRST = 'select first item, save price and name'
    SELECT_SECOND = 'select second item, save price and name'
    SELECT_THIRD = 'select third item, save price and name'
    ADD_TO_CART = 'add to cart'
    FIND_PRICE = 'find price'

    ITEM_ID = {
        1: "1127052",
        2: "1126116",
        3: "1125741",
    }

    def __init__(self, browser: Browser):
        self.browser = browser
        self.driver = make_driver(browser=browser)

    def execute(self):
        open_drop_down_list(browser=self.browser, driver=self.driver)

        with allure.step(self.SELECT_JEWELRY_TOPIC):
            try:
                works = self.driver.find_element(
                    By.CSS_SELECTOR,
                    "#left_container > div > ul:nth-child(2) > li:nth-child(5) > a"
                )
                works.click()
            except Exception:
                make_screenshot(browser=self.browser, driver=self.driver)
                raise AllureStepError(browser=self.browser, step=self.SELECT_JEWELRY_TOPIC)

        with allure.step(self.SELECT_FIRST):
            price_1, name_1 = self._select_and_add_to_cart(item=1)
            self.driver.back()
            self.driver.back()

        with allure.step(self.SELECT_SECOND):
            price_2, name_2 = self._select_and_add_to_cart(item=2)
            self.driver.back()
            self.driver.back()

        with allure.step(self.SELECT_THIRD):
            price_3, name_3 = self._select_and_add_to_cart(item=3)

        try:
            assert not "В вашей корзине пока нет товаров" in str(self.driver.page_source)
        except AssertionError("Жанр картины - не реализм"):
            make_screenshot(browser=self.browser, driver=self.driver)
            raise

        with allure.step(self.FIND_PRICE):
            try:
                cart_price_1, cart_name_1 = self.get_price_and_name_from_cart(item=1)
                cart_price_2, cart_name_2 = self.get_price_and_name_from_cart(item=2)
                cart_price_3, cart_name_3 = self.get_price_and_name_from_cart(item=3)
            except Exception:
                make_screenshot(browser=self.browser, driver=self.driver)
                raise AllureStepError(browser=self.browser, step=self.FIND_PRICE)

        if any(
            [
                cart_price_1 != price_1,
                cart_price_2 != price_2,
                cart_price_3 != price_3,
                cart_name_1 != name_1,
                cart_name_2 != name_2,
                cart_name_3 != name_3,
            ]
        ):
            make_screenshot(browser=self.browser, driver=self.driver)
            assert False

        self.driver.close()
        self.driver.quit()
        assert True

    def _select_and_add_to_cart(self, item: int) -> (int, str):
        try:
            chosen_work = self.driver.find_element(
                By.CSS_SELECTOR,
                f"#sa_container > div:nth-child({item+2}) > a:nth-child(1) > div"
            )  # первая картина начинается с индекса 3
            chosen_work.click()
            price = int(re.findall(r'<b>Цена</b> <b>(.*?) руб', str(self.driver.page_source))[0])
            name = self.driver.find_element(
                By.CSS_SELECTOR,
                "#main_container > div:nth-child(3) > div.imgcontainer > h1"
            ).text
        except Exception:
            make_screenshot(browser=self.browser, driver=self.driver)
            raise AllureStepError(browser=self.browser, step=self.SELECT_FIRST)

        with allure.step(self.ADD_TO_CART):
            try:
                add_to_basket = self.driver.find_element(
                    By.CSS_SELECTOR,
                    f"#CartButton{self.ITEM_ID[item]}"
                )
                add_to_basket.click()
                time.sleep(2)
                to_basket = self.driver.find_element(By.CSS_SELECTOR, "#cmodal > div > p > button.ok-button")
                to_basket.click()
            except Exception:
                make_screenshot(browser=self.browser, driver=self.driver)
                raise AllureStepError(browser=self.browser, step=self.ADD_TO_CART)

        return price, name

    def get_price_and_name_from_cart(self, item: int) -> (int, str):
        cart_name = self.driver.find_element(
            By.CSS_SELECTOR,
            f"#cart{self.ITEM_ID[item]} > div.c_cell > div:nth-child(1) > a"
        ).text
        cart_price = int(
            self.driver.find_element(
                By.CSS_SELECTOR,
                f"#cart{self.ITEM_ID[item]} > div.c_cell > div.shop > div.price"
            ).text.split()[0]
        )

        return cart_price, cart_name
