#!/usr/bin/env python
# encoding: utf-8
#
#  ------------------------------------------------------------------------------
#  Name: html_collector.py
#  Version: 0.0.1
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
        chess_players_table = soup.find("table", {
            'border': "0",
            'cellpadding': "2",
            'cellspacing': "0",
            'width': "100%"
        })
        chess_players_links = chess_players_table.find_all('a')

        chess_players_information = []
        for chess_players in chess_players_links:
            if not '.mp3' in chess_players.get('href'):
                href = f"https://www.chessgames.com{chess_players.get('href')}"
                player_name = chess_players.contents[0].string.strip()
                chess_players_information.append({
                    'href': href,
                    'player': player_name
                })
            else:
                continue

        return chess_players_information
