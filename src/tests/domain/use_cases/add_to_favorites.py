import allure
from selenium.webdriver.common.by import By

from tests.domain.use_cases.base import BaseUseCase
from tests.services.utils import (
    make_screenshot,
    open_drop_down_list,

)
from tests.core.exceptions import AllureStepError


class AddToFavorites(BaseUseCase):
    GO_TO_BATIC = 'go to batic'
    CHOOSE_PAINTING = 'choose painting'
    ADD_TO_FAVORITE = 'add to favorite'
    GO_TO_FAVORITES = 'go to favorites'
    SEARCH_IN_FAVORITES = 'search in favorites'

    def execute(self):
        open_drop_down_list(browser=self.browser, driver=self.driver)

        with allure.step(self.GO_TO_BATIC):
            try:
                paintings = self.driver.find_element(
                    By.CSS_SELECTOR,
                    "#left_container > div > ul:nth-child(2) > li:nth-child(3) > a"
                )
                paintings.click()
            except Exception:
                make_screenshot(browser=self.browser, driver=self.driver)
                raise AllureStepError(browser=self.browser, step=self.GO_TO_BATIC)

        with allure.step(self.CHOOSE_PAINTING):
            try:
                chosen_painting = self.driver.find_element(
                    By.CSS_SELECTOR,
                    "#sa_container > div:nth-child(3) > a:nth-child(1) > div"
                )
                chosen_painting.click()
            except Exception:
                make_screenshot(browser=self.browser, driver=self.driver)
                raise AllureStepError(browser=self.browser, step=self.CHOOSE_PAINTING)

        with allure.step(self.ADD_TO_FAVORITE):
            try:
                name_at_page = self.driver.find_element(
                    By.CSS_SELECTOR,
                    "#main_container > div:nth-child(3) > div.imgcontainer > h1"
                ).text
                favorite_button = self.driver.find_element(
                    By.CSS_SELECTOR,
                    "#main_container > div:nth-child(3) > div.infocontainer > div.sale-span > span"
                )
                favorite_button.click()
            except Exception:
                make_screenshot(browser=self.browser, driver=self.driver)
                raise AllureStepError(browser=self.browser, step=self.ADD_TO_FAVORITE)

        with allure.step(self.GO_TO_FAVORITES):
            try:
                favorites = self.driver.find_element(By.CSS_SELECTOR, "body > div.topheader > span.fvtico > img")
                favorites.click()
            except Exception:
                make_screenshot(browser=self.browser, driver=self.driver)
                raise AllureStepError(browser=self.browser, step=self.GO_TO_FAVORITES)

        with allure.step(self.SEARCH_IN_FAVORITES):
            try:
                name_at_favorites = self.driver.find_element(
                    By.CSS_SELECTOR,
                    "#sa_container > div.post > a:nth-child(1) > div"
                ).text.split('\n')[1]
            except Exception:
                make_screenshot(browser=self.browser, driver=self.driver)
                raise AllureStepError(browser=self.browser, step=self.SEARCH_IN_FAVORITES)

        if name_at_page != name_at_favorites:
            make_screenshot(browser=self.browser, driver=self.driver)
            assert False

        self.driver.close()
        self.driver.quit()
        assert True
