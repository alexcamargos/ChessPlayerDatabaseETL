#!/usr/bin/env python
# encoding: utf-8
#
#  ------------------------------------------------------------------------------
#  Name: extractor_html_information_test.py
#  Version: 0.0.1
#  Summary: Chess Player Database
#           A complete implementation of ETL process.
#
#  Author: Alexsander Lopes Camargos
#  Author-email: alcamargos@vivaldi.net
#
#  License: MIT
#  ------------------------------------------------------------------------------

from datetime import date as dt

from src.drivers.http_requester import HttpRequester
from src.drivers.html_collector import HtmlCollector
from src.exception.extract_exception import ExtractException

from .extractor_html_information import ExtractorHtmlInformation
from ..contracts.extract_contract import ExtractContract

URL = 'https://www.chessgames.com/directory/A.html'


def test_extract_html_information():
    requester = HttpRequester(URL)
    collector = HtmlCollector()

    extractor = ExtractorHtmlInformation(requester=requester,
                                         collector=collector)
    response = extractor.extract()

    assert isinstance(response, ExtractContract)
    assert isinstance(response.extraction_date, dt)
    assert isinstance(response.raw_information, list)
    assert isinstance(response.raw_information[0], dict)

    assert 'href' in response.raw_information[0]
    assert 'player' in response.raw_information[0]

    assert response.extraction_date == dt.today()


def test_extract_html_information_requester_exception():
    requester = None
    collector = HtmlCollector()

    extractor = ExtractorHtmlInformation(requester=requester,
                                         collector=collector)
    try:
        response = extractor.extract()  #pylint: disable=unused-variable
    except Exception as error:  #pylint: disable=broad-except
        assert isinstance(error, ExtractException)


def test_extract_html_information_collector_exception():
    requester = HttpRequester(URL)
    collector = None

    extractor = ExtractorHtmlInformation(requester=requester,
                                         collector=collector)
    try:
        response = extractor.extract()  #pylint: disable=unused-variable
    except Exception as error:  #pylint: disable=broad-except
        assert isinstance(error, ExtractException)
