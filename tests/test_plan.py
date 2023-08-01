from selene import browser
import allure
from allure_commons.types import Severity


@allure.tag('web')
@allure.severity(Severity.BLOCKER)
@allure.label('owner', 'nsbelova')
@allure.feature('Issues names')
@allure.story('Issues in public repository can be found')
@allure.link('https://github.com', name='Testing')
def test_issue_name_for_github_repo_dynamic_steps():
    with allure.step('Open main page'):
        browser.open('https://github.com/')
