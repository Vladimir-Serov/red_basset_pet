
from selene import browser, be, have
import time

def test_for_authorization(size_window):
    browser.open('https://redbasset.tech/')
    browser.element('[class="Button_button__341xg UserMenu_authButton__3bJH8 Button_button_outline__13DSB"]').click()
    browser.element('[name="email"][class="Input_input__3YQfM Input_input-common__1WU22"]').should(be.blank).type('axmofy@mailto.plus')
    browser.element('[name="password"][class="Input_input__3YQfM Input_input-common__1WU22"]').should(be.blank).type('axmofy@mailto.plus').press_enter()
    browser.element('[class="Typography_root__3zCC6 Typography_root_body___AwBW UserMenu_userName__2uqUl"]').should(have.text('axmofy@mailto.plus'))


def test_podcaster_cabinet(authorization):
    browser.element('[class="Typography_root__3zCC6 Typography_root_body___AwBW UserMenu_userName__2uqUl"]').click()
    browser.element('[class="UserMenu_dropLink__3JTzn"][href="/podcaster"]').click()
    time.sleep(1)
    browser.element('[class ="Modal_close__2f-7E"]').click()
    time.sleep(3)


def test_creating_author(podcaster_cabinet):
    browser.element('[class="Button_podcasterButton__115KA Button_button_secondary__2R4a7 Button_button_fullWidth__1ibfW"]').click()
    input_field = browser.element('input[type=file]')
    input_field.send_keys('C:/Users/hello/PycharmProjects/red_basset_pet/img/Mona_Lisa1.jpg')
    time.sleep(10)