#!/usr/bin/env python
# encoding: utf-8
#
#  ------------------------------------------------------------------------------
#  Name: transform_raw_information.py
#  Version: 0.0.2
#  Summary: Chess Player Database
#           A complete implementation of ETL process.
#
#  Author: Alexsander Lopes Camargos
#  Author-email: alcamargos@vivaldi.net
#
#  License: MIT
#  ------------------------------------------------------------------------------

from src.exception.transform_exception import TransformException

from ..contracts.extract_contract import ExtractContract
from ..contracts.transform_contract import TransformContract


class TransformRawInformation:

    def transform(self,
                  extract_contract: ExtractContract) -> TransformContract:
        try:
            filter_information = self.__filter_information(extract_contract)

            filter_information_contract = TransformContract(
                load_information=filter_information)

            return filter_information_contract
        except Exception as exception:
            raise TransformException(exception) from exception

    def __filter_information(self, contract):
        raw_information = contract.raw_information
        extraction_date = contract.extraction_date

        transformed_information = []
        for information in raw_information:
            # Extract single information from the raw information.
            player_name = information['player_name']
            highest_rating = information['highest_rating']
            years_covered = information['years_covered']
            number_of_games = information['number_of_games']
            href = information['href']

            # Transform single information.
            transformed_data = self.__transform_information(
                player_name, highest_rating, years_covered, number_of_games,
                href)
            transformed_data['extraction_date'] = extraction_date

            # Append transformed information to the list.
            transformed_information.append(transformed_data)

        return transformed_information

    #pylint: disable=too-many-arguments
    def __transform_information(self,
                                player_name,
                                highest_rating,
                                years_covered,
                                number_of_games,
                                href):

        if ',' in player_name:
            names = player_name.split(', ')
            last_name = names[0].strip().capitalize()
            first_name = names[1].strip().capitalize()
        else:
            last_name = ''
            first_name = player_name.strip().capitalize()

        if ',' in highest_rating:
            highest_rating = highest_rating.replace(',', '')

        if highest_rating == '':
            highest_rating = 0

        if 'pid' in href:
            player_id = href.split('?pid=')[1]
        else:
            player_id = ''

        if '-' in years_covered:
            years = years_covered.split('-')
            start_year = years[0]
            end_year = years[1]
        else:
            start_year = years_covered
            end_year = years_covered

        if ',' in number_of_games:
            number_of_games = number_of_games.replace(',', '')

        if number_of_games == '':
            number_of_games = 0

        return {
            'first_name': first_name,
            'last_name': last_name,
            'player_id': int(player_id),
            'highest_rating': int(highest_rating),
            'start_year': int(start_year),
            'end_year': int(end_year),
            'number_of_games': int(number_of_games),
            'href': href
        }
