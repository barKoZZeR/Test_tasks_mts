import pytest
from playwright.sync_api import Page

@pytest.fixture
def setup(page: Page):
    # Ставим таймаут 30 секунд
    page.set_default_timeout(30000)
    yield page

def test_positive_case(setup):
    page = setup

    # Шаг 1: Открываем сайт mts.ru
    page.goto("https://mts.ru")

    # Шаг 2: Кликаем на наш регион, чтобы его изменить
    page.wait_for_selector('mts-header-button-location > div > div')
    page.click('mts-header-button-location > div > div')

    # Ожидание 3 секунды
    page.wait_for_timeout(3000)

    # Ожидание появления списка городов и выбор "Санкт-Петербург"
    page.wait_for_selector('#grid-favorite-2214168')

    # Шаг 3: Кликаем на "Санкт-Петербург", чтобы поменять регион
    page.click('#grid-favorite-2214168')

    # Шаг 4: Нажимаем на кнопку "Тарифы" и находим Тариф №1
    page.click('body > mts-root > div.g-page-wrapper > div > div.mts16-footer__to-bottom-content > mts-main-page > mts-widget-zone:nth-child(1) > mts-ecosystem-navigation-widget > section > div > div > div > a:nth-child(1)')

    # Ожидаем появления элемента "Тариф № 1"
    page.wait_for_selector('#\\34 547316 > mm-web-universal-card > div')

    # Шаг 5: Нажимаем на кнопку "Подключить", которая находится внизу элемента "Тариф №1"
    page.click('#\\34 547316 > mm-web-universal-card > div > div.card-footer.card-footer__padding.card-footer__margin > div.card-actions__wrapper.card-actions__wrapper-margin > mm-web-universal-card-button:nth-child(1) > mm-web-button > div > button')

    # Убеждаемся в том, что появляется форма для ввода адреса
    page.wait_for_selector('#mat-dialog-0')

    # Шаг 6: Вводим корректный адрес, например: "Санкт-Петербург, Новоколомяжский проспект, 11"
    page.fill('#mat-dialog-0 > mts-tariffs-address-dialog > section > div.map-dialog__search-wrapper.ng-tns-c131-1.ng-star-inserted > mts-address-search-input > div > div > div > mts-autocomplete-input > mts-input > div > input', 'Санкт-Петербург, Новоколомяжский проспект, 11')

    # Шаг 7: Выбираем предложенный вариант адреса
    page.wait_for_timeout(5000)

    # Ожидаем появления списка вариантов
    page.wait_for_selector('mat-option')

    # Клик на первый вариант в списке
    page.locator('mat-option').nth(0).click()

    # Ожидаем, пока прогрузится наша локация
    page.wait_for_timeout(5000)

    # Шаг 8: Нажимаем на кнопку "Проверить"
    page.click('#mat-dialog-0 > mts-tariffs-address-dialog > section > div.map-dialog__search-wrapper.ng-tns-c131-1.ng-star-inserted > button')

    # Шаг 9: Проверяем, что появляется форма для заполнения данных
    assert page.wait_for_selector('body > div.g-page-wrapper > div > div.mts16-footer__to-bottom-content > mts-tariffs-catalog-main > mts-tariffs-catalog > div.tabs.tabs_relative.tabs_combined.content__wrap.basket_padding > div > div > div > mts-connect-basket > div > div.connect-basket__content > div.connect-basket__form.ng-star-inserted > mts-connect-simple-form-map > div > form')


import pytest
from playwright.sync_api import Page

@pytest.fixture
def setup(page: Page):
    # Ставим таймаут 30 секунд
    page.set_default_timeout(30000)
    yield page

def test_negative_case(setup):
    page = setup

    # Шаг 1: Открываем сайт mts.ru
    page.goto("https://mts.ru")

    # Шаг 2: Кликаем на наш регион, чтобы его изменить
    page.wait_for_selector('mts-header-button-location > div > div')
    page.click('mts-header-button-location > div > div')

    # Ожидание 3 секунды
    page.wait_for_timeout(3000)

    # Ожидание появления списка городов и выбор "Санкт-Петербург"
    page.wait_for_selector('#grid-favorite-2214168')

    # Шаг 3: Кликаем на "Санкт-Петербург", чтобы поменять регион
    page.click('#grid-favorite-2214168')

    # Шаг 4: Нажимаем на кнопку "Тарифы" и находим Тариф №1
    page.click('body > mts-root > div.g-page-wrapper > div > div.mts16-footer__to-bottom-content > mts-main-page > mts-widget-zone:nth-child(1) > mts-ecosystem-navigation-widget > section > div > div > div > a:nth-child(1)')

    # Ожидаем появления элемента "Тариф № 1"
    page.wait_for_selector('#\\34 547316 > mm-web-universal-card > div')

    # Шаг 5: Нажимаем на кнопку "Подключить", которая находится внизу элемента "Тариф №1"
    page.click('#\\34 547316 > mm-web-universal-card > div > div.card-footer.card-footer__padding.card-footer__margin > div.card-actions__wrapper.card-actions__wrapper-margin > mm-web-universal-card-button:nth-child(1) > mm-web-button > div > button')

    # Убеждаемся в том, что появляется форма для ввода адреса
    page.wait_for_selector('#mat-dialog-0')

    # Шаг 6: Вводим некорректный адрес, например: "sfdcaladicn"
    page.fill('#mat-dialog-0 > mts-tariffs-address-dialog > section > div.map-dialog__search-wrapper.ng-tns-c131-1.ng-star-inserted > mts-address-search-input > div > div > div > mts-autocomplete-input > mts-input > div > input', 'sfdcaladicn')

    # Шаг 7: Нажимаем на кнопку "Проверить"
    page.click('#mat-dialog-0 > mts-tariffs-address-dialog > section > div.map-dialog__search-wrapper.ng-tns-c131-1.ng-star-inserted > button')

    # Шаг 8: Ожидаем и проверяем появления сообщения об ошибке
    page.wait_for_timeout(3000)

    # Проверяем, что появляется сообщение об ошибке
    assert page.is_visible('#mat-dialog-0 > mts-tariffs-address-dialog > section > div.map-dialog__search-wrapper.ng-tns-c131-1.ng-star-inserted > mts-address-search-input > div > div > span'), "Сообщение об ошибке не появилось"