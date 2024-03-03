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
    browser: Browser

    SELECT_JEWELRY_TOPIC = 'select jewelry topic'
    ADD_FIRST = 'add first item, save price and name'
    ADD_SECOND = 'add second item, save price and name'
    ADD_THIRD = 'add third item, save price and name'
    ADD_TO_CART = 'add to cart'
    FIND_PRICE = 'find price'

    def __init__(self, browser: Browser):
        self.browser = browser

    def execute(self):
        driver = make_driver(self.browser)

        open_drop_down_list(browser=self.browser, driver=driver)

        with allure.step(self.SELECT_JEWELRY_TOPIC):
            try:
                works = driver.find_element(
                    By.CSS_SELECTOR,
                    "#left_container > div > ul:nth-child(20) > li:nth-child(5) > a"
                )
                works.click()
            except Exception:
                make_screenshot(browser=self.browser, driver=driver)
                raise AllureStepError(browser=self.browser, step=self.SELECT_JEWELRY_TOPIC)

        with allure.step(self.ADD_FIRST):
            try:
                chosen_work = driver.find_element(
                    By.CSS_SELECTOR,
                    "#sa_container > div:nth-child(3) > a:nth-child(1) > div"
                )
                chosen_work.click()
                price_1 = int(re.findall(r'<b>Цена</b> <b>(.*?) руб', str(driver.page_source))[0])
            except Exception:
                make_screenshot(browser=self.browser, driver=driver)
                raise AllureStepError(browser=self.browser, step=self.ADD_FIRST)

        with allure.step(self.ADD_TO_CART):
            try:
                add_to_basket = driver.find_element(By.CSS_SELECTOR, "#CartButton1127052")
                add_to_basket.click()
                time.sleep(2)
                to_basket = driver.find_element(By.CSS_SELECTOR, "#cmodal > div > p > button.ok-button")
                to_basket.click()
            except Exception:
                make_screenshot(browser=self.browser, driver=driver)
                raise AllureStepError(browser=self.browser, step=self.ADD_TO_CART)

        try:
            assert not "В вашей корзине пока нет товаров" in str(driver.page_source)
        except AssertionError("Жанр картины - не реализм"):
            make_screenshot(browser=self.browser, driver=driver)
            raise

        with allure.step(self.FIND_PRICE):
            try:
                cart_price_1 = re.findall(r'class="price">(.*?) руб', str(driver.page_source))[0]
            except Exception:
                make_screenshot(browser=self.browser, driver=driver)
                raise AllureStepError(browser=self.browser, step=self.FIND_PRICE)

        if int(str(cart_price_1)) != price_1:
            make_screenshot(browser=self.browser, driver=driver)
            assert False

        driver.close()
        driver.quit()
        assert True
