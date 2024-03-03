import allure
from allure_commons.types import AttachmentType
from selenium.webdriver.common.by import By
from selenium.webdriver import Chrome, Firefox

from tests.core.config import setting
from tests.resources.enums import Story, Browser, AllureStep
from tests.core.exceptions import DriverCreateError, AllureStepError


def make_story(story: Story, browser: Browser) -> str:
    return story + ' in ' + browser


def make_screenshot(browser: Browser, driver: Chrome | Firefox) -> None:
    with allure.step(AllureStep.MAKE_SCREENSHOT):
        allure.attach(
            driver.get_screenshot_as_png(),
            name=f"{browser} error",
            attachment_type=AttachmentType.PNG
        )
    driver.close()
    driver.quit()


def make_driver(browser: Browser) -> Chrome | Firefox:
    with allure.step(AllureStep.MAKE_DRIVER):
        try:
            driver = Chrome() if browser == Browser.CHROME else Firefox()
            driver.get(setting.MAIN_TEST_URL)

            return driver
        except Exception:
            make_screenshot(browser=browser, driver=driver)

            raise DriverCreateError(browser=browser)


def open_drop_down_list(browser: Browser, driver: Chrome | Firefox):
    with allure.step(AllureStep.OPEN_DROP_DOWN_LIST):
        try:
            drop_down_list = driver.find_element(
                By.CSS_SELECTOR,
                "#left_container > div > ul:nth-child(2) > li.menu-group.gids > div")
            drop_down_list.click()
        except Exception:
            make_screenshot(browser=browser, driver=driver)

            raise AllureStepError(step=AllureStep.OPEN_DROP_DOWN_LIST, browser=browser)
