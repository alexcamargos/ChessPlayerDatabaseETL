#!/usr/bin/env python
# encoding: utf-8
#
#  ------------------------------------------------------------------------------
#  Name: extract_exception.py
#  Version: 0.0.1
#  Summary: Chess Player Database
#           A complete implementation of ETL process.
#
#  Author: Alexsander Lopes Camargos
#  Author-email: alcamargos@vivaldi.net
#
#  License: MIT
#  ------------------------------------------------------------------------------


class ExtractException(Exception):
    """Exception class for extract stage."""

    def __init__(self, *args: object) -> None:
        super().__init__(*args)
        self.mensagem = args[0]
        self.exception_type = 'ExtractException'
