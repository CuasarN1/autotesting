import time
import re

import allure
from selenium.webdriver.common.by import By

from tests.domain.use_cases.base import BaseUseCase
from tests.services.utils import make_screenshot
from tests.core.exceptions import AllureStepError


class IncludeGiraffe(BaseUseCase):
    ENTER_GIRAFFE = 'enter giraffe'
    SEARCH_FOR_GIRAFFE = 'search for giraffe'
    GIRAFFE_KEY = 'Жираф'

    def execute(self) -> None:
        with allure.step(self.ENTER_GIRAFFE):
            try:
                find_bar = self.driver.find_element(
                    By.CSS_SELECTOR,
                    "#MainSearchForm > div > div:nth-child(1) > input.inp.scLarge"
                )
                find_bar.click()
                find_bar.send_keys(self.GIRAFFE_KEY)
                use = self.driver.find_element(By.CSS_SELECTOR, "button.control")
                use.click()
                time.sleep(3)
            except Exception:
                make_screenshot(browser=self.browser, driver=self.driver)
                raise AllureStepError(browser=self.browser, step=self.ENTER_GIRAFFE)

        with allure.step(self.SEARCH_FOR_GIRAFFE):
            try:
                response = re.search(
                    r'<meta itemprop="description" content="(.*?)">',
                    str(self.driver.page_source)
                ).group()
            except Exception:
                make_screenshot(browser=self.browser, driver=self.driver)
                raise AllureStepError(browser=self.browser, step=self.SEARCH_FOR_GIRAFFE)

        if self.GIRAFFE_KEY not in response:
            make_screenshot(browser=self.browser, driver=self.driver)
            assert False

        self.driver.close()
        self.driver.quit()
        assert True
