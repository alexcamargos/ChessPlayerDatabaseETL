#!/usr/bin/env python
# encoding: utf-8
#
#  ------------------------------------------------------------------------------
#  Name: load_data_test.py
#  Version: 0.0.1
#  Summary: Chess Player Database
#           A complete implementation of ETL process.
#
#  Author: Alexsander Lopes Camargos
#  Author-email: alcamargos@vivaldi.net
#
#  License: MIT
#  ------------------------------------------------------------------------------

from ..contracts.mocks.transform_contract import transform_contract_mock
from .load_data import LoadData


class DatabaseRepositorySpy:
    """Repository that stores the data in memory."""

    def __init__(self):
        self.chess_player_data = []

    def insert_chess_player(self, data):
        self.chess_player_data.append(data)


def test_load():
    repository = DatabaseRepositorySpy()
    load_data = LoadData(repository)
    load_data.load(transform_contract_mock)

    assert repository.chess_player_data == transform_contract_mock.load_information
