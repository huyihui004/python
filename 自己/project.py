#!/usr/bin/env python
#coding=utf-8

import ConfigParser

conf = ConfigParser.ConfigParser()
conf.read('/etc/project.cnf')
sections = conf.sections()
print 'sections:',sections
options = conf.options('trend')
print 'trend options:',options
kvs = conf.items('trend')
print 'trend key:',kvs

str_trend = conf.get("trend","server_host")
int_trend = conf.get("trend","server_host")
print str_trend
print int_trend
conf.set("trend","server_host","192.168.10.183")
conf.write(open("/etc/project.cnf","w"))
kvs2 = conf.items('trend')
print kvs2
