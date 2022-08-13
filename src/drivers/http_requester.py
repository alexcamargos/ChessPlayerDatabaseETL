#!/usr/bin/env python
#  encoding: utf-8
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

import requests


class HttpRequester:
    """Represents a complete HTTP request."""

    def __init__(self, url):
        self.__url = url

    def __header(self):
        return {
            'User-Agent':
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
            '(KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'
        }

    def make_request(self):
        """Make request to the url and return the response."""

        try:
            response = requests.get(self.__url, headers=self.__header())
            return {
                'status_code': response.status_code,
                'content': response.text
            }
        except requests.RequestException as error:
            print(error)
            return None
