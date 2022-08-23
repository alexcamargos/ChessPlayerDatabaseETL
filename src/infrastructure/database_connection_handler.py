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

from os import environ
from pony import orm

# Database connection information get for environment variables.
# Database provider db4free.net
# https://www.db4free.net/phpMyAdmin
DATABASE = environ.get('DATABASE')                      # Database name.
DATABASE_HOST = environ.get('DATABASE_HOST')            # Database host.
DATABASE_PORT = environ.get('DATABASE_PORT')            # Database port.
DATABASE_USER = environ.get('DATABASE_USER')            # Database user.
DATABASE_PASSWORD = environ.get('DATABASE_PASSWORD')    # Database password.


class DatabaseConnectionHandler:

    params = {'sqlite': dict(provider='sqlite',
                             filename='chess_player_database.sqlite',
                             create_db=True),
              'mysql': dict(provider='mysql',
                            host=DATABASE_HOST,
                            user=DATABASE_USER,
                            passwd=DATABASE_PASSWORD,
                            db=DATABASE),
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
            extraction_date = orm.Optional(int, size=32)

    def connect(self, provider='mysql', create_tables=True):
        self.database = orm.Database()
        self.database.bind(**self.params[provider])
        self.__define_entities(self.database)
        self.database.generate_mapping(create_tables=create_tables)

        return self.database
