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

from abc import ABC, abstractmethod


class HtmlCollectorInterface(ABC):

    @abstractmethod
    def collect_information(self, html: str):
        """Collect information from the html."""

        raise NotImplementedError("You should implement this method.")
