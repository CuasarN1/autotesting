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


class TrolleyTrackExists(BaseUseCase):
    FIND_TROLLEY_TRACK = 'find trolley track'

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

        with allure.step(self.FIND_TROLLEY_TRACK):
            try:
                response = re.findall(
                    r'<meta itemprop="description" content="(.*)">',
                    str(self.driver.page_source)
                )
                flag = False
                for item in response:
                    if "Трамвайный путь" in item:
                        flag = True
            except Exception:
                make_screenshot(browser=self.browser, driver=self.driver)
                raise AllureStepError(browser=self.browser, step=self.FIND_TROLLEY_TRACK)

        if not flag:
            make_screenshot(browser=self.browser, driver=self.driver)
            assert False

        self.driver.close()
        self.driver.quit()
        assert True
