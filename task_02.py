#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""sending automated e-mails"""


#appointment = [('Wiley', 'Monday, March 16, 2015'), ('Emily', 'Tuesday')]
email = 'Dear {},\nI look forward to meeting with you on {}.\nBest,\nMe'

def prepare_email(name, time):
    """generates email"""
    for item in prepare_email:
        item = []
        print email.format(name, time)
