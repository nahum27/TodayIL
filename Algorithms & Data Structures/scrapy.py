# -*- coding: utf-8 -*-
"""
Created on Wed May 27 03:05:28 2020

@author: Geo
"""

import dryscrape

sess = dryscrape.Session(base_url = 'http://google.com')


from requests_html import HTMLSession


session = HTMLSession()

r = session.get("https://news.naver.com/")

r.html.render()

r.close

r.headers

r.text

r.url

r.request