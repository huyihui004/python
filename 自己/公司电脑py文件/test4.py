#!/usr/bin/env python
#coding=utf-8

import zipfile
from hashlib import md5

import hashlib
import commands

print commands.getstatus('/bin/ls')


m2 = hashlib.md5()
m2.update('ROOT.zip')
print m2.hexdigest()




'''
m = md5()
org_file = open('ROOT.zip','rb')
m.update(org_file.read())
org_file.close()
print m.hexdigest()
'''

'''
z = zipfile.ZipFile('ROOT.zip','r')
Valuer = z.namelist()
print Valuer

#for f in z.namelist():
#    print f


#for i in z.infolist():
#    print i.filename,i.file_size,i.header_offset

'''

