#!/usr/bin/env python
# encoding: utf-8
#
#  ------------------------------------------------------------------------------
#  Name: html_collector_test.py
#  Version: 0.0.2
#  Summary: Chess Player Database
#           A complete implementation of ETL process.
#
#  Author: Alexsander Lopes Camargos
#  Author-email: alcamargos@vivaldi.net
#
#  License: MIT
#  ------------------------------------------------------------------------------

from .html_collector import HtmlCollector
from .mocks.http_requester_mock import mock_request_from_page


def test_collect_information():
    http_request_response = mock_request_from_page()

    html_collector = HtmlCollector()
    collect_information = html_collector.collect_information(http_request_response['html'])

    assert isinstance(collect_information, list)
    assert isinstance(collect_information[0], dict)

    assert 'player_name' in collect_information[0]
    assert 'highest_rating' in collect_information[0]
    assert 'years_covered' in collect_information[0]
    assert 'number_of_games' in collect_information[0]
    assert 'href' in collect_information[0]
