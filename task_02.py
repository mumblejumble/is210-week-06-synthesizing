#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""creating emails with for loop"""


def prepare_email(appointments):
    """creates emails with for loop and DRY principle

    arguments:
        appointments: a list of two item tuples with the client's name and
        their appointment times as members.

        for loop: loops email statements and inserting list dataset everytime.

    examples:
        >>>prepare_email([('Jen', '2015'), ('Max', 'March 3')])
        ['Dear Jen, \nI look forward to metting you with you on 2015.\nMe',
        'Dear Max, \nI look forward to meeting you on March 3.\nBest\nMe']
    """
    statement = 'Dear {},\nI look forward to meeting with you on {}.\nBest,\nMe'
    for appoint in appointments:
        print statement.format(appoint[0], appoint[1])
