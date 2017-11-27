#! /usr/bin/env python
# -*- coding: utf-8 -*-

from selene.api import *
from selene.conditions import *
from entity.email import Email
from entity.user import User

import pytest
import allure
import allure_pytest



#ON THE REAL PROJECT!!! - ADD ALL PAGE-OPBEJCS TO THE SEPARATE FILES


email_filed = by.name("identifier")
password_filed = by.name("password")
email_error = by.xpath('//*[@id="view_container"]/form/div[2]/div/div[1]/div[1]/div/div[2]/div[2]')
password_error = by.xpath('//*[@id="password"]/div[2]/div[2]')

#---------------------------------------------------------------


class Login_Page(object):

    def __init__(self):
        self.user = User

    def _email_field(self):
        return s(email_filed)

    def _password_field(self):
        return s(password_filed)

    def _email_error(self):
        return s(email_error)

    def _password_error(self):
        s(password_error)


    @allure.step("Open Login page")
    def open(self):
        browser.open_url("/")
        return self

    @allure.step("Login as test user")
    def login_as(self, user):
        self._email_field().should_be(visible).set_value(user.email).press_enter()
        self._password_field().should_be(visible).set_value(user.password).press_enter()
        return Main_Page()









account_button = by.xpath('//*[@id="gb"]/div[1]/div[1]/div[2]/div[5]/div[1]/a')
logout_button = by.text("Выйти")
new_email_button = by.text("НАПИСАТЬ")
sucess_link = by.text("Просмотреть сообщение")
new_email_area = by.xpath('/html/body/div[15]/div/div/div/div[1]/div[3]/div[1]/div[1]/div/div/div')
email_list = by.xpath('//div[@role="tabpanel"]/div[2]/div/table/tbody/tr[@jscontroller]')

retly_to_fiedld = by.css("textarea[name='to']")
subject_field  = by.name("subjectbox")
message_body_field = by.css("div[aria-label='Тело письма']")
sent_button = by.text("Отправить")

email_list_body = by.xpath('//div[@role="tabpanel"]/div[2]/div/table/tbody')
email_subject = by.css(".bog b")
email_message = by.xpath('//td[6]/div/div/div[2]/span[2]')

#---------------------------------------------------------------



class Main_Page(object):

    def __init__(self):
        self.email_field = Email_Field()
        self.emails_list = Emails_List()

    def _account_button(self):
        return s(account_button)

    def _logout_button(self):
        return s(logout_button)

    def _password_field(self):
        return s(password_filed)

    def _new_email_button(self):
        return s(new_email_button)

    def _success_sent_link(self):
        return s(sucess_link)

    def _email_list(self):
        return ss(email_list)

    def openInbox(self):
        browser.open_url("/#inbox")
        return self


    def send_new_email(self):
        with allure.step("Press New Email button"):
            self._new_email_button().click()
            self.email_field.container.should_be(visible)
        return Email_Field()


    def log_out(self):
        with allure.step("Log Out"):
            self._account_button().click()
            self._logout_button().should_be(visible).click()
            self._password_field().should_be(visible)
        return Login_Page()




class Email_Field(object):

    def __init__(self):
        self.container = s(new_email_area)
        self.email = Email

    def _email_field(self):
        return s(retly_to_fiedld)

    def _subject_field(self):
        return s(subject_field)

    def _email_body(self):
        return s(message_body_field)

    def _send_button(self):
        return s(sent_button)

    def send_message(self, subject, message, retly_to):
        with allure.step("Send message"):
            self._email_field().should_be(visible).set_value(retly_to)
            self._subject_field().set_value(subject)
            self._email_body().set_value(message)
            self._send_button().click()
        return Main_Page()

    def send_message_with(self, email):
        with allure.step("Send message"):
            self._email_field().should_be(visible).set_value(email.retlyTo)
            self._subject_field().set_value(email.subject)
            self._email_body().set_value(email.message)
            self._send_button().click()
        return Main_Page()


#---------------------------------------------------------------


class Emails_List(object):

    def __init__(self):
        self.container = s(email_list_body)


    def _emails(self):
        return browser.all(email_list)


    def _should_have_size(self, number):
        self._emails().should_have(size(number))
        return self


    def _get(self, index):
        return Message(index-1)



class Message(object):

    def __init__(self, index):
        self.emails_list = Emails_List()
        self.email = Emails_List()._emails().__getitem__(index)



    def _subject(self):
        return self.email.s(email_subject)

    def _message(self):
        return self.email.s(email_message)
