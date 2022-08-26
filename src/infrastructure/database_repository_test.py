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

from src.stages.contracts.mocks.transform_contract import \
    transform_contract_mock

from .database_connection_handler import DatabaseConnectionHandler
from .database_repository import DatabaseRepository

database = DatabaseRepository(connection_handler=DatabaseConnectionHandler())


def test_insert_chess_player():

    for row_data in transform_contract_mock.load_information:
        database.insert_chess_player(row_data)


def test_list_all_chess_players():

    all_chess_players = database.list_all_chess_players()
    assert len(all_chess_players) == len(transform_contract_mock.load_information)

    database.database.drop_all_tables(with_all_data=True)
