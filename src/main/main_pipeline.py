#!/usr/bin/env python
# encoding: utf-8
#
#  ------------------------------------------------------------------------------
#  Name: main_pipeline.py
#  Version: 0.0.1
#  Summary: Chess Player Database
#           A complete implementation of ETL process.
#
#  Author: Alexsander Lopes Camargos
#  Author-email: alcamargos@vivaldi.net
#
#  License: MIT
#  ------------------------------------------------------------------------------

from src.stages.extractor.extractor_html_information import ExtractorHtmlInformation as Extractor
from src.stages.transform.transform_raw_information import TransformRawInformation as Transformer
from src.stages.loader.load_data import LoadData as Loader
from src.drivers.http_requester import HttpRequester
from src.drivers.html_collector import HtmlCollector
from src.infrastructure.database_connection_handler import DatabaseConnectionHandler
from src.infrastructure.database_repository import DatabaseRepository


class MainPipeline:

    def __init__(self, url):
        self.__extractor = Extractor(requester=HttpRequester(url=url),
                                     collector=HtmlCollector())

        self.__transformer = Transformer()
        self.__loader = Loader(repository=DatabaseRepository(
            connection_handler=DatabaseConnectionHandler()))

    def run(self):
        extract_contract = self.__extractor.extract()
        transform_contract = self.__transformer.transform(extract_contract)
        self.__loader.load(transform_contract)
