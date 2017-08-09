#!/usr/bin/env python
#coding=utf-8


if __name__ == '__main__':
    import time
    start = time.time()
    for i in range(3000):
        print i
    end = time.time()
    print start
    print end

    print end - start