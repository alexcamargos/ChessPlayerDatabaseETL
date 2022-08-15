#!/usr/bin/env python
# encoding: utf-8
#
#  ------------------------------------------------------------------------------
#  Name: http_requester_mock.py
#  Version: 0.0.1
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
#pylint: disable=(too-many-lines


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
!function(f,b,e,v,n,t,s){if(f.fbq)return;n=f.fbq=function(){n.callMethod?
n.callMethod.apply(n,arguments):n.queue.push(arguments)};if(!f._fbq)f._fbq=n;
n.push=n;n.loaded=!0;n.version='2.0';n.queue=[];t=b.createElement(e);t.async=!0;
t.src=v;s=b.getElementsByTagName(e)[0];s.parentNode.insertBefore(t,s)}(window,
document,'script','https://connect.facebook.net/en_US/fbevents.js');
fbq('init', '292563634274827');
fbq('track', 'PageView');
</script>
<noscript><img height="1" width="1" style="display:none"
src="https://www.facebook.com/tr?id=292563634274827&ev=PageView&noscript=1"
/></noscript>
<!-- DO NOT MODIFY -->
<!-- End Facebook Pixel Code -->







		<script type="text/javascript">
                function OpenWin(pagename) {
                        SmallWin = window.open(pagename,'popup','scrollbars,resizable,toolbar=no,height=394,width=412,left=200,top=200');
                        if (window.focus) {
                                SmallWin.focus();
                        }
                }
		</script>




<link rel="stylesheet" type="text/css" href="//cdnjs.cloudflare.com/ajax/libs/cookieconsent2/3.1.0/cookieconsent.min.css" />
<script src="//cdnjs.cloudflare.com/ajax/libs/cookieconsent2/3.1.0/cookieconsent.min.js"></script>
<script>
window.addEventListener("load", function(){
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
})});
</script>


</head>

<body>


<table border="0" cellpadding="0" cellspacing="0" bgcolor="#FFFFFF" width="100%">
<tr>
<td valign="top" align="left" background="/chessimages/header_stripes.gif"><a href="/index.html"><img src="/chessimages/chessgameslogo.png"
style="margin-left:-6px;" width="431" height="60" border="0" alt="chessgames.com"></a></td>

<td width="100%" background="/chessimages/header_stripes.gif" align="right" valign="top"><img src="/chessimages/header_menu.gif"
style="margin-right:-6px;" width="238" height="60" usemap="#navbar" border="0"></td>
</tr>
</table>
<map name="navbar">
<area shape=rect coords="9,21,62,40" href="/index.html">
<area shape=rect coords="65,21,118,40" href="/perl/chessnew">
<area shape=rect coords="121,21,174,40" href="/perl/chessuser">
<area shape=rect coords="177,21,230,40" href="/chesshelp.html">
</map>


<!--beginmenu--><div class="cgc-ns1 xsm w-100pct b1s000000 bc-FFFFEE tc-000000 center tcenter" style="margin-bottom:4px; padding:2px;">
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
 function gtag(){dataLayer.push(arguments);}
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
<table border=0 cellpadding=0 cellspacing=0 width=579><tr><td>
<font face="verdana,arial,helvetica">
<B><font size=+1 color=#663300>CHESS PLAYER DIRECTORY</font></B>
<br>
This is a directory of the most eminent chess players in the database.
</font>
</td></tr></table></center>
<P>

