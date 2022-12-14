#!/usr/bin/env python
# encoding: utf-8
#
#  ------------------------------------------------------------------------------
#  Name: transform_contract.py
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

from ..transform_contract import TransformContract

date_ordinal = dt.today().toordinal()

load_information = [{
    'first_name': 'Anton',
    'last_name': 'Aaberg',
    'player_id': 67200,
    'highest_rating': 2400,
    'start_year': 1991,
    'end_year': 2012,
    'number_of_games': 60,
    'href': 'https://www.chessgames.com/perl/chessplayer?pid=67200',
    'extraction_date': date_ordinal
}, {
    'first_name': 'Jacob',
    'last_name': 'Aagaard',
    'player_id': 35994,
    'highest_rating': 2542,
    'start_year': 1991,
    'end_year': 2021,
    'number_of_games': 237,
    'href': 'https://www.chessgames.com/perl/chessplayer?pid=35994',
    'extraction_date': date_ordinal
}, {
    'first_name': 'Hagawane',
    'last_name': 'Aakanksha',
    'player_id': 151600,
    'highest_rating': 2334,
    'start_year': 2014,
    'end_year': 2019,
    'number_of_games': 64,
    'href': 'https://www.chessgames.com/perl/chessplayer?pid=151600',
    'extraction_date': date_ordinal
}, {
    'first_name': 'Stein arild',
    'last_name': 'Aarland',
    'player_id': 16475,
    'highest_rating': 2311,
    'start_year': 1991,
    'end_year': 2007,
    'number_of_games': 17,
    'href': 'https://www.chessgames.com/perl/chessplayer?pid=16475',
    'extraction_date': date_ordinal
}, {
    'first_name': 'Deepak',
    'last_name': 'Aaron',
    'player_id': 131259,
    'highest_rating': 2362,
    'start_year': 2008,
    'end_year': 2021,
    'number_of_games': 35,
    'href': 'https://www.chessgames.com/perl/chessplayer?pid=131259',
    'extraction_date': date_ordinal
}, {
    'first_name': 'Manuel',
    'last_name': 'Aaron',
    'player_id': 18943,
    'highest_rating': 2315,
    'start_year': 1960,
    'end_year': 1984,
    'number_of_games': 91,
    'href': 'https://www.chessgames.com/perl/chessplayer?pid=18943',
    'extraction_date': date_ordinal
}, {
    'first_name': 'Varshney',
    'last_name': 'Aaryan',
    'player_id': 158828,
    'highest_rating': 2309,
    'start_year': 2017,
    'end_year': 2020,
    'number_of_games': 42,
    'href': 'https://www.chessgames.com/perl/chessplayer?pid=158828',
    'extraction_date': date_ordinal
}, {
    'first_name': 'Denis',
    'last_name': 'Abasheev',
    'player_id': 52307,
    'highest_rating': 2442,
    'start_year': 1996,
    'end_year': 2004,
    'number_of_games': 21,
    'href': 'https://www.chessgames.com/perl/chessplayer?pid=52307',
    'extraction_date': date_ordinal
}, {
    'first_name': 'Nijat',
    'last_name': 'Abasov',
    'player_id': 110381,
    'highest_rating': 2664,
    'start_year': 2005,
    'end_year': 2022,
    'number_of_games': 440,
    'href': 'https://www.chessgames.com/perl/chessplayer?pid=110381',
    'extraction_date': date_ordinal
}, {
    'first_name': 'Roger f t',
    'last_name': 'Abayasekera',
    'player_id': 104892,
    'highest_rating': 2208,
    'start_year': 1976,
    'end_year': 2005,
    'number_of_games': 21,
    'href': 'https://www.chessgames.com/perl/chessplayer?pid=104892',
    'extraction_date': date_ordinal
}, {
    'first_name': 'Daniel',
    'last_name': 'Abbas',
    'player_id': 157096,
    'highest_rating': 2329,
    'start_year': 2016,
    'end_year': 2019,
    'number_of_games': 42,
    'href': 'https://www.chessgames.com/perl/chessplayer?pid=157096',
    'extraction_date': date_ordinal
}, {
    'first_name': 'Zoubaier',
    'last_name': 'Amdouni',
    'player_id': 89360,
    'highest_rating': 2354,
    'start_year': 2002,
    'end_year': 2022,
    'number_of_games': 57,
    'href': 'https://www.chessgames.com/perl/chessplayer?pid=89360',
    'extraction_date': date_ordinal
}, {
    'first_name': 'Moheb',
    'last_name': 'Ameir',
    'player_id': 155278,
    'highest_rating': 2435,
    'start_year': 2016,
    'end_year': 2020,
    'number_of_games': 33,
    'href': 'https://www.chessgames.com/perl/chessplayer?pid=155278',
    'extraction_date': date_ordinal
}, {
    'first_name': 'Karim',
    'last_name': 'Amer',
    'player_id': 127285,
    'highest_rating': 2257,
    'start_year': 1989,
    'end_year': 2010,
    'number_of_games': 70,
    'href': 'https://www.chessgames.com/perl/chessplayer?pid=127285',
    'extraction_date': date_ordinal
}, {
    'first_name': 'Katrina',
    'last_name': 'Amerika',
    'player_id': 54946,
    'highest_rating': 2242,
    'start_year': 2001,
    'end_year': 2017,
    'number_of_games': 111,
    'href': 'https://www.chessgames.com/perl/chessplayer?pid=54946',
    'extraction_date': date_ordinal
}, {
    'first_name': 'Jaap',
    'last_name': 'Amesz',
    'player_id': 64509,
    'highest_rating': 2222,
    'start_year': 1999,
    'end_year': 2000,
    'number_of_games': 12,
    'href': 'https://www.chessgames.com/perl/chessplayer?pid=64509',
    'extraction_date': date_ordinal
}, {
    'first_name': 'Emmanuel',
    'last_name': 'Amigues',
    'player_id': 51994,
    'highest_rating': 2393,
    'start_year': 2000,
    'end_year': 2008,
    'number_of_games': 18,
    'href': 'https://www.chessgames.com/perl/chessplayer?pid=51994',
    'extraction_date': date_ordinal
}, {
    'first_name': 'Bassem',
    'last_name': 'Amin',
    'player_id': 87335,
    'highest_rating': 2700,
    'start_year': 1998,
    'end_year': 2022,
    'number_of_games': 815,
    'href': 'https://www.chessgames.com/perl/chessplayer?pid=87335',
    'extraction_date': date_ordinal
}, {
    'first_name': 'Battsooj',
    'last_name': 'Amina',
    'player_id': 154429,
    'highest_rating': 2274,
    'start_year': 2016,
    'end_year': 2016,
    'number_of_games': 16,
    'href': 'https://www.chessgames.com/perl/chessplayer?pid=154429',
    'extraction_date': date_ordinal
}, {
    'first_name': 'Andrey',
    'last_name': 'Aminov',
    'player_id': 141341,
    'highest_rating': 2324,
    'start_year': 2012,
    'end_year': 2022,
    'number_of_games': 21,
    'href': 'https://www.chessgames.com/perl/chessplayer?pid=141341',
    'extraction_date': date_ordinal
}, {
    'first_name': 'Pablo adib tapie',
    'last_name': 'Amione',
    'player_id': 143029,
    'highest_rating': 2312,
    'start_year': 2007,
    'end_year': 2022,
    'number_of_games': 16,
    'href': 'https://www.chessgames.com/perl/chessplayer?pid=143029',
    'extraction_date': date_ordinal
}, {
    'first_name': 'Philipp',
    'last_name': 'Ammann',
    'player_id': 22323,
    'highest_rating': 2221,
    'start_year': 1973,
    'end_year': 2004,
    'number_of_games': 24,
    'href': 'https://www.chessgames.com/perl/chessplayer?pid=22323',
    'extraction_date': date_ordinal
}, {
    'first_name': 'Sedrani',
    'last_name': 'Ammar',
    'player_id': 154383,
    'highest_rating': 2274,
    'start_year': 2016,
    'end_year': 2021,
    'number_of_games': 65,
    'href': 'https://www.chessgames.com/perl/chessplayer?pid=154383',
    'extraction_date': date_ordinal
}]

transform_contract_mock = TransformContract(load_information=load_information)
