#! /usr/bin/env python
# -*- coding: utf-8 -*-

class Email(object):

    #email - genchevskiy.test@gmail.com

    def __init__(self, retlyTo, subject, message):
        self.retlyTo = retlyTo
        self.subject = subject
        self.message = message

