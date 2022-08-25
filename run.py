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

import time

from tqdm import tqdm

from src.main.main_pipeline import MainPipeline

if __name__ == "__main__":
    # A string list with all the letters of the alphabet A-Z.
    alphabet = [chr(i) for i in range(65, 91)]

    print('Chess Player Database Pipeline Started!')
    print('This process will take a while...\n\n')

    # Get the start time.
    start_time = time.time()

    for letter in tqdm(alphabet,
                       total=len(alphabet),
                       unit_scale=True,
                       colour='green'):
        URL = f'https://www.chessgames.com/directory/{letter}.html'
        pipeline = MainPipeline(url=URL)
        pipeline.run()
        time.sleep(10)  # Sleep 10 seconds to avoid too many requests.

    # Get the end time.
    end_time = time.time()

    # Calculate the elapsed time.
    elapsed_time = end_time - start_time
    gmtime = time.gmtime(elapsed_time)

    print('\n\nChess Player Database Pipeline Finished!')
    print(f'Execution time: {time.strftime("%H:%M:%S", gmtime)}')
