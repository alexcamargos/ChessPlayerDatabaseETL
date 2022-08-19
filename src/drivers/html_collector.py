#!/usr/bin/env python
# encoding: utf-8
#
#  ------------------------------------------------------------------------------
#  Name: html_collector.py
#  Version: 0.0.2
#  Summary: Chess Player Database
#           A complete implementation of ETL process.
#
#  Author: Alexsander Lopes Camargos
#  Author-email: alcamargos@vivaldi.net
#
#  License: MIT
#  ------------------------------------------------------------------------------

from bs4 import BeautifulSoup as bs

from .interfaces.html_collector import HtmlCollectorInterface


class HtmlCollector(HtmlCollectorInterface):

    @classmethod
    def collect_information(cls, html: str):  #pylint: disable=arguments-differ
        """Collect information from the html."""

        soup = bs(html, 'html.parser')
        chess_players_tables = soup.find_all("table", {'border': "0",
                                                       'cellpadding': "2",
                                                       'cellspacing': "0",
                                                       'width': "100%"})

        chess_players_rows = []
        for chess_players_table in chess_players_tables:
            chess_players_rows.extend(chess_players_table.find_all('tr'))

        chess_players_data = []
        for row in chess_players_rows:
            if row.find('font',  {'color': "#FFFFFF"}):
                continue

            chess_players_data.append(row.find_all('font'))

        chess_players_information = []
        for information in chess_players_data:
            highest_rating = information[0].contents[0].strip()
            player_name = information[1].find('a').contents[0].string.strip()
            years_covered = information[2].contents[0].strip()
            number_of_games = information[3].contents[0].strip()
            href = f"https://www.chessgames.com{information[1].find('a').get('href')}"

            chess_players_information.append({'player_name': player_name,
                                            'highest_rating': highest_rating,
                                            'years_covered': years_covered,
                                            'number_of_games': number_of_games,
                                            'href': href})

        return chess_players_information
