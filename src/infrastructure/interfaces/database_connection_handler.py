#!/usr/bin/env python
# encoding: utf-8
#
#  ------------------------------------------------------------------------------
#  Name: database_connection_handler.py
#  Version: 0.0.2
#  Summary: database_connection_handler.py
#           A complete implementation of ETL process.
#
#  Author: Alexsander Lopes Camargos
#  Author-email: alcamargos@vivaldi.net
#
#  License: MIT
#  ------------------------------------------------------------------------------

from abc import ABC, abstractmethod


class DatabaseConnectionHandlerInterface(ABC):

    @abstractmethod
    def connect(self, provider: str, create_tables: bool) -> None:
        raise NotImplementedError('You must implement this method')
