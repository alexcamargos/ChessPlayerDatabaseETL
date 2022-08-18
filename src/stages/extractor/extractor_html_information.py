#!/usr/bin/env python
# encoding: utf-8
#
#  ------------------------------------------------------------------------------
#  Name: extractor_html_information.py
#  Version: 0.0.1
#  Summary: Chess Player Database
#           A complete implementation of ETL process.
#
#  Author: Alexsander Lopes Camargos
#  Author-email: alcamargos@vivaldi.net
#
#  License: MIT
#  ------------------------------------------------------------------------------

from src.drivers.interfaces.http_requester import HttpRequesterInterface
from src.drivers.interfaces.html_collector import HtmlCollectorInterface


class ExtractorHtmlInformation:

    def __init__(self, requester: HttpRequesterInterface, collector: HtmlCollectorInterface):
        self.__requester = requester
        self.__collector = collector

    def extract(self):
        html_information = self.__requester.make_request()
        collect_information = self.__collector.collect_information(html_information['content'])

        return collect_information
