#!/usr/bin/env python
# encoding: utf-8
#
#  ------------------------------------------------------------------------------
#  Name: transform_raw_information_test.py
#  Version: 0.0.2
#  Summary: Chess Player Database
#           A complete implementation of ETL process.
#
#  Author: Alexsander Lopes Camargos
#  Author-email: alcamargos@vivaldi.net
#
#  License: MIT
#  ------------------------------------------------------------------------------

from datetime import date

from src.exception.transform_exception import TransformException

from ..contracts.extract_contract import ExtractContract
from ..contracts.mocks.extract_contract import extract_contract_mock
from ..contracts.transform_contract import TransformContract
from .transform_raw_information import TransformRawInformation


def test_transform():
    transform_raw_information = TransformRawInformation()
    transformed_data = transform_raw_information.transform(extract_contract_mock)

    assert isinstance(transformed_data, TransformContract)
    assert isinstance(transformed_data.load_information, list)
    assert isinstance(transformed_data.load_information[0], dict)

    assert 'first_name' in transformed_data.load_information[0]
    assert 'last_name' in transformed_data.load_information[0]
    assert 'player_id' in transformed_data.load_information[0]
    assert 'highest_rating' in transformed_data.load_information[0]
    assert 'start_year' in transformed_data.load_information[0]
    assert 'end_year' in transformed_data.load_information[0]
    assert 'number_of_games' in transformed_data.load_information[0]
    assert 'href' in transformed_data.load_information[0]
    assert 'extraction_date' in transformed_data.load_information[0]

    assert isinstance(transformed_data.load_information[0]['first_name'], str)
    assert isinstance(transformed_data.load_information[0]['last_name'], str)
    assert isinstance(transformed_data.load_information[0]['player_id'], int)
    assert isinstance(transformed_data.load_information[0]['highest_rating'], int)
    assert isinstance(transformed_data.load_information[0]['start_year'], int)
    assert isinstance(transformed_data.load_information[0]['end_year'], int)
    assert isinstance(transformed_data.load_information[0]['number_of_games'], int)
    assert isinstance(transformed_data.load_information[0]['href'], str)
    assert isinstance(transformed_data.load_information[0]['extraction_date'], date)


def test_transform_with_now_data():
    transform_raw_information = TransformRawInformation()
    transformed_data = transform_raw_information.transform(
        extract_contract_mock)

    assert isinstance(transformed_data, TransformContract)
    assert isinstance(transformed_data.load_information, list)
    assert isinstance(transformed_data.load_information[0], dict)

    assert transformed_data.load_information[0]['first_name'] == 'Anton'
    assert transformed_data.load_information[0]['last_name'] == 'Aaberg'
    assert transformed_data.load_information[0]['player_id'] == 67200
    assert transformed_data.load_information[0]['highest_rating'] == 2400
    assert transformed_data.load_information[0]['start_year'] == 1991
    assert transformed_data.load_information[0]['end_year'] == 2012
    assert transformed_data.load_information[0]['number_of_games'] == 60
    assert transformed_data.load_information[0][
        'href'] == 'https://www.chessgames.com/perl/chessplayer?pid=67200'
    assert transformed_data.load_information[0][
        'extraction_date'] == date.today()


def test_transform_with_empty_raw_information():
    transform_raw_information = TransformRawInformation()
    transformed_data = transform_raw_information.transform(
        ExtractContract(raw_information=[], extraction_date=date.today()))

    assert isinstance(transformed_data, TransformContract)
    assert isinstance(transformed_data.load_information, list)
    assert len(transformed_data.load_information) == 0

def test_transform_exception():

    transform_raw_information = TransformRawInformation()

    try:
        transform_raw_information.transform(extract_contract=None)
    except Exception as error: #pylint: disable=broad-except
        assert isinstance(error, TransformException)