<center>
<table border=0 cellpadding=1 cellspacing=0><tr><td bgcolor=#996633>
<table border=0 cellpadding=5 cellspacing=0>
<tr><td background="/chessimages/highlight_stripes.gif">
<font face="verdana,arial,helvetica"><B>
<font size=+2 color=#CC0000>A</font>&nbsp;<a href="/directory/B.html">B</a>&nbsp;<a href="/directory/C.html">C</a>&nbsp;<a href="/directory/D.html">D</a>&nbsp;<a href="/directory/E.html">E</a>&nbsp;<a href="/directory/F.html">F</a>&nbsp;<a href="/directory/G.html">G</a>&nbsp;<a href="/directory/H.html">H</a>&nbsp;<a href="/directory/I.html">I</a>&nbsp;<a href="/directory/J.html">J</a>&nbsp;<a href="/directory/K.html">K</a>&nbsp;<a href="/directory/L.html">L</a>&nbsp;<a href="/directory/M.html">M</a>&nbsp;<a href="/directory/N.html">N</a>&nbsp;<a href="/directory/O.html">O</a>&nbsp;<a href="/directory/P.html">P</a>&nbsp;<a href="/directory/Q.html">Q</a>&nbsp;<a href="/directory/R.html">R</a>&nbsp;<a href="/directory/S.html">S</a>&nbsp;<a href="/directory/T.html">T</a>&nbsp;<a href="/directory/U.html">U</a>&nbsp;<a href="/directory/V.html">V</a>&nbsp;<a href="/directory/W.html">W</a>&nbsp;<a href="/directory/X.html">X</a>&nbsp;<a href="/directory/Y.html">Y</a>&nbsp;<a href="/directory/Z.html">Z</a>
</font>
</td></tr></table>
</td></tr></table>
</center><br><center>
<table border=0 cellpadding=5 cellspacing=0><tr><td valign=TOP>
<table border=0 cellpadding=2 cellspacing=0 bgcolor=#333333><tr><td valign=TOP>
<table border=0 cellpadding=2 cellspacing=0 width=100%>
<tr bgcolor=#663300>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-1 color=#FFFFFF>highest<br>rating</font></td>
<td colspan=2><font face="verdana,arial,helvetica" size=-1 color=#FFFFFF>&nbsp;&nbsp;&nbsp;&nbsp;player name</font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-1 color=#FFFFFF>Years</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-1 color=#FFFFFF># of<br>Games</font></td>
</tr><tr bgcolor=#FFFFFF>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2400</font></td>
<td><img src="/chessimages/chat.gif" alt="18" width=16 height=16><img src="/chessimages/book.gif" alt="biography" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=67200"><B>AABERG, Anton </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;1991-2012</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;60</font></td></tr>
<tr bgcolor=#FFEEDD>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2542</font></td>
<td><img src="/chessimages/chat.gif" alt="159" width=16 height=16><img src="/chessimages/book.gif" alt="biography" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=35994"><B>AAGAARD, Jacob </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;1991-2021</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;237</font></td></tr>
<tr bgcolor=#FFFFFF>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2334</font></td>
<td>&nbsp;<img src="/chessimages/book.gif" alt="biography" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=151600"><B>AAKANKSHA, Hagawane </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;2014-2019</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;64</font></td></tr>
<tr bgcolor=#FFEEDD>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2311</font></td>
<td><img src="/chessimages/chat.gif" alt="4" width=16 height=16><img src="/chessimages/book.gif" alt="biography" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=16475"><B>AARLAND, Stein Arild </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;1991-2007</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;17</font></td></tr>
<tr bgcolor=#FFFFFF>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2362</font></td>
<td>&nbsp;<img src="/chessimages/book.gif" alt="biography" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=131259"><B>AARON, Deepak </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;2008-2021</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;35</font></td></tr>
<tr bgcolor=#FFEEDD>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2315</font></td>
<td><img src="/chessimages/chat.gif" alt="34" width=16 height=16><img src="/chessimages/book.gif" alt="biography" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=18943"><B>AARON, Manuel </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;1960-1984</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;91</font></td></tr>
<tr bgcolor=#FFFFFF>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2309</font></td>
<td>&nbsp;</td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=158828"><B>AARYAN, Varshney </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;2017-2020</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;42</font></td></tr>
<tr bgcolor=#FFEEDD>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2442</font></td>
<td><img src="/chessimages/chat.gif" alt="2" width=16 height=16><img src="/chessimages/book.gif" alt="biography" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=52307"><B>ABASHEEV, Denis </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;1996-2004</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;21</font></td></tr>
<tr bgcolor=#FFFFFF>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2664</font></td>
<td><img src="/chessimages/chat.gif" alt="12" width=16 height=16><img src="/chessimages/book.gif" alt="biography" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=110381"><B>ABASOV, Nijat </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;2005-2022</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;440</font></td></tr>
<tr bgcolor=#FFEEDD>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2208</font></td>
<td>&nbsp;</td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=104892"><B>ABAYASEKERA, Roger F T </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;1976-2005</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;21</font></td></tr>
<tr bgcolor=#FFFFFF>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2329</font></td>
<td>&nbsp;<img src="/chessimages/book.gif" alt="biography" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=157096"><B>ABBAS, Daniel </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;2016-2019</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;42</font></td></tr>
<tr bgcolor=#FFEEDD>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2305</font></td>
<td>&nbsp;<img src="/chessimages/book.gif" alt="biography" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=43282"><B>ABBASI, Nasser M </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;1988-1994</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;26</font></td></tr>
<tr bgcolor=#FFFFFF>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2506</font></td>
<td><img src="/chessimages/chat.gif" alt="7" width=16 height=16><img src="/chessimages/book.gif" alt="biography" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=58114"><B>ABBASIFAR, Hasan </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;1994-2019</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;32</font></td></tr>
<tr bgcolor=#FFEEDD>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2578</font></td>
<td><img src="/chessimages/chat.gif" alt="6" width=16 height=16><img src="/chessimages/book.gif" alt="biography" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=49449"><B>ABBASOV, Farid </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;1993-2022</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;472</font></td></tr>
<tr bgcolor=#FFFFFF>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2302</font></td>
<td><img src="/chessimages/chat.gif" alt="1" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=114818"><B>ABBASOV, Vusal </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;2008-2017</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;10</font></td></tr>
<tr bgcolor=#FFEEDD>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2259</font></td>
<td><img src="/chessimages/chat.gif" alt="3" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=41457"><B>ABBINK, Michel </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;1992-2002</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;46</font></td></tr>
<tr bgcolor=#FFFFFF>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2335</font></td>
<td>&nbsp;<img src="/chessimages/book.gif" alt="biography" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=131907"><B>ABDALLA, Luiz Guilherme Aurelli </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;2010-2014</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;33</font></td></tr>
<tr bgcolor=#FFEEDD>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2264</font></td>
<td><img src="/chessimages/chat.gif" alt="2" width=16 height=16><img src="/chessimages/book.gif" alt="biography" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=140227"><B>ABDALSALAM, Abubukr </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;2012-2022</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;40</font></td></tr>
<tr bgcolor=#FFFFFF>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2214</font></td>
<td>&nbsp;<img src="/chessimages/book.gif" alt="biography" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=155302"><B>ABDELAZEEZ, Mohamed Abdalla </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;2016-2022</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;26</font></td></tr>
<tr bgcolor=#FFEEDD>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2484</font></td>
<td><img src="/chessimages/chat.gif" alt="3" width=16 height=16><img src="/chessimages/book.gif" alt="biography" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=55370"><B>ABDELNABBI, Imed </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;1984-2019</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;130</font></td></tr>
<tr bgcolor=#FFFFFF>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2397</font></td>
<td>&nbsp;<img src="/chessimages/book.gif" alt="biography" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=158375"><B>ABDISALIMOV, Abdimalik </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;2016-2021</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;42</font></td></tr>
<tr bgcolor=#FFEEDD>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2362</font></td>
<td>&nbsp;</td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=160425"><B>ABDRLAUF, Elham </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;2018-2021</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;43</font></td></tr>
<tr bgcolor=#FFFFFF>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2282</font></td>
<td>&nbsp;<img src="/chessimages/book.gif" alt="biography" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=103206"><B>ABDUL, Majeed Mohamad </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;1989-2009</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;39</font></td></tr>
<tr bgcolor=#FFEEDD>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2264</font></td>
<td>&nbsp;<img src="/chessimages/book.gif" alt="biography" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=120656"><B>ABDUL, Malek Mohammed </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;2004-2009</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;39</font></td></tr>
<tr bgcolor=#FFFFFF>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2320</font></td>
<td>&nbsp;<img src="/chessimages/book.gif" alt="biography" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=121612"><B>ABDULLA, Khayala </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;2008-2021</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;247</font></td></tr>
<tr bgcolor=#FFEEDD>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2316</font></td>
<td>&nbsp;<img src="/chessimages/book.gif" alt="biography" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=156954"><B>ABDULLA, Murad </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;2016-2020</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;59</font></td></tr>
<tr bgcolor=#FFFFFF>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2302</font></td>
<td>&nbsp;</td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=74230"><B>ABDULLAEV, Mahish </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;2000-2004</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;16</font></td></tr>
<tr bgcolor=#FFEEDD>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2357</font></td>
<td><img src="/chessimages/chat.gif" alt="7" width=16 height=16><img src="/chessimages/book.gif" alt="biography" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=109360"><B>ABDULLAH, Hassan </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;1998-2019</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;113</font></td></tr>
<tr bgcolor=#FFFFFF>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2235</font></td>
<td>&nbsp;</td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=39631"><B>ABDULLAH, Mohd Kamal </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;1989-2016</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;18</font></td></tr>
<tr bgcolor=#FFEEDD>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2270</font></td>
<td>&nbsp;<img src="/chessimages/book.gif" alt="biography" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=27816"><B>ABDULLAH, Mansoor </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;1987-2001</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;22</font></td></tr>
<tr bgcolor=#FFFFFF>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2535</font></td>
<td><img src="/chessimages/chat.gif" alt="6" width=16 height=16><img src="/chessimages/book.gif" alt="biography" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=11586"><B>ABDULLAH, Al Rakib Mollah </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;1992-2018</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;272</font></td></tr>
<tr bgcolor=#FFEEDD>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2429</font></td>
<td><img src="/chessimages/chat.gif" alt="1" width=16 height=16><img src="/chessimages/book.gif" alt="biography" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=110379"><B>ABDULOV, Orkhan </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;2003-2019</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;137</font></td></tr>
<tr bgcolor=#FFFFFF>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2346</font></td>
<td><img src="/chessimages/chat.gif" alt="10" width=16 height=16><img src="/chessimages/book.gif" alt="biography" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=127191"><B>ABDULWAHHAB, Ahmed Abdulsattar A </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;2004-2022</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;101</font></td></tr>
<tr bgcolor=#FFEEDD>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2488</font></td>
<td><img src="/chessimages/chat.gif" alt="48" width=16 height=16><img src="/chessimages/book.gif" alt="biography" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=113680"><B>ABDUMALIK, Zhansaya </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;2007-2022</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;531</font></td></tr>
<tr bgcolor=#FFFFFF>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2633</font></td>
<td><img src="/chessimages/chat.gif" alt="107" width=16 height=16><img src="/chessimages/book.gif" alt="biography" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=149949"><B>ABDUSATTOROV, Nodirbek </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;2014-2022</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;691</font></td></tr>
<tr bgcolor=#FFEEDD>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2406</font></td>
<td>&nbsp;<img src="/chessimages/book.gif" alt="biography" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=140131"><B>ABDYJAPAR, Asyl </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;2012-2022</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;121</font></td></tr>
<tr bgcolor=#FFFFFF>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2211</font></td>
<td>&nbsp;</td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=129544"><B>ABEDI, Ali </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;2004-2016</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;16</font></td></tr>
<tr bgcolor=#FFEEDD>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2476</font></td>
<td><img src="/chessimages/chat.gif" alt="2" width=16 height=16><img src="/chessimages/book.gif" alt="biography" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=118413"><B>ABEL, Dennes </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;2006-2019</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;147</font></td></tr>
<tr bgcolor=#FFFFFF>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2430</font></td>
<td>&nbsp;<img src="/chessimages/book.gif" alt="biography" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=116901"><B>ABEL, Lajos </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;1986-2012</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;24</font></td></tr>
<tr bgcolor=#FFEEDD>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2393</font></td>
<td>&nbsp;<img src="/chessimages/book.gif" alt="biography" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=46898"><B>ABELN, Michiel </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;1990-2015</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;87</font></td></tr>
<tr bgcolor=#FFFFFF>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2547</font></td>
<td><img src="/chessimages/chat.gif" alt="8" width=16 height=16><img src="/chessimages/book.gif" alt="biography" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=51933"><B>ABERGEL, Thal </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;1998-2022</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;290</font></td></tr>
<tr bgcolor=#FFEEDD>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2269</font></td>
<td>&nbsp;</td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=131281"><B>ABHILASH, Reddy M L </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;2011-2019</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;39</font></td></tr>
<tr bgcolor=#FFFFFF>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2383</font></td>
<td><img src="/chessimages/chat.gif" alt="1" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=113309"><B>ABHISHEK, Das </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;2007-2018</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;12</font></td></tr>
<tr bgcolor=#FFEEDD>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2422</font></td>
<td>&nbsp;<img src="/chessimages/book.gif" alt="biography" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=117403"><B>ABHISHEK, Kelkar </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;2008-2019</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;101</font></td></tr>
<tr bgcolor=#FFFFFF>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2385</font></td>
<td><img src="/chessimages/chat.gif" alt="4" width=16 height=16><img src="/chessimages/book.gif" alt="biography" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=55445"><B>ABOLIANIN, Arthur </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;1994-2013</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;52</font></td></tr>
<tr bgcolor=#FFEEDD>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2235</font></td>
<td>&nbsp;<img src="/chessimages/book.gif" alt="biography" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=57600"><B>ABOUDI, Marwan </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;1983-2022</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;57</font></td></tr>
<tr bgcolor=#FFFFFF>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;&nbsp;</font></td>
<td><img src="/chessimages/chat.gif" alt="41" width=16 height=16><img src="/chessimages/book.gif" alt="biography" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=23883"><B>ABRAHAMS, Gerald </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;1923-1963</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;182</font></td></tr>
<tr bgcolor=#FFEEDD>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2397</font></td>
<td><img src="/chessimages/chat.gif" alt="29" width=16 height=16><img src="/chessimages/book.gif" alt="biography" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=57342"><B>ABRAHAMYAN, Tatev </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;1998-2022</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;476</font></td></tr>
<tr bgcolor=#FFFFFF>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;&nbsp;</font></td>
<td><img src="/chessimages/chat.gif" alt="2" width=16 height=16><img src="/chessimages/book.gif" alt="biography" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=43478"><B>ABRAMOV, Lev Yakovlevich </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;1930-1975</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;49</font></td></tr>
<tr bgcolor=#FFEEDD>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2524</font></td>
<td><img src="/chessimages/chat.gif" alt="18" width=16 height=16><img src="/chessimages/book.gif" alt="biography" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=15490"><B>ABRAMOVIC, Bosko </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;1973-2021</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;567</font></td></tr>
<tr bgcolor=#FFFFFF>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2221</font></td>
<td><img src="/chessimages/chat.gif" alt="1" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=16423"><B>ABRAMSON, Horacio </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;1978-1996</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;11</font></td></tr>
<tr bgcolor=#FFEEDD>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2327</font></td>
<td>&nbsp;<img src="/chessimages/book.gif" alt="biography" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=13948"><B>ABRAVANEL, Chely </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;1983-1994</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;36</font></td></tr>
<tr bgcolor=#FFFFFF>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2237</font></td>
<td>&nbsp;</td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=151461"><B>ABREKOV, Mussa </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;2014-2022</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;25</font></td></tr>
<tr bgcolor=#FFEEDD>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2397</font></td>
<td><img src="/chessimages/chat.gif" alt="1" width=16 height=16><img src="/chessimages/book.gif" alt="biography" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=100847"><B>ABRIL, Ramon Jose </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;1995-2001</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;11</font></td></tr>
<tr bgcolor=#FFFFFF>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2241</font></td>
<td><img src="/chessimages/chat.gif" alt="193" width=16 height=16><img src="/chessimages/book.gif" alt="biography" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=73320"><B>ACERS, Jude </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;1960-2013</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;36</font></td></tr>
<tr bgcolor=#FFEEDD>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2395</font></td>
<td><img src="/chessimages/chat.gif" alt="7" width=16 height=16><img src="/chessimages/book.gif" alt="biography" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=88873"><B>ACEVEDO, Cristobal Jose Blanco </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;1993-2021</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;69</font></td></tr>
<tr bgcolor=#FFFFFF>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2381</font></td>
<td>&nbsp;</td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=114319"><B>ACHER, Mathieu </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;1999-2009</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;21</font></td></tr>
<tr bgcolor=#FFEEDD>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2367</font></td>
<td>&nbsp;<img src="/chessimages/book.gif" alt="biography" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=102977"><B>ACKERMANN, Hans Werner </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;1976-2017</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;51</font></td></tr>
<tr bgcolor=#FFFFFF>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2344</font></td>
<td><img src="/chessimages/chat.gif" alt="1" width=16 height=16><img src="/chessimages/book.gif" alt="biography" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=43238"><B>ACOSTA, Alejandro </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;1978-2015</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;21</font></td></tr>
<tr bgcolor=#FFEEDD>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2502</font></td>
<td><img src="/chessimages/chat.gif" alt="8" width=16 height=16><img src="/chessimages/book.gif" alt="biography" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=49567"><B>ACOSTA, Bernal Gonzalez </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;1978-2018</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;153</font></td></tr>
<tr bgcolor=#FFFFFF>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2465</font></td>
<td><img src="/chessimages/chat.gif" alt="1" width=16 height=16><img src="/chessimages/book.gif" alt="biography" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=151731"><B>ACOSTA, Pablo Ismael </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;2014-2020</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;64</font></td></tr>
<tr bgcolor=#FFEEDD>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2527</font></td>
<td>&nbsp;<img src="/chessimages/book.gif" alt="biography" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=44769"><B>ACOSTA, Diasmany Otero </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;1996-2019</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;66</font></td></tr>
<tr bgcolor=#FFFFFF>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2607</font></td>
<td><img src="/chessimages/chat.gif" alt="19" width=16 height=16><img src="/chessimages/book.gif" alt="biography" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=31033"><B>ACS, Peter </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;1992-2022</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;442</font></td></tr>
<tr bgcolor=#FFEEDD>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2480</font></td>
<td><img src="/chessimages/chat.gif" alt="4" width=16 height=16><img src="/chessimages/book.gif" alt="biography" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=27727"><B>DE ACUNA, Jose Luis Vilela </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;1972-2015</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;193</font></td></tr>
<tr bgcolor=#FFFFFF>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2573</font></td>
<td><img src="/chessimages/chat.gif" alt="2" width=16 height=16><img src="/chessimages/book.gif" alt="biography" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=139197"><B>ACZEL, Gergely </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;2012-2022</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;112</font></td></tr>
<tr bgcolor=#FFEEDD>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2492</font></td>
<td><img src="/chessimages/chat.gif" alt="3" width=16 height=16><img src="/chessimages/book.gif" alt="biography" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=113772"><B>ADAIR, James R </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;2007-2019</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;187</font></td></tr>
<tr bgcolor=#FFFFFF>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2382</font></td>
<td>&nbsp;<img src="/chessimages/book.gif" alt="biography" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=134400"><B>ADAMEK, Jiri </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;2000-2017</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;29</font></td></tr>
<tr bgcolor=#FFEEDD>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2294</font></td>
<td>&nbsp;</td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=62159"><B>ADAMEK, Zdenek </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;1992-1995</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;16</font></td></tr>
<tr bgcolor=#FFFFFF>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2258</font></td>
<td>&nbsp;</td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=27341"><B>ADAMS, Nick A </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;1984-2011</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;57</font></td></tr>
<tr bgcolor=#FFEEDD>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2211</font></td>
<td>&nbsp;<img src="/chessimages/book.gif" alt="biography" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=88727"><B>ADAMS, William Bermudez </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;2004-2008</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;23</font></td></tr>
<tr bgcolor=#FFFFFF>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2234</font></td>
<td><img src="/chessimages/chat.gif" alt="4" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=52175"><B>ADAMS, David M </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;1978-2007</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;34</font></td></tr>
<tr bgcolor=#FFEEDD>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2761</font></td>
<td><img src="/chessimages/chat.gif" alt="1824" width=16 height=16><img src="/chessimages/book.gif" alt="biography" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=10900"><B>ADAMS, Michael </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;1984-2022</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;3,098</font></td></tr>
<tr bgcolor=#FFFFFF>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;&nbsp;</font></td>
<td><img src="/chessimages/chat.gif" alt="56" width=16 height=16><img src="/chessimages/book.gif" alt="biography" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=42883"><B>ADAMS, Weaver </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;1936-1958</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;223</font></td></tr>
<tr bgcolor=#FFEEDD>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2275</font></td>
<td><img src="/chessimages/chat.gif" alt="1" width=16 height=16><img src="/chessimages/book.gif" alt="biography" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=47874"><B>ADAMSKI, Andrzej </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;1961-1998</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;71</font></td></tr>
<tr bgcolor=#FFFFFF>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2470</font></td>
<td><img src="/chessimages/chat.gif" alt="6" width=16 height=16><img src="/chessimages/book.gif" alt="biography" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=71158"><B>ADAMSKI, Jan </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;1962-2021</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;1,324</font></td></tr>
<tr bgcolor=#FFEEDD>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2354</font></td>
<td><img src="/chessimages/chat.gif" alt="13" width=16 height=16><img src="/chessimages/book.gif" alt="biography" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=19345"><B>ADAMSON, Robby </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;1989-2021</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;87</font></td></tr>
<tr bgcolor=#FFFFFF>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2343</font></td>
<td><img src="/chessimages/chat.gif" alt="1" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=53574"><B>ADAN, Carlos Mate </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;1997-2012</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;19</font></td></tr>
<tr bgcolor=#FFEEDD>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2266</font></td>
<td><img src="/chessimages/chat.gif" alt="2" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=50416"><B>ADDISON, Bret C </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;2001-2016</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;76</font></td></tr>
<tr bgcolor=#FFFFFF>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2490</font></td>
<td><img src="/chessimages/chat.gif" alt="29" width=16 height=16><img src="/chessimages/book.gif" alt="biography" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=26628"><B>ADDISON, William </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;1950-1970</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;173</font></td></tr>
<tr bgcolor=#FFEEDD>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2272</font></td>
<td>&nbsp;<img src="/chessimages/book.gif" alt="biography" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=91160"><B>ADEBAYO, Adegboyega </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;2003-2022</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;34</font></td></tr>
<tr bgcolor=#FFFFFF>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2245</font></td>
<td><img src="/chessimages/chat.gif" alt="1" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=119901"><B>ADELBERG, David </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;2008-2012</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;17</font></td></tr>
<tr bgcolor=#FFEEDD>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2352</font></td>
<td><img src="/chessimages/chat.gif" alt="2" width=16 height=16><img src="/chessimages/book.gif" alt="biography" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=79592"><B>ADERITO, Pedro </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;1995-2016</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;59</font></td></tr>
<tr bgcolor=#FFFFFF>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2287</font></td>
<td>&nbsp;<img src="/chessimages/book.gif" alt="biography" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=140382"><B>ADESINA, Adeyinka </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;2012-2016</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;17</font></td></tr>
<tr bgcolor=#FFEEDD>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2272</font></td>
<td>&nbsp;<img src="/chessimages/book.gif" alt="biography" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=79264"><B>ADHAMI, Vangjel </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;1970-2002</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;22</font></td></tr>
<tr bgcolor=#FFFFFF>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2689</font></td>
<td><img src="/chessimages/chat.gif" alt="54" width=16 height=16><img src="/chessimages/book.gif" alt="biography" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=117280"><B>ADHIBAN, Baskaran </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;2006-2022</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;906</font></td></tr>
<tr bgcolor=#FFEEDD>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2634</font></td>
<td><img src="/chessimages/chat.gif" alt="33" width=16 height=16><img src="/chessimages/book.gif" alt="biography" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=16249"><B>ADIANTO, Utut </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;1980-2016</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;751</font></td></tr>
<tr bgcolor=#FFFFFF>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2438</font></td>
<td><img src="/chessimages/chat.gif" alt="4" width=16 height=16><img src="/chessimages/book.gif" alt="biography" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=155275"><B>ADITYA, Mittal </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;2016-2021</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;281</font></td></tr>
<tr bgcolor=#FFEEDD>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2514</font></td>
<td><img src="/chessimages/chat.gif" alt="4" width=16 height=16><img src="/chessimages/book.gif" alt="biography" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=39754"><B>ADLA, Diego Gustavo </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;1986-2020</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;148</font></td></tr>
<tr bgcolor=#FFFFFF>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2221</font></td>
<td>&nbsp;</td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=48423"><B>ADLER, Bo </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;1975-2017</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;60</font></td></tr>
<tr bgcolor=#FFEEDD>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2342</font></td>
<td>&nbsp;<img src="/chessimages/book.gif" alt="biography" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=22345"><B>ADLER, Joel </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;1984-2006</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;43</font></td></tr>
<tr bgcolor=#FFFFFF>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2440</font></td>
<td>&nbsp;<img src="/chessimages/book.gif" alt="biography" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=26779"><B>ADLER, Viktor </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;1963-2005</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;37</font></td></tr>
<tr bgcolor=#FFEEDD>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2640</font></td>
<td><img src="/chessimages/chat.gif" alt="42" width=16 height=16><img src="/chessimages/book.gif" alt="biography" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=49127"><B>ADLY, Ahmed </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;1997-2022</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;737</font></td></tr>
<tr bgcolor=#FFFFFF>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2510</font></td>
<td><img src="/chessimages/chat.gif" alt="11" width=16 height=16><img src="/chessimages/book.gif" alt="biography" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=117715"><B>ADMIRAAL, Miguoel </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;2008-2021</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;181</font></td></tr>
<tr bgcolor=#FFEEDD>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2455</font></td>
<td>&nbsp;<img src="/chessimages/book.gif" alt="biography" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=61215"><B>ADNANI, Mokliss El </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;1994-2021</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;90</font></td></tr>
<tr bgcolor=#FFFFFF>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2312</font></td>
<td>&nbsp;<img src="/chessimages/book.gif" alt="biography" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=52930"><B>ADNOY, Hallvard Voll </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;2000-2009</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;37</font></td></tr>
<tr bgcolor=#FFEEDD>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2565</font></td>
<td><img src="/chessimages/chat.gif" alt="136" width=16 height=16><img src="/chessimages/book.gif" alt="biography" width=16 height=16><a href="/audio/14589.mp3"><img src="/chessimages/speaker.gif" alt="pronunciation" width=16 height=16 border=0></a></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=14589"><B>ADORJAN, Andras </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;1963-2000</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;1,594</font></td></tr>
<tr bgcolor=#FFFFFF>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2391</font></td>
<td><img src="/chessimages/chat.gif" alt="2" width=16 height=16><img src="/chessimages/book.gif" alt="biography" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=24043"><B>ADRIAN, Claude </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;1985-2019</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;132</font></td></tr>
<tr bgcolor=#FFEEDD>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2312</font></td>
<td><img src="/chessimages/chat.gif" alt="2" width=16 height=16><img src="/chessimages/book.gif" alt="biography" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=10184"><B>ADU, Oladapo Oluto </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;1998-2020</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;97</font></td></tr>
<tr bgcolor=#FFFFFF>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2412</font></td>
<td>&nbsp;<img src="/chessimages/book.gif" alt="biography" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=27489"><B>ADY, Jonathan </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;1981-1999</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;69</font></td></tr>
<tr bgcolor=#FFEEDD>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2209</font></td>
<td><img src="/chessimages/chat.gif" alt="1" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=120959"><B>AERNI, Andreas </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;2009-2013</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;36</font></td></tr>
<tr bgcolor=#FFFFFF>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2508</font></td>
<td><img src="/chessimages/chat.gif" alt="4" width=16 height=16><img src="/chessimages/book.gif" alt="biography" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=141302"><B>AFANASIEV, Nikita </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;2012-2022</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;451</font></td></tr>
<tr bgcolor=#FFEEDD>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2381</font></td>
<td><img src="/chessimages/chat.gif" alt="23" width=16 height=16><img src="/chessimages/book.gif" alt="biography" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=19657"><B>AFEK, Yochanan </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;1977-2015</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;409</font></td></tr>
<tr bgcolor=#FFFFFF>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2405</font></td>
<td><img src="/chessimages/chat.gif" alt="21" width=16 height=16><img src="/chessimages/book.gif" alt="biography" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=24656"><B>AFIFI, Assem Abdel Razik </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;1980-2001</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;102</font></td></tr>
<tr bgcolor=#FFEEDD>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2303</font></td>
<td>&nbsp;<img src="/chessimages/book.gif" alt="biography" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=155682"><B>AFONASIEVA, Anna </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;2016-2022</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;117</font></td></tr>
<tr bgcolor=#FFFFFF>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2205</font></td>
<td>&nbsp;</td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=103462"><B>AFRIANY, Valery </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;1990-2006</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;20</font></td></tr>
<tr bgcolor=#FFEEDD>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2646</font></td>
<td><img src="/chessimages/chat.gif" alt="144" width=16 height=16><img src="/chessimages/book.gif" alt="biography" width=16 height=16><a href="/audio/66272.mp3"><img src="/chessimages/speaker.gif" alt="pronunciation" width=16 height=16 border=0></a></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=66272"><B>AFROMEEV, Vladimir </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;2000-2007</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;30</font></td></tr>
<tr bgcolor=#FFFFFF>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2248</font></td>
<td>&nbsp;<img src="/chessimages/book.gif" alt="biography" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=58553"><B>AFSHARI, Mohammadreza </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;2001-2018</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;21</font></td></tr>
<tr bgcolor=#FFEEDD>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2241</font></td>
<td><img src="/chessimages/chat.gif" alt="2" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=53827"><B>AFTSOGLOU, Ioannis </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;2000-2012</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;15</font></td></tr>
<tr bgcolor=#FFFFFF>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2362</font></td>
<td><img src="/chessimages/chat.gif" alt="4" width=16 height=16><img src="/chessimages/book.gif" alt="biography" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=57478"><B>AGABABEAN, Naira </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;1979-2017</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;59</font></td></tr>
<tr bgcolor=#FFEEDD>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2356</font></td>
<td>&nbsp;<img src="/chessimages/book.gif" alt="biography" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=56828"><B>AGAFII, Victor </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;1999-2015</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;19</font></td></tr>
<tr bgcolor=#FFFFFF>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2395</font></td>
<td><img src="/chessimages/chat.gif" alt="1" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=29304"><B>AGAPOV, Konstantin </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;1983-1987</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;20</font></td></tr>
<tr bgcolor=#FFEEDD>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2502</font></td>
<td><img src="/chessimages/chat.gif" alt="3" width=16 height=16><img src="/chessimages/book.gif" alt="biography" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=80801"><B>AGARAGIMOV, Djakhangir </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;2003-2012</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;43</font></td></tr>
<tr bgcolor=#FFFFFF>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2276</font></td>
<td><img src="/chessimages/chat.gif" alt="7" width=16 height=16><img src="/chessimages/book.gif" alt="biography" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=40301"><B>AGDAMUS, Jose Luis </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;1970-1995</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;29</font></td></tr>
<tr bgcolor=#FFEEDD>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2402</font></td>
<td><img src="/chessimages/chat.gif" alt="3" width=16 height=16><img src="/chessimages/book.gif" alt="biography" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=20754"><B>AGDESTEIN, Espen </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;1982-2004</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;33</font></td></tr>
<tr bgcolor=#FFFFFF>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2637</font></td>
<td><img src="/chessimages/chat.gif" alt="168" width=16 height=16><img src="/chessimages/book.gif" alt="biography" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=14040"><B>AGDESTEIN, Simen </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;1981-2021</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;777</font></td></tr>
<tr bgcolor=#FFEEDD>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2402</font></td>
<td><img src="/chessimages/chat.gif" alt="4" width=16 height=16><img src="/chessimages/book.gif" alt="biography" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=40981"><B>AGEICHENKO, Genadi A </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;1966-2019</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;112</font></td></tr>
<tr bgcolor=#FFFFFF>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2246</font></td>
<td>&nbsp;</td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=66541"><B>AGER, Josef </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;1998-2017</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;28</font></td></tr>
<tr bgcolor=#FFEEDD>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2357</font></td>
<td><img src="/chessimages/chat.gif" alt="3" width=16 height=16><img src="/chessimages/book.gif" alt="biography" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=117750"><B>AGGELIS, Nikolaos </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;2006-2015</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;25</font></td></tr>
<tr bgcolor=#FFFFFF>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2218</font></td>
<td><img src="/chessimages/chat.gif" alt="3" width=16 height=16><img src="/chessimages/book.gif" alt="biography" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=106327"><B>AGHABEKIAN, Liana </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;2001-2018</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;38</font></td></tr>
<tr bgcolor=#FFEEDD>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2523</font></td>
<td><img src="/chessimages/chat.gif" alt="3" width=16 height=16><img src="/chessimages/book.gif" alt="biography" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=98974"><B>AGHAMALIYEV, Cemil </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;1991-2019</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;82</font></td></tr>
<tr bgcolor=#FFFFFF>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2537</font></td>
<td><img src="/chessimages/chat.gif" alt="2" width=16 height=16><img src="/chessimages/book.gif" alt="biography" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=113373"><B>AGHASARYAN, Robert </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;2004-2018</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;91</font></td></tr>
<tr bgcolor=#FFEEDD>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2441</font></td>
<td><img src="/chessimages/chat.gif" alt="1" width=16 height=16><img src="/chessimages/book.gif" alt="biography" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=110393"><B>AGHASIYEV, Kamal </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;2007-2017</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;26</font></td></tr>
<tr bgcolor=#FFFFFF>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2209</font></td>
<td>&nbsp;<img src="/chessimages/book.gif" alt="biography" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=126941"><B>AGHASIYEVA, Fidan </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;2001-2019</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;24</font></td></tr>
<tr bgcolor=#FFEEDD>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2424</font></td>
<td>&nbsp;<img src="/chessimages/book.gif" alt="biography" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=131797"><B>AGHAYEV, Miragha </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;2011-2021</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;32</font></td></tr>
<tr bgcolor=#FFFFFF>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2407</font></td>
<td>&nbsp;<img src="/chessimages/book.gif" alt="biography" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=80806"><B>AGHAYEV, Nijat </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;2001-2017</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;68</font></td></tr>
<tr bgcolor=#FFEEDD>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2413</font></td>
<td>&nbsp;</td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=161575"><B>AGIBILEG, Uurtsaikh </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;2014-2020</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;16</font></td></tr>
<tr bgcolor=#FFFFFF>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2380</font></td>
<td><img src="/chessimages/chat.gif" alt="12" width=16 height=16><img src="/chessimages/book.gif" alt="biography" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=50078"><B>AGINIAN, Nelly </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;1996-2012</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;200</font></td></tr>
<tr bgcolor=#FFEEDD>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2407</font></td>
<td>&nbsp;<img src="/chessimages/book.gif" alt="biography" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=154678"><B>AGMANOV, Zhandos </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;2016-2021</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;88</font></td></tr>
<tr bgcolor=#FFFFFF>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2229</font></td>
<td><img src="/chessimages/chat.gif" alt="3" width=16 height=16><img src="/chessimages/book.gif" alt="biography" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=88823"><B>AGNELO, Amorim </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;1998-2014</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;45</font></td></tr>
<tr bgcolor=#FFEEDD>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2465</font></td>
<td><img src="/chessimages/chat.gif" alt="3" width=16 height=16><img src="/chessimages/book.gif" alt="biography" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=49862"><B>AGOPOV, Mikael </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;1990-2021</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;356</font></td></tr>
<tr bgcolor=#FFFFFF>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2314</font></td>
<td>&nbsp;<img src="/chessimages/book.gif" alt="biography" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=151570"><B>AGRAWAL, Vantika </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;2014-2022</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;223</font></td></tr>
<tr bgcolor=#FFEEDD>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2616</font></td>
<td><img src="/chessimages/chat.gif" alt="17" width=16 height=16><img src="/chessimages/book.gif" alt="biography" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=18229"><B>AGREST, Evgenij </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;1980-2021</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;702</font></td></tr>
<tr bgcolor=#FFFFFF>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2314</font></td>
<td><img src="/chessimages/chat.gif" alt="2" width=16 height=16><img src="/chessimages/book.gif" alt="biography" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=96112"><B>AGREST, Inna </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;2005-2022</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;392</font></td></tr>
<tr bgcolor=#FFEEDD>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2276</font></td>
<td><img src="/chessimages/chat.gif" alt="2" width=16 height=16><img src="/chessimages/book.gif" alt="biography" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=52426"><B>AGREST, Svetlana </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;1995-2009</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;81</font></td></tr>
<tr bgcolor=#FFFFFF>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2365</font></td>
<td><img src="/chessimages/chat.gif" alt="1" width=16 height=16><img src="/chessimages/book.gif" alt="biography" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=78384"><B>AGUADO, Enrique Fernandez </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;1985-2012</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;98</font></td></tr>
<tr bgcolor=#FFEEDD>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2329</font></td>
<td><img src="/chessimages/chat.gif" alt="1" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=82846"><B>AGUADO, Juan Luis Fernandez </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;1984-2004</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;39</font></td></tr>
<tr bgcolor=#FFFFFF>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2321</font></td>
<td><img src="/chessimages/chat.gif" alt="1" width=16 height=16><img src="/chessimages/book.gif" alt="biography" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=106959"><B>AGUADO, Joan Martorell </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;2004-2006</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;3</font></td></tr>
<tr bgcolor=#FFEEDD>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2443</font></td>
<td><img src="/chessimages/chat.gif" alt="1" width=16 height=16><img src="/chessimages/book.gif" alt="biography" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=107925"><B>AGUETTAZ, Maxime </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;2003-2015</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;44</font></td></tr>
<tr bgcolor=#FFFFFF>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2262</font></td>
<td><img src="/chessimages/chat.gif" alt="1" width=16 height=16><img src="/chessimages/book.gif" alt="biography" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=123759"><B>AGUILA, Gustavo </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;1978-2008</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;9</font></td></tr>
<tr bgcolor=#FFEEDD>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2331</font></td>
<td>&nbsp;<img src="/chessimages/book.gif" alt="biography" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=81302"><B>AGUILAR, Andres </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;2001-2019</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;39</font></td></tr>
<tr bgcolor=#FFFFFF>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2368</font></td>
<td>&nbsp;<img src="/chessimages/book.gif" alt="biography" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=81976"><B>AGUILAR, Guillermo Dominguez </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;2003-2022</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;37</font></td></tr>
<tr bgcolor=#FFEEDD>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2254</font></td>
<td>&nbsp;<img src="/chessimages/book.gif" alt="biography" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=20928"><B>AGUILAR, Juan </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;1987-1996</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;17</font></td></tr>
<tr bgcolor=#FFFFFF>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2301</font></td>
<td>&nbsp;<img src="/chessimages/book.gif" alt="biography" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=155293"><B>AGUILAR, Luis Miguel </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;2016-2018</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;19</font></td></tr>
<tr bgcolor=#FFEEDD>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2339</font></td>
<td>&nbsp;<img src="/chessimages/book.gif" alt="biography" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=129674"><B>AGUILAR, Pablo Alexander Ruiz </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;2000-2012</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;21</font></td></tr>
<tr bgcolor=#FFFFFF>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2238</font></td>
<td><img src="/chessimages/chat.gif" alt="1" width=16 height=16><img src="/chessimages/book.gif" alt="biography" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=129673"><B>AGUILERA, Antonio Rodriguez </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;1991-2008</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;13</font></td></tr>
<tr bgcolor=#FFEEDD>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2347</font></td>
<td>&nbsp;<img src="/chessimages/book.gif" alt="biography" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=58302"><B>AGUIRRE, Manuel Abarca </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;1982-2003</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;78</font></td></tr>
<tr bgcolor=#FFFFFF>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2281</font></td>
<td><img src="/chessimages/chat.gif" alt="1" width=16 height=16><img src="/chessimages/book.gif" alt="biography" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=131806"><B>AGUSTENCH, Eduard Lopez </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;1987-2011</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;4</font></td></tr>
<tr bgcolor=#FFEEDD>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2315</font></td>
<td>&nbsp;<img src="/chessimages/book.gif" alt="biography" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=131912"><B>AGUSTSSON, Johannes </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;1986-1998</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;17</font></td></tr>
<tr bgcolor=#FFFFFF>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2590</font></td>
<td><img src="/chessimages/chat.gif" alt="16" width=16 height=16><img src="/chessimages/book.gif" alt="biography" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=16887"><B>AGZAMOV, Georgy </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;1973-1986</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;202</font></td></tr>
<tr bgcolor=#FFEEDD>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2255</font></td>
<td>&nbsp;<img src="/chessimages/book.gif" alt="biography" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=62594"><B>AGZAMOV, Viacheslav </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;1967-2016</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;25</font></td></tr>
<tr bgcolor=#FFFFFF>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2367</font></td>
<td>&nbsp;<img src="/chessimages/book.gif" alt="biography" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=120089"><B>AHARON, Ofir </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;2008-2022</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;92</font></td></tr>
<tr bgcolor=#FFEEDD>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2446</font></td>
<td><img src="/chessimages/chat.gif" alt="3" width=16 height=16><img src="/chessimages/book.gif" alt="biography" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=67199"><B>AHLANDER, Bjorn </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;1980-2021</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;147</font></td></tr>
<tr bgcolor=#FFFFFF>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2206</font></td>
<td>&nbsp;</td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=159022"><B>AHLUWALIA, Amardip </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;2017-2018</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;26</font></td></tr>
<tr bgcolor=#FFEEDD>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2335</font></td>
<td>&nbsp;<img src="/chessimages/book.gif" alt="biography" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=128025"><B>AHMAD, Al Khatib </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;2010-2022</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;64</font></td></tr>
<tr bgcolor=#FFFFFF>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2354</font></td>
<td>&nbsp;</td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=150793"><B>AHMAD, Ali Syed </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;2014-2016</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;22</font></td></tr>
<tr bgcolor=#FFEEDD>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2460</font></td>
<td><img src="/chessimages/chat.gif" alt="1" width=16 height=16><img src="/chessimages/book.gif" alt="biography" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=87973"><B>AHMADINIA, Ebrahim </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;2002-2019</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;58</font></td></tr>
<tr bgcolor=#FFFFFF>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2431</font></td>
<td>&nbsp;<img src="/chessimages/book.gif" alt="biography" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=154706"><B>AHMADZADA, Ahmad </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;2016-2022</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;186</font></td></tr>
<tr bgcolor=#FFEEDD>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2360</font></td>
<td>&nbsp;<img src="/chessimages/book.gif" alt="biography" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=140129"><B>AHMED, Ali Layth </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;2007-2022</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;36</font></td></tr>
<tr bgcolor=#FFFFFF>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2408</font></td>
<td><img src="/chessimages/chat.gif" alt="3" width=16 height=16><img src="/chessimages/book.gif" alt="biography" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=58580"><B>AHMED, Esam Aly </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;1994-2003</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;46</font></td></tr>
<tr bgcolor=#FFEEDD>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2296</font></td>
<td>&nbsp;</td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=102609"><B>AHMED, Haseeb </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;2000-2012</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;24</font></td></tr>
<tr bgcolor=#FFFFFF>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2379</font></td>
<td><img src="/chessimages/chat.gif" alt="1" width=16 height=16><img src="/chessimages/book.gif" alt="biography" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=88809"><B>AHMED, Sheikh Nasir </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;2001-2018</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;73</font></td></tr>
<tr bgcolor=#FFEEDD>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2347</font></td>
<td><img src="/chessimages/chat.gif" alt="7" width=16 height=16><img src="/chessimages/book.gif" alt="biography" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=52719"><B>AHN, Martin </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;1992-2020</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;94</font></td></tr>
<tr bgcolor=#FFFFFF>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;&nbsp;</font></td>
<td><img src="/chessimages/chat.gif" alt="27" width=16 height=16><img src="/chessimages/book.gif" alt="biography" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=10671"><B>AHUES, Carl </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;1908-1949</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;267</font></td></tr>
<tr bgcolor=#FFEEDD>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2342</font></td>
<td>&nbsp;<img src="/chessimages/book.gif" alt="biography" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=139698"><B>AHVENJARVI, Jani </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;2012-2019</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;59</font></td></tr>
<tr bgcolor=#FFFFFF>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2298</font></td>
<td><img src="/chessimages/chat.gif" alt="14" width=16 height=16><img src="/chessimages/book.gif" alt="biography" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=75473"><B>AIGNER, Michael </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;1999-2008</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;32</font></td></tr>
<tr bgcolor=#FFEEDD>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2305</font></td>
<td><img src="/chessimages/chat.gif" alt="6" width=16 height=16><img src="/chessimages/book.gif" alt="biography" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=11462"><B>AIKHOJE, Odion </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;1998-2009</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;58</font></td></tr>
<tr bgcolor=#FFFFFF>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2502</font></td>
<td>&nbsp;<img src="/chessimages/book.gif" alt="biography" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=125222"><B>AIRAPETIAN, Gor </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;2003-2020</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;115</font></td></tr>
<tr bgcolor=#FFEEDD>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2268</font></td>
<td>&nbsp;<img src="/chessimages/book.gif" alt="biography" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=105117"><B>AIRAPETIAN, Tatevik </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;2004-2007</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;30</font></td></tr>
<tr bgcolor=#FFFFFF>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2457</font></td>
<td><img src="/chessimages/chat.gif" alt="2" width=16 height=16><img src="/chessimages/book.gif" alt="biography" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=120098"><B>AITBAYEV, Aslan </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;2008-2022</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;83</font></td></tr>
<tr bgcolor=#FFEEDD>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2276</font></td>
<td><img src="/chessimages/chat.gif" alt="1" width=16 height=16><img src="/chessimages/book.gif" alt="biography" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=95795"><B>AITHMIDOU, Mohamed-Mehdi </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;2004-2018</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;28</font></td></tr>
<tr bgcolor=#FFFFFF>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;&nbsp;</font></td>
<td><img src="/chessimages/chat.gif" alt="31" width=16 height=16><img src="/chessimages/book.gif" alt="biography" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=47707"><B>AITKEN, James Macrae </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;1932-1977</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;291</font></td></tr>
<tr bgcolor=#FFEEDD>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2252</font></td>
<td>&nbsp;<img src="/chessimages/book.gif" alt="biography" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=156252"><B>AIZENBERG, Benny </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;2016-2022</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;33</font></td></tr>
<tr bgcolor=#FFFFFF>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2369</font></td>
<td>&nbsp;</td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=90350"><B>AIZPURUA, Jose Maria Olano </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;1998-1999</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;15</font></td></tr>
<tr bgcolor=#FFEEDD>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2345</font></td>
<td>&nbsp;<img src="/chessimages/book.gif" alt="biography" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=127240"><B>AIZPURUA, Patrick </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;2010-2019</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;37</font></td></tr>
<tr bgcolor=#FFFFFF>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2315</font></td>
<td>&nbsp;<img src="/chessimages/book.gif" alt="biography" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=158829"><B>AJAY, Karthikeyan </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;2017-2019</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;27</font></td></tr>
<tr bgcolor=#FFEEDD>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2201</font></td>
<td><img src="/chessimages/chat.gif" alt="1" width=16 height=16><img src="/chessimages/book.gif" alt="biography" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=127350"><B>AJIBOWO, Olamide Patrick </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;2010-2017</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;23</font></td></tr>
<tr bgcolor=#FFFFFF>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2443</font></td>
<td>&nbsp;<img src="/chessimages/book.gif" alt="biography" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=125588"><B>AJRAPETIAN, Gevorg </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;2005-2016</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;51</font></td></tr>
<tr bgcolor=#FFEEDD>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2537</font></td>
<td><img src="/chessimages/chat.gif" alt="7" width=16 height=16><img src="/chessimages/book.gif" alt="biography" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=87001"><B>AJRAPETJAN, Yuriy </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;2001-2014</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;83</font></td></tr>
<tr bgcolor=#FFFFFF>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2240</font></td>
<td>&nbsp;</td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=127942"><B>AJVAZI, Ramadan </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;2008-2017</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;34</font></td></tr>
<tr bgcolor=#FFEEDD>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2504</font></td>
<td><img src="/chessimages/chat.gif" alt="10" width=16 height=16><img src="/chessimages/book.gif" alt="biography" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=76737"><B>AKBAEV, Kazbek </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;1998-2013</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;51</font></td></tr>
<tr bgcolor=#FFFFFF>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2413</font></td>
<td><img src="/chessimages/chat.gif" alt="9" width=16 height=16><img src="/chessimages/book.gif" alt="biography" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=51278"><B>AKBARINIA, Sayed Arash </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;1996-2014</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;44</font></td></tr>
<tr bgcolor=#FFEEDD>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2278</font></td>
<td>&nbsp;</td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=104935"><B>AKDAG, Dara </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;2006-2021</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;38</font></td></tr>
<tr bgcolor=#FFFFFF>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2346</font></td>
<td><img src="/chessimages/chat.gif" alt="9" width=16 height=16><img src="/chessimages/book.gif" alt="biography" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=50756"><B>AKESSON, Joel </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;1998-2017</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;55</font></td></tr>
<tr bgcolor=#FFEEDD>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2494</font></td>
<td><img src="/chessimages/chat.gif" alt="5" width=16 height=16><img src="/chessimages/book.gif" alt="biography" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=21594"><B>AKESSON, Ralf </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;1978-2021</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;747</font></td></tr>
<tr bgcolor=#FFFFFF>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2330</font></td>
<td><img src="/chessimages/chat.gif" alt="11" width=16 height=16><img src="/chessimages/book.gif" alt="biography" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=51296"><B>AKETAYEVA, Dana </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;2001-2009</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;61</font></td></tr>
<tr bgcolor=#FFEEDD>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2302</font></td>
<td>&nbsp;<img src="/chessimages/book.gif" alt="biography" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=100351"><B>AKHAYAN, Ruben </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;2003-2008</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;16</font></td></tr>
<tr bgcolor=#FFFFFF>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2439</font></td>
<td><img src="/chessimages/chat.gif" alt="8" width=16 height=16><img src="/chessimages/book.gif" alt="biography" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=50176"><B>AKHMADEEV, Vadim </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;1983-2010</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;67</font></td></tr>
<tr bgcolor=#FFEEDD>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2483</font></td>
<td><img src="/chessimages/chat.gif" alt="3" width=16 height=16><img src="/chessimages/book.gif" alt="biography" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=53200"><B>AKHMETOV, Artiom </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;1996-2015</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;56</font></td></tr>
<tr bgcolor=#FFFFFF>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2438</font></td>
<td>&nbsp;<img src="/chessimages/book.gif" alt="biography" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=134831"><B>AKHMETOV, Ayan </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;2010-2020</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;87</font></td></tr>
<tr bgcolor=#FFEEDD>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2310</font></td>
<td><img src="/chessimages/chat.gif" alt="7" width=16 height=16><img src="/chessimages/book.gif" alt="biography" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=84377"><B>AKHSHARUMOVA, Anna M </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;1975-1996</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;48</font></td></tr>
<tr bgcolor=#FFFFFF>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2358</font></td>
<td>&nbsp;<img src="/chessimages/book.gif" alt="biography" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=155646"><B>AKHVLEDIANI, Irakli </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;2015-2021</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;32</font></td></tr>
<tr bgcolor=#FFEEDD>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2434</font></td>
<td><img src="/chessimages/chat.gif" alt="13" width=16 height=16><img src="/chessimages/book.gif" alt="biography" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=49685"><B>AKIMOV, Ivan </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;2000-2008</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;52</font></td></tr>
<tr bgcolor=#FFFFFF>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2282</font></td>
<td>&nbsp;<img src="/chessimages/book.gif" alt="biography" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=63354"><B>AKINTOLA, Fola </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;1990-2006</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;15</font></td></tr>
<tr bgcolor=#FFEEDD>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2401</font></td>
<td>&nbsp;<img src="/chessimages/book.gif" alt="biography" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=127111"><B>AKKOZOV, Berik </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;2010-2017</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;53</font></td></tr>
<tr bgcolor=#FFFFFF>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2673</font></td>
<td><img src="/chessimages/chat.gif" alt="200" width=16 height=16><img src="/chessimages/book.gif" alt="biography" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=51148"><B>AKOBIAN, Varuzhan </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;1993-2021</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;1,185</font></td></tr>
<tr bgcolor=#FFEEDD>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2263</font></td>
<td><img src="/chessimages/chat.gif" alt="1" width=16 height=16><img src="/chessimages/book.gif" alt="biography" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=59548"><B>AKOPIAN, Gagik </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;1963-2008</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;29</font></td></tr>
<tr bgcolor=#FFFFFF>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2713</font></td>
<td><img src="/chessimages/chat.gif" alt="271" width=16 height=16><img src="/chessimages/book.gif" alt="biography" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=14125"><B>AKOPIAN, Vladimir </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;1982-2021</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;1,957</font></td></tr>
<tr bgcolor=#FFEEDD>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2249</font></td>
<td><img src="/chessimages/chat.gif" alt="3" width=16 height=16><img src="/chessimages/book.gif" alt="biography" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=12547"><B>AKOPYAN, Harutyun </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;1998-2014</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;24</font></td></tr>
<tr bgcolor=#FFFFFF>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2446</font></td>
<td><img src="/chessimages/chat.gif" alt="4" width=16 height=16><img src="/chessimages/book.gif" alt="biography" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=49065"><B>AKSELROD, Vladislav </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;2001-2012</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;48</font></td></tr>
<tr bgcolor=#FFEEDD>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2414</font></td>
<td><img src="/chessimages/chat.gif" alt="3" width=16 height=16><img src="/chessimages/book.gif" alt="biography" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=117318"><B>AKSHAT, Khamparia </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;2005-2022</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;102</font></td></tr>
<tr bgcolor=#FFFFFF>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2512</font></td>
<td><img src="/chessimages/chat.gif" alt="7" width=16 height=16><img src="/chessimages/book.gif" alt="biography" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=79905"><B>AKSHAYRAJ, Kore </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;2000-2014</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;100</font></td></tr>
<tr bgcolor=#FFEEDD>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2357</font></td>
<td>&nbsp;</td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=131882"><B>AKULOV, Leonid </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;1999-2007</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;22</font></td></tr>
<tr bgcolor=#FFFFFF>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2230</font></td>
<td>&nbsp;<img src="/chessimages/book.gif" alt="biography" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=47783"><B>AKVIST, Hakan </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;1965-2002</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;85</font></td></tr>
<tr bgcolor=#FFEEDD>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2390</font></td>
<td>&nbsp;</td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=127195"><B>AKYLBEKOV, Nasyr </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;2010-2017</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;19</font></td></tr>
<tr bgcolor=#FFFFFF>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2370</font></td>
<td><img src="/chessimages/chat.gif" alt="4" width=16 height=16><img src="/chessimages/book.gif" alt="biography" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=15200"><B>ALAAN, Vince </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;1987-1992</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;14</font></td></tr>
<tr bgcolor=#FFEEDD>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2307</font></td>
<td><img src="/chessimages/chat.gif" alt="13" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=49701"><B>ALAGULIAN, Kamo </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;1999-2015</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;25</font></td></tr>
<tr bgcolor=#FFFFFF>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2415</font></td>
<td>&nbsp;</td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=56761"><B>ALAGUZOV, Maxat </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;2000-2007</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;22</font></td></tr>
<tr bgcolor=#FFEEDD>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2331</font></td>
<td><img src="/chessimages/chat.gif" alt="1" width=16 height=16><img src="/chessimages/book.gif" alt="biography" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=70544"><B>DEL ALAMO, Antonio Lopez </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;2000-2004</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;8</font></td></tr>
<tr bgcolor=#FFFFFF>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;&nbsp;</font></td>
<td><img src="/chessimages/chat.gif" alt="32" width=16 height=16><img src="/chessimages/book.gif" alt="biography" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=10538"><B>ALAPIN, Semion </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;1875-1921</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;339</font></td></tr>
<tr bgcolor=#FFEEDD>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2406</font></td>
<td><img src="/chessimages/chat.gif" alt="1" width=16 height=16><img src="/chessimages/book.gif" alt="biography" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=155801"><B>ALARCON, Andres Merario </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;2015-2022</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;90</font></td></tr>
<tr bgcolor=#FFFFFF>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2435</font></td>
<td>&nbsp;<img src="/chessimages/book.gif" alt="biography" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=120646"><B>ALARCON, Julian Antonio Rojas </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;2008-2018</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;37</font></td></tr>
<tr bgcolor=#FFEEDD>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;&nbsp;</font></td>
<td><img src="/chessimages/chat.gif" alt="14" width=16 height=16><img src="/chessimages/book.gif" alt="biography" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=20464"><B>ALATORTSEV, Vladimir </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;1926-1965</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;406</font></td></tr>
<tr bgcolor=#FFFFFF>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2218</font></td>
<td>&nbsp;<img src="/chessimages/book.gif" alt="biography" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=63578"><B>ALAVA, Mikko </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;1992-2017</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;16</font></td></tr>
<tr bgcolor=#FFEEDD>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2379</font></td>
<td>&nbsp;<img src="/chessimages/book.gif" alt="biography" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=106307"><B>ALAVERDYAN, Gevorg </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;2000-2021</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;38</font></td></tr>
<tr bgcolor=#FFFFFF>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2504</font></td>
<td><img src="/chessimages/chat.gif" alt="2" width=16 height=16><img src="/chessimages/book.gif" alt="biography" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=50144"><B>ALAVKIN, Arseny </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;1994-2015</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;166</font></td></tr>
<tr bgcolor=#FFEEDD>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2228</font></td>
<td><img src="/chessimages/chat.gif" alt="1" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=55366"><B>ALBADALEJO, Mariano Jimenez </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;2001-2005</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2</font></td></tr>
<tr bgcolor=#FFFFFF>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2304</font></td>
<td><img src="/chessimages/chat.gif" alt="5" width=16 height=16><img src="/chessimages/book.gif" alt="biography" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=119381"><B>ALBANO, Marco </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;1966-2004</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;146</font></td></tr>
<tr bgcolor=#FFEEDD>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2406</font></td>
<td>&nbsp;<img src="/chessimages/book.gif" alt="biography" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=50591"><B>ALBARRACIN, Francisco D Garcia </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;1989-2018</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;32</font></td></tr>
<tr bgcolor=#FFFFFF>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2283</font></td>
<td><img src="/chessimages/chat.gif" alt="4" width=16 height=16><img src="/chessimages/book.gif" alt="biography" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=42716"><B>ALBARRAN, Gustavo </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;1996-2006</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;34</font></td></tr>
<tr bgcolor=#FFEEDD>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2400</font></td>
<td>&nbsp;<img src="/chessimages/book.gif" alt="biography" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=30517"><B>ALBER, Horst </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;1982-2017</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;30</font></td></tr>
<tr bgcolor=#FFFFFF>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;&nbsp;</font></td>
<td><img src="/chessimages/chat.gif" alt="9" width=16 height=16><img src="/chessimages/book.gif" alt="biography" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=19213"><B>ALBERO, Roman Toran </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;1947-1975</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;578</font></td></tr>
<tr bgcolor=#FFEEDD>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2280</font></td>
<td><img src="/chessimages/chat.gif" alt="3" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=157651"><B>ALBERSTON, Bruce </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;1979</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;10</font></td></tr>
<tr bgcolor=#FFFFFF>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2209</font></td>
<td>&nbsp;</td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=99455"><B>ALBERTO, Manuel </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;1994-2020</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;19</font></td></tr>
<tr bgcolor=#FFEEDD>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;&nbsp;</font></td>
<td><img src="/chessimages/chat.gif" alt="39" width=16 height=16><img src="/chessimages/book.gif" alt="biography" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=18641"><B>ALBIN, Adolf </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;1886-1914</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;319</font></td></tr>
<tr bgcolor=#FFFFFF>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2267</font></td>
<td>&nbsp;<img src="/chessimages/book.gif" alt="biography" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=81317"><B>ALBORNOZ, Guillermo Cerda </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;2003-2018</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;35</font></td></tr>
<tr bgcolor=#FFEEDD>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2580</font></td>
<td><img src="/chessimages/chat.gif" alt="371" width=16 height=16><img src="/chessimages/book.gif" alt="biography" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=15271"><B>ALBURT, Lev </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;1965-2013</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;916</font></td></tr>
<tr bgcolor=#FFFFFF>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2620</font></td>
<td><img src="/chessimages/chat.gif" alt="5" width=16 height=16><img src="/chessimages/book.gif" alt="biography" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=139888"><B>ALCANTARA, Jose Eduardo Martinez </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;2012-2022</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;102</font></td></tr>
<tr bgcolor=#FFEEDD>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2512</font></td>
<td><img src="/chessimages/chat.gif" alt="5" width=16 height=16><img src="/chessimages/book.gif" alt="biography" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=124531"><B>ALCARAZ, Andres Felipe Gallego </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;2006-2019</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;71</font></td></tr>
<tr bgcolor=#FFFFFF>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2280</font></td>
<td>&nbsp;<img src="/chessimages/book.gif" alt="biography" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=102996"><B>ALDROVANDI, Costantino </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;1997-2005</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;47</font></td></tr>
<tr bgcolor=#FFEEDD>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2549</font></td>
<td><img src="/chessimages/chat.gif" alt="1" width=16 height=16><img src="/chessimages/book.gif" alt="biography" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=133277"><B>ALEJANO, Carlos Antonio Hevia </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;2010-2020</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;69</font></td></tr>
<tr bgcolor=#FFFFFF>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2220</font></td>
<td><img src="/chessimages/chat.gif" alt="3" width=16 height=16><img src="/chessimages/book.gif" alt="biography" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=59473"><B>ALEKHINA, Natalia V </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;1969-1995</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;7</font></td></tr>
<tr bgcolor=#FFEEDD>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;&nbsp;</font></td>
<td><img src="/chessimages/chat.gif" alt="3497" width=16 height=16><img src="/chessimages/book.gif" alt="biography" width=16 height=16><a href="/audio/10240.mp3"><img src="/chessimages/speaker.gif" alt="pronunciation" width=16 height=16 border=0></a></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=10240"><B>ALEKHINE, Alexander </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;1905-1946</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2,189</font></td></tr>
<tr bgcolor=#FFFFFF>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2679</font></td>
<td><img src="/chessimages/chat.gif" alt="14" width=16 height=16><img src="/chessimages/book.gif" alt="biography" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=17278"><B>ALEKSANDROV, Aleksej </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;1987-2022</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;1,815</font></td></tr>
<tr bgcolor=#FFEEDD>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2274</font></td>
<td>&nbsp;</td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=149283"><B>ALEKSANYAN, Hrant </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;2013-2018</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;22</font></td></tr>
<tr bgcolor=#FFFFFF>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2715</font></td>
<td><img src="/chessimages/chat.gif" alt="32" width=16 height=16><img src="/chessimages/book.gif" alt="biography" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=117648"><B>ALEKSEENKO, Kirill </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;2007-2021</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;654</font></td></tr>
<tr bgcolor=#FFEEDD>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2340</font></td>
<td><img src="/chessimages/chat.gif" alt="1" width=16 height=16><img src="/chessimages/book.gif" alt="biography" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=29350"><B>ALEKSEEV, Andrey </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;1961-2019</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;38</font></td></tr>
<tr bgcolor=#FFFFFF>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2725</font></td>
<td><img src="/chessimages/chat.gif" alt="46" width=16 height=16><img src="/chessimages/book.gif" alt="biography" width=16 height=16><a href="/audio/68679.mp3"><img src="/chessimages/speaker.gif" alt="pronunciation" width=16 height=16 border=0></a></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=68679"><B>ALEKSEEV, Evgeny </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;1998-2022</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;1,550</font></td></tr>
<tr bgcolor=#FFEEDD>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2375</font></td>
<td><img src="/chessimages/chat.gif" alt="2" width=16 height=16><img src="/chessimages/book.gif" alt="biography" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=62504"><B>ALEKSEEV, Vadim </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;1953-2021</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;18</font></td></tr>
<tr bgcolor=#FFFFFF>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2274</font></td>
<td>&nbsp;<img src="/chessimages/book.gif" alt="biography" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=71943"><B>ALEKSEEVA, Alena </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;2001-2009</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;23</font></td></tr>
<tr bgcolor=#FFEEDD>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2417</font></td>
<td><img src="/chessimages/chat.gif" alt="3" width=16 height=16><img src="/chessimages/book.gif" alt="biography" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=58825"><B>ALEKSIC, Nenad </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;1981-2021</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;86</font></td></tr>
<tr bgcolor=#FFFFFF>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2425</font></td>
<td>&nbsp;<img src="/chessimages/book.gif" alt="biography" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=98718"><B>ALESHIN, Oleg </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;2001-2009</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;34</font></td></tr>
<tr bgcolor=#FFEEDD>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2590</font></td>
<td><img src="/chessimages/chat.gif" alt="1" width=16 height=16><img src="/chessimages/book.gif" alt="biography" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=105463"><B>ALESHNYA, Valery </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;1997-2009</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;66</font></td></tr>
<tr bgcolor=#FFFFFF>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2421</font></td>
<td><img src="/chessimages/chat.gif" alt="2" width=16 height=16><img src="/chessimages/book.gif" alt="biography" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=85210"><B>ALESKEROV, Faik </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;1993-2019</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;113</font></td></tr>
<tr bgcolor=#FFEEDD>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2220</font></td>
<td>&nbsp;</td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=64456"><B>ALET, Jean-Pierre </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;1988-2005</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;19</font></td></tr>
<tr bgcolor=#FFFFFF>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2224</font></td>
<td>&nbsp;<img src="/chessimages/book.gif" alt="biography" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=52412"><B>ALEXAKIS, Dimitrios </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;1979-2021</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;35</font></td></tr>
<tr bgcolor=#FFEEDD>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;&nbsp;</font></td>
<td><img src="/chessimages/chat.gif" alt="100" width=16 height=16><img src="/chessimages/book.gif" alt="biography" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=23967"><B>ALEXANDER, Conel Hugh O'Donel </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;1928-1973</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;386</font></td></tr>
<tr bgcolor=#FFFFFF>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2375</font></td>
<td><img src="/chessimages/chat.gif" alt="6" width=16 height=16><img src="/chessimages/book.gif" alt="biography" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=25216"><B>ALEXANDRIA, Nana </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;1968-2005</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;216</font></td></tr>
<tr bgcolor=#FFEEDD>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2449</font></td>
<td><img src="/chessimages/chat.gif" alt="14" width=16 height=16><img src="/chessimages/book.gif" alt="biography" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=49635"><B>ALEXANDROVA, Olga </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;1996-2014</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;228</font></td></tr>
<tr bgcolor=#FFFFFF>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2211</font></td>
<td>&nbsp;<img src="/chessimages/book.gif" alt="biography" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=94532"><B>ALEXANIAN, Nelli </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;2005-2019</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;45</font></td></tr>
<tr bgcolor=#FFEEDD>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2359</font></td>
<td>&nbsp;</td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=139048"><B>ALEXIADIS, Hristos </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;2012-2021</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;21</font></td></tr>
<tr bgcolor=#FFFFFF>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2408</font></td>
<td><img src="/chessimages/chat.gif" alt="3" width=16 height=16><img src="/chessimages/book.gif" alt="biography" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=89205"><B>ALEXIEVA, Silvia </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;1990-2017</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;349</font></td></tr>
<tr bgcolor=#FFEEDD>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2432</font></td>
<td><img src="/chessimages/chat.gif" alt="6" width=16 height=16><img src="/chessimages/book.gif" alt="biography" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=54537"><B>ALEXIKOV, Alexander </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;1997-2021</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;40</font></td></tr>
<tr bgcolor=#FFFFFF>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2254</font></td>
<td>&nbsp;<img src="/chessimages/book.gif" alt="biography" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=18876"><B>ALEXOPOULOS, Georgios </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;1969-2003</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;37</font></td></tr>
<tr bgcolor=#FFEEDD>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2231</font></td>
<td>&nbsp;<img src="/chessimages/book.gif" alt="biography" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=97176"><B>ALFARO, William </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;2005-2022</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;61</font></td></tr>
<tr bgcolor=#FFFFFF>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2359</font></td>
<td>&nbsp;<img src="/chessimages/book.gif" alt="biography" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=28247"><B>ALFONSO, Braulio </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;1989-1999</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;18</font></td></tr>
<tr bgcolor=#FFEEDD>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2294</font></td>
<td>&nbsp;<img src="/chessimages/book.gif" alt="biography" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=129956"><B>ALFRED, Nathan S W </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;1996-2012</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;35</font></td></tr>
<tr bgcolor=#FFFFFF>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2403</font></td>
<td><img src="/chessimages/chat.gif" alt="1" width=16 height=16><img src="/chessimages/book.gif" alt="biography" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=127216"><B>ALI, Omar Noaman Al </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;2010-2021</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;214</font></td></tr>
<tr bgcolor=#FFEEDD>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2412</font></td>
<td><img src="/chessimages/chat.gif" alt="1" width=16 height=16><img src="/chessimages/book.gif" alt="biography" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=161862"><B>ALI, Ehsan </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;2006-2007</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2</font></td></tr>
<tr bgcolor=#FFFFFF>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2274</font></td>
<td><img src="/chessimages/chat.gif" alt="3" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=95227"><B>ALI, Mohamad Nour Kara </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;2000-2004</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;16</font></td></tr>
<tr bgcolor=#FFEEDD>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2439</font></td>
<td><img src="/chessimages/chat.gif" alt="7" width=16 height=16><img src="/chessimages/book.gif" alt="biography" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=139009"><B>ALI, Muhammad Lutfi </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;2012-2021</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;83</font></td></tr>
<tr bgcolor=#FFFFFF>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2248</font></td>
<td><img src="/chessimages/chat.gif" alt="2" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=85106"><B>ALI, Syed Nasir </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;1977-2009</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;26</font></td></tr>
<tr bgcolor=#FFEEDD>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2404</font></td>
<td>&nbsp;<img src="/chessimages/book.gif" alt="biography" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=52091"><B>ALI, Sebbar </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;2001-2014</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;46</font></td></tr>
<tr bgcolor=#FFFFFF>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2421</font></td>
<td>&nbsp;<img src="/chessimages/book.gif" alt="biography" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=110949"><B>ALIAVDIN, Nikolai </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;2005-2011</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;49</font></td></tr>
<tr bgcolor=#FFEEDD>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2316</font></td>
<td><img src="/chessimages/chat.gif" alt="1" width=16 height=16><img src="/chessimages/book.gif" alt="biography" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=58545"><B>ALIBAEV, Akbar </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;2000-2001</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;12</font></td></tr>
<tr bgcolor=#FFFFFF>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2202</font></td>
<td>&nbsp;<img src="/chessimages/book.gif" alt="biography" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=119002"><B>ALICE, Mateus Felizardo Viageiro </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;2005-2016</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;40</font></td></tr>
<tr bgcolor=#FFEEDD>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2407</font></td>
<td><img src="/chessimages/chat.gif" alt="2" width=16 height=16><img src="/chessimages/book.gif" alt="biography" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=101700"><B>ALIENKIN, Aleksander </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;1978-2022</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;35</font></td></tr>
<tr bgcolor=#FFFFFF>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2411</font></td>
<td><img src="/chessimages/chat.gif" alt="2" width=16 height=16><img src="/chessimages/book.gif" alt="biography" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=50878"><B>ALIEV, Kerim </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;1998-2005</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;9</font></td></tr>
<tr bgcolor=#FFEEDD>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2259</font></td>
<td>&nbsp;<img src="/chessimages/book.gif" alt="biography" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=92559"><B>ALIEVA, Elmira </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;1981-2007</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;18</font></td></tr>
<tr bgcolor=#FFFFFF>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2455</font></td>
<td>&nbsp;<img src="/chessimages/book.gif" alt="biography" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=53210"><B>ALIKHANOV, Felix </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;2001-2007</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;31</font></td></tr>
<tr bgcolor=#FFEEDD>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2411</font></td>
<td><img src="/chessimages/chat.gif" alt="1" width=16 height=16><img src="/chessimages/book.gif" alt="biography" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=149957"><B>ALIKULOV, Elbek </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;2014-2017</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;19</font></td></tr>
<tr bgcolor=#FFFFFF>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2320</font></td>
<td><img src="/chessimages/chat.gif" alt="3" width=16 height=16><img src="/chessimages/book.gif" alt="biography" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=155113"><B>ALINASAB, Mobina </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;2016-2022</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;109</font></td></tr>
<tr bgcolor=#FFEEDD>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2302</font></td>
<td>&nbsp;<img src="/chessimages/book.gif" alt="biography" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=91444"><B>ALIYEV, Rasim </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;1997-2015</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;29</font></td></tr>
<tr bgcolor=#FFFFFF>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2346</font></td>
<td><img src="/chessimages/chat.gif" alt="1" width=16 height=16><img src="/chessimages/book.gif" alt="biography" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=155820"><B>ALIYEV, Ravan </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;2015-2019</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;48</font></td></tr>
<tr bgcolor=#FFEEDD>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2689</font></td>
<td><img src="/chessimages/chat.gif" alt="3" width=16 height=16><img src="/chessimages/book.gif" alt="biography" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=31171"><B>ALLAHVERDIYEV, Anar </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;1993-2019</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;47</font></td></tr>
<tr bgcolor=#FFFFFF>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2226</font></td>
<td>&nbsp;</td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=80808"><B>ALLAJOV, Ramil </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;2003-2016</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;15</font></td></tr>
<tr bgcolor=#FFEEDD>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2355</font></td>
<td><img src="/chessimages/chat.gif" alt="3" width=16 height=16><img src="/chessimages/book.gif" alt="biography" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=22415"><B>ALLAN, Denis </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;1964-1999</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;86</font></td></tr>
<tr bgcolor=#FFFFFF>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2369</font></td>
<td><img src="/chessimages/chat.gif" alt="1" width=16 height=16><img src="/chessimages/book.gif" alt="biography" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=108815"><B>ALLARIA, Carlos Salgado </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;1989-2007</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;14</font></td></tr>
<tr bgcolor=#FFEEDD>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2231</font></td>
<td><img src="/chessimages/chat.gif" alt="2" width=16 height=16><img src="/chessimages/book.gif" alt="biography" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=99585"><B>ALLEGRO, Valery </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;1980-1995</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;30</font></td></tr>
<tr bgcolor=#FFFFFF>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2288</font></td>
<td>&nbsp;</td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=51109"><B>ALLEMANN, Anton </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;1997-2005</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;19</font></td></tr>
<tr bgcolor=#FFEEDD>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2263</font></td>
<td><img src="/chessimages/chat.gif" alt="3" width=16 height=16><img src="/chessimages/book.gif" alt="biography" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=58816"><B>ALLEN, Andrew </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;1991-2001</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;50</font></td></tr>
<tr bgcolor=#FFFFFF>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2289</font></td>
<td><img src="/chessimages/chat.gif" alt="1" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=28827"><B>ALLEN, Keith </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;1977-2019</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;153</font></td></tr>
<tr bgcolor=#FFEEDD>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2380</font></td>
<td>&nbsp;<img src="/chessimages/book.gif" alt="biography" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=123791"><B>ALLER, Fernando Sanchez </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;1999-2018</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;29</font></td></tr>
<tr bgcolor=#FFFFFF>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2324</font></td>
<td><img src="/chessimages/chat.gif" alt="3" width=16 height=16><img src="/chessimages/book.gif" alt="biography" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=126450"><B>ALLICOCK, Rawle Anthony </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;1997-2019</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;27</font></td></tr>
<tr bgcolor=#FFEEDD>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;&nbsp;</font></td>
<td><img src="/chessimages/chat.gif" alt="3" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=12691"><B>ALLIES, Alekhine / </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;1907-1934</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;5</font></td></tr>
<tr bgcolor=#FFFFFF>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2352</font></td>
<td>&nbsp;<img src="/chessimages/book.gif" alt="biography" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=37730"><B>ALMADA, Enrique </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;1982-2012</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;31</font></td></tr>
<tr bgcolor=#FFEEDD>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2440</font></td>
<td><img src="/chessimages/chat.gif" alt="4" width=16 height=16><img src="/chessimages/book.gif" alt="biography" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=38805"><B>ALMASI, Istvan </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;1990-2018</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;97</font></td></tr>
<tr bgcolor=#FFFFFF>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2726</font></td>
<td><img src="/chessimages/chat.gif" alt="55" width=16 height=16><img src="/chessimages/book.gif" alt="biography" width=16 height=16><a href="/audio/14210.mp3"><img src="/chessimages/speaker.gif" alt="pronunciation" width=16 height=16 border=0></a></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=14210"><B>ALMASI, Zoltan </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;1990-2021</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;1,335</font></td></tr>
<tr bgcolor=#FFEEDD>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2298</font></td>
<td><img src="/chessimages/chat.gif" alt="3" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=69325"><B>ALMEIDA, Rui Camejo </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;1987-2001</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;28</font></td></tr>
<tr bgcolor=#FFFFFF>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2447</font></td>
<td><img src="/chessimages/chat.gif" alt="4" width=16 height=16><img src="/chessimages/book.gif" alt="biography" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=30801"><B>ALMEYRA, Jorge Sanchez </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;1987-2001</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;66</font></td></tr>
<tr bgcolor=#FFEEDD>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2372</font></td>
<td>&nbsp;</td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=127844"><B>ALMIRON, Antonio </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;2009-2021</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;24</font></td></tr>
<tr bgcolor=#FFFFFF>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2575</font></td>
<td>&nbsp;<img src="/chessimages/book.gif" alt="biography" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=162133"><B>ALMIRON, Luis </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;2007-2010</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;32</font></td></tr>
<tr bgcolor=#FFEEDD>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2605</font></td>
<td><img src="/chessimages/chat.gif" alt="2" width=16 height=16><img src="/chessimages/book.gif" alt="biography" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=131801"><B>ALONSO, Yusnel Bacallao </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;2009-2018</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;112</font></td></tr>
<tr bgcolor=#FFFFFF>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2504</font></td>
<td><img src="/chessimages/chat.gif" alt="2" width=16 height=16><img src="/chessimages/book.gif" alt="biography" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=71088"><B>ALONSO, Alejandro Franco </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;2001-2021</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;97</font></td></tr>
<tr bgcolor=#FFEEDD>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2482</font></td>
<td><img src="/chessimages/chat.gif" alt="1" width=16 height=16><img src="/chessimages/book.gif" alt="biography" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=100019"><B>ALONSO, Santiago Roa </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;1991-2007</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;29</font></td></tr>
<tr bgcolor=#FFFFFF>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2524</font></td>
<td><img src="/chessimages/chat.gif" alt="3" width=16 height=16><img src="/chessimages/book.gif" alt="biography" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=20995"><B>ALONSO, Salvador </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;1994-2019</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;235</font></td></tr>
<tr bgcolor=#FFEEDD>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2415</font></td>
<td><img src="/chessimages/chat.gif" alt="4" width=16 height=16><img src="/chessimages/book.gif" alt="biography" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=50380"><B>ALONSO, Francisco Javier Sanz </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;1974-2015</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;229</font></td></tr>
<tr bgcolor=#FFFFFF>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2246</font></td>
<td>&nbsp;<img src="/chessimages/book.gif" alt="biography" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=21456"><B>ALONZO, Luis Manuel Belliard </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;1968-2010</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;34</font></td></tr>
<tr bgcolor=#FFEEDD>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;&nbsp;</font></td>
<td><img src="/chessimages/chat.gif" alt="19" width=16 height=16><img src="/chessimages/book.gif" alt="biography" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=28668"><B>ALSTER, Ladislav </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;1944-1989</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;309</font></td></tr>
<tr bgcolor=#FFFFFF>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2333</font></td>
<td>&nbsp;<img src="/chessimages/book.gif" alt="biography" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=81303"><B>ALTAMIRANO, Benjamin </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;1992-2004</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;24</font></td></tr>
<tr bgcolor=#FFEEDD>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2287</font></td>
<td>&nbsp;<img src="/chessimages/book.gif" alt="biography" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=156149"><B>ALTANTUYA, Boldbaatar </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;2016-2019</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;43</font></td></tr>
<tr bgcolor=#FFFFFF>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2615</font></td>
<td><img src="/chessimages/chat.gif" alt="28" width=16 height=16><img src="/chessimages/book.gif" alt="biography" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=17034"><B>ALTERMAN, Boris </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;1983-2012</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;322</font></td></tr>
<tr bgcolor=#FFEEDD>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2426</font></td>
<td><img src="/chessimages/chat.gif" alt="1" width=16 height=16><img src="/chessimages/book.gif" alt="biography" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=139770"><B>ALTINI, Nicola </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;2012-2016</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;27</font></td></tr>
<tr bgcolor=#FFFFFF>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2465</font></td>
<td><img src="/chessimages/chat.gif" alt="5" width=16 height=16><img src="/chessimages/book.gif" alt="biography" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=51149"><B>ALTOUNIAN, Levon </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;1993-2018</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;101</font></td></tr>
<tr bgcolor=#FFEEDD>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2343</font></td>
<td>&nbsp;<img src="/chessimages/book.gif" alt="biography" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=97330"><B>ALTSHUL, Raffael </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;2005-2012</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;27</font></td></tr>
<tr bgcolor=#FFFFFF>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;&nbsp;</font></td>
<td><img src="/chessimages/chat.gif" alt="10" width=16 height=16><img src="/chessimages/book.gif" alt="biography" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=20191"><B>ALVAREZ, Rodrigo Flores </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;1927-1965</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;185</font></td></tr>
<tr bgcolor=#FFEEDD>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2250</font></td>
<td>&nbsp;<img src="/chessimages/book.gif" alt="biography" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=109690"><B>ALVAREZ, Franklin </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;1972-2008</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;26</font></td></tr>
<tr bgcolor=#FFFFFF>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2557</font></td>
<td>&nbsp;<img src="/chessimages/book.gif" alt="biography" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=97630"><B>ALVAREZ, Roberto Gabriel </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;1994-2008</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;31</font></td></tr>
<tr bgcolor=#FFEEDD>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2368</font></td>
<td><img src="/chessimages/chat.gif" alt="1" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=40254"><B>ALVAREZ, Jose </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;1980-2002</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;17</font></td></tr>
<tr bgcolor=#FFFFFF>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2316</font></td>
<td>&nbsp;<img src="/chessimages/book.gif" alt="biography" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=117507"><B>ALVAREZ, Inigo Martin </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;2008-2014</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;18</font></td></tr>
<tr bgcolor=#FFEEDD>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2601</font></td>
<td><img src="/chessimages/chat.gif" alt="73" width=16 height=16><img src="/chessimages/book.gif" alt="biography" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=49584"><B>ALVAREZ, Alejandro Ramirez </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;1995-2021</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;547</font></td></tr>
<tr bgcolor=#FFFFFF>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2283</font></td>
<td>&nbsp;<img src="/chessimages/book.gif" alt="biography" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=69199"><B>ALVAREZ, Vidal Rodriguez </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;2001-2019</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;33</font></td></tr>
<tr bgcolor=#FFEEDD>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2409</font></td>
<td><img src="/chessimages/chat.gif" alt="2" width=16 height=16><img src="/chessimages/book.gif" alt="biography" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=159744"><B>ALVAREZ, Roberto Carlos Sanchez </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;2016-2022</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;47</font></td></tr>
<tr bgcolor=#FFFFFF>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2437</font></td>
<td><img src="/chessimages/chat.gif" alt="1" width=16 height=16><img src="/chessimages/book.gif" alt="biography" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=68277"><B>ALVAREZ, Ismael Teran </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;1991-2019</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;181</font></td></tr>
<tr bgcolor=#FFEEDD>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2295</font></td>
<td><img src="/chessimages/chat.gif" alt="4" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=38701"><B>VON ALVENSLEBEN, Wolfram </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;1856-1997</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;21</font></td></tr>
<tr bgcolor=#FFFFFF>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2404</font></td>
<td><img src="/chessimages/chat.gif" alt="5" width=16 height=16><img src="/chessimages/book.gif" alt="biography" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=103438"><B>ALVIR, Aco </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;1986-2016</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;29</font></td></tr>
<tr bgcolor=#FFEEDD>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2430</font></td>
<td><img src="/chessimages/chat.gif" alt="3" width=16 height=16><img src="/chessimages/book.gif" alt="biography" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=15662"><B>ALZATE, Dario </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;1982-2017</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;103</font></td></tr>
<tr bgcolor=#FFFFFF>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2310</font></td>
<td>&nbsp;</td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=148089"><B>ALZATE, Javier </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;1966-1974</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;26</font></td></tr>
<tr bgcolor=#FFEEDD>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2541</font></td>
<td><img src="/chessimages/chat.gif" alt="7" width=16 height=16><img src="/chessimages/book.gif" alt="biography" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=56753"><B>AMANOV, Mesgen </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;1999-2014</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;180</font></td></tr>
<tr bgcolor=#FFFFFF>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2421</font></td>
<td><img src="/chessimages/chat.gif" alt="1" width=16 height=16><img src="/chessimages/book.gif" alt="biography" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=103826"><B>AMANOV, Zhanibek </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;2006-2019</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;62</font></td></tr>
<tr bgcolor=#FFEEDD>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2474</font></td>
<td><img src="/chessimages/chat.gif" alt="2" width=16 height=16><img src="/chessimages/book.gif" alt="biography" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=99126"><B>AMARELLE, Mariano Ortega </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;2004-2022</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;41</font></td></tr>
<tr bgcolor=#FFFFFF>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2357</font></td>
<td><img src="/chessimages/chat.gif" alt="1" width=16 height=16><img src="/chessimages/book.gif" alt="biography" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=55394"><B>AMARO, Josue Exposito </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;2001-2021</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;9</font></td></tr>
<tr bgcolor=#FFEEDD>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2350</font></td>
<td><img src="/chessimages/chat.gif" alt="1" width=16 height=16><img src="/chessimages/book.gif" alt="biography" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=156115"><B>AMARTUVSHIN, Ganzorig </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;2016-2022</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;55</font></td></tr>
<tr bgcolor=#FFFFFF>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2350</font></td>
<td><img src="/chessimages/chat.gif" alt="2" width=16 height=16><img src="/chessimages/book.gif" alt="biography" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=142874"><B>AMATO, Andrea </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;2005-2017</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;38</font></td></tr>
<tr bgcolor=#FFEEDD>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2424</font></td>
<td><img src="/chessimages/chat.gif" alt="4" width=16 height=16><img src="/chessimages/book.gif" alt="biography" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=27627"><B>AMBARTSOUMIAN, Armen </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;1978-2003</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;32</font></td></tr>
<tr bgcolor=#FFFFFF>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2377</font></td>
<td><img src="/chessimages/chat.gif" alt="2" width=16 height=16><img src="/chessimages/book.gif" alt="biography" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=103244"><B>AMBARTSUMOVA, Karina </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;2005-2021</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;345</font></td></tr>
<tr bgcolor=#FFEEDD>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2292</font></td>
<td>&nbsp;</td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=51101"><B>AMBROSINI, Nicola </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;1993-2001</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;19</font></td></tr>
<tr bgcolor=#FFFFFF>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2485</font></td>
<td><img src="/chessimages/chat.gif" alt="12" width=16 height=16><img src="/chessimages/book.gif" alt="biography" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=24612"><B>AMBROZ, Jan </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;1973-1995</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;392</font></td></tr>
<tr bgcolor=#FFEEDD>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2400</font></td>
<td><img src="/chessimages/chat.gif" alt="1" width=16 height=16><img src="/chessimages/book.gif" alt="biography" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=56711"><B>AMBRUS, Endre </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;1998-2009</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;20</font></td></tr>
</table></td></tr></table></td><td bgcolor=#FFFFFF>&nbsp;</td><td valign=TOP><table border=0 cellpadding=2 cellspacing=0 bgcolor=#333333><tr><td valign=TOP>
<table border=0 cellpadding=2 cellspacing=0 width=100%>
<tr bgcolor=#663300>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-1 color=#FFFFFF>highest<br>rating</font></td>
<td colspan=2><font face="verdana,arial,helvetica" size=-1 color=#FFFFFF>&nbsp;&nbsp;&nbsp;&nbsp;player name</font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-1 color=#FFFFFF>Years</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-1 color=#FFFFFF># of<br>Games</font></td>
</tr><tr bgcolor=#FFFFFF>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2354</font></td>
<td>&nbsp;<img src="/chessimages/book.gif" alt="biography" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=89360"><B>AMDOUNI, Zoubaier </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;2002-2022</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;57</font></td></tr>
<tr bgcolor=#FFEEDD>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2435</font></td>
<td>&nbsp;<img src="/chessimages/book.gif" alt="biography" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=155278"><B>AMEIR, Moheb </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;2016-2020</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;33</font></td></tr>
<tr bgcolor=#FFFFFF>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2257</font></td>
<td><img src="/chessimages/chat.gif" alt="1" width=16 height=16><img src="/chessimages/book.gif" alt="biography" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=127285"><B>AMER, Karim </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;1989-2010</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;70</font></td></tr>
<tr bgcolor=#FFEEDD>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2242</font></td>
<td><img src="/chessimages/chat.gif" alt="4" width=16 height=16><img src="/chessimages/book.gif" alt="biography" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=54946"><B>AMERIKA, Katrina </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;2001-2017</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;111</font></td></tr>
<tr bgcolor=#FFFFFF>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2222</font></td>
<td><img src="/chessimages/chat.gif" alt="1" width=16 height=16><img src="/chessimages/book.gif" alt="biography" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=64509"><B>AMESZ, Jaap </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;1999-2000</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;12</font></td></tr>
<tr bgcolor=#FFEEDD>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2393</font></td>
<td>&nbsp;<img src="/chessimages/book.gif" alt="biography" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=51994"><B>AMIGUES, Emmanuel </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;2000-2008</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;18</font></td></tr>
<tr bgcolor=#FFFFFF>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2700</font></td>
<td><img src="/chessimages/chat.gif" alt="28" width=16 height=16><img src="/chessimages/book.gif" alt="biography" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=87335"><B>AMIN, Bassem </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;1998-2022</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;815</font></td></tr>
<tr bgcolor=#FFEEDD>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2274</font></td>
<td>&nbsp;<img src="/chessimages/book.gif" alt="biography" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=154429"><B>AMINA, Battsooj </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;2016</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;16</font></td></tr>
<tr bgcolor=#FFFFFF>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2324</font></td>
<td>&nbsp;</td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=141341"><B>AMINOV, Andrey </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;2012-2022</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;21</font></td></tr>
<tr bgcolor=#FFEEDD>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2312</font></td>
<td>&nbsp;<img src="/chessimages/book.gif" alt="biography" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=143029"><B>AMIONE, Pablo Adib Tapie </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;2007-2022</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;16</font></td></tr>
<tr bgcolor=#FFFFFF>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2221</font></td>
<td>&nbsp;<img src="/chessimages/book.gif" alt="biography" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=22323"><B>AMMANN, Philipp </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;1973-2004</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;24</font></td></tr>
<tr bgcolor=#FFEEDD>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2274</font></td>
<td>&nbsp;<img src="/chessimages/book.gif" alt="biography" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=154383"><B>AMMAR, Sedrani </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;2016-2021</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;65</font></td></tr>
<tr bgcolor=#FFFFFF>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2650</font></td>
<td><img src="/chessimages/chat.gif" alt="19" width=16 height=16><img src="/chessimages/book.gif" alt="biography" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=50168"><B>AMONATOV, Farrukh </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;1992-2022</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;575</font></td></tr>
<tr bgcolor=#FFEEDD>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2355</font></td>
<td><img src="/chessimages/chat.gif" alt="4" width=16 height=16><img src="/chessimages/book.gif" alt="biography" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=21467"><B>AMOS, Bruce M </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;1966-1976</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;88</font></td></tr>
<tr bgcolor=#FFFFFF>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2250</font></td>
<td>&nbsp;</td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=65051"><B>AMOVILLI, Mauro </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;1982-1988</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;20</font></td></tr>
<tr bgcolor=#FFEEDD>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2447</font></td>
<td><img src="/chessimages/chat.gif" alt="5" width=16 height=16><img src="/chessimages/book.gif" alt="biography" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=24807"><B>AMURA, Claudia Noemi </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;1970-2018</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;196</font></td></tr>
<tr bgcolor=#FFFFFF>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2305</font></td>
<td><img src="/chessimages/chat.gif" alt="1" width=16 height=16><img src="/chessimages/book.gif" alt="biography" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=132979"><B>ANADON, Daniel Gomez </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;2001-2020</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;19</font></td></tr>
<tr bgcolor=#FFEEDD>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2456</font></td>
<td><img src="/chessimages/chat.gif" alt="4" width=16 height=16><img src="/chessimages/book.gif" alt="biography" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=53956"><B>ANAGNOSTOPOULOS, Dimitrios </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;1984-2002</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;188</font></td></tr>
<tr bgcolor=#FFFFFF>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2357</font></td>
<td><img src="/chessimages/chat.gif" alt="1" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=140956"><B>ANAGNOSTOPOULOS, Konstantinos </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;2011-2019</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;20</font></td></tr>
<tr bgcolor=#FFEEDD>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2260</font></td>
<td>&nbsp;</td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=53202"><B>ANANCHENKO, Igor </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;1997-2009</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;21</font></td></tr>
<tr bgcolor=#FFFFFF>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2373</font></td>
<td><img src="/chessimages/chat.gif" alt="1" width=16 height=16><img src="/chessimages/book.gif" alt="biography" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=161648"><B>ANAND, Nadar </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;2017-2019</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;37</font></td></tr>
<tr bgcolor=#FFEEDD>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2425</font></td>
<td><img src="/chessimages/chat.gif" alt="10" width=16 height=16><img src="/chessimages/book.gif" alt="biography" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=79916"><B>ANAND, S Poobesh </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;2002-2007</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;37</font></td></tr>
<tr bgcolor=#FFFFFF>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2817</font></td>
<td><img src="/chessimages/chat.gif" alt="237" width=16 height=16><img src="/chessimages/book.gif" alt="biography" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=12088"><B>ANAND, Viswanathan </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;1984-2022</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;3,923</font></td></tr>
<tr bgcolor=#FFEEDD>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2429</font></td>
<td>&nbsp;<img src="/chessimages/book.gif" alt="biography" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=42774"><B>ANAPOLSKY, Sergey Gennadyevich </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;1991-2005</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;26</font></td></tr>
<tr bgcolor=#FFFFFF>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2225</font></td>
<td><img src="/chessimages/chat.gif" alt="5" width=16 height=16><img src="/chessimages/book.gif" alt="biography" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=149954"><B>ANARKULOV, Alisher </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;2004-2014</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;13</font></td></tr>
<tr bgcolor=#FFEEDD>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2606</font></td>
<td><img src="/chessimages/chat.gif" alt="31" width=16 height=16><img src="/chessimages/book.gif" alt="biography" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=42522"><B>ANASTASIAN, Ashot </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;1983-2011</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;606</font></td></tr>
<tr bgcolor=#FFFFFF>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2230</font></td>
<td><img src="/chessimages/chat.gif" alt="4" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=62795"><B>ANBUHL, Edgar </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;1981-1982</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;23</font></td></tr>
<tr bgcolor=#FFEEDD>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2266</font></td>
<td>&nbsp;</td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=18365"><B>ANCESCHI, Vittorio </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;1981-2004</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;95</font></td></tr>
<tr bgcolor=#FFFFFF>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;&nbsp;</font></td>
<td><img src="/chessimages/chat.gif" alt="16" width=16 height=16><img src="/chessimages/book.gif" alt="biography" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=40151"><B>ANDERSEN, Borge </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;1954-1974</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;155</font></td></tr>
<tr bgcolor=#FFEEDD>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2273</font></td>
<td><img src="/chessimages/chat.gif" alt="5" width=16 height=16><img src="/chessimages/book.gif" alt="biography" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=98749"><B>ANDERSEN, Daniel </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;1992-2019</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;147</font></td></tr>
<tr bgcolor=#FFFFFF>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2239</font></td>
<td>&nbsp;</td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=105194"><B>ANDERSEN, Harry </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;2006-2009</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;16</font></td></tr>
<tr bgcolor=#FFEEDD>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2405</font></td>
<td>&nbsp;</td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=78261"><B>ANDERSEN, Jackie </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;1983-2016</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;21</font></td></tr>
<tr bgcolor=#FFFFFF>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2606</font></td>
<td><img src="/chessimages/chat.gif" alt="20" width=16 height=16><img src="/chessimages/book.gif" alt="biography" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=105215"><B>ANDERSEN, Mads </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;2006-2022</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;477</font></td></tr>
<tr bgcolor=#FFEEDD>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2256</font></td>
<td>&nbsp;</td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=53704"><B>ANDERSEN, Alf Roger </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;2001-2019</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;46</font></td></tr>
<tr bgcolor=#FFFFFF>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2500</font></td>
<td>&nbsp;<img src="/chessimages/book.gif" alt="biography" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=116885"><B>ANDERSON, John </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;1985-2019</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;146</font></td></tr>
<tr bgcolor=#FFEEDD>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2332</font></td>
<td>&nbsp;<img src="/chessimages/book.gif" alt="biography" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=28519"><B>ANDERSON, Selby K </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;1986-2018</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;22</font></td></tr>
<tr bgcolor=#FFFFFF>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2290</font></td>
<td><img src="/chessimages/chat.gif" alt="4" width=16 height=16><img src="/chessimages/book.gif" alt="biography" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=84200"><B>ANDERSON, Bruce R </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;1963-2003</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;91</font></td></tr>
<tr bgcolor=#FFEEDD>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2380</font></td>
<td><img src="/chessimages/chat.gif" alt="2" width=16 height=16><img src="/chessimages/book.gif" alt="biography" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=65266"><B>ANDERSON, Renard W </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;1968-2009</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;95</font></td></tr>
<tr bgcolor=#FFFFFF>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;&nbsp;</font></td>
<td><img src="/chessimages/chat.gif" alt="212" width=16 height=16><img src="/chessimages/book.gif" alt="biography" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=10342"><B>ANDERSSEN, Adolf </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;1844-1878</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;818</font></td></tr>
<tr bgcolor=#FFEEDD>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2252</font></td>
<td><img src="/chessimages/chat.gif" alt="12" width=16 height=16><img src="/chessimages/book.gif" alt="biography" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=78909"><B>ANDERSSON, Christin </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;1990-2012</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;207</font></td></tr>
<tr bgcolor=#FFFFFF>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2317</font></td>
<td>&nbsp;<img src="/chessimages/book.gif" alt="biography" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=52934"><B>ANDERSSON, Fredrik </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;1975-2018</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;38</font></td></tr>
<tr bgcolor=#FFEEDD>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2414</font></td>
<td>&nbsp;<img src="/chessimages/book.gif" alt="biography" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=106799"><B>ANDERSSON, Tommy </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;1994-2019</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;28</font></td></tr>
<tr bgcolor=#FFFFFF>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2640</font></td>
<td><img src="/chessimages/chat.gif" alt="333" width=16 height=16><img src="/chessimages/book.gif" alt="biography" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=12112"><B>ANDERSSON, Ulf </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;1967-2018</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2,499</font></td></tr>
<tr bgcolor=#FFEEDD>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2216</font></td>
<td><img src="/chessimages/chat.gif" alt="5" width=16 height=16><img src="/chessimages/book.gif" alt="biography" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=29777"><B>ANDERSSON, Peter Göran Valter </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;1971-2015</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;14</font></td></tr>
<tr bgcolor=#FFFFFF>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2244</font></td>
<td>&nbsp;</td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=14114"><B>ANDERTON, Matthew N </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;1992-2012</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;57</font></td></tr>
<tr bgcolor=#FFEEDD>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2267</font></td>
<td><img src="/chessimages/chat.gif" alt="3" width=16 height=16><img src="/chessimages/book.gif" alt="biography" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=48371"><B>ANDERTON, David W </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;1967-2018</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;84</font></td></tr>
<tr bgcolor=#FFFFFF>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2475</font></td>
<td>&nbsp;<img src="/chessimages/book.gif" alt="biography" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=18101"><B>ANDONOV, Bogomil </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;1981-2009</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;102</font></td></tr>
<tr bgcolor=#FFEEDD>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2335</font></td>
<td>&nbsp;<img src="/chessimages/book.gif" alt="biography" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=10922"><B>ANDONOVSKI, Ljubisa </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;1996-2021</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;89</font></td></tr>
<tr bgcolor=#FFFFFF>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2218</font></td>
<td><img src="/chessimages/chat.gif" alt="2" width=16 height=16><img src="/chessimages/book.gif" alt="biography" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=81320"><B>ANDRADE, Roberto Luiz Costa </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;1994-2018</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;34</font></td></tr>
<tr bgcolor=#FFEEDD>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2266</font></td>
<td>&nbsp;</td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=78632"><B>ANDRADE, Leonardo </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;1995-2010</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;31</font></td></tr>
<tr bgcolor=#FFFFFF>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2268</font></td>
<td>&nbsp;<img src="/chessimages/book.gif" alt="biography" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=132688"><B>ANDRADE, Jose M Vieira </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;2001-2018</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;21</font></td></tr>
<tr bgcolor=#FFEEDD>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2386</font></td>
<td>&nbsp;</td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=125161"><B>ANDRE, Gordon </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;2010-2019</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;45</font></td></tr>
<tr bgcolor=#FFFFFF>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2242</font></td>
<td>&nbsp;</td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=86622"><B>ANDRE, Wolfgang </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;1977-1991</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;15</font></td></tr>
<tr bgcolor=#FFEEDD>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2260</font></td>
<td>&nbsp;<img src="/chessimages/book.gif" alt="biography" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=127654"><B>ANDREASEN, Joan Hendrik </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;2008-2017</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;38</font></td></tr>
<tr bgcolor=#FFFFFF>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2325</font></td>
<td>&nbsp;<img src="/chessimages/book.gif" alt="biography" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=64340"><B>ANDREASEN, Per Naesby </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;1984-2013</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;57</font></td></tr>
<tr bgcolor=#FFEEDD>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2233</font></td>
<td>&nbsp;</td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=108843"><B>ANDREASSEN, Lars </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;2006-2007</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;26</font></td></tr>
<tr bgcolor=#FFFFFF>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2370</font></td>
<td>&nbsp;</td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=18388"><B>ANDREASSON, Ingvar </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;1983-2021</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;34</font></td></tr>
<tr bgcolor=#FFEEDD>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2514</font></td>
<td><img src="/chessimages/chat.gif" alt="2" width=16 height=16><img src="/chessimages/book.gif" alt="biography" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=56967"><B>ANDREEV, Eduard </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;1994-2020</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;179</font></td></tr>
<tr bgcolor=#FFFFFF>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2250</font></td>
<td>&nbsp;<img src="/chessimages/book.gif" alt="biography" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=25414"><B>ANDREIEVA, Olga A </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;1966-1990</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;17</font></td></tr>
<tr bgcolor=#FFEEDD>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2736</font></td>
<td><img src="/chessimages/chat.gif" alt="112" width=16 height=16><img src="/chessimages/book.gif" alt="biography" width=16 height=16><a href="/audio/49702.mp3"><img src="/chessimages/speaker.gif" alt="pronunciation" width=16 height=16 border=0></a></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=49702"><B>ANDREIKIN, Dmitry </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;1999-2022</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;1,382</font></td></tr>
<tr bgcolor=#FFFFFF>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2287</font></td>
<td>&nbsp;<img src="/chessimages/book.gif" alt="biography" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=118874"><B>ANDREJIC, Vladica </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;2004-2016</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;33</font></td></tr>
<tr bgcolor=#FFEEDD>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2272</font></td>
<td>&nbsp;<img src="/chessimages/book.gif" alt="biography" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=109950"><B>ANDRENKO, Irina </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;2007-2017</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;55</font></td></tr>
<tr bgcolor=#FFFFFF>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2316</font></td>
<td>&nbsp;</td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=14259"><B>ANDRESEN, Steffen </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;1984-2012</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;15</font></td></tr>
<tr bgcolor=#FFEEDD>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2398</font></td>
<td>&nbsp;</td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=90474"><B>ANDRESEN, Tarald </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;1997-2000</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;17</font></td></tr>
<tr bgcolor=#FFFFFF>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2375</font></td>
<td><img src="/chessimages/chat.gif" alt="3" width=16 height=16><img src="/chessimages/book.gif" alt="biography" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=135504"><B>ANDREU, Eric Sos </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;2012-2021</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;45</font></td></tr>
<tr bgcolor=#FFEEDD>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2337</font></td>
<td><img src="/chessimages/chat.gif" alt="2" width=16 height=16><img src="/chessimages/book.gif" alt="biography" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=57160"><B>ANDREWS, Todd D </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;1996-2018</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;40</font></td></tr>
<tr bgcolor=#FFFFFF>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2255</font></td>
<td><img src="/chessimages/chat.gif" alt="1" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=27235"><B>ANDREWS, Randal </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;1985-1991</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2</font></td></tr>
<tr bgcolor=#FFEEDD>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2439</font></td>
<td><img src="/chessimages/chat.gif" alt="8" width=16 height=16><img src="/chessimages/book.gif" alt="biography" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=16922"><B>ANDRIANOV, Nikolai </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;1978-2021</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;165</font></td></tr>
<tr bgcolor=#FFFFFF>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2645</font></td>
<td><img src="/chessimages/chat.gif" alt="42" width=16 height=16><img src="/chessimages/book.gif" alt="biography" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=84227"><B>ANDRIASIAN, Zaven </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;1998-2022</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;1,374</font></td></tr>
<tr bgcolor=#FFEEDD>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2298</font></td>
<td><img src="/chessimages/chat.gif" alt="6" width=16 height=16><img src="/chessimages/book.gif" alt="biography" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=54822"><B>ANDRIASYAN, Siranush </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;1996-2017</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;129</font></td></tr>
<tr bgcolor=#FFFFFF>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2384</font></td>
<td>&nbsp;<img src="/chessimages/book.gif" alt="biography" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=28765"><B>ANDRIJEVIC, Milan </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;1980-2015</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;67</font></td></tr>
<tr bgcolor=#FFEEDD>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2430</font></td>
<td><img src="/chessimages/chat.gif" alt="12" width=16 height=16><img src="/chessimages/book.gif" alt="biography" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=27012"><B>ANDRUET, Gilles </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;1981-1995</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;521</font></td></tr>
<tr bgcolor=#FFFFFF>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2343</font></td>
<td>&nbsp;<img src="/chessimages/book.gif" alt="biography" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=88541"><B>ANDUJAR, William Staling Puntier </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;2001-2014</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;33</font></td></tr>
<tr bgcolor=#FFEEDD>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2390</font></td>
<td><img src="/chessimages/chat.gif" alt="2" width=16 height=16><img src="/chessimages/book.gif" alt="biography" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=127100"><B>ANDYKA, Pitra </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;2010-2019</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;55</font></td></tr>
<tr bgcolor=#FFFFFF>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2303</font></td>
<td>&nbsp;<img src="/chessimages/book.gif" alt="biography" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=68303"><B>ANELLI, Antonio </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;1972-2017</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;34</font></td></tr>
<tr bgcolor=#FFEEDD>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2271</font></td>
<td>&nbsp;<img src="/chessimages/book.gif" alt="biography" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=148813"><B>ANG, Alphaeus Wei Ern </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;2013-2018</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;83</font></td></tr>
<tr bgcolor=#FFFFFF>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2295</font></td>
<td><img src="/chessimages/chat.gif" alt="8" width=16 height=16><img src="/chessimages/book.gif" alt="biography" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=22462"><B>ANGANTYSSON, Haukur </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;1968-1993</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;82</font></td></tr>
<tr bgcolor=#FFEEDD>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2292</font></td>
<td><img src="/chessimages/chat.gif" alt="3" width=16 height=16><img src="/chessimages/book.gif" alt="biography" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=28323"><B>ANGELOV, Kosta </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;1971-2013</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;26</font></td></tr>
<tr bgcolor=#FFFFFF>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2246</font></td>
<td>&nbsp;</td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=55915"><B>ANGELOV, Angel Valeviev </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;1972-2010</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;16</font></td></tr>
<tr bgcolor=#FFEEDD>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2230</font></td>
<td><img src="/chessimages/chat.gif" alt="1" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=17727"><B>ANGQVIST, Thore </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;1990</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;1</font></td></tr>
<tr bgcolor=#FFFFFF>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2271</font></td>
<td>&nbsp;</td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=89785"><B>ANGSKOG, Kent </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;1991-2016</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;34</font></td></tr>
<tr bgcolor=#FFEEDD>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2469</font></td>
<td><img src="/chessimages/chat.gif" alt="6" width=16 height=16><img src="/chessimages/book.gif" alt="biography" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=17308"><B>ANIC, Darko </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;1988-2015</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;119</font></td></tr>
<tr bgcolor=#FFFFFF>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2455</font></td>
<td><img src="/chessimages/chat.gif" alt="4" width=16 height=16><img src="/chessimages/book.gif" alt="biography" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=42272"><B>ANIKAEV, Yuri N </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;1967-2010</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;176</font></td></tr>
<tr bgcolor=#FFEEDD>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2403</font></td>
<td>&nbsp;<img src="/chessimages/book.gif" alt="biography" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=152856"><B>ANIKONOV, Dmitry </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;2015-2019</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;70</font></td></tr>
<tr bgcolor=#FFFFFF>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2340</font></td>
<td>&nbsp;<img src="/chessimages/book.gif" alt="biography" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=40423"><B>ANILKUMAR, N R </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;1982-2001</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;15</font></td></tr>
<tr bgcolor=#FFEEDD>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2541</font></td>
<td><img src="/chessimages/chat.gif" alt="1" width=16 height=16><img src="/chessimages/book.gif" alt="biography" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=49079"><B>ANISIMOV, Pavel </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;1996-2021</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;238</font></td></tr>
<tr bgcolor=#FFFFFF>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2487</font></td>
<td><img src="/chessimages/chat.gif" alt="8" width=16 height=16><img src="/chessimages/book.gif" alt="biography" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=18196"><B>ANKA, Emil </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;1988-2007</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;127</font></td></tr>
<tr bgcolor=#FFEEDD>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2210</font></td>
<td>&nbsp;</td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=85384"><B>ANKERST, Marjan </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;1961-1965</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;20</font></td></tr>
<tr bgcolor=#FFFFFF>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2370</font></td>
<td>&nbsp;<img src="/chessimages/book.gif" alt="biography" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=102849"><B>ANKERST, Mihael </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;1992-2004</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;50</font></td></tr>
<tr bgcolor=#FFEEDD>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2511</font></td>
<td>&nbsp;<img src="/chessimages/book.gif" alt="biography" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=117473"><B>ANKIT, R Rajpara </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;2008-2019</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;99</font></td></tr>
<tr bgcolor=#FFFFFF>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2243</font></td>
<td><img src="/chessimages/chat.gif" alt="1" width=16 height=16><img src="/chessimages/book.gif" alt="biography" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=88958"><B>ANKUDINOVA, Yelena </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;2004-2017</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;25</font></td></tr>
<tr bgcolor=#FFEEDD>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2532</font></td>
<td><img src="/chessimages/chat.gif" alt="3" width=16 height=16><img src="/chessimages/book.gif" alt="biography" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=53982"><B>ANNABERDIEV, Meilis </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;2001-2021</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;167</font></td></tr>
<tr bgcolor=#FFFFFF>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2503</font></td>
<td><img src="/chessimages/chat.gif" alt="7" width=16 height=16><img src="/chessimages/book.gif" alt="biography" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=53020"><B>ANNAGELDYEV, Orazly </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;1987-2016</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;132</font></td></tr>
<tr bgcolor=#FFEEDD>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2527</font></td>
<td><img src="/chessimages/chat.gif" alt="4" width=16 height=16><img src="/chessimages/book.gif" alt="biography" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=19874"><B>ANNAKOV, Babakuli </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;1991-2004</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;87</font></td></tr>
<tr bgcolor=#FFFFFF>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2280</font></td>
<td>&nbsp;<img src="/chessimages/book.gif" alt="biography" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=156478"><B>ANSAT, Aldiyar </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;2016-2022</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;46</font></td></tr>
<tr bgcolor=#FFEEDD>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2427</font></td>
<td><img src="/chessimages/chat.gif" alt="1" width=16 height=16><img src="/chessimages/book.gif" alt="biography" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=39710"><B>ANSELL, Simon T </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;1990-2019</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;363</font></td></tr>
<tr bgcolor=#FFFFFF>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2571</font></td>
<td><img src="/chessimages/chat.gif" alt="3" width=16 height=16><img src="/chessimages/book.gif" alt="biography" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=50407"><B>ANTAL, Gergely </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;1995-2021</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;268</font></td></tr>
<tr bgcolor=#FFEEDD>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2424</font></td>
<td><img src="/chessimages/chat.gif" alt="1" width=16 height=16><img src="/chessimages/book.gif" alt="biography" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=117586"><B>ANTAL, Tibor Kende </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;2008-2021</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;113</font></td></tr>
<tr bgcolor=#FFFFFF>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2523</font></td>
<td><img src="/chessimages/chat.gif" alt="8" width=16 height=16><img src="/chessimages/book.gif" alt="biography" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=28784"><B>ANTIC, Dejan </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;1988-2019</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;253</font></td></tr>
<tr bgcolor=#FFEEDD>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2216</font></td>
<td>&nbsp;</td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=133386"><B>ANTINYAN, Armen </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;2011-2014</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;31</font></td></tr>
<tr bgcolor=#FFFFFF>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2626</font></td>
<td><img src="/chessimages/chat.gif" alt="16" width=16 height=16><img src="/chessimages/book.gif" alt="biography" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=121886"><B>ANTIPOV, Mikhail </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;2007-2022</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;750</font></td></tr>
<tr bgcolor=#FFEEDD>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2340</font></td>
<td>&nbsp;<img src="/chessimages/book.gif" alt="biography" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=161904"><B>ANTO, Cristiano F Manish </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;2018-2021</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;152</font></td></tr>
<tr bgcolor=#FFFFFF>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2286</font></td>
<td>&nbsp;</td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=50230"><B>ANTOGNINI, Francesco </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;2000-2016</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;29</font></td></tr>
<tr bgcolor=#FFEEDD>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2227</font></td>
<td><img src="/chessimages/chat.gif" alt="1" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=54255"><B>ANTOK, Daniel </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;2001-2009</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;6</font></td></tr>
<tr bgcolor=#FFFFFF>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2323</font></td>
<td><img src="/chessimages/chat.gif" alt="1" width=16 height=16><img src="/chessimages/book.gif" alt="biography" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=142127"><B>ANTOLAK, Julia </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;2012-2021</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;83</font></td></tr>
<tr bgcolor=#FFEEDD>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2486</font></td>
<td>&nbsp;<img src="/chessimages/book.gif" alt="biography" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=56992"><B>ANTOMS, Guntars </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;1978-2019</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;32</font></td></tr>
<tr bgcolor=#FFFFFF>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2464</font></td>
<td><img src="/chessimages/chat.gif" alt="1" width=16 height=16><img src="/chessimages/book.gif" alt="biography" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=115568"><B>ANTON, Teodor </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;2001-2016</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;108</font></td></tr>
<tr bgcolor=#FFEEDD>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2630</font></td>
<td><img src="/chessimages/chat.gif" alt="2" width=16 height=16><img src="/chessimages/book.gif" alt="biography" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=90140"><B>ANTON, Volker-Michael </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;1984-1996</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;25</font></td></tr>
<tr bgcolor=#FFFFFF>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2391</font></td>
<td>&nbsp;<img src="/chessimages/book.gif" alt="biography" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=158689"><B>ANTONENKO, Vladimir </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;2017-2019</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;18</font></td></tr>
<tr bgcolor=#FFEEDD>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2614</font></td>
<td><img src="/chessimages/chat.gif" alt="4" width=16 height=16><img src="/chessimages/book.gif" alt="biography" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=55107"><B>ANTONIEWSKI, Rafal </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;1993-2021</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;238</font></td></tr>
<tr bgcolor=#FFFFFF>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2435</font></td>
<td>&nbsp;<img src="/chessimages/book.gif" alt="biography" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=117407"><B>ANTONIO, Viani D'cunha </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;2008-2020</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;84</font></td></tr>
<tr bgcolor=#FFEEDD>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2231</font></td>
<td>&nbsp;<img src="/chessimages/book.gif" alt="biography" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=57004"><B>ANTONIOU, Antonis </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;1994-2017</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;102</font></td></tr>
<tr bgcolor=#FFFFFF>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2345</font></td>
<td><img src="/chessimages/chat.gif" alt="2" width=16 height=16><img src="/chessimages/book.gif" alt="biography" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=59574"><B>ANTONOV, Vladimir </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;1969-2003</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;34</font></td></tr>
<tr bgcolor=#FFEEDD>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2568</font></td>
<td><img src="/chessimages/chat.gif" alt="4" width=16 height=16><img src="/chessimages/book.gif" alt="biography" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=29087"><B>ANTONSEN, Mikkel </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;1988-2021</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;153</font></td></tr>
<tr bgcolor=#FFFFFF>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2335</font></td>
<td>&nbsp;<img src="/chessimages/book.gif" alt="biography" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=150465"><B>ANTOVA, Gabriela </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;2014-2022</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;171</font></td></tr>
<tr bgcolor=#FFEEDD>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2412</font></td>
<td><img src="/chessimages/chat.gif" alt="3" width=16 height=16><img src="/chessimages/book.gif" alt="biography" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=14903"><B>ANTUNAC, Goran </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;1963-2018</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;81</font></td></tr>
<tr bgcolor=#FFFFFF>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2545</font></td>
<td><img src="/chessimages/chat.gif" alt="9" width=16 height=16><img src="/chessimages/book.gif" alt="biography" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=16998"><B>ANTUNES, Antonio </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;1980-2000</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;584</font></td></tr>
<tr bgcolor=#FFEEDD>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2376</font></td>
<td><img src="/chessimages/chat.gif" alt="1" width=16 height=16><img src="/chessimages/book.gif" alt="biography" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=157881"><B>ANUJ, Shrivatri </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;2017-2020</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;22</font></td></tr>
<tr bgcolor=#FFFFFF>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2305</font></td>
<td><img src="/chessimages/chat.gif" alt="2" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=99247"><B>ANWAR, Shazuli Syed </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;1999-2009</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;18</font></td></tr>
<tr bgcolor=#FFEEDD>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2429</font></td>
<td><img src="/chessimages/chat.gif" alt="4" width=16 height=16><img src="/chessimages/book.gif" alt="biography" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=124943"><B>ANWESH, Upadhyaya </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;2008-2017</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;104</font></td></tr>
<tr bgcolor=#FFFFFF>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2336</font></td>
<td><img src="/chessimages/chat.gif" alt="2" width=16 height=16><img src="/chessimages/book.gif" alt="biography" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=155268"><B>ANWULI, Daniel </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;2016-2019</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;22</font></td></tr>
<tr bgcolor=#FFEEDD>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2291</font></td>
<td><img src="/chessimages/chat.gif" alt="1" width=16 height=16><img src="/chessimages/book.gif" alt="biography" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=20694"><B>APARICIO, Anibal </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;1973-2012</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;61</font></td></tr>
<tr bgcolor=#FFFFFF>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2353</font></td>
<td>&nbsp;</td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=91831"><B>APAYDIN, Fethi </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;2002-2022</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;55</font></td></tr>
<tr bgcolor=#FFEEDD>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2352</font></td>
<td>&nbsp;<img src="/chessimages/book.gif" alt="biography" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=139377"><B>APECHECHE, Yanira Vigoa </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;2010-2014</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;20</font></td></tr>
<tr bgcolor=#FFFFFF>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2555</font></td>
<td><img src="/chessimages/chat.gif" alt="23" width=16 height=16><img src="/chessimages/book.gif" alt="biography" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=27273"><B>APICELLA, Manuel </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;1984-2019</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;470</font></td></tr>
<tr bgcolor=#FFEEDD>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2455</font></td>
<td><img src="/chessimages/chat.gif" alt="2" width=16 height=16><img src="/chessimages/book.gif" alt="biography" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=115448"><B>APONTE, Felix Jose Ynojosa </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;2008-2020</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;140</font></td></tr>
<tr bgcolor=#FFFFFF>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2552</font></td>
<td><img src="/chessimages/chat.gif" alt="7" width=16 height=16><img src="/chessimages/book.gif" alt="biography" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=26324"><B>APPEL, Ralf </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;1989-2016</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;245</font></td></tr>
<tr bgcolor=#FFEEDD>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2301</font></td>
<td><img src="/chessimages/chat.gif" alt="29" width=16 height=16><img src="/chessimages/book.gif" alt="biography" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=22093"><B>APPLEBERRY, Martin </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;1971-2004</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;42</font></td></tr>
<tr bgcolor=#FFFFFF>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2392</font></td>
<td>&nbsp;<img src="/chessimages/book.gif" alt="biography" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=141598"><B>APRYSHKO, Gleb </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;2012-2020</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;73</font></td></tr>
<tr bgcolor=#FFEEDD>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;&nbsp;</font></td>
<td><img src="/chessimages/chat.gif" alt="7" width=16 height=16><img src="/chessimages/book.gif" alt="biography" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=13351"><B>APSENIEKS, Fricis </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;1913-1941</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;264</font></td></tr>
<tr bgcolor=#FFFFFF>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2240</font></td>
<td><img src="/chessimages/chat.gif" alt="8" width=16 height=16><img src="/chessimages/book.gif" alt="biography" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=81202"><B>APTEKAR, Lev </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;1963-1983</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;55</font></td></tr>
<tr bgcolor=#FFEEDD>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2487</font></td>
<td><img src="/chessimages/chat.gif" alt="5" width=16 height=16><img src="/chessimages/book.gif" alt="biography" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=79493"><B>ARAB, Adlane </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;2000-2018</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;53</font></td></tr>
<tr bgcolor=#FFFFFF>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2428</font></td>
<td><img src="/chessimages/chat.gif" alt="18" width=16 height=16><img src="/chessimages/book.gif" alt="biography" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=118082"><B>ARABIDZE, Meri </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;2007-2022</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;476</font></td></tr>
<tr bgcolor=#FFEEDD>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2316</font></td>
<td><img src="/chessimages/chat.gif" alt="1" width=16 height=16><img src="/chessimages/book.gif" alt="biography" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=151614"><B>ARADHYA, Garg </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;2014-2021</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;103</font></td></tr>
<tr bgcolor=#FFFFFF>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2384</font></td>
<td><img src="/chessimages/chat.gif" alt="7" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=50179"><B>ARAKELOV, Ilya </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;1995-2009</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;31</font></td></tr>
<tr bgcolor=#FFEEDD>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2307</font></td>
<td><img src="/chessimages/chat.gif" alt="1" width=16 height=16><img src="/chessimages/book.gif" alt="biography" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=42683"><B>ARAMBEL, Sergio Javier </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;1994-2006</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;29</font></td></tr>
<tr bgcolor=#FFFFFF>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2280</font></td>
<td><img src="/chessimages/chat.gif" alt="9" width=16 height=16><img src="/chessimages/book.gif" alt="biography" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=78843"><B>ARAMIL, William J </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;1999-2014</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;54</font></td></tr>
<tr bgcolor=#FFEEDD>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2511</font></td>
<td><img src="/chessimages/chat.gif" alt="2" width=16 height=16><img src="/chessimages/book.gif" alt="biography" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=130706"><B>ARANDA, Angel Espinosa </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;2003-2022</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;240</font></td></tr>
<tr bgcolor=#FFFFFF>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2286</font></td>
<td><img src="/chessimages/chat.gif" alt="1" width=16 height=16><img src="/chessimages/book.gif" alt="biography" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=138437"><B>ARANGUREN, Alain Prieto </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;2012-2017</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;11</font></td></tr>
<tr bgcolor=#FFEEDD>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2402</font></td>
<td><img src="/chessimages/chat.gif" alt="3" width=16 height=16><img src="/chessimages/book.gif" alt="biography" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=109895"><B>ARANOVITCH, Emiliano </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;1995-2021</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;29</font></td></tr>
<tr bgcolor=#FFFFFF>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2437</font></td>
<td><img src="/chessimages/chat.gif" alt="4" width=16 height=16><img src="/chessimages/book.gif" alt="biography" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=17644"><B>ARAPOVIC, Vitomir </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;1974-2021</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;272</font></td></tr>
<tr bgcolor=#FFEEDD>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2388</font></td>
<td>&nbsp;<img src="/chessimages/book.gif" alt="biography" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=49420"><B>ARAQUE, Rafael </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;1991-2001</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;29</font></td></tr>
<tr bgcolor=#FFFFFF>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2441</font></td>
<td><img src="/chessimages/chat.gif" alt="3" width=16 height=16><img src="/chessimages/book.gif" alt="biography" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=117663"><B>ARAT, Ufuk Sezen </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;2008-2017</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;93</font></td></tr>
<tr bgcolor=#FFEEDD>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2258</font></td>
<td>&nbsp;<img src="/chessimages/book.gif" alt="biography" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=168267"><B>ARAUJO, Adalberto Marcos </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;2003-2005</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;18</font></td></tr>
<tr bgcolor=#FFFFFF>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2641</font></td>
<td><img src="/chessimages/chat.gif" alt="39" width=16 height=16><img src="/chessimages/book.gif" alt="biography" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=131329"><B>ARAVINDH, Chithambaram V R </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;2011-2021</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;592</font></td></tr>
<tr bgcolor=#FFEEDD>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2266</font></td>
<td><img src="/chessimages/chat.gif" alt="1" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=86169"><B>ARAY, Asrul </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;2000</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;1</font></td></tr>
<tr bgcolor=#FFFFFF>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2500</font></td>
<td><img src="/chessimages/chat.gif" alt="15" width=16 height=16><img src="/chessimages/book.gif" alt="biography" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=18122"><B>ARBAKOV, Valentin </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;1966-2003</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;246</font></td></tr>
<tr bgcolor=#FFEEDD>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2270</font></td>
<td>&nbsp;<img src="/chessimages/book.gif" alt="biography" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=44528"><B>ARBOUCHE, Muhamed </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;1986-2008</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;26</font></td></tr>
<tr bgcolor=#FFFFFF>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2395</font></td>
<td><img src="/chessimages/chat.gif" alt="1" width=16 height=16><img src="/chessimages/book.gif" alt="biography" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=25922"><B>ARCHANGELSKY, Mikhail </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;1992-2016</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;42</font></td></tr>
<tr bgcolor=#FFEEDD>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2220</font></td>
<td>&nbsp;<img src="/chessimages/book.gif" alt="biography" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=155524"><B>ARCHIBALDO, Orlando Andres Leon </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;2016-2022</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;28</font></td></tr>
<tr bgcolor=#FFFFFF>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2356</font></td>
<td>&nbsp;<img src="/chessimages/book.gif" alt="biography" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=155361"><B>ARCHIBOLD, Nestor Cofre </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;2016-2018</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;19</font></td></tr>
<tr bgcolor=#FFEEDD>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2396</font></td>
<td><img src="/chessimages/chat.gif" alt="1" width=16 height=16><img src="/chessimages/book.gif" alt="biography" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=20984"><B>ARCIJA, Diego Pereyra </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;1991-2004</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;46</font></td></tr>
<tr bgcolor=#FFFFFF>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2380</font></td>
<td>&nbsp;</td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=139967"><B>ARCUTI, Davide </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;2012-2021</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;24</font></td></tr>
<tr bgcolor=#FFEEDD>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2257</font></td>
<td><img src="/chessimages/chat.gif" alt="2" width=16 height=16><img src="/chessimages/book.gif" alt="biography" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=140302"><B>ARDA, Cagil Irmak </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;2012-2018</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;53</font></td></tr>
<tr bgcolor=#FFFFFF>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2432</font></td>
<td><img src="/chessimages/chat.gif" alt="3" width=16 height=16><img src="/chessimages/book.gif" alt="biography" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=63606"><B>ARDAMAN, Miles </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;1983-2016</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;198</font></td></tr>
<tr bgcolor=#FFEEDD>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2526</font></td>
<td><img src="/chessimages/chat.gif" alt="2" width=16 height=16><img src="/chessimages/book.gif" alt="biography" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=49389"><B>ARDELEAN, George-Catalin </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;1995-2018</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;68</font></td></tr>
<tr bgcolor=#FFFFFF>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2443</font></td>
<td>&nbsp;<img src="/chessimages/book.gif" alt="biography" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=74125"><B>ARDELEANU, Alin </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;1992-2014</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;69</font></td></tr>
<tr bgcolor=#FFEEDD>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2421</font></td>
<td><img src="/chessimages/chat.gif" alt="1" width=16 height=16><img src="/chessimages/book.gif" alt="biography" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=52595"><B>ARDESHI, Mehrdad </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;2001-2007</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;29</font></td></tr>
<tr bgcolor=#FFFFFF>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2304</font></td>
<td>&nbsp;</td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=132900"><B>ARDIAN, Jashari </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;2011-2021</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;17</font></td></tr>
<tr bgcolor=#FFEEDD>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2430</font></td>
<td><img src="/chessimages/chat.gif" alt="8" width=16 height=16><img src="/chessimages/book.gif" alt="biography" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=14348"><B>ARDIANSYAH, Haji </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;1969-2012</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;265</font></td></tr>
<tr bgcolor=#FFFFFF>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2379</font></td>
<td><img src="/chessimages/chat.gif" alt="2" width=16 height=16><img src="/chessimages/book.gif" alt="biography" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=28194"><B>ARDUMAN, Can </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;1981-2012</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;129</font></td></tr>
<tr bgcolor=#FFEEDD>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2496</font></td>
<td><img src="/chessimages/chat.gif" alt="3" width=16 height=16><img src="/chessimages/book.gif" alt="biography" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=118551"><B>ARENAS, David </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;2008-2022</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;84</font></td></tr>
<tr bgcolor=#FFFFFF>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2435</font></td>
<td><img src="/chessimages/chat.gif" alt="1" width=16 height=16><img src="/chessimages/book.gif" alt="biography" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=39707"><B>ARENCIBIA, Juan Joel </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;1987-2001</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;24</font></td></tr>
<tr bgcolor=#FFEEDD>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2720</font></td>
<td><img src="/chessimages/chat.gif" alt="32" width=16 height=16><img src="/chessimages/book.gif" alt="biography" width=16 height=16><a href="/audio/10862.mp3"><img src="/chessimages/speaker.gif" alt="pronunciation" width=16 height=16 border=0></a></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=10862"><B>ARESHCHENKO, Alexander </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;1996-2022</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;935</font></td></tr>
<tr bgcolor=#FFFFFF>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2231</font></td>
<td>&nbsp;<img src="/chessimages/book.gif" alt="biography" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=54831"><B>ARESHCHENKO, Kateryna </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;2000-2009</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;19</font></td></tr>
<tr bgcolor=#FFEEDD>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2324</font></td>
<td>&nbsp;<img src="/chessimages/book.gif" alt="biography" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=52329"><B>ARESTANOV, Timur </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;2001-2016</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;15</font></td></tr>
<tr bgcolor=#FFFFFF>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2406</font></td>
<td>&nbsp;<img src="/chessimages/book.gif" alt="biography" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=51404"><B>ARIAS, Lemnys Antonio </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;2001-2022</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;106</font></td></tr>
<tr bgcolor=#FFEEDD>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2311</font></td>
<td><img src="/chessimages/chat.gif" alt="2" width=16 height=16><img src="/chessimages/book.gif" alt="biography" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=140159"><B>ARIAS, Daniel </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;2012-2020</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;43</font></td></tr>
<tr bgcolor=#FFFFFF>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2389</font></td>
<td><img src="/chessimages/chat.gif" alt="8" width=16 height=16><img src="/chessimages/book.gif" alt="biography" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=36732"><B>ARIEL, Donny </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;1994-2011</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;38</font></td></tr>
<tr bgcolor=#FFEEDD>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2284</font></td>
<td><img src="/chessimages/chat.gif" alt="1" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=134830"><B>ARIPOV, Iskandar </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;2009-2021</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;10</font></td></tr>
<tr bgcolor=#FFFFFF>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2477</font></td>
<td><img src="/chessimages/chat.gif" alt="5" width=16 height=16><img src="/chessimages/book.gif" alt="biography" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=155085"><B>ARJUN, Kalyan </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;2015-2021</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;145</font></td></tr>
<tr bgcolor=#FFEEDD>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2283</font></td>
<td><img src="/chessimages/chat.gif" alt="1" width=16 height=16><img src="/chessimages/book.gif" alt="biography" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=103945"><B>ARJUN, Vishnuvardhan </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;2002-2018</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;20</font></td></tr>
<tr bgcolor=#FFFFFF>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2545</font></td>
<td><img src="/chessimages/chat.gif" alt="45" width=16 height=16><img src="/chessimages/book.gif" alt="biography" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=13774"><B>ARKELL, Keith </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;1977-2022</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;1,152</font></td></tr>
<tr bgcolor=#FFEEDD>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2416</font></td>
<td><img src="/chessimages/chat.gif" alt="3" width=16 height=16><img src="/chessimages/book.gif" alt="biography" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=45269"><B>ARKHANGELSKY, Boris </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;1979-2008</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;75</font></td></tr>
<tr bgcolor=#FFFFFF>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2249</font></td>
<td>&nbsp;</td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=32972"><B>ARKHIPKIN, Yury </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;1971-1988</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;25</font></td></tr>
<tr bgcolor=#FFEEDD>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2540</font></td>
<td><img src="/chessimages/chat.gif" alt="3" width=16 height=16><img src="/chessimages/book.gif" alt="biography" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=16948"><B>ARKHIPOV, Sergey </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;1964-2016</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;238</font></td></tr>
<tr bgcolor=#FFFFFF>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2458</font></td>
<td><img src="/chessimages/chat.gif" alt="3" width=16 height=16><img src="/chessimages/book.gif" alt="biography" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=16258"><B>ARLANDI, Ennio </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;1981-2014</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;495</font></td></tr>
<tr bgcolor=#FFEEDD>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2386</font></td>
<td><img src="/chessimages/chat.gif" alt="1" width=16 height=16><img src="/chessimages/book.gif" alt="biography" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=92045"><B>ARMAN, Deniz </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;2001-2021</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;70</font></td></tr>
<tr bgcolor=#FFFFFF>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2399</font></td>
<td>&nbsp;<img src="/chessimages/book.gif" alt="biography" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=55618"><B>ARMANDA, Ivica </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;1992-2013</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;62</font></td></tr>
<tr bgcolor=#FFEEDD>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2440</font></td>
<td><img src="/chessimages/chat.gif" alt="3" width=16 height=16><img src="/chessimages/book.gif" alt="biography" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=83066"><B>ARMAS, Julius </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;1977-2007</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;67</font></td></tr>
<tr bgcolor=#FFFFFF>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2326</font></td>
<td>&nbsp;<img src="/chessimages/book.gif" alt="biography" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=95751"><B>ARMBRUST, Florian </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;2005-2014</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;25</font></td></tr>
<tr bgcolor=#FFEEDD>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;&nbsp;</font></td>
<td><img src="/chessimages/chat.gif" alt="7" width=16 height=16><img src="/chessimages/book.gif" alt="biography" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=36978"><B>ARNAL, Angel Ribera </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;1927-1957</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;54</font></td></tr>
<tr bgcolor=#FFFFFF>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2555</font></td>
<td><img src="/chessimages/chat.gif" alt="15" width=16 height=16><img src="/chessimages/book.gif" alt="biography" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=13837"><B>ARNASON, Jon </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;1977-2017</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;599</font></td></tr>
<tr bgcolor=#FFEEDD>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2242</font></td>
<td>&nbsp;</td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=96127"><B>ARNASON, Asgeir Thor </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;1978-2004</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;61</font></td></tr>
<tr bgcolor=#FFFFFF>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2291</font></td>
<td>&nbsp;<img src="/chessimages/book.gif" alt="biography" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=28120"><B>ARNASON, Throstur </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;1982-2017</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;60</font></td></tr>
<tr bgcolor=#FFEEDD>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2276</font></td>
<td>&nbsp;</td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=34422"><B>ARNAUDOV, Petar </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;1967-2013</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;78</font></td></tr>
<tr bgcolor=#FFFFFF>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2492</font></td>
<td><img src="/chessimages/chat.gif" alt="4" width=16 height=16><img src="/chessimages/book.gif" alt="biography" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=106854"><B>ARNAUDOV, G Petar </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;2005-2021</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;237</font></td></tr>
<tr bgcolor=#FFEEDD>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2262</font></td>
<td>&nbsp;</td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=105860"><B>ARNDT, Stefan </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;1987-2001</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;67</font></td></tr>
<tr bgcolor=#FFFFFF>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2311</font></td>
<td><img src="/chessimages/chat.gif" alt="2" width=16 height=16><img src="/chessimages/book.gif" alt="biography" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=16863"><B>ARNETT, David A </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;1992-2000</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;14</font></td></tr>
<tr bgcolor=#FFEEDD>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2404</font></td>
<td><img src="/chessimages/chat.gif" alt="2" width=16 height=16><img src="/chessimages/book.gif" alt="biography" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=56539"><B>ARNGRIMSSON, Dagur </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;1999-2021</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;317</font></td></tr>
<tr bgcolor=#FFFFFF>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2431</font></td>
<td><img src="/chessimages/chat.gif" alt="1" width=16 height=16><img src="/chessimages/book.gif" alt="biography" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=43412"><B>ARNOLD, Lothar </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;1976-2008</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;80</font></td></tr>
<tr bgcolor=#FFEEDD>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2540</font></td>
<td><img src="/chessimages/chat.gif" alt="15" width=16 height=16><img src="/chessimages/book.gif" alt="biography" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=57309"><B>ARNOLD, Marc Tyler </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;2001-2018</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;168</font></td></tr>
<tr bgcolor=#FFFFFF>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2830</font></td>
<td><img src="/chessimages/chat.gif" alt="3687" width=16 height=16><img src="/chessimages/book.gif" alt="biography" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=17316"><B>ARONIAN, Levon </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;1993-2022</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;3,614</font></td></tr>
<tr bgcolor=#FFEEDD>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;&nbsp;</font></td>
<td><img src="/chessimages/chat.gif" alt="33" width=16 height=16><img src="/chessimages/book.gif" alt="biography" width=16 height=16><a href="/audio/16535.mp3"><img src="/chessimages/speaker.gif" alt="pronunciation" width=16 height=16 border=0></a></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=16535"><B>ARONIN, Lev </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;1940-1969</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;328</font></td></tr>
<tr bgcolor=#FFFFFF>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2229</font></td>
<td>&nbsp;</td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=126849"><B>ARONOV, Yuri </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;1995-2011</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;17</font></td></tr>
<tr bgcolor=#FFEEDD>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;&nbsp;</font></td>
<td><img src="/chessimages/chat.gif" alt="8" width=16 height=16><img src="/chessimages/book.gif" alt="biography" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=17385"><B>ARONSON, Lev </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;1947-1977</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;56</font></td></tr>
<tr bgcolor=#FFFFFF>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2396</font></td>
<td>&nbsp;</td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=154519"><B>ARONSSON, Marten </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;2016-2018</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;15</font></td></tr>
<tr bgcolor=#FFEEDD>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2436</font></td>
<td><img src="/chessimages/chat.gif" alt="1" width=16 height=16><img src="/chessimages/book.gif" alt="biography" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=160798"><B>ARONYAK, Ghosh </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;2018-2021</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;35</font></td></tr>
<tr bgcolor=#FFFFFF>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2206</font></td>
<td><img src="/chessimages/chat.gif" alt="1" width=16 height=16><img src="/chessimages/book.gif" alt="biography" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=38146"><B>AROSEMENA, Jorge Luis </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;1985-2012</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;44</font></td></tr>
<tr bgcolor=#FFEEDD>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2582</font></td>
<td><img src="/chessimages/chat.gif" alt="8" width=16 height=16><img src="/chessimages/book.gif" alt="biography" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=50109"><B>AROSHIDZE, Levan </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;1996-2020</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;196</font></td></tr>
<tr bgcolor=#FFFFFF>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2377</font></td>
<td>&nbsp;<img src="/chessimages/book.gif" alt="biography" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=49126"><B>AROUSY, Abdul Hameed El </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;1988-2012</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;94</font></td></tr>
<tr bgcolor=#FFEEDD>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2201</font></td>
<td>&nbsp;</td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=78530"><B>AROVEN, Mikael </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;1994-2017</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;32</font></td></tr>
<tr bgcolor=#FFFFFF>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2234</font></td>
<td>&nbsp;<img src="/chessimages/book.gif" alt="biography" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=158001"><B>ARPITA, Mukherjee </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;2016-2021</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;55</font></td></tr>
<tr bgcolor=#FFEEDD>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2375</font></td>
<td>&nbsp;<img src="/chessimages/book.gif" alt="biography" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=64321"><B>ARROS, Cristian Eduardo Salas </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;1997-2007</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;26</font></td></tr>
<tr bgcolor=#FFFFFF>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2229</font></td>
<td>&nbsp;</td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=92111"><B>ARSENAULT, Nicolas </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;2005-2010</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;34</font></td></tr>
<tr bgcolor=#FFEEDD>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2350</font></td>
<td>&nbsp;</td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=44875"><B>ARSENIEV, Vladimir V </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;1955-1968</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;29</font></td></tr>
<tr bgcolor=#FFFFFF>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2424</font></td>
<td>&nbsp;<img src="/chessimages/book.gif" alt="biography" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=118207"><B>ARSLANOV, Shamil </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;2007-2020</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;89</font></td></tr>
<tr bgcolor=#FFEEDD>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2504</font></td>
<td><img src="/chessimages/chat.gif" alt="10" width=16 height=16><img src="/chessimages/book.gif" alt="biography" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=49483"><B>ARSOVIC, Goran </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;1989-2021</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;159</font></td></tr>
<tr bgcolor=#FFFFFF>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2490</font></td>
<td><img src="/chessimages/chat.gif" alt="10" width=16 height=16><img src="/chessimages/book.gif" alt="biography" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=24883"><B>ARSOVIC, Zoran </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;1989-2021</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;154</font></td></tr>
<tr bgcolor=#FFEEDD>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2298</font></td>
<td>&nbsp;</td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=139289"><B>ARTAMONOV, Valery </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;2011-2019</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;31</font></td></tr>
<tr bgcolor=#FFFFFF>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2420</font></td>
<td><img src="/chessimages/chat.gif" alt="10" width=16 height=16><img src="/chessimages/book.gif" alt="biography" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=28698"><B>ARTEAGA, Eldis Cobo </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;1952-1978</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;333</font></td></tr>
<tr bgcolor=#FFEEDD>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2326</font></td>
<td><img src="/chessimages/chat.gif" alt="1" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=107239"><B>ARTEAGA, Daniel Uribe </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;2005-2019</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;26</font></td></tr>
<tr bgcolor=#FFFFFF>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2396</font></td>
<td>&nbsp;<img src="/chessimages/book.gif" alt="biography" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=131270"><B>ARTEMENKO, Oleg </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;2011-2020</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;24</font></td></tr>
<tr bgcolor=#FFEEDD>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2731</font></td>
<td><img src="/chessimages/chat.gif" alt="117" width=16 height=16><img src="/chessimages/book.gif" alt="biography" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=137614"><B>ARTEMIEV, Vladislav </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;2011-2022</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;1,195</font></td></tr>
<tr bgcolor=#FFFFFF>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2265</font></td>
<td><img src="/chessimages/chat.gif" alt="1" width=16 height=16><img src="/chessimages/book.gif" alt="biography" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=168839"><B>ARTERO, Guerau Masague </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;2019-2020</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;12</font></td></tr>
<tr bgcolor=#FFEEDD>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2424</font></td>
<td><img src="/chessimages/chat.gif" alt="1" width=16 height=16><img src="/chessimages/book.gif" alt="biography" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=118266"><B>ARTZI, Ido Ben </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;2008-2022</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;199</font></td></tr>
<tr bgcolor=#FFFFFF>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;&nbsp;</font></td>
<td><img src="/chessimages/chat.gif" alt="4" width=16 height=16><img src="/chessimages/book.gif" alt="biography" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=17436"><B>ARULAID, Aleksander </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;1942-1970</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;54</font></td></tr>
<tr bgcolor=#FFEEDD>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2391</font></td>
<td><img src="/chessimages/chat.gif" alt="1" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=117339"><B>ARUN, Karthik R </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;2007-2010</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;27</font></td></tr>
<tr bgcolor=#FFFFFF>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2593</font></td>
<td><img src="/chessimages/chat.gif" alt="6" width=16 height=16><img src="/chessimages/book.gif" alt="biography" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=50088"><B>ARUTINIAN, David </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;1999-2020</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;362</font></td></tr>
<tr bgcolor=#FFEEDD>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2330</font></td>
<td>&nbsp;</td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=80111"><B>ARVIND, Shastry </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;2003-2011</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;37</font></td></tr>
<tr bgcolor=#FFFFFF>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2297</font></td>
<td><img src="/chessimages/chat.gif" alt="2" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=101729"><B>ARWANITAKIS, Michael </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;1999-2006</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;10</font></td></tr>
<tr bgcolor=#FFEEDD>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2585</font></td>
<td><img src="/chessimages/chat.gif" alt="9" width=16 height=16><img src="/chessimages/book.gif" alt="biography" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=117361"><B>ARYAN, Chopra </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;2008-2022</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;150</font></td></tr>
<tr bgcolor=#FFFFFF>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2265</font></td>
<td>&nbsp;<img src="/chessimages/book.gif" alt="biography" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=98251"><B>ARYANEJAD, Hossein </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;1990-2008</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;43</font></td></tr>
<tr bgcolor=#FFEEDD>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2504</font></td>
<td><img src="/chessimages/chat.gif" alt="1" width=16 height=16><img src="/chessimages/book.gif" alt="biography" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=56969"><B>ARZUMANIAN, Georgy </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;1996-2007</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;119</font></td></tr>
<tr bgcolor=#FFFFFF>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2286</font></td>
<td><img src="/chessimages/chat.gif" alt="2" width=16 height=16><img src="/chessimages/book.gif" alt="biography" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=84009"><B>ASABRI, Hussien </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;1998-2020</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;75</font></td></tr>
<tr bgcolor=#FFEEDD>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2232</font></td>
<td>&nbsp;<img src="/chessimages/book.gif" alt="biography" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=149978"><B>ASADI, Motahare </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;2014-2020</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;24</font></td></tr>
<tr bgcolor=#FFFFFF>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2572</font></td>
<td><img src="/chessimages/chat.gif" alt="2" width=16 height=16><img src="/chessimages/book.gif" alt="biography" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=153015"><B>ASADLI, Vugar </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;2015-2022</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;390</font></td></tr>
<tr bgcolor=#FFEEDD>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2449</font></td>
<td><img src="/chessimages/chat.gif" alt="12" width=16 height=16><img src="/chessimages/book.gif" alt="biography" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=16903"><B>ASANOV, Bolat </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;1980-2017</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;76</font></td></tr>
<tr bgcolor=#FFFFFF>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2422</font></td>
<td><img src="/chessimages/chat.gif" alt="2" width=16 height=16><img src="/chessimages/book.gif" alt="biography" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=86562"><B>ASANOV, Timur </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;2001-2004</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;9</font></td></tr>
<tr bgcolor=#FFEEDD>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2345</font></td>
<td><img src="/chessimages/chat.gif" alt="1" width=16 height=16><img src="/chessimages/book.gif" alt="biography" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=36747"><B>ASAUSKAS, Henrikas </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;1998-2018</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;59</font></td></tr>
<tr bgcolor=#FFFFFF>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2280</font></td>
<td><img src="/chessimages/chat.gif" alt="2" width=16 height=16><img src="/chessimages/book.gif" alt="biography" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=106693"><B>ASCHENBRENNER, Robert </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;1999-2014</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;31</font></td></tr>
<tr bgcolor=#FFEEDD>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2396</font></td>
<td>&nbsp;<img src="/chessimages/book.gif" alt="biography" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=49221"><B>ASCIC, Pero </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;1990-2019</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;49</font></td></tr>
<tr bgcolor=#FFFFFF>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2591</font></td>
<td><img src="/chessimages/chat.gif" alt="12" width=16 height=16><img src="/chessimages/book.gif" alt="biography" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=17703"><B>ASEEV, Konstantin N </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;1980-2003</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;482</font></td></tr>
<tr bgcolor=#FFEEDD>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2222</font></td>
<td>&nbsp;</td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=60606"><B>ASEEVA, Marina </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;1992-2018</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;17</font></td></tr>
<tr bgcolor=#FFFFFF>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2357</font></td>
<td>&nbsp;<img src="/chessimages/book.gif" alt="biography" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=84540"><B>ASENDORF, Joachim </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;1991-2015</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;17</font></td></tr>
<tr bgcolor=#FFEEDD>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2245</font></td>
<td>&nbsp;<img src="/chessimages/book.gif" alt="biography" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=104450"><B>ASFORA, Marco Antonio </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;1973-2006</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;64</font></td></tr>
<tr bgcolor=#FFFFFF>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2316</font></td>
<td>&nbsp;<img src="/chessimages/book.gif" alt="biography" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=105803"><B>ASGARI, Morteza </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;2006-2019</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;19</font></td></tr>
<tr bgcolor=#FFEEDD>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2452</font></td>
<td>&nbsp;<img src="/chessimages/book.gif" alt="biography" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=143117"><B>ASGARIZADEH, Ahmad </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;2012-2019</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;89</font></td></tr>
<tr bgcolor=#FFFFFF>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2298</font></td>
<td>&nbsp;<img src="/chessimages/book.gif" alt="biography" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=126962"><B>ASGAROV, Mushfig </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;2008-2014</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;17</font></td></tr>
<tr bgcolor=#FFEEDD>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2204</font></td>
<td>&nbsp;</td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=106167"><B>ASGEIRSSON, Heimir </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;1995-2009</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;52</font></td></tr>
<tr bgcolor=#FFFFFF>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2226</font></td>
<td>&nbsp;<img src="/chessimages/book.gif" alt="biography" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=108871"><B>ASHBY, Anthony C </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;1963-2017</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;34</font></td></tr>
<tr bgcolor=#FFEEDD>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2419</font></td>
<td>&nbsp;<img src="/chessimages/book.gif" alt="biography" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=118273"><B>ASHIKU, Franc </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;2005-2022</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;103</font></td></tr>
<tr bgcolor=#FFFFFF>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2579</font></td>
<td><img src="/chessimages/chat.gif" alt="458" width=16 height=16><img src="/chessimages/book.gif" alt="biography" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=21714"><B>ASHLEY, Maurice </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;1988-2013</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;376</font></td></tr>
<tr bgcolor=#FFEEDD>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2398</font></td>
<td>&nbsp;<img src="/chessimages/book.gif" alt="biography" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=78905"><B>ASHTON, Adam G </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;2000-2019</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;203</font></td></tr>
<tr bgcolor=#FFFFFF>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2374</font></td>
<td>&nbsp;</td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=107225"><B>ASHWATH, R </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;2006-2019</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;78</font></td></tr>
<tr bgcolor=#FFEEDD>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2515</font></td>
<td><img src="/chessimages/chat.gif" alt="2" width=16 height=16><img src="/chessimages/book.gif" alt="biography" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=113316"><B>ASHWIN, Jayaram </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;2004-2019</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;215</font></td></tr>
<tr bgcolor=#FFFFFF>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2454</font></td>
<td>&nbsp;</td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=171095"><B>ASHWIN, Jayram </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;2009-2021</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;25</font></td></tr>
<tr bgcolor=#FFEEDD>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2368</font></td>
<td>&nbsp;<img src="/chessimages/book.gif" alt="biography" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=92078"><B>ASIK, Josip </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;2001-2018</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;30</font></td></tr>
<tr bgcolor=#FFFFFF>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2260</font></td>
<td><img src="/chessimages/chat.gif" alt="31" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=43641"><B>ASK, Josef </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;1997-2019</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;115</font></td></tr>
<tr bgcolor=#FFEEDD>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2274</font></td>
<td>&nbsp;</td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=10846"><B>ASKARIAN, Karen </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;1999-2005</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;43</font></td></tr>
<tr bgcolor=#FFFFFF>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2425</font></td>
<td><img src="/chessimages/chat.gif" alt="1" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=95330"><B>ASKAROV, Bakhtiyar </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;1996-2019</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;26</font></td></tr>
<tr bgcolor=#FFEEDD>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2561</font></td>
<td><img src="/chessimages/chat.gif" alt="2" width=16 height=16><img src="/chessimages/book.gif" alt="biography" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=78952"><B>ASKAROV, Marat </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;1997-2010</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;55</font></td></tr>
<tr bgcolor=#FFFFFF>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2445</font></td>
<td><img src="/chessimages/chat.gif" alt="1" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=90513"><B>ASKER, Sven </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;1951-1988</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;11</font></td></tr>
<tr bgcolor=#FFEEDD>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2335</font></td>
<td>&nbsp;<img src="/chessimages/book.gif" alt="biography" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=157179"><B>ASKEROV, Marat </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;2016-2021</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;48</font></td></tr>
<tr bgcolor=#FFFFFF>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2370</font></td>
<td>&nbsp;<img src="/chessimages/book.gif" alt="biography" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=93952"><B>ASMAT, Jorge Luis Pacheco </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;1988-1997</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;23</font></td></tr>
<tr bgcolor=#FFEEDD>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2405</font></td>
<td><img src="/chessimages/chat.gif" alt="9" width=16 height=16><img src="/chessimages/book.gif" alt="biography" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=29969"><B>ASMUNDSSON, Ingvar </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;1957-2005</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;238</font></td></tr>
<tr bgcolor=#FFFFFF>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2445</font></td>
<td><img src="/chessimages/chat.gif" alt="1" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=173039"><B>ASON, Dylan Isidro Berdayes </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;2016-2022</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;12</font></td></tr>
<tr bgcolor=#FFEEDD>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2207</font></td>
<td><img src="/chessimages/chat.gif" alt="1" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=55402"><B>ASPA, Xavier Serrano </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;2001-2021</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;6</font></td></tr>
<tr bgcolor=#FFFFFF>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2646</font></td>
<td><img src="/chessimages/chat.gif" alt="112" width=16 height=16><img src="/chessimages/book.gif" alt="biography" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=47195"><B>ASRIAN, Karen </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;1993-2008</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;503</font></td></tr>
<tr bgcolor=#FFEEDD>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2421</font></td>
<td><img src="/chessimages/chat.gif" alt="19" width=16 height=16><img src="/chessimages/book.gif" alt="biography" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=147741"><B>ASSAUBAYEVA, Bibisara </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;2013-2022</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;331</font></td></tr>
<tr bgcolor=#FFFFFF>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2405</font></td>
<td><img src="/chessimages/chat.gif" alt="1" width=16 height=16><img src="/chessimages/book.gif" alt="biography" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=113066"><B>VAN ASSENDELFT, Floris </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;2005-2018</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;74</font></td></tr>
<tr bgcolor=#FFEEDD>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2325</font></td>
<td><img src="/chessimages/chat.gif" alt="2" width=16 height=16><img src="/chessimages/book.gif" alt="biography" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=27726"><B>ASSIOUTI, Sheriff El </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;1992-1994</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;6</font></td></tr>
<tr bgcolor=#FFFFFF>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2335</font></td>
<td><img src="/chessimages/chat.gif" alt="13" width=16 height=16><img src="/chessimages/book.gif" alt="biography" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=86655"><B>ASSMANN, Thomas </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;1981-2004</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;11</font></td></tr>
<tr bgcolor=#FFEEDD>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2285</font></td>
<td>&nbsp;<img src="/chessimages/book.gif" alt="biography" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=16390"><B>ASSUMPCAO, Roberto </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;1978-2012</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;29</font></td></tr>
<tr bgcolor=#FFFFFF>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2336</font></td>
<td>&nbsp;</td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=99350"><B>ASTASHOV, Gleb </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;1998-2005</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;18</font></td></tr>
<tr bgcolor=#FFEEDD>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2218</font></td>
<td>&nbsp;</td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=67265"><B>ASTENGO, Corrado </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;1992-2017</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;53</font></td></tr>
<tr bgcolor=#FFFFFF>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2468</font></td>
<td><img src="/chessimages/chat.gif" alt="2" width=16 height=16><img src="/chessimages/book.gif" alt="biography" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=17738"><B>ASTROM, Robert </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;1990-2007</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;39</font></td></tr>
<tr bgcolor=#FFEEDD>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2384</font></td>
<td>&nbsp;</td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=58090"><B>ASYLGUZHIN, Radik </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;1999-2004</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;50</font></td></tr>
<tr bgcolor=#FFFFFF>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;&nbsp;</font></td>
<td><img src="/chessimages/chat.gif" alt="27" width=16 height=16><img src="/chessimages/book.gif" alt="biography" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=10639"><B>ASZTALOS, Lajos </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;1911-1938</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;147</font></td></tr>
<tr bgcolor=#FFEEDD>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2519</font></td>
<td><img src="/chessimages/chat.gif" alt="7" width=16 height=16><img src="/chessimages/book.gif" alt="biography" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=109538"><B>ATABAYEV, Maksat </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;2005-2019</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;171</font></td></tr>
<tr bgcolor=#FFFFFF>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2445</font></td>
<td><img src="/chessimages/chat.gif" alt="1" width=16 height=16><img src="/chessimages/book.gif" alt="biography" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=129552"><B>ATABAYEV, Saparmyrat </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;2011-2020</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;81</font></td></tr>
<tr bgcolor=#FFEEDD>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2475</font></td>
<td><img src="/chessimages/chat.gif" alt="2" width=16 height=16><img src="/chessimages/book.gif" alt="biography" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=127367"><B>ATABAYEV, Yusup </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;2008-2021</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;148</font></td></tr>
<tr bgcolor=#FFFFFF>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2293</font></td>
<td>&nbsp;<img src="/chessimages/book.gif" alt="biography" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=155832"><B>ATAKISHIYEV, Elmar </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;2015-2022</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;78</font></td></tr>
<tr bgcolor=#FFEEDD>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2293</font></td>
<td><img src="/chessimages/chat.gif" alt="2" width=16 height=16><img src="/chessimages/book.gif" alt="biography" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=106084"><B>ATAKISI, Fatih </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;1979-2007</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;59</font></td></tr>
<tr bgcolor=#FFFFFF>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2441</font></td>
<td><img src="/chessimages/chat.gif" alt="6" width=16 height=16><img src="/chessimages/book.gif" alt="biography" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=51574"><B>ATAKISI, Umut </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;1994-2019</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;368</font></td></tr>
<tr bgcolor=#FFEEDD>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2481</font></td>
<td><img src="/chessimages/chat.gif" alt="17" width=16 height=16><img src="/chessimages/book.gif" alt="biography" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=55596"><B>ATALIK, Ekaterina </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;1996-2022</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;880</font></td></tr>
<tr bgcolor=#FFFFFF>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2636</font></td>
<td><img src="/chessimages/chat.gif" alt="72" width=16 height=16><img src="/chessimages/book.gif" alt="biography" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=17359"><B>ATALIK, Suat </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;1980-2022</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;886</font></td></tr>
<tr bgcolor=#FFEEDD>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2255</font></td>
<td>&nbsp;<img src="/chessimages/book.gif" alt="biography" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=123347"><B>ATAMAN, Alper Efe </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;2002-2015</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;30</font></td></tr>
<tr bgcolor=#FFFFFF>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2205</font></td>
<td>&nbsp;<img src="/chessimages/book.gif" alt="biography" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=156501"><B>ATANASOV, Anthony </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;2016-2021</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;25</font></td></tr>
<tr bgcolor=#FFEEDD>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2296</font></td>
<td><img src="/chessimages/chat.gif" alt="1" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=38922"><B>ATANASOV, Gospodin </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;1968-1976</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;6</font></td></tr>
<tr bgcolor=#FFFFFF>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2349</font></td>
<td><img src="/chessimages/chat.gif" alt="1" width=16 height=16><img src="/chessimages/book.gif" alt="biography" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=77828"><B>ATANASOV, Petko </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;1967-1991</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;33</font></td></tr>
<tr bgcolor=#FFEEDD>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2363</font></td>
<td>&nbsp;<img src="/chessimages/book.gif" alt="biography" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=42630"><B>ATARIA, Ernesto Mendez </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;1990-2001</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;16</font></td></tr>
<tr bgcolor=#FFFFFF>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;&nbsp;</font></td>
<td><img src="/chessimages/chat.gif" alt="112" width=16 height=16><img src="/chessimages/book.gif" alt="biography" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=12879"><B>ATKINS, Henry Ernest </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;1890-1939</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;317</font></td></tr>
<tr bgcolor=#FFEEDD>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2344</font></td>
<td><img src="/chessimages/chat.gif" alt="1" width=16 height=16><img src="/chessimages/book.gif" alt="biography" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=27162"><B>ATLAS, Dimitry </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;1987-2017</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;30</font></td></tr>
<tr bgcolor=#FFFFFF>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2340</font></td>
<td><img src="/chessimages/chat.gif" alt="2" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=46517"><B>ATLAS, Robert </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;1976-1989</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;10</font></td></tr>
<tr bgcolor=#FFEEDD>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2503</font></td>
<td><img src="/chessimages/chat.gif" alt="29" width=16 height=16><img src="/chessimages/book.gif" alt="biography" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=17260"><B>ATLAS, Valery </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;1985-2022</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;150</font></td></tr>
<tr bgcolor=#FFFFFF>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2309</font></td>
<td><img src="/chessimages/chat.gif" alt="1" width=16 height=16><img src="/chessimages/book.gif" alt="biography" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=104775"><B>ATOUFI, Pedram </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;2002-2017</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;27</font></td></tr>
<tr bgcolor=#FFEEDD>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2336</font></td>
<td><img src="/chessimages/chat.gif" alt="1" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=15227"><B>ATUTUBO, Rodrigo </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;1992-1995</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;6</font></td></tr>
<tr bgcolor=#FFFFFF>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2250</font></td>
<td>&nbsp;<img src="/chessimages/book.gif" alt="biography" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=150743"><B>ATWELL, Adrian Winter </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;2014-2022</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;39</font></td></tr>
<tr bgcolor=#FFEEDD>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2239</font></td>
<td><img src="/chessimages/chat.gif" alt="4" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=78813"><B>AU, Leslie </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;1989-2004</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;28</font></td></tr>
<tr bgcolor=#FFFFFF>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2410</font></td>
<td>&nbsp;<img src="/chessimages/book.gif" alt="biography" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=155708"><B>AUDI, Ameya </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;2016-2022</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;30</font></td></tr>
<tr bgcolor=#FFEEDD>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2337</font></td>
<td><img src="/chessimages/chat.gif" alt="2" width=16 height=16><img src="/chessimages/book.gif" alt="biography" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=28009"><B>AUGUSTIN, Josef </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;1959-2006</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;316</font></td></tr>
<tr bgcolor=#FFFFFF>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2417</font></td>
<td><img src="/chessimages/chat.gif" alt="6" width=16 height=16><img src="/chessimages/book.gif" alt="biography" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=127530"><B>AULIA, Medina Warda </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;2010-2022</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;135</font></td></tr>
<tr bgcolor=#FFEEDD>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2328</font></td>
<td>&nbsp;<img src="/chessimages/book.gif" alt="biography" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=115709"><B>AULLANA, Jose Ramon Ibanez </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;1993-2021</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;32</font></td></tr>
<tr bgcolor=#FFFFFF>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2316</font></td>
<td><img src="/chessimages/chat.gif" alt="1" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=102960"><B>AUMANN, Welf </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;1998-2007</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;4</font></td></tr>
<tr bgcolor=#FFEEDD>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2595</font></td>
<td><img src="/chessimages/chat.gif" alt="41" width=16 height=16><img src="/chessimages/book.gif" alt="biography" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=11036"><B>AUNG, Aung Myo Hlaing Aung </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;1999-2011</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;30</font></td></tr>
<tr bgcolor=#FFFFFF>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2320</font></td>
<td>&nbsp;</td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=139223"><B>VAN DER AUWERAERT, Elwin </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;2012-2013</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;15</font></td></tr>
<tr bgcolor=#FFEEDD>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2342</font></td>
<td><img src="/chessimages/chat.gif" alt="2" width=16 height=16><img src="/chessimages/book.gif" alt="biography" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=163513"><B>AVALYAN, Artur </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;2016-2019</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;3</font></td></tr>
<tr bgcolor=#FFFFFF>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2259</font></td>
<td><img src="/chessimages/chat.gif" alt="21" width=16 height=16><img src="/chessimages/book.gif" alt="biography" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=108222"><B>AVARI, Viraf </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;1996-2004</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;48</font></td></tr>
<tr bgcolor=#FFEEDD>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2204</font></td>
<td>&nbsp;<img src="/chessimages/book.gif" alt="biography" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=76701"><B>AVDEENKO, Tatiana </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;2003-2012</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;18</font></td></tr>
<tr bgcolor=#FFFFFF>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2376</font></td>
<td><img src="/chessimages/chat.gif" alt="1" width=16 height=16><img src="/chessimages/book.gif" alt="biography" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=107053"><B>AVELLANA, Jordi Cuadras </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;1974-2020</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;44</font></td></tr>
<tr bgcolor=#FFEEDD>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2445</font></td>
<td><img src="/chessimages/chat.gif" alt="250" width=16 height=16><img src="/chessimages/book.gif" alt="biography" width=16 height=16><a href="/audio/20559.mp3"><img src="/chessimages/speaker.gif" alt="pronunciation" width=16 height=16 border=0></a></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=20559"><B>AVERBAKH, Yuri </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;1938-2007</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;904</font></td></tr>
<tr bgcolor=#FFFFFF>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2214</font></td>
<td><img src="/chessimages/chat.gif" alt="1" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=11443"><B>AVERBUKH, Alex </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;1999-2022</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;34</font></td></tr>
<tr bgcolor=#FFEEDD>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2335</font></td>
<td>&nbsp;<img src="/chessimages/book.gif" alt="biography" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=102357"><B>AVERCHENKO, Sergej </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;1997-1998</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;15</font></td></tr>
<tr bgcolor=#FFFFFF>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2400</font></td>
<td>&nbsp;<img src="/chessimages/book.gif" alt="biography" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=54471"><B>AVERJANOV, Alexey </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;1999-2006</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;50</font></td></tr>
<tr bgcolor=#FFEEDD>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2394</font></td>
<td><img src="/chessimages/chat.gif" alt="4" width=16 height=16><img src="/chessimages/book.gif" alt="biography" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=29734"><B>AVERKIN, Orest </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;1964-1998</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;131</font></td></tr>
<tr bgcolor=#FFFFFF>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2207</font></td>
<td><img src="/chessimages/chat.gif" alt="1" width=16 height=16><img src="/chessimages/book.gif" alt="biography" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=104001"><B>AVERY, Robert </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;1971-1994</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;13</font></td></tr>
<tr bgcolor=#FFEEDD>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2545</font></td>
<td><img src="/chessimages/chat.gif" alt="11" width=16 height=16><img src="/chessimages/book.gif" alt="biography" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=99144"><B>AVESKULOV, Valeriy </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;1996-2010</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;165</font></td></tr>
<tr bgcolor=#FFFFFF>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2245</font></td>
<td><img src="/chessimages/chat.gif" alt="2" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=48200"><B>AVNER, Uri </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;1964-1966</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;12</font></td></tr>
<tr bgcolor=#FFEEDD>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2350</font></td>
<td><img src="/chessimages/chat.gif" alt="11" width=16 height=16><img src="/chessimages/book.gif" alt="biography" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=26783"><B>AVNI, Amatzia </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;1981-1995</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;12</font></td></tr>
<tr bgcolor=#FFFFFF>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2315</font></td>
<td>&nbsp;<img src="/chessimages/book.gif" alt="biography" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=150462"><B>AVRAMIDOU, Anastasia </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;2014-2022</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;94</font></td></tr>
<tr bgcolor=#FFEEDD>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2668</font></td>
<td><img src="/chessimages/chat.gif" alt="21" width=16 height=16><img src="/chessimages/book.gif" alt="biography" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=18270"><B>AVRUKH, Boris </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;1991-2017</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;668</font></td></tr>
<tr bgcolor=#FFFFFF>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2475</font></td>
<td>&nbsp;<img src="/chessimages/book.gif" alt="biography" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=29202"><B>AVSHALUMOV, Alex </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;1980-1992</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;38</font></td></tr>
<tr bgcolor=#FFEEDD>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2351</font></td>
<td><img src="/chessimages/chat.gif" alt="2" width=16 height=16><img src="/chessimages/book.gif" alt="biography" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=106705"><B>AXELROD, Arie </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;2005-2014</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;26</font></td></tr>
<tr bgcolor=#FFFFFF>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2406</font></td>
<td><img src="/chessimages/chat.gif" alt="1" width=16 height=16><img src="/chessimages/book.gif" alt="biography" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=110190"><B>AYALA, Ivan Cabezas </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;2001-2018</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;44</font></td></tr>
<tr bgcolor=#FFEEDD>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2243</font></td>
<td>&nbsp;<img src="/chessimages/book.gif" alt="biography" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=47477"><B>AYAPBERGENOV, A </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;1993-1994</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;16</font></td></tr>
<tr bgcolor=#FFFFFF>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2285</font></td>
<td>&nbsp;</td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=140218"><B>AYDINCELEBI, Kagan </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;2012-2019</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;35</font></td></tr>
<tr bgcolor=#FFEEDD>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2263</font></td>
<td><img src="/chessimages/chat.gif" alt="1" width=16 height=16><img src="/chessimages/book.gif" alt="biography" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=86764"><B>DE AYSA, Manuel Llopis </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;1992-2021</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;18</font></td></tr>
<tr bgcolor=#FFFFFF>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2403</font></td>
<td>&nbsp;<img src="/chessimages/book.gif" alt="biography" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=53206"><B>AYUPOV, Damir </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;2001-2012</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;43</font></td></tr>
<tr bgcolor=#FFEEDD>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2250</font></td>
<td><img src="/chessimages/chat.gif" alt="7" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=24022"><B>AYYAR, Rajan </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;1979-1980</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;6</font></td></tr>
<tr bgcolor=#FFFFFF>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2264</font></td>
<td>&nbsp;</td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=95137"><B>AZADHARF, Farrokh </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;1977-2006</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;17</font></td></tr>
<tr bgcolor=#FFEEDD>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2499</font></td>
<td><img src="/chessimages/chat.gif" alt="3" width=16 height=16><img src="/chessimages/book.gif" alt="biography" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=96066"><B>AZALADZE, Shota </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;2000-2021</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;259</font></td></tr>
<tr bgcolor=#FFFFFF>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2333</font></td>
<td>&nbsp;<img src="/chessimages/book.gif" alt="biography" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=150827"><B>AZAMBUJA, Nicolas Lopez </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;2014-2019</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;26</font></td></tr>
<tr bgcolor=#FFEEDD>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2667</font></td>
<td><img src="/chessimages/chat.gif" alt="9" width=16 height=16><img src="/chessimages/book.gif" alt="biography" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=17281"><B>AZAROV, Sergei </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;1992-2022</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;769</font></td></tr>
<tr bgcolor=#FFFFFF>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2314</font></td>
<td>&nbsp;<img src="/chessimages/book.gif" alt="biography" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=125820"><B>AZAROVA, Nadezhda </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;2006-2009</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;40</font></td></tr>
<tr bgcolor=#FFEEDD>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2389</font></td>
<td>&nbsp;<img src="/chessimages/book.gif" alt="biography" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=141256"><B>AZARYA, Jodi Setyaki </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;2012-2021</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;62</font></td></tr>
<tr bgcolor=#FFFFFF>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2269</font></td>
<td>&nbsp;</td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=49137"><B>AZIEM, Ramadan Abdel </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;2001-2003</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;18</font></td></tr>
<tr bgcolor=#FFEEDD>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2679</font></td>
<td><img src="/chessimages/chat.gif" alt="353" width=16 height=16><img src="/chessimages/book.gif" alt="biography" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=14175"><B>AZMAIPARASHVILI, Zurab </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;1968-2015</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;1,155</font></td></tr>
<tr bgcolor=#FFFFFF>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;2496</font></td>
<td><img src="/chessimages/chat.gif" alt="1" width=16 height=16><img src="/chessimages/book.gif" alt="biography" width=16 height=16></td><td width=160><font face="verdana,arial,helvetica" size=-1><a
href="/perl/chessplayer?pid=88419"><B>DE AZUA, Ernesto Real </B></a></font></td>
<td align=CENTER><font face="verdana,arial,helvetica" size=-2>&nbsp;1995-2020</font></td>
<td align=RIGHT><font face="verdana,arial,helvetica" size=-2>&nbsp;151</font></td></tr>

