#!/usr/bin/env python
# encoding: utf-8
#
#  ------------------------------------------------------------------------------
#  Name: http_requester_mock.py
#  Version: 0.0.2
#  Summary: Chess Player Database
#           A complete implementation of ETL process.
#
#  Author: Alexsander Lopes Camargos
#  Author-email: alcamargos@vivaldi.net
#
#  License: MIT
#  ------------------------------------------------------------------------------

#pylint: disable=line-too-long
#pylint: disable=trailing-whitespace
#pylint: disable=too-many-lines


def mock_request_from_page():

    return {
        'status_code':
        200,
        'html':
        '''<html>

<head>
    <meta name="keywords" content="chess, chess games, ajedrez, scacchi, schach, PGN">
    <meta name="description" content="The internet's oldest and best chess database and community.">
    <meta charset="UTF-8">

    <link rel="stylesheet" href="/bootstrap/css/bootstrap.min.css">

    <link rel="stylesheet" href="/css/cgc2a.css" />
    <title>Chess Player Directory</title>
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>
    <script async src="/js/hide-ad.js"></script>

    <script type="text/javascript" src="https://increaserev.com/ads/ob/tage/chessgames.js"></script>

    <!-- Google reCAPTCHA integration -->
    <script src="https://www.google.com/recaptcha/api.js?render=6LcPzqQUAAAAAKp0xQoWaR1mMZqtQ00O-Z6uAzQJ"></script>

    <!-- Facebook Pixel Code -->
    <script>
        !function (f, b, e, v, n, t, s) {
            if (f.fbq) return; n = f.fbq = function () {
                n.callMethod ?
                    n.callMethod.apply(n, arguments) : n.queue.push(arguments)
            }; if (!f._fbq) f._fbq = n;
            n.push = n; n.loaded = !0; n.version = '2.0'; n.queue = []; t = b.createElement(e); t.async = !0;
            t.src = v; s = b.getElementsByTagName(e)[0]; s.parentNode.insertBefore(t, s)
        }(window,
            document, 'script', 'https://connect.facebook.net/en_US/fbevents.js');
        fbq('init', '292563634274827');
        fbq('track', 'PageView');
    </script>
    <noscript><img height="1" width="1" style="display:none"
            src="https://www.facebook.com/tr?id=292563634274827&ev=PageView&noscript=1" /></noscript>
    <!-- DO NOT MODIFY -->
    <!-- End Facebook Pixel Code -->

    <script type="text/javascript">
        function OpenWin(pagename) {
            SmallWin = window.open(pagename, 'popup', 'scrollbars,resizable,toolbar=no,height=394,width=412,left=200,top=200');
            if (window.focus) {
                SmallWin.focus();
            }
        }
    </script>

    <link rel="stylesheet" type="text/css"
        href="//cdnjs.cloudflare.com/ajax/libs/cookieconsent2/3.1.0/cookieconsent.min.css" />
    <script src="//cdnjs.cloudflare.com/ajax/libs/cookieconsent2/3.1.0/cookieconsent.min.js"></script>
    <script>
        window.addEventListener("load", function () {
            window.cookieconsent.initialise({
                "palette": {
                    "popup": {
                        "background": "#000"
                    },
                    "button": {
                        "background": "#f1d600"
                    }
                },
                "content": {
                    "href": "https://www.chessgames.com/chessprivacy.html"
                }
            })
        });
    </script>
</head>

<body>

    <table border="0" cellpadding="0" cellspacing="0" bgcolor="#FFFFFF" width="100%">
        <tr>
            <td valign="top" align="left" background="/chessimages/header_stripes.gif"><a href="/index.html"><img
                        src="/chessimages/chessgameslogo.png" style="margin-left:-6px;" width="431" height="60"
                        border="0" alt="chessgames.com"></a></td>

            <td width="100%" background="/chessimages/header_stripes.gif" align="right" valign="top"><img
                    src="/chessimages/header_menu.gif" style="margin-right:-6px;" width="238" height="60"
                    usemap="#navbar" border="0"></td>
        </tr>
    </table>
    <map name="navbar">
        <area shape=rect coords="9,21,62,40" href="/index.html">
        <area shape=rect coords="65,21,118,40" href="/perl/chessnew">
        <area shape=rect coords="121,21,174,40" href="/perl/chessuser">
        <area shape=rect coords="177,21,230,40" href="/chesshelp.html">
    </map>

    <!--beginmenu-->
    <div class="cgc-ns1 xsm w-100pct b1s000000 bc-FFFFEE tc-000000 center tcenter"
        style="margin-bottom:4px; padding:2px;">
        <a href="/perl/chessmembers">Members</a> <b>&#183;</b>
        <a href="/perl/chessprofile.pl">Prefs</a> <b>&#183;</b>
        <a href="/perl/analyzer.pl">Laboratory</a> <b>&#183;</b>
        <a href="/perl/collections">Collections</a> <b>&#183;</b>
        <a href="/perl/explorer">Openings</a> <b>&#183;</b>
        <a href="/perl/chessending">Endgames</a> <b>&#183;</b>
        <a href="/perl/sacrifices">Sacrifices</a> <b>&#183;</b>
        <a href="/perl/history">History</a> <b>&#183;</b>
        <a href="/perl/searchkibitzes">Search Kibitzing</a> <b>&#183;</b>
        <a href="/perl/chessforum.pl">Kibitzer's Caf&eacute;</a> <b>&#183;</b>
        <a href="/perl/chessnew?chessforums=1">Chessforums</a> <b>&#183;</b>
        <a href="/perl/tournaments">Tournament Index</a> <b>&#183;</b>
        <a href="/directory/">Players</a> <b>&#183;</b>
        <a href="#kibitzing"><img src="/chessimages/arrow_down.gif" width="7" height="8" border="0">Kibitzing</a>
    </div>
    <!--endmenu-->
    <!-- Global site tag (gtag.js) - Google Analytics -->
    <script async src="https://www.googletagmanager.com/gtag/js?id=UA-169342218-1"></script>
    <script>
        window.dataLayer = window.dataLayer || [];
        function gtag() { dataLayer.push(arguments); }
        gtag('js', new Date());

        gtag('config', 'UA-169342218-1');
    </script>

    <!--TEMP - SSM for maintenance
    <div>
        <h6 style="text-align:center;color:red;width:80%;margin:0 auto;">Chessgames.com will be unavailable Wednesday, December 22, 2021 from 4AM through 5AM(UTC/GMT) for maintenance.<br>
        We apologize for this inconvenience.</h6>
    </div>
    < TEMP - SSM END-->

    <div class="increaserev bidmcm1200x250"></div>
    <script>ir_ads_push();</script>
    &nbsp;<br>
    <center>
        <table border=0 cellpadding=0 cellspacing=0 width=579>
            <tr>
                <td>
                    <font face="verdana,arial,helvetica">
                        <B>
                            <font size=+1 color=#663300>CHESS PLAYER DIRECTORY</font>
                        </B>
                        <br>
                        This is a directory of the most eminent chess players in the database.
                    </font>
                </td>
            </tr>
        </table>
    </center>
    <P>
        <center>
            <table border=0 cellpadding=1 cellspacing=0>
                <tr>
                    <td bgcolor=#996633>
                        <table border=0 cellpadding=5 cellspacing=0>
                            <tr>
                                <td background="/chessimages/highlight_stripes.gif">
                                    <font face="verdana,arial,helvetica"><B>
                                            <font size=+2 color=#CC0000>A</font>&nbsp;<a
                                                href="/directory/B.html">B</a>&nbsp;<a
                                                href="/directory/C.html">C</a>&nbsp;<a
                                                href="/directory/D.html">D</a>&nbsp;<a
                                                href="/directory/E.html">E</a>&nbsp;<a
                                                href="/directory/F.html">F</a>&nbsp;<a
                                                href="/directory/G.html">G</a>&nbsp;<a
                                                href="/directory/H.html">H</a>&nbsp;<a
                                                href="/directory/I.html">I</a>&nbsp;<a
                                                href="/directory/J.html">J</a>&nbsp;<a
                                                href="/directory/K.html">K</a>&nbsp;<a
                                                href="/directory/L.html">L</a>&nbsp;<a
                                                href="/directory/M.html">M</a>&nbsp;<a
                                                href="/directory/N.html">N</a>&nbsp;<a
                                                href="/directory/O.html">O</a>&nbsp;<a
                                                href="/directory/P.html">P</a>&nbsp;<a
                                                href="/directory/Q.html">Q</a>&nbsp;<a
                                                href="/directory/R.html">R</a>&nbsp;<a
                                                href="/directory/S.html">S</a>&nbsp;<a
                                                href="/directory/T.html">T</a>&nbsp;<a
                                                href="/directory/U.html">U</a>&nbsp;<a
                                                href="/directory/V.html">V</a>&nbsp;<a
                                                href="/directory/W.html">W</a>&nbsp;<a
                                                href="/directory/X.html">X</a>&nbsp;<a
                                                href="/directory/Y.html">Y</a>&nbsp;<a href="/directory/Z.html">Z</a>
                                    </font>
                                </td>
                            </tr>
                        </table>
                    </td>
                </tr>
            </table>
        </center><br>
        <center>
            <table border=0 cellpadding=5 cellspacing=0>
                <tr>
                    <td valign=TOP>
                        <table border=0 cellpadding=2 cellspacing=0 bgcolor=#333333>
                            <tr>
                                <td valign=TOP>
                                    <table border=0 cellpadding=2 cellspacing=0 width=100%>
                                        <tr bgcolor=#663300>
                                            <td align=RIGHT>
                                                <font face="verdana,arial,helvetica" size=-1 color=#FFFFFF>
                                                    highest<br>rating</font>
                                            </td>
                                            <td colspan=2>
                                                <font face="verdana,arial,helvetica" size=-1 color=#FFFFFF>
                                                    &nbsp;&nbsp;&nbsp;&nbsp;player name</font>
                                            </td>
                                            <td align=CENTER>
                                                <font face="verdana,arial,helvetica" size=-1 color=#FFFFFF>Years</font>
                                            </td>
                                            <td align=RIGHT>
                                                <font face="verdana,arial,helvetica" size=-1 color=#FFFFFF># of<br>Games
                                                </font>
                                            </td>
                                        </tr>
                                        <tr bgcolor=#FFFFFF>
                                            <td align=RIGHT>
                                                <font face="verdana,arial,helvetica" size=-2>&nbsp;2400</font>
                                            </td>
                                            <td><img src="/chessimages/chat.gif" alt="18" width=16 height=16><img
                                                    src="/chessimages/book.gif" alt="biography" width=16 height=16></td>
                                            <td width=160>
                                                <font face="verdana,arial,helvetica" size=-1><a
                                                        href="/perl/chessplayer?pid=67200"><B>AABERG, Anton </B></a>
                                                </font>
                                            </td>
                                            <td align=CENTER>
                                                <font face="verdana,arial,helvetica" size=-2>&nbsp;1991-2012</font>
                                            </td>
                                            <td align=RIGHT>
                                                <font face="verdana,arial,helvetica" size=-2>&nbsp;60</font>
                                            </td>
                                        </tr>
                                        <tr bgcolor=#FFEEDD>
                                            <td align=RIGHT>
                                                <font face="verdana,arial,helvetica" size=-2>&nbsp;2542</font>
                                            </td>
                                            <td><img src="/chessimages/chat.gif" alt="159" width=16 height=16><img
                                                    src="/chessimages/book.gif" alt="biography" width=16 height=16></td>
                                            <td width=160>
                                                <font face="verdana,arial,helvetica" size=-1><a
                                                        href="/perl/chessplayer?pid=35994"><B>AAGAARD, Jacob </B></a>
                                                </font>
                                            </td>
                                            <td align=CENTER>
                                                <font face="verdana,arial,helvetica" size=-2>&nbsp;1991-2021</font>
                                            </td>
                                            <td align=RIGHT>
                                                <font face="verdana,arial,helvetica" size=-2>&nbsp;237</font>
                                            </td>
                                        </tr>
                                        <tr bgcolor=#FFFFFF>
                                            <td align=RIGHT>
                                                <font face="verdana,arial,helvetica" size=-2>&nbsp;2334</font>
                                            </td>
                                            <td>&nbsp;<img src="/chessimages/book.gif" alt="biography" width=16
                                                    height=16></td>
                                            <td width=160>
                                                <font face="verdana,arial,helvetica" size=-1><a
                                                        href="/perl/chessplayer?pid=151600"><B>AAKANKSHA, Hagawane
                                                        </B></a></font>
                                            </td>
                                            <td align=CENTER>
                                                <font face="verdana,arial,helvetica" size=-2>&nbsp;2014-2019</font>
                                            </td>
                                            <td align=RIGHT>
                                                <font face="verdana,arial,helvetica" size=-2>&nbsp;64</font>
                                            </td>
                                        </tr>
                                        <tr bgcolor=#FFEEDD>
                                            <td align=RIGHT>
                                                <font face="verdana,arial,helvetica" size=-2>&nbsp;2311</font>
                                            </td>
                                            <td><img src="/chessimages/chat.gif" alt="4" width=16 height=16><img
                                                    src="/chessimages/book.gif" alt="biography" width=16 height=16></td>
                                            <td width=160>
                                                <font face="verdana,arial,helvetica" size=-1><a
                                                        href="/perl/chessplayer?pid=16475"><B>AARLAND, Stein Arild
                                                        </B></a></font>
                                            </td>
                                            <td align=CENTER>
                                                <font face="verdana,arial,helvetica" size=-2>&nbsp;1991-2007</font>
                                            </td>
                                            <td align=RIGHT>
                                                <font face="verdana,arial,helvetica" size=-2>&nbsp;17</font>
                                            </td>
                                        </tr>
                                        <tr bgcolor=#FFFFFF>
                                            <td align=RIGHT>
                                                <font face="verdana,arial,helvetica" size=-2>&nbsp;2362</font>
                                            </td>
                                            <td>&nbsp;<img src="/chessimages/book.gif" alt="biography" width=16
                                                    height=16></td>
                                            <td width=160>
                                                <font face="verdana,arial,helvetica" size=-1><a
                                                        href="/perl/chessplayer?pid=131259"><B>AARON, Deepak </B></a>
                                                </font>
                                            </td>
                                            <td align=CENTER>
                                                <font face="verdana,arial,helvetica" size=-2>&nbsp;2008-2021</font>
                                            </td>
                                            <td align=RIGHT>
                                                <font face="verdana,arial,helvetica" size=-2>&nbsp;35</font>
                                            </td>
                                        </tr>
                                        <tr bgcolor=#FFEEDD>
                                            <td align=RIGHT>
                                                <font face="verdana,arial,helvetica" size=-2>&nbsp;2315</font>
                                            </td>
                                            <td><img src="/chessimages/chat.gif" alt="34" width=16 height=16><img
                                                    src="/chessimages/book.gif" alt="biography" width=16 height=16></td>
                                            <td width=160>
                                                <font face="verdana,arial,helvetica" size=-1><a
                                                        href="/perl/chessplayer?pid=18943"><B>AARON, Manuel </B></a>
                                                </font>
                                            </td>
                                            <td align=CENTER>
                                                <font face="verdana,arial,helvetica" size=-2>&nbsp;1960-1984</font>
                                            </td>
                                            <td align=RIGHT>
                                                <font face="verdana,arial,helvetica" size=-2>&nbsp;91</font>
                                            </td>
                                        </tr>
                                        <tr bgcolor=#FFFFFF>
                                            <td align=RIGHT>
                                                <font face="verdana,arial,helvetica" size=-2>&nbsp;2309</font>
                                            </td>
                                            <td>&nbsp;</td>
                                            <td width=160>
                                                <font face="verdana,arial,helvetica" size=-1><a
                                                        href="/perl/chessplayer?pid=158828"><B>AARYAN, Varshney </B></a>
                                                </font>
                                            </td>
                                            <td align=CENTER>
                                                <font face="verdana,arial,helvetica" size=-2>&nbsp;2017-2020</font>
                                            </td>
                                            <td align=RIGHT>
                                                <font face="verdana,arial,helvetica" size=-2>&nbsp;42</font>
                                            </td>
                                        </tr>
                                        <tr bgcolor=#FFEEDD>
                                            <td align=RIGHT>
                                                <font face="verdana,arial,helvetica" size=-2>&nbsp;2442</font>
                                            </td>
                                            <td><img src="/chessimages/chat.gif" alt="2" width=16 height=16><img
                                                    src="/chessimages/book.gif" alt="biography" width=16 height=16></td>
                                            <td width=160>
                                                <font face="verdana,arial,helvetica" size=-1><a
                                                        href="/perl/chessplayer?pid=52307"><B>ABASHEEV, Denis </B></a>
                                                </font>
                                            </td>
                                            <td align=CENTER>
                                                <font face="verdana,arial,helvetica" size=-2>&nbsp;1996-2004</font>
                                            </td>
                                            <td align=RIGHT>
                                                <font face="verdana,arial,helvetica" size=-2>&nbsp;21</font>
                                            </td>
                                        </tr>
                                        <tr bgcolor=#FFFFFF>
                                            <td align=RIGHT>
                                                <font face="verdana,arial,helvetica" size=-2>&nbsp;2664</font>
                                            </td>
                                            <td><img src="/chessimages/chat.gif" alt="12" width=16 height=16><img
                                                    src="/chessimages/book.gif" alt="biography" width=16 height=16></td>
                                            <td width=160>
                                                <font face="verdana,arial,helvetica" size=-1><a
                                                        href="/perl/chessplayer?pid=110381"><B>ABASOV, Nijat </B></a>
                                                </font>
                                            </td>
                                            <td align=CENTER>
                                                <font face="verdana,arial,helvetica" size=-2>&nbsp;2005-2022</font>
                                            </td>
                                            <td align=RIGHT>
                                                <font face="verdana,arial,helvetica" size=-2>&nbsp;440</font>
                                            </td>
                                        </tr>
                                        <tr bgcolor=#FFEEDD>
                                            <td align=RIGHT>
                                                <font face="verdana,arial,helvetica" size=-2>&nbsp;2208</font>
                                            </td>
                                            <td>&nbsp;</td>
                                            <td width=160>
                                                <font face="verdana,arial,helvetica" size=-1><a
                                                        href="/perl/chessplayer?pid=104892"><B>ABAYASEKERA, Roger F T
                                                        </B></a></font>
                                            </td>
                                            <td align=CENTER>
                                                <font face="verdana,arial,helvetica" size=-2>&nbsp;1976-2005</font>
                                            </td>
                                            <td align=RIGHT>
                                                <font face="verdana,arial,helvetica" size=-2>&nbsp;21</font>
                                            </td>
                                        </tr>
                                        <tr bgcolor=#FFFFFF>
                                            <td align=RIGHT>
                                                <font face="verdana,arial,helvetica" size=-2>&nbsp;2329</font>
                                            </td>
                                            <td>&nbsp;<img src="/chessimages/book.gif" alt="biography" width=16
                                                    height=16></td>
                                            <td width=160>
                                                <font face="verdana,arial,helvetica" size=-1><a
                                                        href="/perl/chessplayer?pid=157096"><B>ABBAS, Daniel </B></a>
                                                </font>
                                            </td>
                                            <td align=CENTER>
                                                <font face="verdana,arial,helvetica" size=-2>&nbsp;2016-2019</font>
                                            </td>
                                            <td align=RIGHT>
                                                <font face="verdana,arial,helvetica" size=-2>&nbsp;42</font>
                                            </td>
                                        </tr>
                                    </table>
                                </td>
                            </tr>
                        </table>
                    </td>
                    <td bgcolor=#FFFFFF>&nbsp;</td>
                    <td valign=TOP>
                        <table border=0 cellpadding=2 cellspacing=0 bgcolor=#333333>
                            <tr>
                                <td valign=TOP>
                                    <table border=0 cellpadding=2 cellspacing=0 width=100%>
                                        <tr bgcolor=#663300>
                                            <td align=RIGHT>
                                                <font face="verdana,arial,helvetica" size=-1 color=#FFFFFF>
                                                    highest<br>rating</font>
                                            </td>
                                            <td colspan=2>
                                                <font face="verdana,arial,helvetica" size=-1 color=#FFFFFF>
                                                    &nbsp;&nbsp;&nbsp;&nbsp;player name</font>
                                            </td>
                                            <td align=CENTER>
                                                <font face="verdana,arial,helvetica" size=-1 color=#FFFFFF>Years</font>
                                            </td>
                                            <td align=RIGHT>
                                                <font face="verdana,arial,helvetica" size=-1 color=#FFFFFF># of<br>Games
                                                </font>
                                            </td>
                                        </tr>
                                        <tr bgcolor=#FFFFFF>
                                            <td align=RIGHT>
                                                <font face="verdana,arial,helvetica" size=-2>&nbsp;2354</font>
                                            </td>
                                            <td>&nbsp;<img src="/chessimages/book.gif" alt="biography" width=16
                                                    height=16></td>
                                            <td width=160>
                                                <font face="verdana,arial,helvetica" size=-1><a
                                                        href="/perl/chessplayer?pid=89360"><B>AMDOUNI, Zoubaier </B></a>
                                                </font>
                                            </td>
                                            <td align=CENTER>
                                                <font face="verdana,arial,helvetica" size=-2>&nbsp;2002-2022</font>
                                            </td>
                                            <td align=RIGHT>
                                                <font face="verdana,arial,helvetica" size=-2>&nbsp;57</font>
                                            </td>
                                        </tr>
                                        <tr bgcolor=#FFEEDD>
                                            <td align=RIGHT>
                                                <font face="verdana,arial,helvetica" size=-2>&nbsp;2435</font>
                                            </td>
                                            <td>&nbsp;<img src="/chessimages/book.gif" alt="biography" width=16
                                                    height=16></td>
                                            <td width=160>
                                                <font face="verdana,arial,helvetica" size=-1><a
                                                        href="/perl/chessplayer?pid=155278"><B>AMEIR, Moheb </B></a>
                                                </font>
                                            </td>
                                            <td align=CENTER>
                                                <font face="verdana,arial,helvetica" size=-2>&nbsp;2016-2020</font>
                                            </td>
                                            <td align=RIGHT>
                                                <font face="verdana,arial,helvetica" size=-2>&nbsp;33</font>
                                            </td>
                                        </tr>
                                        <tr bgcolor=#FFFFFF>
                                            <td align=RIGHT>
                                                <font face="verdana,arial,helvetica" size=-2>&nbsp;2257</font>
                                            </td>
                                            <td><img src="/chessimages/chat.gif" alt="1" width=16 height=16><img
                                                    src="/chessimages/book.gif" alt="biography" width=16 height=16></td>
                                            <td width=160>
                                                <font face="verdana,arial,helvetica" size=-1><a
                                                        href="/perl/chessplayer?pid=127285"><B>AMER, Karim </B></a>
                                                </font>
                                            </td>
                                            <td align=CENTER>
                                                <font face="verdana,arial,helvetica" size=-2>&nbsp;1989-2010</font>
                                            </td>
                                            <td align=RIGHT>
                                                <font face="verdana,arial,helvetica" size=-2>&nbsp;70</font>
                                            </td>
                                        </tr>
                                        <tr bgcolor=#FFEEDD>
                                            <td align=RIGHT>
                                                <font face="verdana,arial,helvetica" size=-2>&nbsp;2242</font>
                                            </td>
                                            <td><img src="/chessimages/chat.gif" alt="4" width=16 height=16><img
                                                    src="/chessimages/book.gif" alt="biography" width=16 height=16></td>
                                            <td width=160>
                                                <font face="verdana,arial,helvetica" size=-1><a
                                                        href="/perl/chessplayer?pid=54946"><B>AMERIKA, Katrina </B></a>
                                                </font>
                                            </td>
                                            <td align=CENTER>
                                                <font face="verdana,arial,helvetica" size=-2>&nbsp;2001-2017</font>
                                            </td>
                                            <td align=RIGHT>
                                                <font face="verdana,arial,helvetica" size=-2>&nbsp;111</font>
                                            </td>
                                        </tr>
                                        <tr bgcolor=#FFFFFF>
                                            <td align=RIGHT>
                                                <font face="verdana,arial,helvetica" size=-2>&nbsp;2222</font>
                                            </td>
                                            <td><img src="/chessimages/chat.gif" alt="1" width=16 height=16><img
                                                    src="/chessimages/book.gif" alt="biography" width=16 height=16></td>
                                            <td width=160>
                                                <font face="verdana,arial,helvetica" size=-1><a
                                                        href="/perl/chessplayer?pid=64509"><B>AMESZ, Jaap </B></a>
                                                </font>
                                            </td>
                                            <td align=CENTER>
                                                <font face="verdana,arial,helvetica" size=-2>&nbsp;1999-2000</font>
                                            </td>
                                            <td align=RIGHT>
                                                <font face="verdana,arial,helvetica" size=-2>&nbsp;12</font>
                                            </td>
                                        </tr>
                                        <tr bgcolor=#FFEEDD>
                                            <td align=RIGHT>
                                                <font face="verdana,arial,helvetica" size=-2>&nbsp;2393</font>
                                            </td>
                                            <td>&nbsp;<img src="/chessimages/book.gif" alt="biography" width=16
                                                    height=16></td>
                                            <td width=160>
                                                <font face="verdana,arial,helvetica" size=-1><a
                                                        href="/perl/chessplayer?pid=51994"><B>AMIGUES, Emmanuel </B></a>
                                                </font>
                                            </td>
                                            <td align=CENTER>
                                                <font face="verdana,arial,helvetica" size=-2>&nbsp;2000-2008</font>
                                            </td>
                                            <td align=RIGHT>
                                                <font face="verdana,arial,helvetica" size=-2>&nbsp;18</font>
                                            </td>
                                        </tr>
                                        <tr bgcolor=#FFFFFF>
                                            <td align=RIGHT>
                                                <font face="verdana,arial,helvetica" size=-2>&nbsp;2700</font>
                                            </td>
                                            <td><img src="/chessimages/chat.gif" alt="28" width=16 height=16><img
                                                    src="/chessimages/book.gif" alt="biography" width=16 height=16></td>
                                            <td width=160>
                                                <font face="verdana,arial,helvetica" size=-1><a
                                                        href="/perl/chessplayer?pid=87335"><B>AMIN, Bassem </B></a>
                                                </font>
                                            </td>
                                            <td align=CENTER>
                                                <font face="verdana,arial,helvetica" size=-2>&nbsp;1998-2022</font>
                                            </td>
                                            <td align=RIGHT>
                                                <font face="verdana,arial,helvetica" size=-2>&nbsp;815</font>
                                            </td>
                                        </tr>
                                        <tr bgcolor=#FFEEDD>
                                            <td align=RIGHT>
                                                <font face="verdana,arial,helvetica" size=-2>&nbsp;2274</font>
                                            </td>
                                            <td>&nbsp;<img src="/chessimages/book.gif" alt="biography" width=16
                                                    height=16></td>
                                            <td width=160>
                                                <font face="verdana,arial,helvetica" size=-1><a
                                                        href="/perl/chessplayer?pid=154429"><B>AMINA, Battsooj </B></a>
                                                </font>
                                            </td>
                                            <td align=CENTER>
                                                <font face="verdana,arial,helvetica" size=-2>&nbsp;2016</font>
                                            </td>
                                            <td align=RIGHT>
                                                <font face="verdana,arial,helvetica" size=-2>&nbsp;16</font>
                                            </td>
                                        </tr>
                                        <tr bgcolor=#FFFFFF>
                                            <td align=RIGHT>
                                                <font face="verdana,arial,helvetica" size=-2>&nbsp;2324</font>
                                            </td>
                                            <td>&nbsp;</td>
                                            <td width=160>
                                                <font face="verdana,arial,helvetica" size=-1><a
                                                        href="/perl/chessplayer?pid=141341"><B>AMINOV, Andrey </B></a>
                                                </font>
                                            </td>
                                            <td align=CENTER>
                                                <font face="verdana,arial,helvetica" size=-2>&nbsp;2012-2022</font>
                                            </td>
                                            <td align=RIGHT>
                                                <font face="verdana,arial,helvetica" size=-2>&nbsp;21</font>
                                            </td>
                                        </tr>
                                        <tr bgcolor=#FFEEDD>
                                            <td align=RIGHT>
                                                <font face="verdana,arial,helvetica" size=-2>&nbsp;2312</font>
                                            </td>
                                            <td>&nbsp;<img src="/chessimages/book.gif" alt="biography" width=16
                                                    height=16></td>
                                            <td width=160>
                                                <font face="verdana,arial,helvetica" size=-1><a
                                                        href="/perl/chessplayer?pid=143029"><B>AMIONE, Pablo Adib Tapie
                                                        </B></a></font>
                                            </td>
                                            <td align=CENTER>
                                                <font face="verdana,arial,helvetica" size=-2>&nbsp;2007-2022</font>
                                            </td>
                                            <td align=RIGHT>
                                                <font face="verdana,arial,helvetica" size=-2>&nbsp;16</font>
                                            </td>
                                        </tr>
                                        <tr bgcolor=#FFFFFF>
                                            <td align=RIGHT>
                                                <font face="verdana,arial,helvetica" size=-2>&nbsp;2221</font>
                                            </td>
                                            <td>&nbsp;<img src="/chessimages/book.gif" alt="biography" width=16
                                                    height=16></td>
                                            <td width=160>
                                                <font face="verdana,arial,helvetica" size=-1><a
                                                        href="/perl/chessplayer?pid=22323"><B>AMMANN, Philipp </B></a>
                                                </font>
                                            </td>
                                            <td align=CENTER>
                                                <font face="verdana,arial,helvetica" size=-2>&nbsp;1973-2004</font>
                                            </td>
                                            <td align=RIGHT>
                                                <font face="verdana,arial,helvetica" size=-2>&nbsp;24</font>
                                            </td>
                                        </tr>
                                        <tr bgcolor=#FFEEDD>
                                            <td align=RIGHT>
                                                <font face="verdana,arial,helvetica" size=-2>&nbsp;2274</font>
                                            </td>
                                            <td>&nbsp;<img src="/chessimages/book.gif" alt="biography" width=16
                                                    height=16></td>
                                            <td width=160>
                                                <font face="verdana,arial,helvetica" size=-1><a
                                                        href="/perl/chessplayer?pid=154383"><B>AMMAR, Sedrani </B></a>
                                                </font>
                                            </td>
                                            <td align=CENTER>
                                                <font face="verdana,arial,helvetica" size=-2>&nbsp;2016-2021</font>
                                            </td>
                                            <td align=RIGHT>
                                                <font face="verdana,arial,helvetica" size=-2>&nbsp;65</font>
                                            </td>
                                        </tr>
                                    </table>
                                </td>
                            </tr>
                        </table>
                    </td>
                </tr>
            </table>
        </center>
    <P>
        <center>
            <table border=0 cellpadding=1 cellspacing=0>
                <tr>
                    <td bgcolor=#996633>
                        <table border=0 cellpadding=5 cellspacing=0>
                            <tr>
                                <td background="/chessimages/highlight_stripes.gif">
                                    <font face="verdana,arial,helvetica"><B>
                                            <font size=+2 color=#CC0000>A</font>&nbsp;<a
                                                href="/directory/B.html">B</a>&nbsp;<a
                                                href="/directory/C.html">C</a>&nbsp;<a
                                                href="/directory/D.html">D</a>&nbsp;<a
                                                href="/directory/E.html">E</a>&nbsp;<a
                                                href="/directory/F.html">F</a>&nbsp;<a
                                                href="/directory/G.html">G</a>&nbsp;<a
                                                href="/directory/H.html">H</a>&nbsp;<a
                                                href="/directory/I.html">I</a>&nbsp;<a
                                                href="/directory/J.html">J</a>&nbsp;<a
                                                href="/directory/K.html">K</a>&nbsp;<a
                                                href="/directory/L.html">L</a>&nbsp;<a
                                                href="/directory/M.html">M</a>&nbsp;<a
                                                href="/directory/N.html">N</a>&nbsp;<a
                                                href="/directory/O.html">O</a>&nbsp;<a
                                                href="/directory/P.html">P</a>&nbsp;<a
                                                href="/directory/Q.html">Q</a>&nbsp;<a
                                                href="/directory/R.html">R</a>&nbsp;<a
                                                href="/directory/S.html">S</a>&nbsp;<a
                                                href="/directory/T.html">T</a>&nbsp;<a
                                                href="/directory/U.html">U</a>&nbsp;<a
                                                href="/directory/V.html">V</a>&nbsp;<a
                                                href="/directory/W.html">W</a>&nbsp;<a
                                                href="/directory/X.html">X</a>&nbsp;<a
                                                href="/directory/Y.html">Y</a>&nbsp;<a href="/directory/Z.html">Z</a>
                                    </font>
                                </td>
                            </tr>
                        </table>
                    </td>
                </tr>
            </table>
        </center>
    <P>
        <center>
            KEY:<br>
            <img src="/chessimages/chat.gif" width=16 height=16>Kibitzing &nbsp;
            <img src="/chessimages/book.gif" width=16 height=16>Biography &nbsp;
            <img src="/chessimages/speaker.gif" width=16 height=16>Pronunciation
        </center>

    <div class="increaserev bidmcm1200x250"></div>
    <script>ir_ads_push();</script>
    <div class="cgc-ns1 xsm mw-100pct b1s000000 bc-FFFFEE tc-000000 center tcenter tbm10" style="padding:2px;">
        <a href="/index.html">Home</a> |
        <a href="/chessabout.html">About</a> |
        <a href="/perl/chesslogin.pl">Login</a> |
        <a href="/perl/chesslogout.pl">Logout</a> |
        <a href="/chesshelp.html">F.A.Q.</a> |
        <a href="/perl/chessuser">Profile</a> |
        <a href="/perl/chessprofile.pl">Preferences</a> |
        <a href="/perl/chessmembers">Premium&nbsp;Membership</a> |
        <a href="/perl/chessforum.pl">Kibitzer's&nbsp;Caf&eacute;</a> |
        <a href="/perl/bistro.pl">Biographer's&nbsp;Bistro</a> |
        <a href="/perl/chessnew">New&nbsp;Kibitzing</a> |
        <a href="/perl/chessnew?chessforums=1">Chessforums</a> |
        <a href="/perl/tournaments">Tournament Index</a> |
        <a href="/directory/">Player&nbsp;Directory</a> |
        <a href="/perl/goat.pl">Notable&nbsp;Games</a> |
        <a href="/wcc.html">World&nbsp;Chess&nbsp;Championships</a> |
        <a href="/perl/explorer">Opening&nbsp;Explorer</a> |
        <a href="/perl/guessthemove">Guess&nbsp;the&nbsp;Move</a> |
        <a href="/perl/collections">Game&nbsp;Collections</a> |
        <a href="/bookie.html">ChessBookie&nbsp;Game</a> |
        <a href="/perl/challenge">Chessgames Challenge</a> |
        <a href="https://store.chessgames.com">Store</a> |
        <a href="/chessprivacy.html">Privacy&nbsp;Notice</a> |
        <a href="mailto:chess@chessgames.com">Contact&nbsp;Us</a>
    </div>
    <p class="cgc-ns1 center tcenter xxsm tbm5">Copyright 2001-2021, Chessgames Services LLC</p>
    <div class="increaserev bidmcms970x90"></div>
    <script>ir_ads_push();</script>
    <script>
        window.googletag = window.googletag || { cmd: [] };
        var interstitialSlot, staticSlot;
        googletag.cmd.push(function () {
            interstitialSlot = googletag.defineOutOfPageSlot(
                '/21722279357/Interstitial_Tage',
                googletag.enums.OutOfPageFormat.INTERSTITIAL);
            if (interstitialSlot) {
                interstitialSlot.addService(googletag.pubads());
                googletag.pubads().enableSingleRequest();
                googletag.enableServices();
            }
        });
    </script>
    <script>
        googletag.cmd.push(function () {
            googletag.display(interstitialSlot);
        });
    </script>
    <pre>
</pre>
</body>

</html>
'''
    }
