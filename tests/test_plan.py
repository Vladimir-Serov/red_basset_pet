from selene import browser


def test_issue_name_for_github_repo(browser_management):
    browser.open('https://github.com/')
