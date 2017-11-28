#! /usr/bin/env python
# -*- coding: utf-8 -*-

import pytest
from selene import browser
from selene import config
from selene.browsers import BrowserName
from selene.conditions import *

from entity.user import User
from entity.email import Email
from entity.pages import Main_Page
from entity.pages import Login_Page
import allure
from test_recorder.decorator import video_recorder, video


@pytest.yield_fixture(scope="session", autouse=True)
def set_up_class():
    # prepare something ahead of all ui_tests
    config.browser_name = BrowserName.CHROME
    config.base_url = "https://mail.google.com/mail"
    config.timeout = 7
    yield
    browser.close()


@pytest.yield_fixture(autouse=True)
def set_up_test():
    browser.driver().implicitly_wait(8)
    browser.driver().delete_all_cookies()
    yield
    Main_Page().log_out()


@video_recorder(video())
@pytest.mark.incremental
class TestLogin(object):


    def test_positive_login(self):
        user = User('genchevskiy', 'test')
        main_page = Login_Page().open().login_as(user)
        main_page._account_button().should_be(visible, 10)
        assert "Аккаунт Google: Savva Genchevskiy" in main_page._account_button().get_attribute("title").encode('utf-8')

    @allure.severity(severity_level="CRITICAL")
    def test_send_email(self):
        user = User('genchevskiy', 'test')
        main_page = Login_Page().open().login_as(user)
        main_page.send_new_email().send_message("Test Subject", "Hello!", user.email)
        main_page._success_sent_link().should_be(visible)
        main_page.openInbox()._email_list().should_have(size_at_least(1))

    def test_send_email_object(self):
        user = User('genchevskiy', 'test')
        email = Email(user.email, 'Test Subject 2', 'Hello')
        main_page = Login_Page().open().login_as(user)
        main_page.send_new_email().send_message_with(email)
        main_page._success_sent_link().should_be(visible)
        main_page.openInbox().emails_list._get(1)._subject().should_be(visible, 10).should_have(text(email.subject))




