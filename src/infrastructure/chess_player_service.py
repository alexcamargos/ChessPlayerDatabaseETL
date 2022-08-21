#!/usr/bin/env python
# encoding: utf-8
#
#  ------------------------------------------------------------------------------
#  Name: chess_player_service.py
#  Version: 0.0.1
#  Summary: Chess Player Database
#           A complete implementation of ETL process.
#
#  Author: Alexsander Lopes Camargos
#  Author-email: alcamargos@vivaldi.net
#
#  License: MIT
#  ------------------------------------------------------------------------------

from pony.orm import db_session


class ChessPlayerService:

    def __init__(self, database_repository):
        self.database = database_repository

    @db_session
    def insert_chess_player(self, data):
        return self.database.ChessPlayer(**data)

    @db_session
    def remove_chess_player(self, identifier):
        return self.database.ChessPlayer[identifier].delete()

    @db_session
    def get_chess_player_by_id(self, identifier):
        return self.database.ChessPlayer.get(id=identifier)

    @db_session
    def list_all_chess_players(self):
        return self.database.ChessPlayer.select()[:]

    @db_session
    def list_chess_players_by_name(self, name):
        return self.database.ChessPlayer.select(
            lambda chess_player: chess_player.first_name.startswith(name))[:]

    @db_session
    def count_chess_players(self):
        return self.database.ChessPlayer.count()
