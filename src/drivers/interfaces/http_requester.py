#!/usr/bin/env python
# encoding: utf-8
#
#  ------------------------------------------------------------------------------
#  Name: http_requester.py
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


class HttpRequesterInterface(ABC):
    """Represents a complete HTTP request."""

    @abstractmethod
    def make_request(self):
        """Make request to the url and return the response."""

        raise NotImplementedError
