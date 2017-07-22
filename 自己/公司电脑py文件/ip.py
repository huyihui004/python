#!/usr/bin/env python
#coding=utf-8

import urllib
import re

def IP_zone(Ip):
    url = 'http://www.ip138.com/ips138.asp?ip=Ip&action=2'
    openurl = urllib.urlopen(url)
    html = openurl.read()
    print html
    reg = re.compile('')



IP_zone('45.64.129.128')