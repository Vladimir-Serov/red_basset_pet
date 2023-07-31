import pytest
from selene import browser, have, be
import tests
from pathlib import Path


def path(file_name):
    return str(Path(tests.__file__).parent.joinpath(f'resourсes/{file_name}').absolute())


@pytest.fixture(scope='function', autouse=True)
def size_window():
    browser.config.driver_name = 'chrome'
    browser.config.base_url = 'https://rbp-1681-data-attributes.main-frontend.stage.redbasset.tech/'
    browser.config.window_width = 1920
    browser.config.window_height = 900
    yield
    browser.quit()


@pytest.fixture()
def authorization(size_window):
    browser.open('https://rbp-1681-data-attributes.main-frontend.stage.redbasset.tech/')
    browser.element('//*[@id="__next"]/div[1]/div/div/div[1]/header/div[2]/div/button').click()
    browser.element('//*[@id="__next"]/div[1]/main/div/div[2]/form/div[1]/div[1]/label/input').should(be.blank).type('tokar.nnov@yandex.ru')
    browser.element('//*[@id="__next"]/div[1]/main/div/div[2]/form/div[1]/div[2]/label/input').should(be.blank).type('tokar.nnov@yandex.ru').press_enter()
    browser.element('//*[@id="__next"]/div[1]/div/div/div[1]/header/div[2]/div/button').should(have.text('tokar.nnov@yandex.ru'))


@pytest.fixture()
def podcaster_cabinet(authorization):
    browser.element('//*[@id="__next"]/div[1]/div/div/div[1]/header/div[2]/div/button').click()
    browser.element('//*[@id="__next"]/div[1]/div/div/div[1]/header/div[2]/div/div/ul/li[2]/a/span[1]').click()
    browser.element('/html/body/div[4]/div/div/button').click()


# testit -u https://tms.testit.software/ -t NmthU3RpenBjTU9ueW4zTzBu -pi a74eee27-03b3-44e4-b532-3dc0d9e5ca0b  -ci 27ced88f-71a3-42fe-938a-2179317be33d -tn TestRun01 -r reports/results.xml