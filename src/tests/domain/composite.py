import allure

from tests.domain.use_cases.add_jewelry_to_cart import AddJewelryToCart

from tests.resources.enums import Browser, SeverityType, Story
from tests.services.utils import make_story


class TestUseCases:
    @allure.story(make_story(Story.FIFTH, Browser.CHROME))
    @allure.severity(SeverityType.BLOCKER)
    def test_add_jewelry_to_cart_chrome(self):
        use_case = AddJewelryToCart(browser=Browser.CHROME)

        use_case.execute()

    @allure.story(make_story(Story.FIFTH, Browser.CHROME))
    @allure.severity(SeverityType.BLOCKER)
    def test_add_jewelry_to_cart_firefox(self):
        use_case = AddJewelryToCart(browser=Browser.FIREFOX)

        use_case.execute()
