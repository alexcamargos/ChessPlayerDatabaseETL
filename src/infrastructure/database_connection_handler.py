#!/usr/bin/env python
# encoding: utf-8
#
#  ------------------------------------------------------------------------------
#  Name: database_connection_handler.py
#  Version: 0.0.1
#  Summary: database_connection_handler.py
#           A complete implementation of ETL process.
#
#  Author: Alexsander Lopes Camargos
#  Author-email: alcamargos@vivaldi.net
#
#  License: MIT
#  ------------------------------------------------------------------------------

from pony import orm


class DatabaseConnectionHandler:

    params = {'sqlite': dict(provider='sqlite',
                             filename='chess_player_database.sqlite',
                             create_db=True),
              'mysql': dict(provider='mysql',
                            host="localhost",
                            user="default",
                            passwd="default",
                            db="chess_player_database"),
              'postgres': dict(provider='postgres',
                               user='default',
                               password='default',
                               host='localhost',
                               database='chess_player_database'),
              'cockroach': dict(provider='cockroach',
                                user='default',
                                host='localhost',
                                port=26257,
                                database='chess_player_database',
                                sslmode='disable'),
              'oracle': dict(provider='oracle',
                             user='default',
                             password='default',
                             dsn='localhost/chess_player_database')}

    database = None

    def __define_entities(self, database):
        class ChessPlayer(database.Entity): #pylint: disable=unused-variable
            _table_ = 'chess_players'

            id = orm.PrimaryKey(int, auto=True)
            first_name = orm.Required(str, 42)
            last_name = orm.Optional(str, 42)
            player_id = orm.Required(int, size=32)
            highest_rating = orm.Optional(int, size=32)
            start_year = orm.Optional(int, size=16)
            end_year = orm.Optional(int, size=16)
            number_of_games = orm.Optional(int, size=32)
            href = orm.Optional(str, 256)

    def connect(self, provider='sqlite', create_tables=True):
        self.database = orm.Database()
        self.database.bind(**self.params[provider])
        self.__define_entities(self.database)
        self.database.generate_mapping(create_tables=create_tables)

        return self.database
