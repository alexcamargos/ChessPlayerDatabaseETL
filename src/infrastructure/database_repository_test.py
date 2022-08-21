#!/usr/bin/env python
# encoding: utf-8
#
#  ------------------------------------------------------------------------------
#  Name: database_repository_test.py
#  Version: 0.0.1
#  Summary: Chess Player Database
#           A complete implementation of ETL process.
#
#  Author: Alexsander Lopes Camargos
#  Author-email: alcamargos@vivaldi.net
#
#  License: MIT
#  ------------------------------------------------------------------------------

from .database_repository import DatabaseRepository
from .mocks.row_test_data import row_test_data


def test_insert_chess_player():
    database = DatabaseRepository()

    for row_data in row_test_data:
        database.insert_chess_player(row_data)


def test_list_all_chess_players():
    database = DatabaseRepository()

    all_chess_players = database.list_all_chess_players()
    assert len(all_chess_players) == len(row_test_data)

    database.database.drop_all_tables(with_all_data=True)
