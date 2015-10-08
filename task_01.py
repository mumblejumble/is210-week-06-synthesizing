#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""counting guests and tables"""


def get_party_stats(families, table_size=6):
    """returns total number of guests and total number of tables in tuple

    arguments:
        families: first argument.

        table_size: second argument, has a default value 6

    returns:
        returns sum of dataset(total_guests), and total number of tables needed.

    examples:
        >>>get_party_stats([['Jan'], ['Jen', 'Jess'], ['Jem', 'Jack', 'Janis']])
        (6, 3)

        >>>get_party_stats([['Jan'], ['Jen', 'Jess'], ['Jem', 'Jack', 'Janis']],
        2)
        (6, 4)
    """

    total_guests = 0
    total_tables = 0
    for guests in families:
        total_guests = total_guests + len(guests)
        total_tables = total_tables + (-((-len(guests)) // table_size))
    return total_guests, total_tables
