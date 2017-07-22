#!/usr/bin/env python
#coding:utf-8

import urllib2


url = 'http://www.cililian.com/main-search.html?kw=LCBD-00761'
urlopen = urllib2.urlopen(url)
html = urlopen.read()
print html