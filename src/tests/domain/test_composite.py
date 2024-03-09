import allure

from tests.domain.use_cases.style_is_realism import StyleIsRealism
from tests.domain.use_cases.add_to_favorites import AddToFavorites
from tests.domain.use_cases.include_giraffe import IncludeGiraffe
from tests.domain.use_cases.add_jewelry_to_cart import AddJewelryToCart

from tests.resources.enums import Browser, SeverityType, Story
from tests.services.utils import make_story


class TestUseCases:
    @allure.story(make_story(Story.SECOND, Browser.CHROME))
    @allure.severity(SeverityType.TRIVIAL)
    def test_style_is_realism_chrome(self):
        use_case = StyleIsRealism(browser=Browser.CHROME)
        use_case.execute()

    @allure.story(make_story(Story.SECOND, Browser.FIREFOX))
    @allure.severity(SeverityType.TRIVIAL)
    def test_style_is_realism_firefox(self):
        use_case = StyleIsRealism(browser=Browser.FIREFOX)
        use_case.execute()

    @allure.story(make_story(Story.THIRD, Browser.CHROME))
    @allure.severity(SeverityType.NORMAL)
    def test_add_to_favorites_chrome(self):
        use_case = AddToFavorites(browser=Browser.CHROME)
        use_case.execute()

    @allure.story(make_story(Story.THIRD, Browser.FIREFOX))
    @allure.severity(SeverityType.NORMAL)
    def test_add_to_favorites_firefox(self):
        use_case = AddToFavorites(browser=Browser.FIREFOX)
        use_case.execute()

    @allure.story(make_story(Story.FOURTH, Browser.CHROME))
    @allure.severity(SeverityType.MINOR)
    def test_include_giraffe_chrome(self):
        use_case = IncludeGiraffe(browser=Browser.CHROME)
        use_case.execute()

    @allure.story(make_story(Story.FOURTH, Browser.FIREFOX))
    @allure.severity(SeverityType.MINOR)
    def test_include_giraffe_firefox(self):
        use_case = IncludeGiraffe(browser=Browser.FIREFOX)
        use_case.execute()

    @allure.story(make_story(Story.FIFTH, Browser.CHROME))
    @allure.severity(SeverityType.BLOCKER)
    def test_add_jewelry_to_cart_chrome(self):
        use_case = AddJewelryToCart(browser=Browser.CHROME)
        use_case.execute()

    @allure.story(make_story(Story.FIFTH, Browser.FIREFOX))
    @allure.severity(SeverityType.BLOCKER)
    def test_add_jewelry_to_cart_firefox(self):
        use_case = AddJewelryToCart(browser=Browser.FIREFOX)
        use_case.execute()
