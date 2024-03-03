from enum import Enum


class SeverityType(str, Enum):
    BLOCKER = 'blocker'
    CRITICAL = 'critical'
    NORMAL = 'normal'
    MINOR = 'minor'
    TRIVIAL = 'trivial'


class Browser(str, Enum):
    CHROME = 'chrome'
    FIREFOX = 'firefox'


class Story(str, Enum):
    FIRST = (
        "Перейти в “Вышитые картины”, произвести поиск по жанру «Городской пейзаж», "
        "проверить, что картина “Трамвайный путь” присутствует в выдаче."
    )
    SECOND = (
        "Перейти в “Вышитые картины”, произвести поиск по жанру «Городской пейзаж», "
        "открыть подробности картины “Трамвайный путь”, проверить, что стиль картины «Реализм»."
    )
    THIRD = (
        "Перейти в “Батик”, добавить первую картину в избранное, "
        "проверить, что выбранная картина сохранилась в разделе «Избранное»."
    )
    FOURTH = (
        "Ввести в поисковую строку «Жираф», проверить, "
        "что название первой картины содержит слово «Жираф»."
    )
    FIFTH = (
        "Перейти в “Ювелирное искусство”, добавить первое изделие в корзину, "
        "проверить, что выбранный товар находится в корзине, стоимость товара не изменилась."
    )


class AllureStep(str, Enum):
    MAKE_DRIVER = 'make driver'
    MAKE_SCREENSHOT = 'make screenshot'
    OPEN_DROP_DOWN_LIST = 'open drop down list'