</table></td></tr></table>
</td></tr></table>
</center>
<P>

<center>
<table border=0 cellpadding=1 cellspacing=0><tr><td bgcolor=#996633>
<table border=0 cellpadding=5 cellspacing=0>
<tr><td background="/chessimages/highlight_stripes.gif">
<font face="verdana,arial,helvetica"><B>
<font size=+2 color=#CC0000>A</font>&nbsp;<a href="/directory/B.html">B</a>&nbsp;<a href="/directory/C.html">C</a>&nbsp;<a href="/directory/D.html">D</a>&nbsp;<a href="/directory/E.html">E</a>&nbsp;<a href="/directory/F.html">F</a>&nbsp;<a href="/directory/G.html">G</a>&nbsp;<a href="/directory/H.html">H</a>&nbsp;<a href="/directory/I.html">I</a>&nbsp;<a href="/directory/J.html">J</a>&nbsp;<a href="/directory/K.html">K</a>&nbsp;<a href="/directory/L.html">L</a>&nbsp;<a href="/directory/M.html">M</a>&nbsp;<a href="/directory/N.html">N</a>&nbsp;<a href="/directory/O.html">O</a>&nbsp;<a href="/directory/P.html">P</a>&nbsp;<a href="/directory/Q.html">Q</a>&nbsp;<a href="/directory/R.html">R</a>&nbsp;<a href="/directory/S.html">S</a>&nbsp;<a href="/directory/T.html">T</a>&nbsp;<a href="/directory/U.html">U</a>&nbsp;<a href="/directory/V.html">V</a>&nbsp;<a href="/directory/W.html">W</a>&nbsp;<a href="/directory/X.html">X</a>&nbsp;<a href="/directory/Y.html">Y</a>&nbsp;<a href="/directory/Z.html">Z</a>
</font>
</td></tr></table>
</td></tr></table>
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
<a href="mailto:chess@chessgames.com">Contact&nbsp;Us</a></div>
<p class="cgc-ns1 center tcenter xxsm tbm5">Copyright 2001-2021, Chessgames Services LLC</p>
<div class="increaserev bidmcms970x90"></div>
<script>ir_ads_push();</script>
	    <script>
	     window.googletag = window.googletag || {cmd: []};
	      var interstitialSlot, staticSlot;
	      googletag.cmd.push(function() {
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
	        googletag.cmd.push(function() {
	          googletag.display(interstitialSlot);
	        });
	    </script>
	
<pre>

</pre>

</body>
</html>
'''
    }
