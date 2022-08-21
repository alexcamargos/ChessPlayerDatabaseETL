#!/usr/bin/env python
# encoding: utf-8
#
#  ------------------------------------------------------------------------------
#  Name: database_repository.py
#  Version: 0.0.1
#  Summary: Chess Player Database
#           A complete implementation of ETL process.
#
#  Author: Alexsander Lopes Camargos
#  Author-email: alcamargos@vivaldi.net
#
#  License: MIT
#  ------------------------------------------------------------------------------

from abc import ABC, abstractmethod
from typing import Dict


class DatabaseRepositoryInterface(ABC):

    @abstractmethod
    def insert_chess_player(self, data: Dict) -> None:
        raise NotImplementedError

    @abstractmethod
    def list_all_chess_players(self) -> list:
        raise NotImplementedError
