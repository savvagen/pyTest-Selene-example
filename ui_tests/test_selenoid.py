#! /usr/bin/env python
# -*- coding: utf-8 -*-

import pytest
import os, sys
from selene import browser
from selenium import webdriver
from selene import config
from selene.browsers import BrowserName
from selene.conditions import *

from entity.user import User
from entity.email import Email
from entity.pages import Main_Page
from entity.pages import Login_Page


@pytest.yield_fixture(scope="session", autouse=True)
def set_up_class():
    driver = webdriver.Remote(
        command_executor='http://127.0.0.1:4444/wd/hub',
        desired_capabilities={'browserName': 'chrome',
                              'version': '60.0',
                              'javascriptEnabled': True,
                              "enableVNC": True,
                              "screenResolution": "1960x1280x24",
                              "platform": os.name.encode('utf-8')})
    browser.set_driver(driver)
    # prepare something ahead of all ui_tests
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


def test_positive_login():
    user = User('genchevskiy', 'test')
    main_page = Login_Page().open().login_as(user)
    main_page._account_button().should_be(visible, 10)
    assert "Аккаунт Google: Savva Genchevskiy" in main_page._account_button().get_attribute("title").encode('utf-8')

def test_send_email_object():
    user = User('genchevskiy', 'test')
    email = Email(user.email, 'Test Subject 2', 'Hello')
    main_page = Login_Page().open().login_as(user)
    main_page.send_new_email().send_message_with(email)
    main_page._success_sent_link().should_be(visible)
    main_page.openInbox().emails_list._get(1)._subject().should_be(visible, 10).should_have(text(email.subject))

def test_send_email():
    user = User('genchevskiy', 'test')
    main_page = Login_Page().open().login_as(user)
    main_page.send_new_email().send_message("Test", "Hello!", user.email)
    main_page._success_sent_link().should_be(visible)
    main_page.openInbox()._email_list().should_have(size_at_least(1))



