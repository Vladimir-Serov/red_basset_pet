import os

import allure
import pytest
from selene import browser

from tests.conftest import auth_page
from tests.conftest import main_page


@pytest.fixture(scope='function', autouse=True)
def browser_management():
    browser.config.base_url = os.getenv('selene.base_url', 'https://redbasset.tech/')
    browser.config.window_width = 1920
    browser.config.window_height = 1080
    yield
    browser.quit()


def test_for_authorization(browser_management):
    with allure.step('Открытие браузера'):
        main_page.open('https://redbasset.tech/')

    with allure.step('Переход на страницу авторизации'):
        main_page.click_log_in_button()

    with allure.step('Заполнение данных для авторизации'):
        auth_page.fill_email('yksyp@mailto.plus')
        auth_page.fill_password('yksyp@mailto.plus')
        auth_page.click_auth_button()

    with allure.step('Проверка что авторизован '):
        main_page.shoud_authorized('yksyp@mailto.plus')
