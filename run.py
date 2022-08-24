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

from time import sleep
from src.main.main_pipeline import MainPipeline

if __name__ == "__main__":
    # A list with A-Z.
    alphabet = [chr(i) for i in range(65, 91)]

    for letter in alphabet:
        URL = f'https://www.chessgames.com/directory/{letter}.html'
        print(f'Processing {URL}')
        pipeline = MainPipeline(url=URL)
        pipeline.run()
        sleep(10)  # Sleep 10 seconds to avoid too many requests.
