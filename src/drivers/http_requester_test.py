#!/usr/bin/env python
# encoding: utf-8
#
#  ------------------------------------------------------------------------------
#  Name: http_requester_test.py
#  Version: 0.0.1
#  Summary: Chess Player Database
#           A complete implementation of ETL process.
#
#  Author: Alexsander Lopes Camargos
#  Author-email: alcamargos@vivaldi.net
#
#  License: MIT
#  ------------------------------------------------------------------------------

from .http_requester import HttpRequester


def test_make_request(requests_mock):
    """Test make_request method."""

    url = 'https://www.chessgames.com/directory/A.html'
    response_status_code = 200
    response_context = '''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>requests-mock test page</title>
    </head>
    <body>
        <h1>requests-mock test page</h1>
        <p>This is a test page for requests-mock.</p>    
    </body>
    </html>
    '''

    requests_mock.get(url, status_code=200, text=response_context)

    http_requester = HttpRequester(url)
    request_response = http_requester.make_request()

    assert request_response['status_code'] == response_status_code
    assert request_response['content'] == response_context
    assert request_response['content'].startswith('\n    <!DOCTYPE html>')
    assert request_response['content'].endswith('</html>\n    ')
