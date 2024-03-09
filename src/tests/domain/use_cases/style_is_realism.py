import time
import re

import allure
from selenium.webdriver.common.by import By

from tests.domain.use_cases.base import BaseUseCase
from tests.services.utils import (
    make_screenshot,
    open_drop_down_list,

)
from tests.resources.enums import AllureStep
from tests.core.exceptions import AllureStepError


class StyleIsRealism(BaseUseCase):
    OPEN_TROLLEY_PAINTING = 'open trolley painting'
    CHECK_STYLE = 'check genre'

    def execute(self):
        open_drop_down_list(browser=self.browser, driver=self.driver)

        with allure.step(AllureStep.GO_TO_PAINTINGS):
            try:
                paintings = self.driver.find_element(
                    By.CSS_SELECTOR,
                    "#left_container > div > ul:nth-child(2) > li:nth-child(8) > a",
                )
                paintings.click()
            except Exception:
                make_screenshot(browser=self.browser, driver=self.driver)
                raise AllureStepError(browser=self.browser, step=AllureStep.GO_TO_PAINTINGS)

        with allure.step(AllureStep.CHOOSE_GENRE):
            try:
                city_landscape = self.driver.find_element(
                    By.CSS_SELECTOR,
                    "#genrebox > div > label:nth-child(2)",
                )
                city_landscape.click()
                time.sleep(3)
                use = self.driver.find_element(By.CSS_SELECTOR, "#applymsg")
                use.click()
                time.sleep(3)
            except Exception:
                make_screenshot(browser=self.browser, driver=self.driver)
                raise AllureStepError(browser=self.browser, step=AllureStep.CHOOSE_GENRE)

        with allure.step(self.OPEN_TROLLEY_PAINTING):
            try:
                tram_track = self.driver.find_element(
                    By.CSS_SELECTOR,
                    "#sa_container > div:nth-child(5) > a > div",
                )
                tram_track.click()
            except Exception:
                make_screenshot(browser=self.browser, driver=self.driver)
                raise AllureStepError(browser=self.browser, step=self.OPEN_TROLLEY_PAINTING)

        with allure.step(self.CHECK_STYLE):
            try:
                response = str(re.search(r'Стиль: (.*?)\.', str(self.driver.page_source)).group())
            except Exception:
                make_screenshot(browser=self.browser, driver=self.driver)
                raise AllureStepError(browser=self.browser, step=self.CHECK_STYLE)

        if 'реализм' not in response:
            make_screenshot(browser=self.browser, driver=self.driver)
            assert False

        self.driver.close()
        self.driver.quit()
        assert True
