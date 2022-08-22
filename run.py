#!/usr/bin/env python
# encoding: utf-8
#
#  ------------------------------------------------------------------------------
#  Name: run.py
#  Version: 0.0.1
#  Summary: Chess Player Database
#           A complete implementation of ETL process.
#
#  Author: Alexsander Lopes Camargos
#  Author-email: alcamargos@vivaldi.net
#
#  License: MIT
#  ------------------------------------------------------------------------------

from src.main.main_pipeline import MainPipeline

if __name__ == "__main__":
    URL = 'https://www.chessgames.com/directory/A.html'
    pipeline = MainPipeline(url=URL)
    pipeline.run()
