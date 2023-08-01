from selene import browser, have, by


def test_issue_name_for_github_repo():
    browser.open('https://github.com/')
