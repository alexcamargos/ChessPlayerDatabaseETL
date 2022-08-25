#!/usr/bin/env python
# encoding: utf-8
#
#  ------------------------------------------------------------------------------
#  Name: __init__.py
#  Version: 0.0.1
#  Summary: data_base_connection_handler_test.py
#           A complete implementation of ETL process.
#
#  Author: Alexsander Lopes Camargos
#  Author-email: alcamargos@vivaldi.net
#
#  License: MIT
#  ------------------------------------------------------------------------------

from os.path import exists

from .database_connection_handler import DatabaseConnectionHandler


def test_connect_sqlite():

    connection = DatabaseConnectionHandler().connect() #pylint: disable=unused-variable
    assert exists('src/infrastructure/chess_player_database.sqlite') is True
