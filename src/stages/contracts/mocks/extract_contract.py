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

raw_information = [
    {'href': 'https://www.chessgames.com/perl/chessplayer?pid=67200',
    'player': 'AABERG, Anton'},
    {'href': 'https://www.chessgames.com/perl/chessplayer?pid=35994',
    'player': 'AAGAARD, Jacob'},
    {'href': 'https://www.chessgames.com/perl/chessplayer?pid=151600',
    'player': 'AAKANKSHA, Hagawane'},
    {'href': 'https://www.chessgames.com/perl/chessplayer?pid=16475',
    'player': 'AARLAND, Stein Arild'},
    {'href': 'https://www.chessgames.com/perl/chessplayer?pid=131259',  
     'player': 'AARON, Deepak'},
    {'href': 'https://www.chessgames.com/perl/chessplayer?pid=18943',
    'player': 'AARON, Manuel'},
    {'href': 'https://www.chessgames.com/perl/chessplayer?pid=158828',  
     'player': 'AARYAN, Varshney'},
    {'href': 'https://www.chessgames.com/perl/chessplayer?pid=52307',  
     'player': 'ABASHEEV, Denis'},
    {'href': 'https://www.chessgames.com/perl/chessplayer?pid=110381',  
     'player': 'ABASOV, Nijat'},
    {'href': 'https://www.chessgames.com/perl/chessplayer?pid=104892',  
     'player': 'ABAYASEKERA, Roger F T'},
    {'href': 'https://www.chessgames.com/perl/chessplayer?pid=157096',  
     'player': 'ABBAS, Daniel'},
    {'href': 'https://www.chessgames.com/perl/chessplayer?pid=89360',  
     'player': 'AMDOUNI, Zoubaier'},
    {'href': 'https://www.chessgames.com/perl/chessplayer?pid=155278',  
     'player': 'AMEIR, Moheb'},
    {'href': 'https://www.chessgames.com/perl/chessplayer?pid=127285',  
     'player': 'AMER, Karim'},
    {'href': 'https://www.chessgames.com/perl/chessplayer?pid=54946',  
     'player': 'AMERIKA, Katrina'},
    {'href': 'https://www.chessgames.com/perl/chessplayer?pid=64509',  
     'player': 'AMESZ, Jaap'},
    {'href': 'https://www.chessgames.com/perl/chessplayer?pid=51994',  
     'player': 'AMIGUES, Emmanuel'},
    {'href': 'https://www.chessgames.com/perl/chessplayer?pid=87335',  
     'player': 'AMIN, Bassem'},
    {'href': 'https://www.chessgames.com/perl/chessplayer?pid=154429',  
     'player': 'AMINA, Battsooj'},
    {'href': 'https://www.chessgames.com/perl/chessplayer?pid=141341',  
     'player': 'AMINOV, Andrey'},
    {'href': 'https://www.chessgames.com/perl/chessplayer?pid=143029',  
     'player': 'AMIONE, Pablo Adib Tapie'},
    {'href': 'https://www.chessgames.com/perl/chessplayer?pid=22323',  
     'player': 'AMMANN, Philipp'},
    {'href': 'https://www.chessgames.com/perl/chessplayer?pid=154383',
    'player': 'AMMAR, Sedrani'}
    ]

extract_contract_mock = ExtractContract(raw_information, extraction_date)
