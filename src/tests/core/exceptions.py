from tests.resources.enums import Browser, AllureStep


class DriverCreateError(Exception):
    browser: Browser
    message: str = "Произошла ошбика при создании драйвера {browser}"

    def __init__(self, browser: Browser):
        self.browser = browser
        self.message = self.message.format(browser=browser.value)

        super().__init__(self.message)


class AllureStepError(Exception):
    browser: Browser
    step: AllureStep
    message: str = "Произошла ошбика во время шага тестирования: {step} в браузере: {browser}"

    def __init__(self, step: AllureStep | str, browser: Browser):
        self.browser = browser
        self.message = self.message.format(step=step, browser=browser.value)

        super().__init__(self.message)
