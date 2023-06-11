import pytest
from selene import browser, be, have
import time

@pytest.fixture()
def size_window():
    browser.config.driver_name = 'chrome'
    browser.config.window_width = 1920
    browser.config.window_height = 1080

@pytest.fixture()
def authorization(size_window):
    browser.open('https://redbasset.tech/')
    browser.element('[class="Button_button__341xg UserMenu_authButton__3bJH8 Button_button_outline__13DSB"]').click()
    browser.element('[name="email"][class="Input_input__3YQfM Input_input-common__1WU22"]').should(be.blank).type('yksyp@mailto.plus')
    browser.element('[name="password"][class="Input_input__3YQfM Input_input-common__1WU22"]').should(be.blank).type('yksyp@mailto.plus').press_enter()
    browser.element('[class="Typography_root__3zCC6 Typography_root_body___AwBW UserMenu_userName__2uqUl"]').should(have.text('yksyp@mailto.plus'))


@pytest.fixture()
def podcaster_cabinet(authorization):
    browser.element('[class="Typography_root__3zCC6 Typography_root_body___AwBW UserMenu_userName__2uqUl"]').click()
    browser.element('[class="UserMenu_dropLink__3JTzn"][href="/podcaster"]').click()
    # browser.element('[class ="Modal_close__2f-7E"]').click()
