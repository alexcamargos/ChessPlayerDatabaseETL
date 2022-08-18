#!/usr/bin/env python
# encoding: utf-8
#
#  ------------------------------------------------------------------------------
#  Name: html_collector_test.py
#  Version: 0.0.1
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

    assert 'href' in collect_information[0]
    assert 'player' in collect_information[0]
