#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""creating emails with for loop"""


def prepare_email(appointments):
    """creates emails with for loop and DRY principle

    arguments:
        appointments: would be passed by a list of two item tuples with the
        client's name and their appointment times as members.

        newlist: makes the returned a list.

        for loop: loops formatted emailbody, and appends itself to the list
        untill the end of the list.

    returns:
        returns a list of formatted loops.

    examples:
        >>>prepare_email([('Jen', '2015'), ('Max', 'March 3')])
        ['Dear Jen, \nI look forward to metting you with you on 2015.\nMe',
        'Dear Max, \nI look forward to meeting you on March 3.\nBest\nMe']
        >>> prepare_email([('Julie', 'Jan 1'), ('Maggie', 'Feb 3'),
        ('App', 'April 1')])
        ['Dear Julie,\nI look forward to meeting with you on Jan 1.\nBest,\nMe',
        'Dear Maggie,\nI look forward to meeting with you on Feb 3.\nBest,\nMe',
        'Dear App,\nI look forward to meeting with you on April 1.\nBest,\nMe']
    """
    emailbody = 'Dear {},\nI look forward to meeting with you on {}.\nBest,\nMe'
    newlist = []
    for appoint in appointments:
        newlist.append(emailbody.format(appoint[0], appoint[1]))
    return newlist
