from selene import browser, be, have
import time

def test_for_authorization(size_window):
    browser.open('https://redbasset.tech/')
    browser.element('[class="Button_button__341xg UserMenu_authButton__3bJH8 Button_button_outline__13DSB"]').click()
    browser.element('[name="email"][class="Input_input__3YQfM Input_input-common__1WU22"]').should(be.blank).type('yksyp@mailto.plus')
    browser.element('[name="password"][class="Input_input__3YQfM Input_input-common__1WU22"]').should(be.blank).type('yksyp@mailto.plus').press_enter()
    browser.element('[class="Typography_root__3zCC6 Typography_root_body___AwBW UserMenu_userName__2uqUl"]').should(have.text('yksyp@mailto.plus'))


def test_podcaster_cabinet(authorization):
    browser.element('[class="Typography_root__3zCC6 Typography_root_body___AwBW UserMenu_userName__2uqUl"]').click()
    browser.element('[class="UserMenu_dropLink__3JTzn"][href="/podcaster"]').click()
    # browser.element('[class ="Modal_close__2f-7E"]').click()


def test_creating_author(podcaster_cabinet):
    browser.element('[class="Button_podcasterButton__115KA Button_button_secondary__2R4a7"][type="button"]').click()
    input_field = browser.element('input[type=file]')
    input_field.send_keys('C:/Users/hello/PycharmProjects/red_basset_pet/img/Mona_Lisa1.jpg')
    time.sleep(3)
    browser.element('input[type=text]').should(be.blank).type('AQA Тест 123')
    browser.element('[name="mainInfo.description"]').should(be.blank).type('По своей сути рыбатекст является альтернативой традиционному '
                                                                         'lorem ipsum, который вызывает у некторых людей недоумение при '
                                                                         'попытках прочитать рыбу текст. В отличии от lorem ipsum, текст рыба '
                                                                         'на русском языке наполнит любой макет непонятным смыслом и придаст '
                                                                         'неповторимый колорит советских времен. '
                                                                         'Вы можете добавить в данное  поле до 600 символов!')
    browser.element('[class="ProgressBar_progressStep__35vGr"]').click()
    browser.element('[name="additionalInfo.email"]').should(be.blank).type('yksyp@mailto.plus')
    browser.element('[name="additionalInfo.phone"]').should(be.blank).type('88005553535')
    browser.element('[class="Button_podcasterButton__115KA Button_button_primary__2JSyq"]').click()
    browser.element('[class="SidebarItem_summaryRoot__39dBz SidebarItem_summaryRootActive__1hXt4"]').should(have.text('AQA Тест 123'))


def test_creating_podcast(podcaster_cabinet):
    browser.element('[class="Podcasts_link__1DQ6S"][href="/podcaster/podcast/new?authorId=1037"]').click()
    input_field = browser.element('input[type="file"]')
    input_field.send_keys('C:/Users/hello/PycharmProjects/red_basset_pet/img/QA.jpeg')
    browser.element('[name="mainInfo.name"]').should(be.blank).type('It\'s not me!')
    browser.element('[name="mainInfo.description"]').should(be.blank).type('Этот подкаст создан с помощью автоматизированного ПО. '
                                                                           'Данное поле вмещает до 600 символов. '
                                                                           'Так же в данное поле можно ввести спецсимволы,'
                                                                           ' такие как: "!@#$%^&*()_+}{"|?"')
    browser.element('//*[@id="__next"]/div[1]/div/div/main/div[2]/form/div[1]/ul/li[2]/button').click()
    browser.element('//*[@id="__next"]/div[1]/div/div/main/div[2]/form/div[2]/div/div[1]/div[1]/div/div').click()
    browser.element('[id="react-select-2-option-16"]').click()
    browser.element('//*[@id="__next"]/div[1]/div/div/main/div[2]/form/div[2]/div/div[3]/div/div').click()
    browser.element('//*[@id="react-select-4-option-0"]').click()
    browser.element('//*[@id="__next"]/div[1]/div/div/main/div[2]/form/div[1]/ul/li[3]/button').click()
    browser.element('[name="additionalInfo.itunesOwnerName"]').should(be.blank).type('Владимир')
    browser.element('[name="additionalInfo.itunesOwnerEmail"]').should(be.blank).type('yksyp@mailto.plus')
    browser.element('[name="additionalInfo.podcastUrl"]').should(be.blank).type('https://slozhna.redbasset.tech/')
    browser.element('[placeholder="Введите ссылку Vkontakte"]').should(be.blank).type('https://m.vk.com/lastsum')
    browser.element('[class="Button_podcasterButton__115KA Button_button_primary__2JSyq"]').click()
    time.sleep(20)


def test_creating_episode(podcaster_cabinet):
    browser.element('[href="/podcaster/podcast/1234"]').click()
    browser.element('[class="Episodes_link__3xhrC"][href="/podcaster/episode/new?podcastId=1234"]').click()
    time.sleep(5)
    input_field = browser.element('[type="file"][class="InputAudioFile_nativeInput__2Y5Sp"]')
    input_field.send_keys('C:/Users/hello/PycharmProjects/red_basset_pet/audio/Как начинающему разработчику найти первую работу в IT (в гостях Влад Соколенко).mp3')
    browser.element('[type="text"][name="episodeInfo.name"]').should(be.blank).type('Как начинающему разработчику найти первую работу')
    browser.element('[class="public-DraftEditorPlaceholder-inner"][id="placeholder-28r31"]').should(be.blank).type('Раз')