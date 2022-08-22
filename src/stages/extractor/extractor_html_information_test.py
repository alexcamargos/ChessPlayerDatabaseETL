#!/usr/bin/env python
# encoding: utf-8
#
#  ------------------------------------------------------------------------------
#  Name: extractor_html_information_test.py
#  Version: 0.0.2
#  Summary: Chess Player Database
#           A complete implementation of ETL process.
#
#  Author: Alexsander Lopes Camargos
#  Author-email: alcamargos@vivaldi.net
#
#  License: MIT
#  ------------------------------------------------------------------------------

from datetime import date as dt

from src.drivers.mocks.http_requester_mock import mock_request_from_page
from src.drivers.http_requester import HttpRequester
from src.drivers.html_collector import HtmlCollector
from src.exception.extract_exception import ExtractException

from .extractor_html_information import ExtractorHtmlInformation
from ..contracts.extract_contract import ExtractContract

URL = 'https://www.chessgames.com/directory/A.html'


def test_extract_html_information(requests_mock):
    """Test extractor html information."""

    response_context = mock_request_from_page()
    requests_mock.get(URL, status_code=200, text=response_context['html'])

    requester = HttpRequester(URL)
    collector = HtmlCollector()

    extractor = ExtractorHtmlInformation(requester=requester,
                                         collector=collector)
    response = extractor.extract()

    assert isinstance(response, ExtractContract)
    assert isinstance(response.extraction_date, int)
    assert isinstance(response.raw_information, list)
    assert isinstance(response.raw_information[0], dict)

    assert 'player_name' in response.raw_information[0]
    assert 'highest_rating' in response.raw_information[0]
    assert 'years_covered' in response.raw_information[0]
    assert 'number_of_games' in response.raw_information[0]
    assert 'href' in response.raw_information[0]

    assert response.extraction_date == dt.today().toordinal()


def test_extract_html_information_requester_exception(requests_mock):
    """Test extractor html information requester exception."""

    response_context = mock_request_from_page()
    requests_mock.get(URL, status_code=200, text=response_context['html'])

    requester = None
    collector = HtmlCollector()

    extractor = ExtractorHtmlInformation(requester=requester,
                                         collector=collector)
    try:
        response = extractor.extract()  #pylint: disable=unused-variable
    except Exception as error:  #pylint: disable=broad-except
        assert isinstance(error, ExtractException)


def test_extract_html_information_collector_exception(requests_mock):
    """Test extractor html information collector exception."""

    response_context = mock_request_from_page()
    requests_mock.get(URL, status_code=200, text=response_context['html'])

    requester = HttpRequester(URL)
    collector = None

    extractor = ExtractorHtmlInformation(requester=requester,
                                         collector=collector)
    try:
        response = extractor.extract()  #pylint: disable=unused-variable
    except Exception as error:  #pylint: disable=broad-except
        assert isinstance(error, ExtractException)
