from tests.resources.enums import Browser

from tests.services.utils import make_driver


class BaseUseCase:
    def __init__(self, browser: Browser):
        self.browser = browser
        self.driver = make_driver(browser=browser)
