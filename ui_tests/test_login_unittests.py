#! /usr/bin/env python
# -*- coding: utf-8 -*-

from selene import browser, driver
from selene import config
from selene.browsers import BrowserName
from selene.conditions import *

from entity.email import Email
from entity.pages import Main_Page
from entity.pages import Login_Page
from entity.user import User
import allure
import unittest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


class TestSmoke(unittest.TestCase):


    @classmethod
    def setUpClass(cls):
        browser.set_driver(webdriver.Chrome(ChromeDriverManager().install()))
        config.browser_name = BrowserName.CHROME
        config.base_url = "https://mail.google.com/mail"
        config.timeout = 7

    def setUp(self):
        browser.driver().implicitly_wait(8)
        browser.driver().delete_all_cookies()


    def test_positive_login(self):
        user = User('genchevskiy', 'test')
        main_page = Login_Page().open().login_as(user)
        main_page._account_button().should_be(visible, 10)
        self.assertIn("Аккаунт Google: Savva Genchevskiy  \n({})".format(user.email), main_page._account_button().get_attribute("title"))

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


    def tearDown(self):
        Main_Page().log_out()

    @classmethod
    def tearDownClass(cls):
        cls.browser = browser
        browser.close()



if __name__ == '__main__':
    unittest.main()
