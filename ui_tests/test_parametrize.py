#! /usr/bin/env python
# -*- coding: utf-8 -*-

import pytest
from selene import browser
from selene import config
from selene.browsers import BrowserName
from selene.conditions import *
from entity.pages import Login_Page
from test_recorder.decorator import video, video_recorder
from test_data.login_data import Test_Data



@pytest.yield_fixture(scope="session", autouse=True)
def set_up_class():
    # prepare something ahead of all ui_tests
    config.browser_name = BrowserName.CHROME
    config.base_url = "https://mail.google.com/mail"
    config.timeout = 7
    yield
    browser.close()


@pytest.yield_fixture(autouse=True)
def set_up_module():
    browser.driver().implicitly_wait(8)
    browser.driver().delete_all_cookies()


@pytest.mark.parametrize("email,message", Test_Data().emailData)
@video()
def test_invalid_email_login(email, message):
    login_page = Login_Page().open()
    login_page._email_field().set_value(email).press_enter()
    assert message in login_page._email_error().should_be(visible).text.encode('utf-8')

