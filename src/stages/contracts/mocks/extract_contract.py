#!/usr/bin/env python
# encoding: utf-8
#
#  ------------------------------------------------------------------------------
#  Name: extract_contract.py
#  Version: 0.0.1
#  Summary: Chess Player Database
#           A complete implementation of ETL process.
#
#  Author: Alexsander Lopes Camargos
#  Author-email: alcamargos@vivaldi.net
#
#  License: MIT
#  ------------------------------------------------------------------------------

#pylint: disable=C0303 # Trailing whitespace

from datetime import date as dt

from ..extract_contract import ExtractContract

extraction_date = dt.today()

raw_information = [{'player_name': 'AABERG, Anton',
                    'highest_rating': '2400',
                    'years_covered': '1991-2012',
                    'number_of_games': '60',
                    'href': 'https://www.chessgames.com/perl/chessplayer?pid=67200'},
                   {'player_name': 'AAGAARD, Jacob',
                    'highest_rating': '2542',
                    'years_covered': '1991-2021',
                    'number_of_games': '237',
                    'href': 'https://www.chessgames.com/perl/chessplayer?pid=35994'},
                   {'player_name': 'AAKANKSHA, Hagawane',
                    'highest_rating': '2334',
                    'years_covered': '2014-2019',
                    'number_of_games': '64',
                    'href': 'https://www.chessgames.com/perl/chessplayer?pid=151600'},
                   {'player_name': 'AARLAND, Stein Arild',
                    'highest_rating': '2311',
                    'years_covered': '1991-2007',
                    'number_of_games': '17',
                    'href': 'https://www.chessgames.com/perl/chessplayer?pid=16475'},
                   {'player_name': 'AARON, Deepak',
                    'highest_rating': '2362',
                    'years_covered': '2008-2021',
                    'number_of_games': '35',
                    'href': 'https://www.chessgames.com/perl/chessplayer?pid=131259'},
                   {'player_name': 'AARON, Manuel',
                    'highest_rating': '2315',
                    'years_covered': '1960-1984',
                    'number_of_games': '91',
                    'href': 'https://www.chessgames.com/perl/chessplayer?pid=18943'},
                   {'player_name': 'AARYAN, Varshney',
                    'highest_rating': '2309',
                    'years_covered': '2017-2020',
                    'number_of_games': '42',
                    'href': 'https://www.chessgames.com/perl/chessplayer?pid=158828'},
                   {'player_name': 'ABASHEEV, Denis',
                    'highest_rating': '2442',
                    'years_covered': '1996-2004',
                    'number_of_games': '21',
                    'href': 'https://www.chessgames.com/perl/chessplayer?pid=52307'},
                   {'player_name': 'ABASOV, Nijat',
                    'highest_rating': '2664',
                    'years_covered': '2005-2022',
                    'number_of_games': '440',
                    'href': 'https://www.chessgames.com/perl/chessplayer?pid=110381'},
                   {'player_name': 'ABAYASEKERA, Roger F T',
                    'highest_rating': '2208',
                    'years_covered': '1976-2005',
                    'number_of_games': '21',
                    'href': 'https://www.chessgames.com/perl/chessplayer?pid=104892'},
                   {'player_name': 'ABBAS, Daniel',
                    'highest_rating': '2329',
                    'years_covered': '2016-2019',
                    'number_of_games': '42',
                    'href': 'https://www.chessgames.com/perl/chessplayer?pid=157096'},
                   {'player_name': 'AMDOUNI, Zoubaier',
                    'highest_rating': '2354',
                    'years_covered': '2002-2022',
                    'number_of_games': '57',
                    'href': 'https://www.chessgames.com/perl/chessplayer?pid=89360'},
                   {'player_name': 'AMEIR, Moheb',
                    'highest_rating': '2435',
                    'years_covered': '2016-2020',
                    'number_of_games': '33',
                    'href': 'https://www.chessgames.com/perl/chessplayer?pid=155278'},
                   {'player_name': 'AMER, Karim',
                    'highest_rating': '2257',
                    'years_covered': '1989-2010',
                    'number_of_games': '70',
                    'href': 'https://www.chessgames.com/perl/chessplayer?pid=127285'},
                   {'player_name': 'AMERIKA, Katrina',
                    'highest_rating': '2242',
                    'years_covered': '2001-2017',
                    'number_of_games': '111',
                    'href': 'https://www.chessgames.com/perl/chessplayer?pid=54946'},
                   {'player_name': 'AMESZ, Jaap',
                    'highest_rating': '2222',
                    'years_covered': '1999-2000',
                    'number_of_games': '12',
                    'href': 'https://www.chessgames.com/perl/chessplayer?pid=64509'},
                   {'player_name': 'AMIGUES, Emmanuel',
                    'highest_rating': '2393',
                    'years_covered': '2000-2008',
                    'number_of_games': '18',
                    'href': 'https://www.chessgames.com/perl/chessplayer?pid=51994'},
                   {'player_name': 'AMIN, Bassem',
                    'highest_rating': '2700',
                    'years_covered': '1998-2022',
                    'number_of_games': '815',
                    'href': 'https://www.chessgames.com/perl/chessplayer?pid=87335'},
                   {'player_name': 'AMINA, Battsooj',
                    'highest_rating': '2274',
                    'years_covered': '2016',
                    'number_of_games': '16',
                    'href': 'https://www.chessgames.com/perl/chessplayer?pid=154429'},
                   {'player_name': 'AMINOV, Andrey',
                    'highest_rating': '2324',
                    'years_covered': '2012-2022',
                    'number_of_games': '21',
                    'href': 'https://www.chessgames.com/perl/chessplayer?pid=141341'},
                   {'player_name': 'AMIONE, Pablo Adib Tapie',
                    'highest_rating': '2312',
                    'years_covered': '2007-2022',
                    'number_of_games': '16',
                    'href': 'https://www.chessgames.com/perl/chessplayer?pid=143029'},
                   {'player_name': 'AMMANN, Philipp',
                    'highest_rating': '2221',
                    'years_covered': '1973-2004',
                    'number_of_games': '24',
                    'href': 'https://www.chessgames.com/perl/chessplayer?pid=22323'},
                   {'player_name': 'AMMAR, Sedrani',
                    'highest_rating': '2274',
                    'years_covered': '2016-2021',
                    'number_of_games': '65',
                    'href': 'https://www.chessgames.com/perl/chessplayer?pid=154383'}]

extract_contract_mock = ExtractContract(raw_information, extraction_date)
