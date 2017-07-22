#!/usr/bin/env python
#coding=utf-8

import ConfigParser

conf = ConfigParser.ConfigParser()
conf.read("E:\Python\project.cnf")
sections = conf.sections()
options = conf.options("trend")
kvs = conf.items("trend")
print conf.get("trend","server_host")


print sections
print options
print kvs

conf.set("trend","server_host","183.61.172.84,183.60.225.3")
conf.set("trend","port","8081")
#conf.add_section('app2')
#conf.set('app2','server_host','183.61.172.66,183.60.225.2')

conf.write(open("E:\Python\project.cnf","w"))
conf.read("E:\Python\project.cnf")
print conf.sections()
