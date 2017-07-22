#!/usr/bin/env python
#coding=utf-8

class FooClass:
    """my very first class:Fooclass"""
    version = 0.1   #class (data) attribute

    def __init__(self,nm='huyihui'):
        """constructor"""
        self.name=nm     #class instance (data) attribute
        print 'Created a class instance for',nm
    def showname(self):
        """display instance attribute and class name"""
        print 'Your name is',self.name
        print 'My name is',self.__class__.__name__
    def showver(self):
        print self.version
    def addMe2Me(self,x):
        return x + x

fool = FooClass('hu')
fool.showname()
fool.showver()
print fool.addMe2Me('hyh')