#!/usr/bin/env python
# encoding: utf-8
#
#  ------------------------------------------------------------------------------
#  Name: transform_raw_information_test.py
#  Version: 0.0.1
#  Summary: Chess Player Database
#           A complete implementation of ETL process.
#
#  Author: Alexsander Lopes Camargos
#  Author-email: alcamargos@vivaldi.net
#
#  License: MIT
#  ------------------------------------------------------------------------------

from datetime import date

from .transform_raw_information import TransformRawInformation

from ..contracts.transform_contract import TransformContract
from ..contracts.mocks.extract_contract import extract_contract_mock


def test_transform():
    transform_raw_information = TransformRawInformation()
    transformed_data = transform_raw_information.transform(extract_contract_mock)

    assert isinstance(transformed_data, TransformContract)
    assert isinstance(transformed_data.load_information, list)
    assert isinstance(transformed_data.load_information[0], dict)

    assert 'frist_name' in transformed_data.load_information[0]
    assert 'last_name' in transformed_data.load_information[0]
    assert 'player_id' in transformed_data.load_information[0]
    assert 'highest_rating' in transformed_data.load_information[0]
    assert 'start_year' in transformed_data.load_information[0]
    assert 'end_year' in transformed_data.load_information[0]
    assert 'number_of_games' in transformed_data.load_information[0]
    assert 'href' in transformed_data.load_information[0]
    assert 'extraction_date' in transformed_data.load_information[0]

    assert isinstance(transformed_data.load_information[0]['frist_name'], str)
    assert isinstance(transformed_data.load_information[0]['last_name'], str)
    assert isinstance(transformed_data.load_information[0]['player_id'], int)
    assert isinstance(transformed_data.load_information[0]['highest_rating'], int)
    assert isinstance(transformed_data.load_information[0]['start_year'], int)
    assert isinstance(transformed_data.load_information[0]['end_year'], int)
    assert isinstance(transformed_data.load_information[0]['number_of_games'], int)
    assert isinstance(transformed_data.load_information[0]['href'], str)
    assert isinstance(transformed_data.load_information[0]['extraction_date'], date)
