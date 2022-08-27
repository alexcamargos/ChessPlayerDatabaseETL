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

from .chess_player_service import ChessPlayerService
from .interfaces.database_repository import DatabaseRepositoryInterface


class DatabaseRepository(DatabaseRepositoryInterface):

    def __init__(self, connection_handler):
        self.database = connection_handler.connect(provider='postgres', create_tables=True)
        self.chess_player_service = ChessPlayerService(self.database)

    def insert_chess_player(self, data) -> None:
        self.chess_player_service.insert_chess_player(data)

    def list_all_chess_players(self) -> list:
        return self.chess_player_service.list_all_chess_players()
