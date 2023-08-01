import os

import pytest
from selene import browser

from pages.authentication_page import AuthPage
from pages.main_site_page import MainPage
from pages.podcasters_page import PodcasterPage

main_page = MainPage()
auth_page = AuthPage()
podcaster = PodcasterPage()


@pytest.fixture(scope='function', autouse=True)
def browser_management():
    browser.config.base_url = os.getenv('selene.base_url', 'https://redbasset.tech/')
    browser.config.window_width = 1920
    browser.config.window_height = 1080
    yield
    browser.quit()

#
# @pytest.fixture()
# def authorization(size_window):
#     main_page.open('https://redbasset.tech/')
#     main_page.click_log_in_button()
#     auth_page.fill_email('yksyp@mailto.plus')
#     auth_page.fill_password('yksyp@mailto.plus')
#     auth_page.click_auth_button()
#     main_page.shoud_authorized('yksyp@mailto.plus')
#
#
# @pytest.fixture()
# def podcarter_cabinet(authorization):
#     main_page.header_drop_button()
#     main_page.to_cabinet_button()
#     podcaster.close_monetization()
#
#
# @pytest.fixture()
# def creating_author(podcarter_cabinet):
#     podcaster.click_creating_author()
#     podcaster.upload_image('\\resources\img\Mona_Lisa1.jpg')
#     podcaster.fill_author_name('AQA Тест 123')
#     podcaster.fill_author_description('По своей сути рыбатекст является альтернативой традиционному '
#                                       'lorem ipsum, который вызывает у некторых людей недоумение при '
#                                       'попытках прочитать рыбу текст. В отличии от lorem ipsum, текст рыба '
#                                       'на русском языке наполнит любой макет непонятным смыслом и придаст '
#                                       'неповторимый колорит советских времен. '
#                                       'Вы можете добавить в данное  поле до 600 символов!')
#     podcaster.additional_about_author()
#     podcaster.fill_additional_email('yksyp@mailto.plus')
#     podcaster.fill_additional_phone('88005553535')
#     podcaster.submit_button()
#
#
# @pytest.fixture()
# def creating_podcast(creating_author):
#     podcaster.click_creating_podcast()
#     podcaster.fill_podcast_name('It\'s not me!')
#     podcaster.fill_description_podcast('Этот подкаст создан с помощью автоматизированного ПО. '
#                                        'Данное поле вмещает до 600 символов. '
#                                        'Так же в данное поле можно ввести спецсимволы,'
#                                        ' такие как: "!@#$%^&*()_+}{"|?"')
#     podcaster.upload_podcast_image('\\resources\img\QA.jpeg')
#     podcaster.click_settings_podcast()
#     podcaster.choose_category('Досуг')
#     podcaster.choose_subcategory('Анимация и манга')
#     podcaster.add_category()
#     podcaster.choose_category('Бизнес')
#     podcaster.choose_subcategory('Маркетинг')
#     podcaster.choose_language('Русский')
#     podcaster.next_page()
#     podcaster.subtit_creating_podcast()
#     podcaster.shoul_exist_podcast('It\'s not me!')
