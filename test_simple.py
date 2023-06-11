from selene import browser, be, have
import time

def test_for_authorization(size_window): #Авторизация
    browser.open('https://redbasset.tech/')
    browser.element('[class="Button_button__341xg UserMenu_authButton__3bJH8 Button_button_outline__13DSB"]').click()
    browser.element('[name="email"][class="Input_input__3YQfM Input_input-common__1WU22"]').should(be.blank).type('yksyp@mailto.plus')
    browser.element('[name="password"][class="Input_input__3YQfM Input_input-common__1WU22"]').should(be.blank).type('yksyp@mailto.plus').press_enter()
    browser.element('[class="Typography_root__3zCC6 Typography_root_body___AwBW UserMenu_userName__2uqUl"]').should(have.text('yksyp@mailto.plus'))


def test_podcaster_cabinet(authorization): #Переход в кабинет подкастера
    browser.element('[class="Typography_root__3zCC6 Typography_root_body___AwBW UserMenu_userName__2uqUl"]').click()
    browser.element('[class="UserMenu_dropLink__3JTzn"][href="/podcaster"]').click()
    # browser.element('[class ="Modal_close__2f-7E"]').click()


def test_creating_author(podcaster_cabinet): #Создание автора
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


def test_creating_podcast(podcaster_cabinet): #Создание подкаста
    browser.element('[class="Button_podcasterButton__115KA PodcasterMenu_button__2F0gP Button_button_primary__2JSyq"]').click()
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


def test_creating_episode(podcaster_cabinet): #Создание выпуска
    browser.element('[class="ListItem_item__jXXyv ListItem_link__3O1lO PodcastItem_card__3H_V1"]').click()
    browser.element('[class="Button_podcasterButton__115KA PodcastMenu_button__1R8-i Button_button_primary__2JSyq"]').click()
    input_field = browser.element('[type="file"][class="InputAudioFile_nativeInput__2Y5Sp"]')
    input_field.send_keys('C:/Users/hello/PycharmProjects/red_basset_pet/audio/Как начинающему разработчику найти первую работу в IT (в гостях Влад Соколенко).mp3')
    browser.element('[type="text"][name="episodeInfo.name"]').should(be.blank).type('Как начинающему разработчику найти первую работу')
    browser.element('//*[@id="__next"]/div[1]/div/div/main/div[2]/div/form/div[2]/div[1]/div[3]/div/div/div[3]/div[2]/div').type('Разбираемся, как можно получить свою первую работу в IT '
                                                                                                                        'в качестве junior фронтенд-разработчика вместе с Алексеем Авдеевым, CTO в Mish,'
                                                                                                                        ' и Владиславом Соколенко, разработчиком в Mish')
    browser.element('//*[@id="__next"]/div[1]/div/div/main/div[2]/div/form/div[1]/ul/li[2]/button').click()
    browser.element('[name="episodeSettings.seasonNumber"]').should(be.blank).type('1')
    browser.element('[name="episodeSettings.episodeNumber"]').should(be.blank).type('1')
    browser.element('//*[@id="__next"]/div[1]/div/div/main/div[2]/div/form/div[1]/ul/li[3]/button').click()
    browser.element('//*[@id="__next"]/div[1]/div/div/main/div[2]/div/div/div/div/button[2]').click()
    time.sleep(10)