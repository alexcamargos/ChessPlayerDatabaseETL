#!/usr/bin/env python
# encoding: utf-8
#
#  ------------------------------------------------------------------------------
#  Name: load_data.py
#  Version: 0.0.1
#  Summary: Chess Player Database
#           A complete implementation of ETL process.
#
#  Author: Alexsander Lopes Camargos
#  Author-email: alcamargos@vivaldi.net
#
#  License: MIT
#  ------------------------------------------------------------------------------


from src.infrastructure.interfaces.database_repository import DatabaseRepositoryInterface
from ..contracts.transform_contract import TransformContract

class LoadData:
    """Load data into the database."""

    def __init__(self, repository: DatabaseRepositoryInterface):
        self.__repository = repository

    def load(self, transformed_contract: TransformContract):
        load_information = transformed_contract.load_information

        for data in load_information:
            self.__repository.insert_chess_player(data)
